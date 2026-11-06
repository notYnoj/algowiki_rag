**Fact 10.2.** _At least_ \(\frac{3}{4}\cdot\frac{n}{f(n)}\) _chunks are sparse._

_Proof._ Suppose not, this means that more than \(\frac{1}{4}\cdot\frac{n}{f(n)}\) have more than _f(n)/_32 real elements. Thus the total number of elements is more than _n/_128 which contradicts the input sparsity assumption of loose compaction.

**Fact 10.3.** _The above algorithm loses at most_ \(1.74\alpha n\) _real elements._

_Proof._ If a `dense` chunk is not contained within the first \(\left\lfloor(\frac{1}{4}+\frac{1}{64})\cdot\frac{n}{f(n)}\right\rfloor\) chunks, we may assume that all elements in it will be lost. Due to the property of the approximate splitter, at most \(\alpha n/f(n)\) `dense` chunks are not contained within the first \(\left\lfloor(\frac{1}{4}+\frac{1}{64})\cdot\frac{n}{f(n)}\right\rfloor\) chunks. Further, when we apply an approximate splitter to compress the trailing \(\left\lceil(\frac{3}{4}-\frac{1}{64})\cdot\frac{n}{f(n)}\right\rceil\) chunks to each to a length of \(\left\lfloor\frac{3f(n)}{64}\right\rfloor\), for each chunk, we may lose at most \(\alpha f(n)\) real elements.

Therefore, the number of real elements lost is upper bounded by the following as long as _n_ is greater than an appropriate constant:

\(\alpha\cdot(n/f(n))\cdot f(n)+\alpha f(n)\cdot\left\lceil(\frac{3}{4}-\frac{1}{64})\cdot\frac{n}{f(n)}\right\rceil\le 1.74\alpha n\)

**Implementing the above algorithm in circuit.** We now analyze the circuit size of the above algorithm. For simplicity, we first assume that _n_ is divisible by _f(n_) and we will later modify our analysis to the more general case when _n_ is not divisible by _f(n_).

1. Due to Fact 6.3, Step 1 of the algorithm requires at most _O(n_) generalized boolean gates as we have _n/f(n_) counters each for a chunk of size _f(n_). The counting for all chunks are performed in parallel, and thus the depth is _O_(log_f(n_)).<tbc>

2. Step 2 is a single invocation of an \((\alpha,1/4,n/f(n),w\cdot f(n))\)-approximate splitter. Assuming that \((\alpha,1/4,n,w)\)-approximate splitter can be realized with \(C_\mathrm{sp}\cdot n\cdot f(n)\) generalized boolean gates and \(C_\mathrm{sp}\cdot n\) selector gates, this step requires at most \(C_\mathrm{sp}\cdot(n/f(n))\cdot f(n/f(n))\le C_\mathrm{sp}\cdot(n/f(n))\cdot f(n)\) generalized boolean gates and \(C_\mathrm{sp}\cdot n/f(n)\) number of \(w\cdot f(n)\)-selector gates. Each such selector gate can in turn be realized with _f(n_) number of _w_-selector gates; moreover, the flag bit needs to be replicated _f(n_) times over a binary tree, requiring _O_(log_f(n_)) depth and _O(f(n_)) generalized boolean gates per chunk. Thus, in total, Step 2 requires \(C_\mathrm{sp}\cdot n+O(n)\) generalized boolean gates, \(C_\mathrm{sp}\cdot n\) number of _w_-selector gates, and requires at most _D_<sub>sp</sub>(_n)+O_(log_f(n_)) depth.<tbc>

3. Step 3 of the algorithm requires applying \(\left\lceil(\frac{3}{4}-\frac{1}{64})\cdot\frac{n}{f(n)}\right\rceil\) number of \((\alpha,1/32,f(n),w)\)-approximate splitters, where, according to our assumption in Theorem 10.1, each such approximate splitter consumes \(C_\mathrm{sp}\cdot f(n)\cdot f(f(n))\) generalized boolean gates and \(C_\mathrm{sp}\cdot f(n)\) number of _w_-selector gates. For sufficiently large _n_ and \(f(n)\le\mathrm{log}_2n\), we have that \(\left\lceil(\frac{3}{4}-\frac{1}{64})\cdot\frac{n}{f(n)}\right\rceil\cdot f(n)\le n\). Therefore, in total there are at most \(C_\mathrm{sp}\cdot n\cdot f(f(n))\) generalized boolean gates and \(C_\mathrm{sp}\cdot n\) number of _w_-selector gates. The depth of this step is upper bounded by _D_<sub>sp</sub>(_f(n_)).<tbc>

<tbc>Summarizing the above, we have the following fact:

