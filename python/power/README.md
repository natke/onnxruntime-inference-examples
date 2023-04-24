# Measure the difference in power consumption between PyTorch and ONNX Runtime

## Setup

```bash
pip install onnxruntime-gpu
pip install transformers
pip install torch (or GPU version)
```

## Tools

https://github.com/Breakend/experiment-impact-tracker

nvidia-smi

nvcc

https://github.com/Syllo/nvtop


https://developer.nvidia.com/nvidia-management-library-nvml 


## Current error

```bash
$ python run_session.py 
Traceback (most recent call last):
  File "C:\Users\nakersha\Develop\code\microsoft\onnxruntime-inference-examples\python\power\run_session.py", line 3, in <module>
    import session_resources as sr
  File "C:\Users\nakersha\Develop\code\microsoft\onnxruntime-inference-examples\python\power\session_resources.py", line 2, in <module>
    import score
  File "C:\Users\nakersha\Develop\code\microsoft\onnxruntime-inference-examples\python\power\score.py", line 8, in <module>
    from experiment_impact_tracker.compute_tracker import ImpactTracker
  File "C:\Users\nakersha\Miniconda3\envs\power\lib\site-packages\experiment_impact_tracker\compute_tracker.py", line 16, in <module>
    from pandas.io.json import json_normalize
ImportError: cannot import name 'json_normalize' from 'pandas.io.json' (C:\Users\nakersha\Miniconda3\envs\power\lib\site-packages\pandas\io\json\__init__.py)
(power) 
```