import torch
from model import Predictor
from torch.onnx import register_custom_op_symbolic

# Define and register a custom op
# TODO Replace this with a custom op from ONNX Runtime Extensions
class CustomInverse(torch.nn.Module):
    def forward(self, x):
        return torch.inverse(x) + x        

def my_inverse(g, self):
    return g.op("ai.onnx.contrib::Inverse", self)

register_custom_op_symbolic('::inverse', my_inverse, 1)

class CenterCrop(torch.nn.Module):
    def __init__(self, size):
        self.target_size = size

    def forward(self, img):
        width, height = self.target_size, self.target_size
        img_h, img_w = img.shape[-2:]
        s_h = torch.div((img_h - height), 2, rounding_mode='trunc')
        s_w = torch.div((img_w - width), 2, rounding_mode='trunc')
        return img[:, :, s_h:s_h + height, s_w:s_w + width]

def custom_center_crop(g, self):
    return g.op("ai.onnx.contrib::CenterCrop", self)

register_custom_op_symbolic('::center_crop', custom_center_crop, 1)


# Export model
device = 'cuda' if torch.cuda.is_available() else 'cpu'
predictor = Predictor().to(device)
predictor.eval()
input_size = torch.zeros((1, 3, 224, 224))  
torch.onnx.export(predictor, input_size, 'model.onnx', export_params=True, opset_version=16)
