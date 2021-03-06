# SCOOD-UDG (ICCV 2021)

[![paper](https://img.shields.io/badge/Paper-arxiv-b31b1b)](https://arxiv.org/abs/2108.11941)
&nbsp;
[![projectpage](https://img.shields.io/badge/Project%20Page-online-52b788)](https://jingkang50.github.io/projects/scood)
&nbsp;
[![gdrive](https://img.shields.io/badge/SCOOD%20dataset-google%20drive-f39f37)](https://drive.google.com/file/d/1cbLXZ39xnJjxXnDM7g2KODHIjE0Qj4gu/view?usp=sharing)&nbsp;
[![onedrive](https://img.shields.io/badge/SCOOD%20dataset-onedrive-blue)](https://entuedu-my.sharepoint.com/:u:/r/personal/jingkang001_e_ntu_edu_sg/Documents/scood_benchmark.zip?csf=1&web=1&e=vl8nr8)

This repository is the official implementation of the paper:

> **Semantically Coherent Out-of-Distribution Detection**<br>
> Jingkang Yang, Haoqi Wang, Litong Feng, Xiaopeng Yan, Huabin Zheng, Wayne Zhang, Ziwei Liu<br>
> Proceedings of the IEEE International Conference on Computer Vision (**ICCV 2021**)<br>

![udg](assets/udg.png)

## Dependencies

We use `conda` to manage our dependencies, and CUDA 10.1 to run our experiments.

You can specify the appropriate `cudatoolkit` version to install on your machine in the `environment.yml` file, and then run the following to create the `conda` environment:

```bash
conda env create -f environment.yml
conda activate scood
```

## SC-OOD Dataset

![scood](assets/benchmark_gif.gif)

The SC-OOD dataset introduced in the paper can be downloaded here.

[![gdrive](https://img.shields.io/badge/SCOOD%20dataset-google%20drive-f39f37)](https://drive.google.com/file/d/1cbLXZ39xnJjxXnDM7g2KODHIjE0Qj4gu/view?usp=sharing)&nbsp;[![onedrive](https://img.shields.io/badge/SCOOD%20dataset-onedrive-blue)](https://entuedu-my.sharepoint.com/:u:/r/personal/jingkang001_e_ntu_edu_sg/Documents/scood_benchmark.zip?csf=1&web=1&e=vl8nr8)

Our codebase accesses the dataset from the root directory in a folder named `data/` by default, i.e.

```
├── ...
├── data
│   ├── images
│   └── imglist
├── scood
├── test.py
├── train.py
├── ...
```

## Training

The entry point for training is the `train.py` script. The hyperparameters for each experiment is specified by a `.yml` configuration file (examples given in [`configs/train/`](configs/train/)).

All experiment artifacts are saved in the specified `args.output_dir` directory.

```bash
python train.py \
    --config configs/train/cifar10_udg.yml \
    --data_dir data \
    --output_dir output/cifar10_udg

python train.py --config configs/train/any.yml --data_dir data  --output_dir output/any
```

## Testing

Evaluation for a trained model is performed by the `test.py` script, with its hyperparameters also specified by a `.yml` configuration file (examples given in [`configs/test/`](configs/test/))

Within the configuration file, you can also specify which post-processing OOD method to use (e.g. ODIN or Energy-based OOD detector (EBO)).

The evaluation results are saved in a `.csv` file as specified.

```bash
python test.py \
    --config configs/test/cifar10.yml \
    --checkpoint output/cifar10_udg/best.ckpt \
    --data_dir data \
    --csv_path output/cifar10_udg/results.csv

python test.py --config configs/test/any.yml --checkpoint output/any/best.ckpt --data_dir data --csv_path output/any/results.csv
```

## Results

We report the mean ± std results from the current codebase as follows, which match the performance reported in our original paper.

### CIFAR-10 (+ Tiny-ImageNet) Results on ResNet18

You can run the following script (specifying the data and output directories) which perform training + testing for our main experimental results:

**CIFAR-10, UDG**

```bash
bash scripts/cifar10_udg.sh data_dir output_dir
```

| Metrics      |         ODIN |          EBO |           OE |       UDG (ours) |
| :----------- | -----------: | -----------: | -----------: | ---------------: |
| FPR95 ↓      | 50.76 ± 3.39 | 50.70 ± 2.86 | 54.99 ± 4.06 | **39.94** ± 3.77 |
| AUROC ↑      | 82.11 ± 0.24 | 83.99 ± 1.05 | 87.48 ± 0.61 | **93.27** ± 0.64 |
| AUPR In ↑    | 73.07 ± 0.40 | 76.84 ± 1.56 | 85.75 ± 1.70 | **93.36** ± 0.56 |
| AUPR Out ↑   | 85.06 ± 0.29 | 85.44 ± 0.73 | 86.95 ± 0.28 | **91.21** ± 1.23 |
| CCR@FPRe-4 ↑ |  0.30 ± 0.04 |  0.26 ± 0.09 |  7.09 ± 0.48 | **16.36** ± 4.33 |
| CCR@FPRe-3 ↑ |  1.22 ± 0.28 |  1.46 ± 0.18 | 13.69 ± 0.78 | **32.99** ± 4.16 |
| CCR@FPRe-2 ↑ |  6.13 ± 0.72 |  8.17 ± 0.96 | 29.60 ± 5.31 | **59.14** ± 2.60 |
| CCR@FPRe-1 ↑ | 39.61 ± 0.72 | 47.57 ± 3.33 | 64.33 ± 3.44 | **81.04** ± 1.46 |

### CIFAR-100 (+ Tiny-ImageNet) Results on WideResNet

You can run the following script (specifying the data and output directories) which perform training + testing for our main experimental results:

**CIFAR-100, UDG**

```bash
bash scripts/cifar100_udg.sh data_dir output_dir
```

| Metrics      |         ODIN |          EBO |           OE |   UDG (ours) |
| :----------- | -----------: | -----------: | -----------: | -----------: |
| FPR95 ↓      | 79.59 ± 1.36 | 78.86 ± 1.70 | 80.08 ± 2.80 | 76.03 ± 2.82 |
| AUROC ↑      | 77.45 ± 0.77 | 80.13 ± 0.56 | 79.24 ± 2.40 | 79.78 ± 1.41 |
| AUPR In ↑    | 75.25 ± 1.20 | 80.18 ± 0.57 | 80.24 ± 3.03 | 79.96 ± 2.02 |
| AUPR Out ↑   |  73.2 ± 0.77 | 73.71 ± 0.58 | 73.14 ± 2.19 | 74.77 ± 1.21 |
| CCR@FPRe-4 ↑ |  0.43 ± 0.21 |  0.58 ± 0.25 |  2.39 ± 0.74 |  1.47 ± 1.08 |
| CCR@FPRe-3 ↑ |  2.31 ± 0.60 |  3.46 ± 0.80 |  7.97 ± 1.47 |  5.43 ± 2.09 |
| CCR@FPRe-2 ↑ | 11.01 ± 1.29 | 17.55 ± 1.24 | 21.97 ± 2.92 | 18.88 ± 3.53 |
| CCR@FPRe-1 ↑ |  43.2 ± 1.80 | 51.54 ± 0.65 | 49.36 ± 3.98 | 48.95 ± 1.91 |

## License and Acknowledgements

This project is open-sourced under the MIT license.

The codebase is refactored by Ang Yi Zhe, and maintained by Jingkang Yang and Ang Yi Zhe.

## Citation

If you find our repository useful for your research, please consider citing our paper:

```bibtex
@InProceedings{yang2021scood,
    author = {Yang, Jingkang and Wang, Haoqi and Feng, Litong and Yan, Xiaopeng and Zheng, Huabin and Zhang, Wayne and Liu, Ziwei},
    title = {Semantically Coherent Out-of-Distribution Detection},
    booktitle = {Proceedings of the IEEE International Conference on Computer Vision},
    year = {2021}
}
```
