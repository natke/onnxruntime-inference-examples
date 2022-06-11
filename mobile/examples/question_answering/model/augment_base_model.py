from pathlib import Path
import torch
from transformers import AutoTokenizer
import onnx
from onnxruntime_extensions import pnp

# get an onnx model by converting HuggingFace pretrained model
qa_bert_model_name = "bert-large-uncased-whole-word-masking-finetuned-squad"
model_name = qa_bert_model_name
model_path = Path(model_name + ".onnx")

# mapping the BertTokenizer outputs into the onnx model inputs
def map_token_output(input_ids, attention_mask, token_type_ids):
    return input_ids.unsqueeze(0), token_type_ids.unsqueeze(0), attention_mask.unsqueeze(0)

# Post process the start and end logits
def post_process(*pred):
    output = torch.softmax(pred[1], dim=1)
    return output

tokenizer = AutoTokenizer.from_pretrained(model_name)
bert_tokenizer = pnp.PreHuggingFaceBert(hf_tok=tokenizer)
bert_model = onnx.load_model(str(model_path))

augmented_model = pnp.SequentialProcessingModule(bert_tokenizer, map_token_output,
                                                 bert_model, post_process)

test_question = ["What is the population of the United States", "The United States had an official resident population of 331,893,745 on July 1, 2021, according to the U.S. Census Bureau."]

# create the final onnx model which includes pre- and post- processing.
augmented_model = pnp.export(augmented_model,
                             test_question,
                             opset_version=12,
                             input_names=['question'],
                             output_names=['start', 'end'],
                             output_path=model_name + '-aug.onnx',
                             dynamic_axes={'question': [0], 'start': [0], 'end': [0]})