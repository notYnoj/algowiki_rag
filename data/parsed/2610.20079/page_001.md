Undirected Network Coding and Faster External-Memory Integer Sorting

Baochun Li University of Toronto

Zongpeng Li Tsinghua University

Sirui Liu Tsinghua University

**Abstract**

Network coding allows intermediate nodes to combine messages. Fractional routing instead splits each message among source--destination paths and forwards its parts without combining different messages. For undirected networks carrying independent messages between multiple source-- destination pairs, the multiple-unicast conjecture asserts that the two methods achieve the same combinations of message rates. We give a finite counterexample and use its linear structure to accelerate external-memory integer sorting, addressing the question of whether integer operations can beat the comparison-sorting input/output (I/O) bound posed by Aggarwal and Vitter in 1988.

We give a deterministic sorting algorithm: for _N_ integers of \(\Theta(logN)\) bits, a memory holding _M_ integers, and block transfers of _B_ integers, where \(2B\le M\le N\), the number of block transfers is

\(O\big(\frac{N}{B}\left[1+\frac{logN}{(log(M/B))^{1-\varepsilon}(logM)^\varepsilon}\right]\big),\)

where \(\varepsilon=1.5\times 10^{-5}\) is an absolute constant. In some parameter ranges, this bound is asymptotically smaller than the classical comparison-sorting bound. Under the external-memory model specified in this paper, we have formally verified the algorithm’s correctness and I/O complexity bound in Lean.

