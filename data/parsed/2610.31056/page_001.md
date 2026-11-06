Pigeonhole Equal Subset Sum: Subexponential Algorithm, Tight Lower Bounds, and Average-Case Analysis

**Abstract**

The Equal Subset Sum problem asks, given _n_ positive integers bounded by _M_, to find two distinct non-empty subsets with the same sum. We study this problem in the regime _M_=2<sup>_o(n_)</sup>, where the pigeonhole principle guarantees that a solution exists, and the main challenge is to find one efficiently. A straightforward dynamic-programming algorithm runs in time \(\mathrm{poly}(n)\cdot M\), and after a sequence of improvements, the current best algorithm, due to Jin, Williams, and Zhang (ESA 2025), achieves running time \(\mathrm{poly}(n)\cdot M^{1/3}\).

In this work, we give the first \(\mathrm{poly}(n)\cdot M^{o(1)}\)-time algorithm for Equal Subset Sum in the regime _M_=2<sup>_o(n_)</sup>. We complement this algorithmic result with a tight conditional lower bound showing that any substantial improvement would require a major breakthrough in approximation algorithms for lattice problems, building on recent techniques of Vafa and Vaikuntanathan (S 2025).

Finally, we show that our techniques yield an asymptotically faster algorithm for the regime when \(M=\Theta(2^n)\): a \(\mathrm{poly}(n)\cdot 2^{n/4}\)-time algorithm in the average case.

## 1 Introduction

Equal Subset Sum is a fundamental problem in combinatorial optimization. The problem can be stated as follows: given a set _S_ of _n_ positive integers bounded by _M_, find two distinct subsets \(A,B\subseteq S\) such that \(\Sigma(A)=\Sigma(B)\), where \(\Sigma(\cdot)\) denotes the sum of the integers in the set. A

<sup>∗</sup>Nanyang Technological University, Singapore. Supported by the Nanyang Assistant Professorship (NAP) and an SUG grant (#025774-00001), both funded by Nanyang Technological University. <sup>†</sup>Work done while at CISPA Helmholtz, Germany. Supported by the European Union (ERC, LACONIC, 101041207). Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European Union or the European Research Council. Neither the European Union nor the granting authority can be held responsible for them. <sup>‡</sup>Max Planck Institute for Informatics, Germany. Supported by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) grant number 559177164.

arXiv:2610.31056v1 [cs.DS] 22 Oct 2026

Deepak Bhati<br> CISPA Helmholtz, Saarbrücken, Germany<br> deepak2602161@gmail.com

Antoine Joux<br> CISPA Helmholtz, Saarbrücken, Germany<br> joux@cispa.de

Pranjal Dutta<sup>∗</sup> Nanyang Technological University, Singapore<br> pranjal.dutta@ntu.edu.sg

Mahesh Sreekumar Rajasree<sup>†</sup> University of Warsaw, Warsaw srmahesh1994@gmail.com

Karol Węrzycki<sup>‡</sup> Max Planck Institute for Informatics, Saarbrücken, Germany kwegrzyc@mpi-inf.mpg.de

