import onnxruntime
import onnxruntime_extensions

test_input = ["Do you like me?"]

# Load the model
session_options = onnxruntime.SessionOptions()
session_options.register_custom_ops_library(onnxruntime_extensions.get_library_path())
session = onnxruntime.InferenceSession('distilbert-base-uncased-finetuned-sst-2-english-aug.onnx', session_options)

# Run the model
results = session.run(["g2_output"], {"g1_it_2589433893008": test_input})

print(results[0])
