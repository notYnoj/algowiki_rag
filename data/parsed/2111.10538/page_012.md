\(\widetilde{\mathfrak{sm}}(\mathfrak{sa}_1)\le\widetilde{\mathfrak{lg}}(\mathfrak{sa}_1)\le\widetilde{\mathfrak{sm}}(\mathfrak{sa}_2)\le\widetilde{\mathfrak{lg}}(\mathfrak{sa}_2)\le\dots\le\widetilde{\mathfrak{sm}}(\mathfrak{sa}_\sqrt{n})\le\widetilde{\mathfrak{lg}}(\mathfrak{sa}_\sqrt{n}).\)

Random sampling does not guarantee that the sampled intervals are monotone. To address this issue, we introduce the notion of _pseudo-solutions_. A pseudo-solution is an assignment of monotone intervals to subarrays in order to approximate sm(sa_<sub>i</sub>_) and lg(sa_<sub>i</sub>_). The _quality_ of a pseudo-solution with intervals \([\ell_1,r_1],[\ell_2,r_2],\dots,[\ell_\sqrt{n},r_\sqrt{n}]\) is equal to \(\sum_i\text{lis}^{[\ell_i,r_i]}(\mathfrak{sa}_i)\). For a fixed pseudo-solution, this can be easily approximated via random sampling. Thus, our goal is to construct a pseudo- solution whose quality is at least an \(\Omega(\lambda^3)\) approximation of the size of the optimal solution. To this end, we present a greedy method in Section 6.2 to construct the desired pseudo-solution.

Finally, in Section 6.4, we show how the above ideas can be generalized to improve the running time down to \(\widetilde{O}(n^\kappa\text{poly}(1/\lambda))\) for any arbitrarily small \(\kappa>0\) by imposing a factor \(\text{poly}(1/\lambda)^\text{12}\) to the approximation guarantee.

<sup>12</sup>The exponent of \(1/\lambda\) exponentially depends on \(1/\kappa\).

sa 1
sa 2
sa 1
sa Vn
(sa)
(sa)
An approximately optimal solution domain

Figure 3: Red rectangles show the elements of sa_<sub>i</sub>_ that contribute to lis(_A_) and gray circles show the elements of sa that are sampled via our algorithm.

