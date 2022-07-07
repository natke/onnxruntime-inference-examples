from torch.onnx import register_custom_op_symbolic


def my_inverse(g, self):
    return g.op("ai.onnx.contrib::CenterCrop", self)

register_custom_op_symbolic('::center_crop', my_center_crop, 1)