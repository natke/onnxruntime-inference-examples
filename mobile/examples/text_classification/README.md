# Use ONNX Runtime with extensions and React Native for Text classification

## Pre-requisites

Install node
Install nvm (On mac, need node version 16.16.0)


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

### iOS

```bash
./build.sh --use_xcode --ios --ios_sysroot iphonesimulator --osx_arch x86_64 --apple_deploy_target 11 --build_extensions
```

* Update brew and install watchman
* 

To debug react native bundle
* yarn add -D react-native-bundle-visualizer
* npx react-native-bundle-visualizer

Errors

```
/Users/nakersha/Develop/code/microsoft/onnxruntime-inference-examples/mobile/examples/text_classification/senti/node_modules/@expo/config-plugins/build/plugins/withIosBaseMods.js:156
  readFile,
  ^

TypeError: Cannot destructure property `readFile` of 'undefined' or 'null'.
    at Object.<anonymous> (/Users/nakersha/Develop/code/microsoft/onnxruntime-inference-examples/mobile/examples/text_classification/senti/node_modules/@expo/config-plugins/build/plugins/withIosBaseMods.js:158:10)
    at Module._compile (internal/modules/cjs/loader.js:689:30)
    at Object.Module._extensions..js (internal/modules/cjs/loader.js:700:10)
    at Module.load (internal/modules/cjs/loader.js:599:32)
    at tryModuleLoad (internal/modules/cjs/loader.js:538:12)
    at Function.Module._load (internal/modules/cjs/loader.js:530:3)
    at Module.require (internal/modules/cjs/loader.js:637:17)
    at require (internal/modules/cjs/helpers.js:22:18)
    at _withIosBaseMods (/Users/nakersha/Develop/code/microsoft/onnxruntime-inference-examples/mobile/examples/text_classification/senti/node_modules/@expo/config-plugins/build/index.js:269:16)
    at Object.<anonymous> (/Users/nakersha/Develop/code/microsoft/onnxruntime-inference-examples/mobile/examples/text_classification/senti/node_modules/@expo/config-plugins/build/index.js:467:20)
Command PhaseScriptExecution failed with a nonzero exit code
```

This error occurs if any expo config plugin is used.

2147483647 = 2GB

file:///Users/nakersha/Library/Developer/CoreSimulator/Devices/B5B7BC8F-F86B-4AB4-9192-6210E89D9102/data/Containers/Data/Application/F2D31122-984E-44DC-8067-C18F8BD38DDB/Library/Caches/ExponentExperienceData/%2540anonymous%252Fsenti-57388358-cfd2-4465-b066-728ea0f9f672/ExponentAsset-b2e57e6781f99a65005d09bb28a7f148.ort

file:///Users/nakersha/Library/Developer/CoreSimulator/Devices/B5B7BC8F-F86B-4AB4-9192-6210E89D9102/data/Containers/Data/Application/F2D31122-984E-44DC-8067-C18F8BD38DDB/Library/Caches/ExponentExperienceData/%2540anonymous%252Fsenti-57388358-cfd2-4465-b066-728ea0f9f672/ExponentAsset-d5c2ade3b2883abcd77b787c61b9ee2e.ort

```
expo install onnxruntime-react-native
```

https://stackoverflow.com/questions/69666568/how-can-i-use-the-types-of-a-conditionally-imported-module-in-typescript




### Web

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
   cp onnxruntime/build/Windows/Debug/ort-wasm.js onnxruntime/js/web/lib/wasm/binding
   cp onnxruntime/build/Windows/Debug/ort-wasm-threaded.js onnxruntime/js/web/lib/wasm/binding
   cp onnxruntime/build/Windows/Debug/ort-wasm-threaded.worker.js onnxruntime/js/web/lib/wasm/binding
   ```

3. Follow instructions to build the npm packahe with the customized wasm files here

   https://onnxruntime.ai/docs/build/web.html#build-onnxruntime-web-npm-package
   

## Application

* Create empty app

  ```bash
  npx create-expo-app
  cd <app name>
  touch tsconfig.json
  expo start
  ```

* Add model

  Copy or link model into assets directory

  Update metro.config.js to handle files with .ort extension



* Run application

  ```bash
  expo start --no-dev --minify
  ```
