## 1 Introduction

A multiple-unicast network carries independent messages between specified source-destination pairs. Network coding allows intermediate nodes to combine messages. Fractional routing instead splits each message among paths and forwards the resulting parts without mixing messages. In 2004, Li and Li proposed the multiple-unicast conjecture: network coding and fractional routing achieve the same message rates in undirected multiple-unicast networks \[LL04\]. The conjecture is also closely connected to several important problems in theoretical computer science; if true, it would imply conditional complexity lower bounds, including for external-memory integer sorting \[AHJ<sup>+</sup>06, FHLS19,AFKL19\].

In 2026, Zhang, Li, and Li \[ZLL26\] and Braverman and He \[BH26\] constructed counterexamples in undirected multiple-unicast networks, showing that network coding can strictly outperform fractional routing and thereby refuting the multiple-unicast conjecture. These counterexamples establish a communication advantage, but invalidating the assumption behind a conditional lower bound does not itself produce a faster algorithm.

External-memory integer sorting is one problem closely tied to the conjecture. The _N_ input integers are stored on disk, with one integer per machine word, a fixed-size unit of storage. Memory holds _M_ words, and each transfer between disk and memory moves one block of _B_ consecutive words. The input/output (I/O) complexity is the total number of these transfers. The optimal classical comparison-sorting bound is \[AV88\]

\(\Theta\big(\frac{N}{B}\left[1+\frac{log(N/M)}{log(M/B)}\right]\big).\) (1)

In 1988, Aggarwal and Vitter asked whether allowing algorithms to exploit the bits of integer keys could improve on this comparison bound \[AV88\]. This has long been a central open problem in external-memory algorithms \[FHLS19\]. Farhadi, Hajiaghayi, Larsen, and Shi \[FHLS19\] proved that, if the multiple-unicast conjecture were true, then for \(B\ge logN\), integer sorting could not asymptotically improve on the comparison-sorting I/O bound, even with arbitrary bit operations.

We turn the communication advantage of coding into fewer block transfers. We first construct a finite undirected multiple-unicast network in which binary linear coding strictly outperforms fractional routing. We use the finite circuit to interchange two address fields, meaning two groups of consecutive digits in an array position. Recursive calls interchange progressively shorter fields; once enough buffers fit in memory, scans perform the remaining movement directly. Building on existing recursive field-exchange techniques \[Ope26\], we combine this operation with Columnsort, which alternates sorting columns with fixed rearrangements, and most-significant-digit (MSD) radix sorting, which partitions integers by their high-order bits first.

Specifically, for every \(2B\le M\le N\), our algorithm sorts _N_ integers of \(\Theta(logN)\) bits in

\(O\big(\frac{N}{B}\left[1+\frac{logN}{(log(M/B))^{1-\varepsilon}(logM)^\varepsilon}\right]\big)\)

I/Os, where the absolute constant can be taken as \(\varepsilon=1.5\times 10^{-5}>0\). The algorithm is correct for every input, including repeated values, and uses at most _M_ words of memory and polynomial disk space under the conventions of Section 3. When \(w<\lceil log_2N\rceil\) and _M_ is below a fixed threshold, those conventions allow the predetermined execution-step index to be stored outside the _M_ words. In particular, when _M_=2_B_ and _N=B_<sup>2</sup>, classical comparison sorting requires \(\Theta(BlogB)\) I/Os, whereas our algorithm uses \(O(B(logB)^{1-\varepsilon})\).

