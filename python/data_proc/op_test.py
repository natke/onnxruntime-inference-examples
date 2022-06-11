import onnx
from onnx import helper, onnx_pb as onnx_proto
import onnxruntime
import onnxruntime_extensions
from onnxruntime_extensions import make_onnx_model

def test_StringEqual():
    nodes = []
    nodes.append(helper.make_node('Identity', ['x'], ['id1']))
    nodes.append(helper.make_node('Identity', ['y'], ['id2']))
    nodes.append(
        helper.make_node(
            'StringEqual', ['id1', 'id2'], ['z'], domain="ai.onnx.contrib"))

    input0 = helper.make_tensor_value_info(
        'x', onnx_proto.TensorProto.STRING, [])
    input1 = helper.make_tensor_value_info(
        'y', onnx_proto.TensorProto.STRING, [])
    output0 = helper.make_tensor_value_info(
        'z', onnx_proto.TensorProto.BOOL, [])

    graph = helper.make_graph(nodes, 'test0', [input0, input1], [output0])
    model = make_onnx_model(graph)

    session_options = onnxruntime.SessionOptions()
    session_options.register_custom_ops_library(onnxruntime_extensions.get_library_path())

    sess = onnxruntime.InferenceSession(model.SerializeToString(), session_options)
        
    output = sess.run(None, {'x': ["Hello"], 'y': ["Goodbye"]})
    print(output)

    return model

model = test_StringEqual()

onnx.save(model, 'string_equal_model.onnx')




