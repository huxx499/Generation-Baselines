### Introduction
**Texar-PyTorch** is a toolkit aiming to support a broad set of machine learning, especially natural language processing and text generation tasks. Texar provides a library of easy-to-use ML modules and functionalities for composing whatever models and algorithms. The tool is designed for both researchers and practitioners for fast prototyping and experimentation.

Texar-PyTorch integrates many of the best features of TensorFlow into PyTorch, delivering highly usable and customizable modules superior to PyTorch native ones. 

Here we use two examples: **Seq2Seq** and **Transformer**, which are available [here](./examples).


### Installation
Texar-PyTorch requires:

* `python == 3.6` or `3.7`
* `torch >= 1.0.0`. Please follow the [official instructions](https://pytorch.org/get-started/locally/#start-locally) to install the appropriate version.

After `torch` is installed, install Texar from PyPI: 
```bash
pip install texar-pytorch
```

To use cutting-edge features or develop locally, install from source: 
```
git clone https://github.com/asyml/texar-pytorch.git
cd texar-pytorch
pip install .
```

To use *tensorboard* support with `Executor`, please install `tensorboardX` with the following command

```commandline
pip install tensorboardX
```


### Getting Started
* [Examples](./examples)
* [Documentation](https://texar-pytorch.readthedocs.io)


### Reference
If you use Texar, please cite the [tech report](https://arxiv.org/abs/1809.00794) with the following BibTex entry:

```
Texar: A Modularized, Versatile, and Extensible Toolkit for Text Generation
Zhiting Hu, Haoran Shi, Bowen Tan, Wentao Wang, Zichao Yang, Tiancheng Zhao, Junxian He, Lianhui Qin, Di Wang, Xuezhe Ma, Zhengzhong Liu, Xiaodan Liang, Wanrong Zhu, Devendra Sachan and Eric Xing
ACL 2019

@inproceedings{hu2019texar,
  title={Texar: A Modularized, Versatile, and Extensible Toolkit for Text Generation},
  author={Hu, Zhiting and Shi, Haoran and Tan, Bowen and Wang, Wentao and Yang, Zichao and Zhao, Tiancheng and He, Junxian and Qin, Lianhui and Wang, Di and others},
  booktitle={ACL 2019, System Demonstrations},
  year={2019}
}
```

### License
[Apache License 2.0](./LICENSE)
