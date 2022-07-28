
import torch

# from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import MobileBertForSequenceClassification

#model_name = "distilbert-base-uncased-finetuned-sst-2-english"
model_name = "lordtt13/emo-mobilebert"
model_path = "./" + "lordtt13-emo-mobilebert" + ".onnx"
model = MobileBertForSequenceClassification.from_pretrained(model_name)

# set the model to inference mode
# It is important to call torch_model.eval() or torch_model.train(False) before exporting the model, 
# to turn the model to inference mode. This is required since operators like dropout or batchnorm 
# behave differently in inference and training mode.
model.eval()

# Generate dummy inputs to the model. Adjust if neccessary
inputs = {
        'input_ids':   torch.randint(32, [1, 32], dtype=torch.long), # list of numerical ids for the tokenized text
        'attention_mask': torch.ones([1, 32], dtype=torch.long)      # dummy list of ones
    }

symbolic_names = {0: 'batch_size', 1: 'max_seq_llsen'}
torch.onnx.export(model,                                         # model being run
                  (inputs['input_ids'],
                   inputs['attention_mask']), 
                  model_path,                                    # where to save the model (can be a file or file-like object)
                  opset_version=11,                              # the ONNX version to export the model to
                  do_constant_folding=True,                      # whether to execute constant folding for optimization
                  input_names=['input_ids',
                               'input_mask'],                    # the model's input names
                  output_names=['output_logits'],                # the model's output names
                  dynamic_axes={'input_ids': symbolic_names,
                                'input_mask' : symbolic_names,
                                'output_logits' : symbolic_names}) # variable length axes
