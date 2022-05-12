import onnx
import torch
from onnxruntime_extensions import pnp

mobilenet_model = onnx.load_model('model/mobilenetv2-7.onnx')
augmented_model = pnp.SequentialProcessingModule(
    pnp.PreMobileNet(224),
    mobilenet_model,
    pnp.PostMobileNet())

# The image size is dynamic, the 400x500 here is to get a fake input to enable export
fake_image_input = torch.ones(500, 400, 3).to(torch.uint8)
augmented_model.forward(fake_image_input)
pnp.export(augmented_model,
           fake_image_input,
           opset_version=11,
           output_path='model/augmented_mobilev2-7.onnx',
           input_names=['image'],
           output_names=['top_classes', 'top_probs'],
           dynamic_axes={'image': [0, 1]})