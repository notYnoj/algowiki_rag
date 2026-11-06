## A Model architecture and training details

We use the same set of hyperparameters to train all models and implement early stopping with patience of 50 epochs. The specifications of the hyperparameters are in s 6 and 7.

We implemented the complex neural layers, entire models, and CG solver in JAX and trained each model in  1 using the same random seeds and patience for early stopping. Figure 8 shows the training dynamics of the two models on _L=_16 cases. The code is available at https://github.com/iamyixuan/MatrixPreNet<sup>4</sup>.

### A.1 Hyperparameter search

We investigate the impact of various hyperparameters to the model performance using both the FNO and FCN models. Through Bayesian optimization using DeepHyper \[6\], we identify most important sets of hyperparameters determining the NN-preconditioners’ performance. The results are visualized in Figure 9.

For the \(\mathcal{N}_{L16}^\mathrm{FNO}\) model, a larger batch size, fewer Fourier modes, fewer FNO blocks, and a smaller learning rate leads to a lower validation loss. Meanwhile, for the \(\mathcal{N}_{L16}^\mathrm{FCN}\) model, a smaller batch size and kernel size, higher hidden dimensions, and a smaller learning rate are corresponding to a lower validation loss. However, in both models, despite the impact of the various hyperparameters, the variation in validation loss across hyperparameter configurations is small relative to the absolute<tbc>

<sup>4</sup>The repository will be made public upon acceptance of this work.

\begin{tabular}{cc}
Hyperparameter & Value \\
# FNO blocks & 4 \\
# Fourier modes & 8 \\
# Lifting layers per block & 1 \\
# Projection layers per block & 1 \\
Activation & PReLU \\
Batch size & 128 \\
Optimizer & Adam \\
Learning rate & 1e-4 \\
Early stopping patience & 50 \\
\end{tabular}

\begin{tabular}{cc}
Hyperparameter & Value \\
# Layers & 4 \\
# Hidden channels & 16 \\
Kernel size & 3 \\
Activation & PReLU \\
Batch size & 128 \\
Optimizer & Adam \\
Learning rate & 1e-4 \\
Early stopping patience & 50 \\
\end{tabular}

6. Hyperparameters of the FNOs

7. Hyperparameters of the FCN

