# Use ONNX Runtime with extensions and React Native for Text classification

## Model

* Environment and dependencies


* Export model
* Augment model
* Convert model to ORT format

  ```bash
  python -m onnxruntime.tools.convert_onnx_models_to_ort --custom_op_library /C/Users/nakersha/Miniconda3/envs/orte/lib/site-packages/onnxruntime_extensions/_ortcustomops.cp3
9-win_amd64.pyd distilbert-base-uncased-finetuned-sst-2-english-aug.onnx
  ```

## Application

* React native / expo template

* Add model

* Run application

  ```bash
  expo start --no-dev --minify
  ```



