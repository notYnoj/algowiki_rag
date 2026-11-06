# Faster Weighted and Unweighted Tree Edit Distance and APSP Equivalence

**Abstract**

The tree edit distance (TED) between two rooted ordered trees with _n_ nodes labeled from an alphabet \(\Sigma\) is the minimum cost of transforming one tree into the other by a sequence of valid operations consisting of insertions, deletions and relabeling of nodes. The tree edit distance is a well-known generalization of string edit distance and has been studied since the 1970s. Its running time has seen steady improvements starting with an O(_n_<sup>6</sup>) algorithm [Tai, J.ACM 1979], improved to O(_n_<sup>4</sup>) [Shasha, Zhang, SICOMP 1989] and to O(_n_<sup>3</sup>log_n_) [Klein, ESA 1998], and culminating in an O(_n_<sup>3</sup>) algorithm [Demaine, Mozes, Rossman, Weimann, ACM TALG 2010]. The latter is known to be optimal for any dynamic programming based algorithm that falls under a certain decomposition framework that captures all known sub-_n_<sup>4</sup> time algorithms. Fine-grained complexity casts further light onto this hardness showing that a truly subcubic time algorithm for TED implies a truly subcubic time algorithm for All-Pairs Shortest Paths (APSP) [Bringmann, Gawrychowski, Mozes, Weimann, ACM TALG 2020]. Therefore, under the popular APSP hypothesis, a truly subcubic time algorithm for TED cannot exist. However, unlike many problems in fine-grained complexity for which conditional hardness based on APSP also comes with equivalence to APSP, whether TED can be reduced to APSP has remained unknown.

In this paper, we resolve this. Not only we show that TED is fine-grained _equivalent_ to APSP, our reduction is tight enough, so that combined with the fastest APSP algorithm to-date [Williams, SICOMP 2018] it gives the first ever subcubic time algorithm for TED running in \(n^3/2^{\Omega(\sqrt{logn})}\) time.

We also consider the unweighted tree edit distance problem in which the cost of each edit (insertion, deletion, and relabeling) is one. For unweighted TED, a truly subcubic algorithm is known due to Mao [Mao, FOCS 2022], and later improved slightly by Dürr [Dürr, IPL 2023] to run in O(_n_<sup>2.9148</sup>) time. Since their algorithm uses bounded monotone min-plus product as a crucial subroutine, and the best running time for this product is \(\tilde{\mathcal{O}}(n^{\frac{3+\omega}{2}})\le\mathcal{O}(n^{2.6857})\) (where \(\omega\) is the exponent of fast matrix multiplication), the much higher running time of unweighted TED remained unsatisfactory. In this work, we close this gap and give an algorithm for unweighted TED that runs in \(\tilde{\mathcal{O}}(n^{\frac{3+\omega}{2}})\) time.

**Jakob Nogler** \(\unknown\)

ETH Zurich, Zurich, Switzerland

**Barna Saha** \(\unknown\)

University of California, San Diego La Jolla, United States

**Yinzhan Xu** \(\unknown\)

University of California, San Diego La Jolla, United States

**Adam Polak** \(\unknown\)

Bocconi University, Milan, Italy

**Virginia Vassilevska Williams** \(\unknown\)

Massachusetts Institute of Technology Cambridge, United States

**Christopher Ye** \(\unknown\)

University of California, San Diego La Jolla, United States

