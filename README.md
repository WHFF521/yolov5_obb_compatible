# Yolov5 for Oriented Object Detection

由于torch和一些库有废弃不能用的函数，将代码中涉及到的函数进行了最小限度的更改。已经能够跑通train过程。

# install

WSL2 Ubuntu 20.04

创建一个虚拟环境
```shell
conda create --name py39obb python=3.9
conda activate py39obb
```

安装cuda
```shell
# 更新pip
pip install --upgrade setuptools pip wheel
# 安装nvidia-pyindex
pip install nvidia-pyindex
# 安装cuda12
pip install nvidia-cuda-runtime-cu12
```

安装cuda版本torch
```shell
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128
```

安装依赖，编译Cpp文件
```shell
pip install -r requirements.txt
pip install ninja
pip install pycocotools
cd utils/nms_rotated
python setup.py build_ext --inplace
```

降级 numpy

```shell
pip uninstall numpy
pip install numpy==1.23.0
```


我所有的环境在`my_dependencies.txt`里面

# 运行指令

```shell
python -W ignore train.py --weights weights/yolov5s.pt --data dataset/DOTASplit-small/dota_obb_split.yaml --epochs 1 --batch-size 8 --img 1024 --name test-dota-img1024-batch8-epoch1 --cache   --device 0
```
