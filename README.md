# tensorflow-yolo





<p align="center"> <img src="demo.gif"/> </p>

## Dependencies

Python3, tensorflow 1.0, numpy, opencv 3.

### Getting started

**`git clone https://github.com/thtrieu/darkflow.git`**

You can choose _one_ of the following three ways to get started with darkflow.

1. Just build the Cython extensions in place. NOTE: If installing this way you will have to use `./flow` in the cloned darkflow directory instead of `flow` as darkflow is not installed globally.
    
    `python3 setup.py build_ext --inplace`
    

2. Let pip install darkflow globally in dev mode (still globally accessible, but changes to the code immediately take effect)
    
    `pip install -e .`
    

3. Install with pip globally
    
  ` pip install .`
    

`pip install tensorflow_gpu==1.9.0, opencv-python numpy`

----------
### test darknet ##

>>> from darkflow.net.build import TFNet
>>>

`>>>python yolo.py`