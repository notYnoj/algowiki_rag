# An improved fast iterative moment method for the simulation of near-continuum gas flows with Shakhov model \(^\star\)

Zhenning Cai<sup>a</sup>, Zhicheng Hu<sup>b,c,∗</sup>, Guanghan Li<sup>b,c</sup>, Chunwu Wang<sup>b,c</sup>, Xiaowen Wang<sup>b,c</sup>

<sup>_a_</sup>_Department of Mathematics, National University of Singapore, Level 4, Block S17, 10 Lower Kent Ridge Road, 119076, Singapore_

<sup>_b_</sup>_School of Mathematics, Nanjing University of Aeronautics and Astronautics, Nanjing, 211106, China_

<sup>_c_</sup>_Key Laboratory of Mathematical Modelling and High Performance Computing of Air Vehicles (NUAA), Nanjing, 211106, China_

**Abstract**

The fast iterative moment (FIM) method developed in [G. Li, C. Wang, and Z. Hu, Comput. Fluids, 311 (2026), 107031] achieves fast convergence for near-continuum gas flows modeled by the Boltzmann-BGK equation through alternating iterations between the high-order moment system and the consistent hydrodynamic equations. In this paper, we extend the FIM solver to the Shakhov model and improve it in the following aspects. A finite volume method with linear reconstruction is employed for high-resolution spatial discretization of both systems. Following the original FIM method, an implicit-explicit scheme treating the Shakhov collision term implicitly is adopted for the high-order moment system. A local Fourier analysis of a linearized one-dimensional BGK model reveals the need for more hydrodynamic iterations at smaller Knudsen numbers and their slower convergence on refined grids. Motivated by these findings, a Newton-multigrid method with a new regularization strategy is introduced for the hydrodynamic equations, generally providing an effective hydrodynamic correction with one step per alternating iteration, thereby reducing the need for empirical tuning. Numerical experiments for planar Couette flow, lid-driven cavity flow, and heat transfer in a bottom-heated cavity are carried out to investigate the performance of the improved FIM solver. The results demonstrate improved efficiency and robustness over the original FIM method, particularly at small Knudsen numbers, and favorable performance with both first- and second-order spatial discretizations.

_Keywords:_ Boltzmann equation, Shakhov model, fast iterative moment method, linear reconstruction, Newton-multigrid method <br>
_2000 MSC:_ 76P05, 65B99, 65M55

### 1. Introduction

In rarefied gas flows, the degree of gas rarefaction is characterized by the Knudsen number _Kn_, which is defined as the ratio between the mean free path \(\lambda\) of gas molecules and the characteristic flow length _L_. The Navier-Stokes-Fourier (NSF) equations based on the continuum fluid hypothesis are usually applicable up to _Kn_∼0.001 [1]. When _Kn_ is larger, the continuum hypothesis breaks down and the NSF equations fail to capture the non-conventional behaviour of the rarefied flow. To model rarefied gas dynamics accurately, mesoscopic kinetic models are generally adopted, among which the Boltzmann equation is the most fundamental one. However, despite the rapid development of modern high-performance computing, the numerical simulation of this equation remains computationally challenging due to its high dimensionality and nonlinear integro-differential structure. To balance efficiency and accuracy, a popular strategy in the near-continuum flow regime (0.001 _\<Kn\<_0.1) is to replace the complex collision integral<tbc>

\(^\star\)The work of Zhenning Cai was supported by the Academic Research Fund of the Ministry of Education of Singapore under grant A-8002392-00-00. The work of others was partially supported by the National Natural Science Foundation of China, No. 12171240 and the National Science and Technology Major Project, No. J2019-II-0007-0027. The computational resources were supported by High Performance Computing Platform of Nanjing University of Aeronautics and Astronautics, China. \(^\star\)Corresponding author: Zhicheng Hu _Email addresses:_ matcz@nus.edu.sg (Zhenning Cai), huzhicheng@nuaa.edu.cn (Zhicheng Hu), liguanghan@nuaa.edu.cn (Guanghan Li), wangcw@nuaa.edu.cn (Chunwu Wang), wangxw@nuaa.edu.cn (Xiaowen Wang)

