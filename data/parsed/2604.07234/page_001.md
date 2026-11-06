# THE RANDOM SUBSEQUENCE MODEL AND UNIFORM CODES FOR THE DELETION CHANNEL

Abstract. We introduce the _Random Subsequence Model_, a spin glass model on pairs of random strings \((X,Y)\in\{0,1\}^N\times\{0,1\}^M\) whose partition function counts subsequence embeddings of _Y_ into _X_. We study two variants: the null model, where _X_ and _Y_ are independent and uniform, and the planted model, where _X_ is uniform and _Y_ is a uniformly-random length-_M_ subsequence of _X_. We connect the Random Sub- sequence Model to longstanding problems in various fields, including the best rate achievable by uniformly- random codes in the deletion channel, the longest common subsequence problem between two random strings, and models of directed polymers in statistical physics.

In the regime where \(N,M\rightarrow\infty\) at a fixed ratio \(\alpha=M/N\in(0,1)\), we exhibit strict asymptotic separations between the null annealed free energy and the quenched free energies of the null and planted models at all values of the density parameter \(\alpha\). This suggests that these models are in a spin glass phase at zero temperature throughout the entire dense regime. As a consequence, we show that uniformly-random codes achieve a positive rate in the deletion channel for all deletion probabilities \(p\in[0,1)\), settling multiple conjectures of [PIW24] and proving the first such positive rate result for the regime \(p\ge 1/2\).

We also give an exact analytic formula for the annealed free energy of the planted model for all values of the density parameter. This implies a corresponding analytic upper bound on the best rate achievable by uniformly-random codes in the deletion channel, complementing the lower bound from our first result. Our upper and lower bounds for the capacity of the deletion channel under uniform codes are far closer to each other than the best known upper and lower bounds for the capacity of the deletion channel.

### 1. Introduction

This paper introduces and studies the _Random Subsequence Model_, a new spin glass model whose zero- temperature partition function counts order-preserving subsequence embeddings for pairs of random binary strings. Given natural numbers \(M\le N\), the _configuration space_ of the model is

\(\Sigma=\Sigma_{N,M}:=\left\{\sigma:[M]\rightarrow[N]:\sigma\text{is strictly increasing}\right\}.\)

Given a pair of random strings \((X,Y)\in\{0,1\}^N\times\{0,1\}^M\), which we call the _disorder_, the _partition function_ is defined as

(1.1) \(Z_{X,Y}:=|S_{X,Y}|:=|\{\sigma\in\Sigma:X_\sigma=Y\}|,\)

where, for a configuration \(\sigma\in\Sigma\), we write

\(X_\sigma=\left(X_{\sigma(1)},\dots,X_{\sigma(M)}\right)\in\{0,1\}^M.\)

In words, _Z<sub>X,Y</sub>_ counts the number of order-preserving embeddings of _Y_ into _X_ as a subsequence. Fixing a density parameter \(\alpha\in(0,1)\), we are interested in the asymptotic regime in which \(N,M\rightarrow\infty\) with \(M/N\rightarrow\alpha\in[0,1]\) under two natural laws on the disorder.

**Null.** _X_ and _Y_ are drawn independently and uniformly from {0,1}_<sup>N</sup>_ and {0,1}_<sup>M</sup>_, respectively.

**Planted.** _X_ is drawn uniformly from {0,1}_<sup>N</sup>_, \(\sigma^*\) is drawn independently of _X_ and uniformly from \(\Sigma\), and we set \(Y=X_{\sigma^*}\).

<sup>∗</sup>Department of Statistics, Stanford University. Email: rsjeong@stanford.edu. <sup>©</sup>Department of Electrical Engineering and Computer Science, Massachusetts Institute of Technology. Email: fpernice@ mit.edu.

arXiv:2604.07234v1 [cs.IT] 8 Apr 2026

RYAN JEONG<sup>∗</sup> AND FRANCISCO PERNICE<sup>©</sup>

