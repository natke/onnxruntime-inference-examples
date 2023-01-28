import onnxruntime
import onnxruntime_extensions

test_input = ["This movie is really terrible"]

# Load the model
session_options = onnxruntime.SessionOptions()
session_options.register_custom_ops_library(onnxruntime_extensions.get_library_path())
session = onnxruntime.InferenceSession('lordtt13-emo-mobilebert-aug.onnx', session_options)

# Run the model
results = session.run(["g2_output"], {"g1_it_140546007589296": test_input})

print(results)
