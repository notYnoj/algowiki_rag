### Correctness.

First, we prove the following:

**Claim 4.0.2.** _If the algorithm does not detect a collision, then_

\(|\mathcal{A}_i^{(j)}|\ge W,\)

_for all_ \(j\in\{0,\dots,\mathrm{log}k\}\) _and_ \(i\in[k/2^j]\).

_Proof:_ Suppose, for contradiction, that the claim is false. Let \(j\ge 0\) be the smallest index for which it fails. We must have _j\>_0, since in the base case we have \(|\mathcal{A}_i^{(0)}|=2^{\lfloor n/k\rfloor}\) for all \(i\in[k]\).

So assume that \(|\mathcal{A}_i^{(j)}|<W\) for some \(i\in[k/2^j]\), and let \(\mathcal{B}:=\mathcal{A}_{2i-1}^{(j-1)}+\mathcal{A}_{2i}^{(j-1)}\). Since the algorithm did not detect a collision at levels _\<j_, it must be that \(|\mathcal{A}_{2i-1}^{(j-1)}|\) and \(|\mathcal{A}_{2i}^{(j-1)}|\) are at least _W_. Hence \(|\mathcal{B}|\ge W^2\), as the algorithm did not detect a collision at level _j_.

On the other hand, by Claim 4.0.1:<tbc>

\(\mathcal{B}=\mathcal{B}_{i,0}^{(j)}\unknown\mathcal{B}_{i,1}^{(j)}\unknown\dots\unknown\mathcal{B}_{i,W-1}^{(j)},\)

<tbc>and by the assumption that \(|\mathcal{B}_{i,p}^{(j)}|\le|\mathcal{A}_i^{(j)}|<W\) for all \(p\in\{0,\dots,W-1\}\), we get:

\(|\mathcal{B}|=\sum_{p=0}^{W-1}|\mathcal{B}_{i,p}^{(j)}|\le\sum_{p=0}^{W-1}|\mathcal{A}_i^{(j)}|<W^2,\)

contradicting \(|\mathcal{B}|\ge W^2\).

With Claim 4.0.2, we can now conclude the proof of Theorem 1.1. Let \(\mathcal{C}=\mathcal{A}_1^{(\mathrm{log}k)}\) and \(p=p_1^{(\mathrm{log}k)}\), and assume that the algorithm did not detect a collision in any of the previous steps. By Claim 4.0.2, we have \(|\mathcal{C}|\ge 2\), so there exist two distinct elements \(a,b\in\mathcal{C}\) such that:

\(a\equiv b\equiv p(\mathrm{mod}W^{\mathrm{log}k}).\)

However, both _a_ and _b_ are bounded above by \(n\cdot M\le 2^{\lfloor n/k\rfloor\mathrm{log}k}\le W^{\mathrm{log}k}\), so the congruence implies _a=b_, contradicting the assumption that no collision was detected.

**Remark 1.** _By plugging in the exact parameters, for k_=2<sup>7</sup>_, algorithm behind Theorem 1.1 solves Equal Subset Sum in_ O<sup>⋆</sup>(2<sup>_n/_64</sup>) _time when_ \(nM\le 2^{7n/128}<2^{n/18}\).

## 5 Conditional Lowerbound: Proof of Theorem 1.2

In this section, we present our lower bound for solving the Pigeonhole Equal Subset Sum problem in the strong regime by reducing it to the problem of finding a short vector in a lattice. We assume reader is familiar with Section 3.

### 5.1 Construction

In this section, we present a reduction from SIVP to PESS. At a high level, the reduction first computes a sufficiently short basis of the input lattice L. It then uses this basis to sample many lattice points from a suitable discrete Gaussian distribution and encodes these samples as positive integers. These integers are given to the PESS algorithm, whose output yields two collision sets. From these sets, the reduction extracts a short-ish (non-zero) lattice vector in L. We begin by describing the basis reduction and sampling procedure used in the reduction, followed by the encoding step and the extraction of the lattice vector. We then analyze the correctness and running time of the reduction.

