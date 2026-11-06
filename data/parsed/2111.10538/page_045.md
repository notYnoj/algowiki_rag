are sampled in our algorithm.

\(Pr[\text{none of the elements in the first}\epsilon/2\text{fraction of}\mathsf{b}\text{is sampled]}\)<br>
\(\le\left(1-\frac{\epsilon}{2}\cdot\epsilon\sqrt{n}\lambda\cdot\frac{1}{\sqrt{n}}\right)^k\)<br>
\(=\left(1-\frac{\epsilon^2\lambda}{2}\right)^{\frac{2}{\epsilon^2\lambda}\cdot 10log(1/\delta)}\)<br>
\(\le e^{-10log(1/\delta)}\)<br>
\(\le\delta/2,\)

where the first step follows from the fact that b contains at least \(\epsilon\lambda\sqrt{n}\) elements, the second step follows from \(k=20log(1/\delta)/(\lambda\epsilon^2)\), and the third step follows from the fact that \((1-1/x)^x\le 1/e\) for \(\forall x\ge 4\). Hence, with probability at least \(1-\delta/2\), at least one of the elements in the first \(\epsilon/2\) fraction of b are sampled.

With the same analysis, one can prove that with probability at least \(1-\delta/2\) at least one of the elements in the last \(\epsilon/2\) fraction of b are also sampled.

Taking a union bound of two events, with probability at least \(1-\delta\), at least one of the elements in the first and at least one of the elements in the last \(\epsilon/2\) fraction of b are sampled.

Therefore, the lis of sa_<sub>i</sub>_ subject to this interval is at least a \(1-\epsilon\) fraction of lis<sup>\[sm(sa_<sub>i</sub>),_lg(sa_<sub>i</sub>_)\]</sup>(sa_<sub>i</sub>_).

Notice that the average contribution of each subarray to opt is \(\sqrt{n}\lambda\) and Lemma 6.1 applies to a subarray if its contribution to opt is at least an \(\epsilon\) fraction of this value. Therefore Lemma 6.1 implies that a considerable fraction of the solution is covered by the candidate domains.

**Corollary 6.2** (existence of a desirable solution)**.** _Let_ \(\lambda\in(0,1)\) _such that_ \(\mathsf{lis}(A)\ge n\lambda\) _and_ \(\epsilon\in(0,1/4)\)_. If we run Algorithm 8 with parameter_ \(\delta=\epsilon\) _on every subarray independently, then with probability at least_ \(1-exp(-\Omega(\epsilon^2\sqrt{n}\lambda))\)_, there exists a set_ \(T\subseteq[\sqrt{n}]\) _and elements_ \(\alpha_i\) _and_ \(\beta_i\) _sampled from_ sa_<sub>i</sub> for each_ \(i\in T\) _such that the following conditions hold:_

1. _For any_ \(i\in T\), \(\alpha_i\le\beta_i\).<tbc>

2. _For any_ \(i,j\in T\) _satisfying i\<j,_ \(\beta_i<\alpha_j\).<tbc>

_3._ \(\sum_{i\in T}\mathsf{lis}^{[\alpha_i,\beta_i]}(\mathsf{sa}_i)\ge(1-4\epsilon)\mathsf{lis}(A)\).<tbc>

<tbc>_Proof._ Lemma 6.1 holds for all subarrays whose contribution to opt is at least \(\epsilon\sqrt{n}\lambda\). Let \(S\subseteq[\sqrt{n}]\) denote the set of coordinates such that for each \(i\in S\)<tbc>

\(\mathsf{lis}^{[\mathsf{sm}(\mathsf{sa}_i),\mathsf{lg}(\mathsf{sa}_i)]}(\mathsf{sa}_i)\ge\epsilon\sqrt{n}\lambda.\)

<tbc>Since \(\sum_{i=1}^{\sqrt{n}}\mathsf{lis}^{[\mathsf{sm}(\mathsf{sa}_i),\mathsf{lg}(\mathsf{sa}_i)]}(\mathsf{sa}_i)=\mathsf{lis}(A)\) and \(\mathsf{lis}^{[\mathsf{sm}(\mathsf{sa}_i),\mathsf{lg}(\mathsf{sa}_i)]}(\mathsf{sa}_i)\le\sqrt{n}\), we have

\(\sum_{i\in S}\mathsf{lis}^{[\mathsf{sm}(\mathsf{sa}_i),\mathsf{lg}(\mathsf{sa}_i)]}(\mathsf{sa}_i)\ge\sum_{i=1}^{\sqrt{n}}\mathsf{lis}^{[\mathsf{sm}(\mathsf{sa}_i),\mathsf{lg}(\mathsf{sa}_i)]}(\mathsf{sa}_i)-\sqrt{n}\cdot\epsilon\sqrt{n}\lambda\ge\mathsf{lis}(A)-\epsilon n\lambda.\) (12)

Let \(T\subseteq S\) denote the set of coordinates such that for each \(i\in T\),

\(\mathsf{lis}^{[\alpha_i,\beta_i]}(\mathsf{sa}_i)\ge(1-\epsilon)\mathsf{lis}^{[\mathsf{sm}(\mathsf{sa}_i),\mathsf{lg}(\mathsf{sa}_i)]}(\mathsf{sa}_i),\text{and}\mathsf{lis}^{[\mathsf{sm}(\mathsf{sa}_i),\mathsf{lg}(\mathsf{sa}_i)]}(\mathsf{sa}_i)\ge\epsilon\sqrt{n}\lambda.\)

