# A Robust GPU-Accelerated Kernel Compensation Solver with Novel Discretization for Photonic Crystals in Anisotropic Media<sup>⋆</sup>

ARTICLE INFO

_Keywords:_ Photonic crystals Anisotropic media Yee’s scheme Kernel compensation method Matrix-free operations GPU acceleration

ABSTRACT

This paper develops a robust solver for the Maxwell eigenproblem in 3D photonic crystals with anisotropic media. The solver employs the kernel compensation technique under the framework of Yee’s scheme to eliminate null space and enable matrix-free, GPU-accelerated operations via 3D discrete Fourier transform. Furthermore, we propose a novel discretization for permittivity tensor containing off-diagonal entries and prove that the resulting matrix is Hermitian positive definite, which ensures the correctness of the kernel compensation technique. Numerical experiments on several benchmark examples are demonstrated to validate the robustness and accuracy of our scheme.

### 1. Introduction

Photonic crystals (PCs) are periodic dielectric or metallic nanostructures recognized as a cornerstone of modern photonics [9]. By offering a mechanism to create photonic bandgaps, PCs provide special capabilities to mold the flow of light, which is essential for developing integrated devices such as efficient spectral filters, on-chip lasers, and optical transistors. The mathematical challenge lies in effectively solving the time-harmonic Maxwell’s equations for dealing with null space and numerical accuracy. The governing system, defined in R<sup>3</sup>, starts with:

\(\left\{\begin{array}{ c c } \nabla\times(\varepsilon^{-1}\nabla\times H)=\omega^2H, & \text{in}\mathbb{R}^3, \\ \nabla\cdot H=0, & \text{in}\mathbb{R}^3.
\end{array}\right.\) (1.1)

In this eigenvalue problem, \(\omega\) is the frequency, **_H_** is the magnetic field and \(\varepsilon\) is the normalized dielectric coefficient. According to Bloch’s theorem, **_H_** satisfies the quasi-periodic condition

\(H(x+a_i)=e^{i\mathbf{k}\cdot a_i}H(x),i=1,2,3,\) (1.2)

where \(\mathbf{k}=(k_1,k_2,k_3)\in\mathbb{R}^3\) is the wave number vector located in the first Brillouin zone, \(\left\{a_i\right\}_{i=1}^3\) are lattice translation vectors that span the primitive cell

\(\Omega:=\left\{x\in\mathbb{R}^3:x=\sum_{i=1}^3x_ia_i,x_i\in[0,1],i=1,2,3\right\}.\) (1.3)

One can find detailed definitions of {**_a_**_<sub>i</sub>_} and **_k_** in (4.1), (4.2) in Section 4. We introduce the transformation \(H_\mathbf{k}(x):=e^{-i\mathbf{k}\cdot x}H(x)\) to convert the problem into the one with pure periodic boundary conditions involving the shifted nabla operator \(\nabla_\mathbf{k}:=\nabla+i\mathbf{k}I\). To avoid ambiguity of notation, the subscript "**_k_**" of "**_H_**<sub>**_k_**</sub>" is left out. We keep using "**_H_**" to

<sup>⋆</sup>This work was supported by Strategic Priority Research Program of the Chinese Academy of Sciences (XDB0640000, XDB0640300, XDB0620203, XDA0480504), National Key Research and Development Program of China (2023YFB3309104), Natural Science Foundations of China (No. 1233000214), National Key Laboratory of Computational Physics (No. 6142A05230501), National Science Challenge Project (TZ2025007), National Center for Mathematics and Interdisciplinary Science, CAS. <sup>∗</sup>Corresponding author `kanit@mail.ustc.edu.cn` (C. Jin); `hhxie@lsec.cc.ac.cn` (H. Xie) ORCID(s): 0009-0001-5857-5400 (C. Jin); 0000-0002-1947-9256 (H. Xie)

Chenhao Jin<sup>_a_</sup>, Hehu Xie<sup>_b,c,_∗</sup>

<sup>_a_</sup>_School of Mathematical Sciences, University of Science and Technology of China, Hefei, Anhui, 230026, China_ <sup>_b_</sup>_SKLMS, Academy of Mathematics and Systems Science, Chinese Academy of Sciences, No.55, Zhongguancun Donglu, Beijing, 100190, China_ <sup>_c_</sup>_School of Mathematical Sciences, University of Chinese Academy of Sciences, Beijing, 100049, China_

arXiv:2511.17107v3 [math.NA] 25 Apr 2026

