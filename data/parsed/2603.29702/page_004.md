## 2 High-level Technical Overview

First, note that if the actual ED or LCS is very small, say \(\varepsilon n\) for some \(\varepsilon=2^{-log^{\Omega(1)}(n)}\), there are exact algorithms with running time \(O(\varepsilon n^2)\) for both problems. Since our goal is to obtain algorithms with a running time of \(n^2/2^{log^{\Omega(1)}(n)}\), we henceforth focus on the case where the ED or LCS is at least \(\varepsilon n\) for \(\varepsilon=2^{-log^{O(1)}(n)}\).

Before we describe our main techniques for ED and LCS, we begin with a simple observation about sums of sequences and their sub-sequences (Section 2.1). This observation plays a crucial role in our algorithm, and analogous results have been applied to other areas of research, (see, for example, \[Dru13\]<sup>5</sup>, \[Pen25\]). We then setup the notation with a standard reduction to optimal path problems on a 2D grid (Section 2.2). In Section 2.3 we explain the core algorithmic idea, which suffices to get an additive approximation scheme (i.e., approximate ED or LCS to within \(\pm o(n)\)). Finally in Section 2.4 we extend those ideas to obtain multiplicative approximation schemes.

### 2.1 An Observation on Tree Total Deviation

One of our core ideas is a simple but powerful observation about sums of sequences and their sub-sequences. Suppose that we have a length-_n_ binary sequence _A_=(_a_<sub>1</sub>_,a_<sub>2</sub>_,...,a<sub>n</sub>_) for some _n_ that is the power of some number _M_. We define the (_M_-way) _tree total deviation_ as a measure of the total "unevenness" of _A_ across scales corresponding to blocks of size _M,M_<sup>2</sup>_,...,M_log_<sub>M</sub>n_.

In more detail, to define the tree total deviation, let _S_:=log_<sub>M</sub>n_ be the number of scales. For each scale \(s\in[S]\), we go through all _n/M_<sup>_S-s_+1</sup> intervals (_l,r_\] of form \(\big(M^{S-s+1}\cdot k,M^{S-s+1}\cdot(k+1)\big]\). Fixing some interval (_l,r_\], for each \(0\le i\le M-1\), let \(\sigma_i=\sum_{l+iM^{S-s}<x\le l+(i+1)M^{S-s}}a_x\). Namely, if we partition _a_<sub>(_l,r_\]</sub> into _M_ equal parts, then \(\sigma_i\) is the total sum of the _i_-th part. Let \(\sigma=\sum_{l<x\le r}a_x\). The contribution from interval (_l,r_\] to the tree total deviation is equal to

\(\sum_i|\sigma_i-\sigma/M|,\)

which is a measurement of how "uneven" the sequence \(\{\sigma_0,\sigma_1,\dots,\sigma_{M-1}\}\) is.

Since _A_ is binary, it is easy to see that the local unevenness at an interval (_l,r_\] is _O(r-l_). Thus the total unevenness on a particular scale is _O(n_). Thus clearly the overall total unevenness (i.e., tree total deviation) is upper bounded by _O(n_log_<sub>M</sub>n_).

<sup>5</sup>The authors are grateful to Moses Charikar for bringing this connection to our attention.

\begin{tabular}{ccc}
Approximation factor & Running time & Reference \\
\(\sqrt{n}\) & _O(n_) & Folklore (building on \[LMS98\]) \\
_n_<sup>1/3+_o_(1)</sup> & \(\widetilde{O}(n)\) & \[BES06\] \\
\(2^{O(\sqrt{log(n)loglog(n)})}\) & \(n\cdot 2^{O(\sqrt{log(n)loglog(n)})}\) & \[AO12\] \\
\(1/\varepsilon\) & \(O(n^{1+\delta(\varepsilon)})\) & \[AN20\] \\
3+_o_(1) & _n_<sup>1.6+_o_(1)</sup> & \[GRS20\] \\
1+_o_(1) & \(n^2/2^{log^{\Omega(1)}(n)}\) & **this work** \\
\end{tabular}

1: State of the art trade-offs of approximation ratios vs running time for ED

