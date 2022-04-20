// A simple program that computes the square root of a number
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <string>

#include <onnxruntime_cxx_api.h>

int main(int argc, char* argv[])
{
    const wchar_t* model_path = L"squeezenet.onnx";

    Ort::Env env;
    Ort::SessionOptions session_options;
    session_options.SetIntraOpNumThreads(1);
    session_options.SetGraphOptimizationLevel(GraphOptimizationLevel::ORT_ENABLE_EXTENDED);
    Ort::RunOptions run_options = Ort::RunOptions();

    Ort::Session session(env, model_path, session_options);
    Ort::IoBinding io_binding{session};

    Ort::AllocatorWithDefaultOptions allocator;
    auto memory_info = Ort::MemoryInfo::CreateCpu(OrtArenaAllocator, OrtMemTypeDefault);

    std::vector<int64_t> input_node_dims;

    // print input node names
    char* input_name = session.GetInputName(0, allocator);
    printf("Input: name=%s\n", input_name);

    // print input node types
    Ort::TypeInfo type_info = session.GetInputTypeInfo(0);
    auto tensor_info = type_info.GetTensorTypeAndShapeInfo();

    ONNXTensorElementDataType type = tensor_info.GetElementType();
    printf("Input: type=%d\n", type);

    // print input shapes/dims
    input_node_dims = tensor_info.GetShape();
    printf("Input: num_dims=%zu\n", input_node_dims.size());
    for (size_t j = 0; j < input_node_dims.size(); j++) {
        printf("Input: dim %zu=%jd\n", j, input_node_dims[j]);
    }

    size_t input_tensor_size = 224 * 224 * 3;  // simplify ... using known dim values to calculate size
                                             // use OrtGetTensorShapeElementCount() to get official size!

    std::vector<float> input_tensor_values(input_tensor_size);

    auto input_tensor = Ort::Value::CreateTensor<float>(memory_info, input_tensor_values.data(), input_tensor_size, input_node_dims.data(), 4);

    io_binding.BindInput(input_name, input_tensor);

    Ort::MemoryInfo output_mem_info{"Cuda", OrtDeviceAllocator, 0, OrtMemTypeDefault};
  
    // Use this to bind output to a device when the shape is not known in advance.
    // If the shape is known you can use the other overload of this function that takes an Ort::Value as input
    // (IoBinding::BindOutput(const char* name, const Value& value)).
    // This internally calls the BindOutputToDevice C API.

    io_binding.BindOutput("softmaxout_1", output_mem_info);
 
    session.Run(run_options, io_binding);
  
    return 0;
}
