const createExpoWebpackConfigAsync = require('@expo/webpack-config');

const CopyPlugin = require("copy-webpack-plugin");

module.exports = async function (env, argv) {

  const config = await createExpoWebpackConfigAsync(env, argv);

  config.plugins.push(
    new CopyPlugin({
      patterns: [
        {
          from: './node_modules/onnxruntime-web/dist/ort-wasm.wasm',
          to: 'static/chunks/pages',
        },             {
          from: './node_modules/onnxruntime-web/dist/ort-wasm-simd.wasm',
          to: 'static/chunks/pages',
        }]          
      }
    )
  )

  return config;
};


