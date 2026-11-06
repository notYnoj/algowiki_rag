<tbc>Two of the most prominent examples of optimization problems in which each constraint contains exactly two variables are MaxCut and Max-_k_-Cut. For MaxCut, a semicircle law restricted to half the minimum distance cannot give a constant improvement over random guessing \[Par25\]. On the other hand, despite the low minimum distance, suitable ensembles of regular graphs permit reliable decoding of a linear number of random errors \[DZ97; NZ16\]. This discrepancy suggests that DQI could be performant on such ensembles. To realize these gains, one must move beyond an understanding of DQI in terms of worst-case decoding guarantees, as dictated by the code minimum distance. Within classical error correction, code performance is more reliably captured by _noise thresholds_ with respect to a given communication channel, which only require success with high probability. Analogously, one should expect DQI to perform reliably out to thresholds corresponding to the noise that the algorithm artificially generates via the weights **w**.

In §2 we prove a version of the semicircle law that applies to fixed Max-LINSAT target sets and accounts for decoding errors. Our fixed-target semicircle law, Theorem 1, together with our LP decoding theorem Theorem 6 and Corollary 2, proves that DQI can, in polynomial time, achieve a satisfaction fraction on MaxCut and Max-_k_-Cut that is asymptotically bounded away from random guessing, but not sufficient to achieve quantum advantage over known classical algorithms. Our algorithmic conclusions are summarized in  2.

## Notation and conventions

Throughout this manuscript, _q_ is a prime power and F_<sub>q</sub>_ is the unique finite field of size _q_. As a caution, note \(\mathbb{F}_q\neq\mathbb{Z}_q\) when _q_ is not prime. We write \(\mathbb{F}_q^\times=\mathbb{F}_q\backslash\{0\}\) for the multiplicative subgroup. For a vector \(\mathbf{v}\in\mathbb{F}^n\) over a field F, let supp**v** be the set of nonzero entries, and |**v**|:=|supp**v**| the Hamming weight. The Hamming distance between words **x** and **y** is |**x**-**y**|. The distance between vertices _u_ and _v_ in graph _G_ is \(\delta_G(u,v)\). The degree of vertex _u_ is _d<sub>G</sub>(u_). The indicator function for a set _A_ is 1_<sub>A</sub>_.

\begin{tabular}{cccc}
**Problem** & **Algorithm** & **Worst-case runtime** & **Expected cut fraction** \\
\multirow{3}{*}{MaxCut} & Random Guess & _O(n_) & \(\frac{1}{2}\) \\
 & TPM & Poly(_n_) & \(\frac{1}{2}+\frac{2}{\pi\sqrt{D}}+O(D^{-1})\) \\
 & DQI + ML & Poly(_n_) & \(\frac{1}{2}\left(1+\frac{1}{D-1}\right)\) \\
\multirow{4}{*}{Max-_k_-Cut (_k\>_2)} & Random Guess & _O(n_) & \(\frac{k-1}{k}\) \\
 & TPM & Poly(_n_) & \(\frac{k-1}{k}+\frac{\kappa_k}{\sqrt{D}}+O_k(D^{-1})\) \\
 & DQI + ML & Exp(_n_) & \(\frac{k-1}{k}\left(1+\frac{1}{D-1}\right)+o(D^{-1})\) \\
 & DQI + LP & Poly(_n_) & \(\frac{k-1}{k}\left(1+\frac{1}{\sqrt{k-1}(D-1)^2}\right)+o(D^{-2})\) \\
\end{tabular}

** 2:** Algorithmic comparison for MaxCut and Max-_k_-Cut, where _k\>_2 is a fixed prime power. The cut fractions concern the Linial-Simkin graph family of Definition 4, with the large-graph limit taken before the large-_D_ limit. The constant \(\kappa_k\) is defined in (95); the DQI + LP entry uses the \(c\uparrow 1\) limit of the certified rate in (85). See §4.1 for details.

