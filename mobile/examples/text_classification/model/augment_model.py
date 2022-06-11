from pathlib import Path
import torch
from transformers import AutoTokenizer
import onnx
from onnxruntime_extensions import pnp

# get an onnx model by converting HuggingFace pretrained model
bert_model_name = "distilbert-base-uncased-finetuned-sst-2-english"
model_name = bert_model_name
model_path = Path(model_name + ".onnx")

# mapping the BertTokenizer outputs into the onnx model inputs
def map_token_output(input_ids, attention_mask, token_type_ids):
    return input_ids.unsqueeze(0), token_type_ids.unsqueeze(0), attention_mask.unsqueeze(0)

# Post process the start and end logits
def post_process(*pred):
    output = torch.argmax(pred[0])
    return output

tokenizer = AutoTokenizer.from_pretrained(model_name)
bert_tokenizer = pnp.PreHuggingFaceBert(hf_tok=tokenizer)
bert_model = onnx.load_model(str(model_path))

augmented_model = pnp.SequentialProcessingModule(bert_tokenizer, map_token_output,
                                                 bert_model, post_process)

test_input = ["This is s test sentence"]

# create the final onnx model which includes pre- and post- processing.
augmented_model = pnp.export(augmented_model,
                             test_input,
                             opset_version=12,
                             input_names=['input'],
                             output_names=['output'],
                             output_path=model_name + '-aug.onnx',
                             dynamic_axes={'input': [0], 'output': [0]})