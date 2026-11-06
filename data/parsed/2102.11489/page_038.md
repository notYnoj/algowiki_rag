that each problem size \(n'\) can be implemented with \(S_\mathrm{sw}(n')+2S_\mathrm{lc}(n')+O(n')\) number of _w_-selector gates and \(S_\mathrm{sw}(n')+B_\mathrm{sw}(n')+B_\mathrm{lc}(n')+4S_\mathrm{lc}(n')+O(n')\) generalized boolean gates.

Summing over all \(n'=n,n/c,n/c^2,\dots\), we have the follow fact:

**Fact 9.7.** _In the above approximate splitter algorithm, the total number of w-selector gates needed is upper bounded by_ 2.5_S_<sub>sw</sub>(_n_)+5_S_<sub>lc</sub>(_n_)+_O(n_) _and the total number of generalized boolean gates is upper bounded by_ 2.5_S_<sub>sw</sub>(_n_)+2.5_B_<sub>sw</sub>(_n_)+2.5_B_<sub>lc</sub>(_n_)+10_S_<sub>lc</sub>(_n_)+_O(n); furthermore, the depth is upper bounded by_ \(\mathrm{log}_{1.79}\frac{1}{\alpha}\cdot(2D_\mathrm{lc}(n)+O(1))\le 2.4\mathrm{log}\frac{1}{\alpha}\cdot(D_\mathrm{lc}(n)+O(1))\).

## 10 Lossy Loose Compaction from Approximate Splitter

In this section, we show how to construct a circuit for lossy loose compaction from an approximate splitter.

**Theorem 10.1.** _Let f(n_) _be some function in n such that_ \(1<f(n)\le\mathrm{log}_2n\) _holds for every n greater than an appropriate constant; let C_<sub>sp</sub>_\>_1 _be a constant. Fix some_ \(\alpha\in(0,1)\) _which may be a function of n. Suppose that for any_ \(\beta\in(0,1/4]\)_, for any n that is greater than an appropriately large constant,_ \((\alpha,\beta,n,w)\)_-approximate splitter can be solved by a circuit with_ \(C_\mathrm{sp}\cdot n\cdot f(n)\) _generalized boolean gates,_ \(C_\mathrm{sp}\cdot n\) _selector gates, and of depth D_<sub>sp</sub>(_n). Then, for any n greater than an appropriately large constant,_ \((1.74\alpha,n,w)\)_-lossy loose compaction can be solved by a circuit with_ \(2.07C_\mathrm{sp}\cdot n\cdot f(f(n))+O(n)\) _generalized boolean gates,_ \(2.07C_\mathrm{sp}\cdot n\) _number of w-selector gates, and of depth_ 2.07_D_<sub>sp</sub>(_n_)+_O_(log_f(n_)).

The remainder of this section will be dedicated to proving the above theorem.

**Proof of Theorem 10.1:** For simplicity, we first consider the case when _n_ is divisible by _f(n_). Looking ahead, we will use _f(n_) to be log<sup>(_x_)</sup>_n_ for some _x_ that is power of 2. We will later extend our theorem statement to the case when _n_ is not divisible by _f(n_). Consider the following algorithm:

\(\text{\textbf{Lossy loose compaction from approximate splitter} 1. Divide the input array into}f(n)\text{-sized chunks. We say that a chunk is}sparse\text{if there are at most}f(n)/32\text{real elements in it; otherwise it is called}dense\text{. Now, count the number of elements in every chunk, and mark each chunk as either}\mathtt{sparse}\text{or}\mathtt{dense}\text{. We will show later in Fact 10.2 that at least}3/4\text{fraction of the chunks are sparse. 2. Call an}(\alpha,1/4,n/f(n),w\cdot f(n))\text{-approximate splitter to move almost all the dense chunks to the front and almost all the sparse chunks to the end. 3. Apply an}(\alpha,1/32,f(n),w)\text{-approximate splitter to the trailing}\left[(\frac{3}{4}-\frac{1}{64})\cdot\frac{n}{f(n)}\right]\text{chunks to compress each of these chunks to a length of}\left[\frac{3f(n)}{64}\right]\text{, losing few elements in the process. The first}\left[(\frac{1}{4}+\frac{1}{64})\cdot\frac{n}{f(n)}\right]\text{chunks are unchanged. Output the resulting array.}\)

At the end of the algorithm, the output array has length at most

\((\frac{3}{4}-\frac{1}{64})\cdot\frac{n}{f(n)}\cdot\frac{3f(n)}{64}+(\frac{1}{4}+\frac{1}{64})\cdot\frac{n}{f(n)}\cdot f(n)\le 0.32n<n/1.9\) (2)

