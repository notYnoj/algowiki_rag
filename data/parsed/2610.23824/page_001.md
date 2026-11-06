# Online Graph Coloring with Random Arrivals

Hirotaka Yoneda<sup>∗</sup> <br>
The University of Tokyo, Japan <br>
squar37@gmail.com

Masataka Yoneda<sup>†</sup> <br>
The University of Tokyo, Japan <br>
e869120@gmail.com

**Abstract**

We study online graph coloring in the random-arrival model, where the vertices are presented in a uniformly random order. Assuming _n_ and _k_ are known in advance, we present a randomized exponential-time algorithm that colors any _k_-colorable graph on _n_ vertices with _O(k_<sup>3</sup>log<sup>2</sup>_k_log<sup>4</sup>_n_) colors in expectation. This is the first online coloring algorithm that uses a polylogarithmic number of colors for all fixed \(k\ge 3\), and is better than a known lower bound of \(\Omega(log^{k-1}n)\) colors under adversarial arrivals for all fixed \(k\ge 6\).

In addition, assuming _n_ is known in advance, we obtain a competitive ratio of \(\widetilde{O}(n^{2/3})\). For comparison, it is known to be NP-hard to approximate (offline) graph coloring within a factor of \(n^{1-\varepsilon}\) for all fixed \(\varepsilon>0\). Therefore, our exponential-time online algorithm achieves a performance guarantee beyond the NP-hardness threshold for polynomial-time approximation algorithms.

<sup>∗</sup>Supported by JSPS JP25K24465, JST ASPIRE JPMJAP2302, and JST ACT-X JPMJAX25CT. <sup>†</sup>Supported by JSPS JP25K24465 and JST ASPIRE JPMJAP2302.

