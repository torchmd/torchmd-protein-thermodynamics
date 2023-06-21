# Machine Learning Coarse-Grained Potentials of Protein Thermodynamics

This repository contains code, data and tutarial for reproducing the paper "Machine Learning Coarse-Grained Potentials of Protein Thermodynamics". https://arxiv.org/abs/2212.07492

## Background

Proteins are the fundamental building blocks of life, and understanding their behavior is crucial for many applications in biology and biotechnology. Thermodynamics is a key tool for studying the behavior of proteins, but traditional methods for simulating protein thermodynamics can be computationally expensive and time-consuming.

## Neural Network Potential

Neural network potentials offer a promising alternative for simulating protein thermodynamics. By using machine learning techniques, we can train a neural network to predict the thermodynamic behavior of proteins based on their structure and other factors. This approach can be much faster and more efficient than traditional methods, and it can also provide more accurate results.

## Contents

This repository contains the following:

- Code for training and evaluating neural network potentials
- Instructions to download datasets and trained models
- Tutorials for using the code and resources

## Getting Started

To get started with this repository, follow these steps:

1. Clone or download the repository to your local machine
2. Install the necessary dependencies:
```
conda env create -f env.yml
```
3. Follow the tutorials and documentation to learn how to use the code and resources

## Citation

Machine Learning Coarse-Grained Potentials of Protein Thermodynamics, https://doi.org/10.48550/arXiv.2212.07492

## License

Note. All the code in this repository is MIT, however we use several file format readers that are taken from Moleculekit which has a free open source non-for-profit, research license. This is mainly in torchmd/run.py. Moleculekit is installed automatically being in the requirement file. Check out Moleculekit here: https://github.com/Acellera/moleculekit
