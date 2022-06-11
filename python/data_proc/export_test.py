import io
import onnx
import torch
import torch.nn as nn
import torch.nn.functional as F
import onnxruntime
import onnxruntime_extensions
from onnxruntime_extensions import pnp

class Model(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, y):
        return x == y

model = Model() 

class CustomInverse(torch.nn.Module):
    def forward(self, x):
        return torch.inverse(x) + x


x0 = torch.randn(3, 3)

# Export model to ONNX
f = io.BytesIO()
t_model = CustomInverse()

from torch.onnx import register_custom_op_symbolic

def my_inverse(g, self):
    return g.op("ai.onnx.contrib::Inverse", self)

register_custom_op_symbolic('::inverse', my_inverse, 1)

torch.onnx.export(t_model, (x0, ), f, input_names=['x'], output_names=['y'], opset_version=12, dynamic_axes={'x': {0: 'x_axis', 1: 'y_axis'}})

onnx_model = onnx.load(io.BytesIO(f.getvalue()))

session_options = onnxruntime.SessionOptions()
session_options.register_custom_ops_library(onnxruntime_extensions.get_library_path())

sess = onnxruntime.InferenceSession(onnx_model.SerializeToString(), session_options)

x1 =torch.rand(4, 4).numpy()

output = sess.run(None, {'x': x1})
print(output)