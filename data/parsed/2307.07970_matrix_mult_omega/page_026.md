Thus, 2<sup>_o(n_)</sup> independent copies of \(\big(\mathrm{CW}_q^{\otimes 2^{\ell-1}}\big)^{\otimes n}\) can be degenerated into \(2^{(A_1E_1+A_2E_2+A_3E_3-o_{1/\varepsilon}(1))n-o(n)}\) independent copies of a direct sum of all level-\(\ell\) interface tensor with parameter list

\(\big\{\big(n\cdot A_r\cdot\alpha^{(r)}\big(i,j,k\big),i,j,k,\xi_{X,i,j,k}^{(r)},\xi_{Y,i,j,k}^{(r)},\xi_{Z,i,j,k}^{(r)}\big)\big\}_{r\in[3],i+j+k=2^\ell}\)

over all such \(\big\{\xi_{W,i,j,k}^{(r)}\big\}\in\widetilde{\mathcal{D}}\), and because a direct sum of some tensors can be degenerated into the sum of these tensors, the theorem follows.

The remainder of this section aims to show and analyze an algorithm that proves Proposition 5.1.

## 5.1 Dividing into Regions

Similar to \[DWZ23\], we consider<tbc>

\(\big(\mathrm{CW}_q^{\otimes 2^{\ell-1}}\big)^{\otimes n}\equiv\big(\mathrm{CW}_q^{\otimes 2^{\ell-1}}\big)^{\otimes A_1\cdot n}\otimes\big(\mathrm{CW}_q^{\otimes 2^{\ell-1}}\big)^{\otimes A_2\cdot n}\otimes\big(\mathrm{CW}_q^{\otimes 2^{\ell-1}}\big)^{\otimes A_3\cdot n}\)

<tbc>for \(A_1,A_2,A_3\ge 0\) and _A_<sub>1</sub>+_A_<sub>2</sub>+_A_<sub>3</sub>=1. We call each of the three factors of the above tensor product a _region_. For \(r\in[3]\), we denote the _r_-th region as

\(\mathcal{T}^{(r)}:=\big(\mathrm{CW}_q^{\otimes 2^{\ell-1}}\big)^{\otimes A_r\cdot n}.\)

The idea is to apply asymmetric hashing on the three regions separately. We will use asymmetric hashing that shares level-\(\ell Z\)-blocks in the first region, _Y_ -blocks in the second region, and _X_-blocks in the third region. Each region will be degenerated into independent copies of a level-\(\ell\) interface tensor and the output will be the tensor product of the independent copies of the three level-\(\ell\) interface tensors from the three regions. Thus we can analyze each region independently and we only give the detailed analysis on the first region as the analysis for the other two regions follow by symmetry.

From now on, we will describe the analysis on T <sup>(1)</sup> in which the level-\(\ell Z\)-variable blocks are shared and we will omit the superscript (1) on all variables for conciseness.

## 5.2 Asymmetric Hashing

Recall that \(\alpha\) is a distribution on \(\{(i,j,k)\in\mathbb{Z}_{\ge 0}^3|i+j+k=2^\ell\}\), i.e., it can be viewed as a distribution on level-\(\ell\) constituent tensors. Recall that \(\alpha\) induces marginal distributions \(\alpha_X,\alpha_Y,\alpha_Z\). We first zero out _X_-, _Y_ -, _Z_-blocks that are not consistent with the marginals \(\alpha_X,\alpha_Y,\alpha_Z\) respectively. Let _N_<sub>BX</sub> be the number of remaining level-\(\ell X\)-blocks, and it is not difficult to see that

\(N_\mathrm{BX}=2^{H(\alpha_X)\cdot A_1n\pm o(n)}.\) (4)

Similarly, let _N_<sub>BY</sub> and _N_<sub>BZ</sub> be the number of remaining _Y_ - and _Z_-blocks, and we have

\(N_\mathrm{BY}=2^{H(\alpha_Y)\cdot A_1n\pm o(n)},N_\mathrm{BZ}=2^{H(\alpha_Z)\cdot A_1n\pm o(n)}.\) (5)

Let \(N_\alpha\) be the number of remaining block triples that are consistent with \(\alpha\). We have

\(N_\alpha=2^{H(\alpha)\cdot A_1n\pm o(n)}.\) (6)

Finally, let \(N_{\alpha_X,\alpha_Y,\alpha_Z}\) be the number of remaining block triples _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_.

