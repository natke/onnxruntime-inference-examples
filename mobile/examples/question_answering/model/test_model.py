from numpy import asarray
import onnxruntime

test_question = ["What is the population of the United States", "The United States had an official resident population of 331,893,745 on July 1, 2021, according to the U.S. Census Bureau."]

# Load the model
session = onnxruntime.InferenceSession('bert-large-uncased-whole-word-masking-finetuned-squad-aug.onnx')

# Run the model
results = session.run(["start", "end"], {"question": test_question})

print(results)