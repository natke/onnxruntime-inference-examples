import onnxruntime
import onnxruntime_extensions

test_question = ["What is the population of the United States"]
#, "The United States had an official resident population of 331,893,745 on July 1, 2021, according to the U.S. Census Bureau."]


# Load the model
session_options = onnxruntime.SessionOptions()
session_options.register_custom_ops_library(onnxruntime_extensions.get_library_path())
session = onnxruntime.InferenceSession('bert-large-uncased-whole-word-masking-finetuned-squad-aug.onnx', session_options)

# Run the model
results = session.run(["g2_start", "g2_end"], {"g1_it_1270856953648": test_question})

print(results[0])
print(results[1])