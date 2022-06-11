import onnxruntime
import onnxruntime_extensions

test_question = ["I hate cats"]

# Load the model
session_options = onnxruntime.SessionOptions()
session_options.register_custom_ops_library(onnxruntime_extensions.get_library_path())
session = onnxruntime.InferenceSession('distilbert-base-uncased-finetuned-sst-2-english-aug.onnx', session_options)

# Run the model
results = session.run(["g2_output"], {"g1_it_2589433893008": test_question})

print(results[0])
