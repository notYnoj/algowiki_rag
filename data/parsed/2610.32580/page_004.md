## 3 Some remarks on the second largest element

For this subsection, again distinguish the subset sums of all _n_ elements from those of the first _n_-1 elements. Write

\(0=t_1<t_2<\cdots<t_{2^{n-1}}=T=\sum_{i=1}^{n-1}a_i.\)

**Theorem 2.**

If \(a_1<a_2<\cdots<a_n\) are positive integers with distinct subset sums, then

\(a_{n-1}\ge\left(\frac{2}{\sqrt{3}}-o(1)\right)\frac{2^{n-1}}{\sqrt{n-1}}.\)

**Lemma 4.**

\(\frac{2^{2(n-1)}}{4}\sum_{i=1}^{n-1}a_i^2=\sum_{i>j}(t_i-t_j)^2.\)

_Proof._ Since _t_<sub>1</sub>_,...,t_<sub>2<sup>_n_-1</sup></sub> are all the subset sums of _a_<sub>1</sub>_,...,a_<sub>_n_-1</sub>, we have

\(\sum_{i>j}(t_i-t_j)^2=\frac{1}{2}\sum_{i=1}^{2^{n-1}}\sum_{j=1}^{2^{n-1}}(t_i-t_j)^2\)<br>
\(=\frac{1}{2}\sum_{i=1}^{2^{n-1}}\sum_{j=1}^{2^{n-1}}(t_i^2+t_j^2-2t_it_j)\)<br>
\(=2^{n-1}\sum_{i=1}^{2^{n-1}}t_i^2-\left(\sum_{i=1}^{2^{n-1}}t_i\right)^2.\)

Each _a<sub>i</sub>_ appears in exactly 2<sup>_n_-2</sup> subset sums. Hence

\(\sum_{i=1}^{2^{n-1}}t_i=2^{n-2}\sum_{i=1}^{n-1}a_i=2^{n-2}T.\)

Moreover, expanding the squares of all subset sums, each \(a_i^2\) appears 2<sup>_n_-2</sup> times, while each product _a<sub>i</sub>a<sub>j</sub>_, with _i\<j_, appears 2<sup>_n_-3</sup> times. Therefore,

\(\sum_{i=1}^{2^{n-1}}t_i^2=2^{n-2}\sum_{i=1}^{n-1}a_i^2+2^{n-2}\sum_{1\le i<j\le n-1}a_ia_j\)<br>
\(=2^{n-3}\left(\sum_{i=1}^{n-1}a_i^2+T^2\right),\)

where we used

\(T^2=\sum_{i=1}^{n-1}a_i^2+2\sum_{1\le i<j\le n-1}a_ia_j.\)

