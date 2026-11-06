The total time used for preprocessing is<tbc>

\(\frac{N}{\ell}\cdot(\ell)^C=N\cdot\ell^{C-1}.\)

<tbc>For each query _q<sub>j</sub>_, one needs to query \(N/\ell\) data structures. Hence, the total query time spent on _q_<sub>1</sub>_,...,q<sub>N</sub>_ is<tbc>

\(N\cdot\frac{N}{\ell}\cdot\ell^{1-\delta}=\frac{N^2}{\ell^\delta}.\)

<tbc>Let \(\delta'>0\) be a number satisfying \(\frac{\delta'}{1-\delta'}<\frac{\delta}{C-1}\) and choose \(\ell\) such that

\(N^{\delta^\prime/\delta}<\ell<N^\frac{1-\delta^\prime}{C-1}.\)

This gives a \(O(N^{2-\delta^\prime})\)-time algorithm for \(\gamma\)-approximate Bichromatic Closest Pair.

## 3.2 \(\mathsf{SVP}_p^{\{0,1\}}\) Hardness implies Hardness of ANN under \(\ell_p\)

In this section, we show that a fast algorithm for \(\gamma\)-approximate Bichromatic Closest Pair under \(\ell_p\) implies a fast algorithm for \(\gamma\)-\(\mathsf{SVP}_p^{\{0,1\}}\). Combined with Lemma 3.1, this shows that a lower bound for \(\gamma\)-\(\mathsf{SVP}_p^{\{0,1\}}\) implies a lower bound for \(\gamma\)-ANN under \(\ell_p\). Assuming SETH, lower bounds for \(\gamma\)-\(\mathsf{SVP}_\infty^{\{0,1\}}\) are known (Theorem 2.8). Hence, our reduction implies hardness of \(\gamma\)-ANN under the \(\ell_\infty\) norm.

**Lemma 3.2.** _If there exists a f(N)-time algorithm that solves_ \(\gamma\)_-approximate Bichromatic Closest Pair under the_ \(\ell_p\) _norm (where_ \(1\le p\le\infty\)_), then there exists an algorithm for_ \(\gamma\)-\(\mathsf{SVP}_p^{\{0,1\}}\) _with the same ambient dimension that runs in_ \(O\left(f(2^{n/2})\right)\) _time, where n denotes the rank of the input lattice._

_Proof._ Consider an instance of \(\gamma\)-\(\mathsf{SVP}_p^{\{0,1\}}\) with a lattice basis \(\mathcal{B}\subset\mathbb{R}^d\) of size _n_. Divide B into B<sub>1</sub> and B<sub>2</sub>, each of size _n/_2, and consider the following sets of vectors.

\(A_0:=\left\{\sum_i\alpha_ib_i|b_i\in\mathcal{B}_1,\vec{\alpha}\in\{0,1\}^{n/2}\right\}\)<br>
\(A_1:=\left\{\sum_i\alpha_ib_i|b_i\in\mathcal{B}_1,\vec{\alpha}\in\{0,1\}^{n/2},\vec{\alpha}\neq\vec{0}\right\}\)<br>
\(B_0:=\left\{-\sum_i\alpha_ib_i|b_i\in\mathcal{B}_2,\vec{\alpha}\in\{0,1\}^{n/2}\right\}\)<br>
\(B_1:=\left\{-\sum_i\alpha_ib_i|b_i\in\mathcal{B}_2,\vec{\alpha}\in\{0,1\}^{n/2},\vec{\alpha}\neq\vec{0}\right\}.\)

Let A be an _f(N_)-time algorithm for \(\gamma\)-approximate Bichromatic Closest Pair. We run A two times with the following inputs, A(_A_<sub>0</sub>_,B_<sub>1</sub>), A(_A_<sub>1</sub>_,B_<sub>0</sub>) and return the OR of the outputs. Since \(|A_1|,|B_1|\le|A_0|,|B_0|\le N=2^{n/2}\), then the runtime is _O(f(N_))=_O(f_(2<sup>_n/_2</sup>)). It remains to show the correctness of our reduction.

**Claim 3.3** (Correctness)**.** _Let_ \(\mathcal{L}^{\{0,1\}}=\{\sum_{i=1}^n\alpha_ib_i|b_i\in\mathcal{B},\vec{\alpha}\in\{0,1\}^n\}\) _and_ \(A-B=\{a-b|a\in A,b\in B\}\)_. Then_<tbc>

\((A_0-B_1)\cup(A_1-B_0)=\mathcal{L}^{\{0,1\}}\backslash\{\vec{0}\}.\)

