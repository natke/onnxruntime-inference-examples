from pathlib import Path
import torch
from transformers import AutoTokenizer
import onnx
from onnxruntime_extensions import pnp

# get an onnx model by converting HuggingFace pretrained model
model_name = "bert-base-cased"
model_path = Path("bert-base-cased.onnx")

# a silly post-processing example function, demo-purpose only
def post_processing_forward(*pred):
    return torch.softmax(pred[1], dim=1)


# mapping the BertTokenizer outputs into the onnx model inputs
def mapping_token_output(_1, _2, _3):
    return _1.unsqueeze(0), _3.unsqueeze(0), _2.unsqueeze(0)


tokenizer = AutoTokenizer.from_pretrained(model_name)
bert_tokenizer = pnp.PreHuggingFaceBert(hf_tok=tokenizer)
bert_model = onnx.load_model(str(model_path))

test_sentence = ["this is a test sentence."]

# create the final onnx model which includes pre- and post- processing.
augmented_model = pnp.export(pnp.SequentialProcessingModule(
                             bert_tokenizer, mapping_token_output,
                             bert_model, post_processing_forward),
                             test_sentence,
                             opset_version=12,
                             output_path=model_name + '-aug.onnx')