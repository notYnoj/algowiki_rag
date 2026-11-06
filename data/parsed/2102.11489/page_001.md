# Optimal Sorting Circuits for Short Keys <sup>∗</sup>

**Abstract**

A long-standing open question in the algorithms and complexity literature is whether there exist sorting circuits of size _o(n_log_n_). A recent work by Asharov, Lin, and Shi (SODA’21) showed that if the elements to be sorted have short keys whose length _k=o_(log_n_), then one can indeed overcome the _n_log_n_ barrier for sorting circuits, by leveraging non-comparison-based techniques. More specifically, Asharov et al. showed that there exist \(O(n)\cdot min(k,logn)\)-sized sorting circuits for _k_-bit keys, ignoring polylog<sup>∗</sup> factors. Interestingly, the recent works by Farhadi et al. (S’19) and Asharov et al. (SODA’21) also showed that the above result is essentially optimal for every key length _k_, assuming that the famous Li-Li network coding conjecture holds. Note also that proving any _unconditional_ super-linear circuit lower bound for a wide class of problems is beyond the reach of current techniques.

Unfortunately, the approach taken by previous works to achieve optimality in size somewhat crucially relies on sacrificing the depth: specifically, their circuit is super-_polyl_logarithmic in depth even for 1-bit keys. Asharov et al. phrase it as an open question how to achieve optimality both in size and depth. In this paper, we close this important gap in our understanding. We construct a sorting circuit of size \(O(n)\cdot min(k,logn)\) (ignoring polylog<sup>∗</sup> terms) and depth _O_(log_n_). To achieve this, our approach departs significantly from the prior works. Our result can be viewed as a generalization of the landmark result by Ajtai, Komlós, and Szemerédi (S’83), simultaneously in terms of size and depth. Specifically, for _k=o_(log_n_), we achieve asymptotical improvements in size over the AKS sorting circuit, while preserving optimality in depth.

### 1 Introduction

Sorting circuits have been investigated for a long time in the algorithms and complexity theory literature, and it is almost surprising that we still do not fully understand sorting circuits. Suppose we want to sort an input array with _n_ elements, each with a _k_-bit comparison key and a _w_- bit payload. A long-standing open question is whether there exist circuits with \((k+w)\cdot o(nlogn)\) boolean gates where each gate is assumed to have constant fan-in and constant fan-out [BN16]. The recent works of Farhadi et al. [FHLS19] (S’19) showed that assuming the famous Li-Li network coding conjecture [LL04], it is impossible to construct sorting circuits of size \((k+w)\cdot o(nlogn)\) when there is no restriction on the key length _k_. Given this conditional lower bound, we seem to have hit another wall. However, shortly afterwards, Asharov, Lin, and Shi [ALS21] showed that we can indeed overcome the _n_log_n_ barrier for _short keys_, specifically, when _k=o_(log_n_). More specifically, Asharov et al. showed that an array containing _n_ elements each with a _k_-bit key and a _w_-bit payload can be sorted in a circuit of size \((k+w)\cdot O(n)\cdot min(k,logn)\) (ignoring polylog<sup>∗</sup> terms); moreover, Asharov et al. [ALS21] prove that this is optimal for every choice of _k_.

<sup>∗</sup>Author ordering is randomly generated.

Wei-Kai Lin Cornell `wklin@cs.cornell.edu`

Elaine Shi CMU `runting@cs.cmu.edu`

arXiv:2102.11489v2 [cs.DS] 7 Nov 2021

