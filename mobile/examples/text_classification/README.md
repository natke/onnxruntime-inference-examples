# Use ONNX Runtime with extensions and React Native for Text classification

## Model

* Environment and dependencies

  ```bash
  conda env list
  conda activate 



* Export model
* Augment model
* Convert model to ORT format

  ```bash
  python -m onnxruntime.tools.convert_onnx_models_to_ort --custom_op_library /C/Users/nakersha/Miniconda3/envs/orte/lib/site-packages/onnxruntime_extensions/_ortcustomops.cp3
9-win_amd64.pyd distilbert-base-uncased-finetuned-sst-2-english-aug.onnx
  ```

## Build ONNX Runtime to include the extensions

1. Build ONNX Runtime with extensions enabled for all WASM variants

   ```bash
   build.sh --build_wasm --use_extensions --parallel --skip_tests
   build.sh --build_wasm --enable_wasm_simd --use_extensions --parallel --skip_tests
   build.sh --build_wasm --enable_wasm_threads --use_extensions --parallel --skip_tests
   build.sh --build_wasm --enable_wasm_simd --enable_wasm_threads --use_extensions --parallel --skip_tests
   ```

2. Copy WASM and js files into the onnxruntime/js/web folder

   ```bash
   mkdir -p onnxruntime/js/web/dist

   cp onnxruntime/build/Windows/Debug/ort-wasm.wasm onnxruntime/js/web/dist
   cp onnxruntime/build/Windows/Debug/ort-wasm-threaded.wasm onnxruntime/js/web/dist
   cp onnxruntime/build/Windows/Debug/ort-wasm-simd.wasm onnxruntime/js/web/dist
   cp onnxruntime/build/Windows/Debug/ort-wasm-simd-threaded.wasm onnxruntime/js/web/dist
   cp: cannot stat 'onnxruntime/build/Windows/Debug/ort-wasm-simd-threaded.wasm': No such file or directory
   cp onnxruntime/build/Windows/Debug/ort-wasm.js onnxruntime/js/web/lib/wasm/binding
   cp onnxruntime/build/Windows/Debug/ort-wasm-threaded.js onnxruntime/js/web/lib/wasm/binding
   cp onnxruntime/build/Windows/Debug/ort-wasm-threaded.worker.js onnxruntime/js/web/lib/wasm/binding
   ```

## Application

* React native / expo template

* Add model

* Run application

  ```bash
  expo start --no-dev --minify
  ```



