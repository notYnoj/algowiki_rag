connected anchor variables. See Figure 1 below for an illustrative example of our construction. Our main theorem uses polynomially many expectation value queries at different phase values to interpolate the required Laurent coefficient for _p_=2. This interpolation argument applies to both exact evaluation and to evaluation with exponentially small additive error. Hence we show Turing reducibility between these problems, written informally as

\(|\#\text{MC}|\le_T\text{Eval}_{p=2}^\text{MC}.\)

The general _p_ result then follows setting all angles in the additional _p_-2 layers to zero. This yields #P-hardness for computing QAOA expectation values rather than NP-hardness as in prior work. We further show that hardness remains when restricted to computing a single-edge correlator \(\langle Z_rZ_s\rangle\).

## 1.1 Main result: Evaluating QAOA _p_=2 expectation values is #P-hard

**Definition 1.1** (QAOA expectation value evaluation problem)**.** _For fixed_ \(p\in\mathbb{N}\)_, let_ \(\text{Eval}_p^\text{MC}\) _be the function problem that maps a graph G and parameters_ \(\unknown,\unknown\) _to the exact algebraic number_<tbc>

\(F_p(G;\unknown,\unknown).\)

<tbc>_The additive-error version additionally receives_ \(b\in\mathbb{N}\) _in unary\[14\] and returns a rational number_ \(\widetilde{F}\) _satisfying_<tbc>

\(\left|\widetilde{F}-F_p(G;\unknown,\unknown)\right|\le 2^{-b}.\)

<tbc>For a designated edge \(e=\{u,v\}\in E(G)\), we additionally define

\(\text{Eval}_p^\text{uv}(G;\unknown,\unknown):=\langle\psi_p|Z_uZ_v|\psi_p\rangle.\)

We will primarily be concerned with deterministic polynomial-time Turing reductions, i.e., what one can solve efficiently given a black box computing \(\text{Eval}_p^\text{MC}\). The output of an exact evaluation oracle is understood to be expressed in a standard basis of the compositum of the number fields in which the input is represented. The particular numerical representation is inessential for the Turing reductions below, provided it supports polynomial-time exact arithmetic and basis conversion. Every oracle (subroutine) query uses a number field of polynomial degree and the inverse Fourier transform is carried out exactly within that field. QAOA angles are specified exactly by algebraic values of their sines and cosines; the reduction uses only roots of unity and fixed algebraic values for the sines and cosines of the mixer angles.\[15\] The explicit number field representation is specified in Appendix B.

Here FP denotes the class of functions computable by a deterministic classical algorithm in time polynomial in the input length.

**Theorem 1.2** (QAOA expectation complexity dichotomy)**.** _For unweighted simple graphs,_

\(\text{Eval}_1^\text{MC}\in\mathsf{FP},\) (5)

\(\text{Eval}_p^\text{MC}\text{\textit{is}}\#P\text{\textit{-hard for every fixed}}p\ge 2.\) (6)

_Moreover, for every fixed_ \(p\ge 2\)_, it suffices to restrict evaluations to QAOA angles_

\(\gamma_1=\gamma_2,\beta_1=arctan\frac{1}{2},\beta_2=\frac{\pi}{4},\gamma_j=\beta_j=0(3\le j\le p).\) (7)

**Corollary 1.3.** _The same conclusions of the theorem hold if the oracle evaluates only one designated two-qubit correlator_ \(\langle Z_rZ_s\rangle\) _rather than the global cost expectation value_ \(\langle C_G\rangle\).

