## 2 Preliminaries

**Model of Computation.** We use the AC0 Word RAM model of computation with word size _w_. This means that we _strict_ ourselves to word operations that can be computed by a poly(_w_)-size circuit of constant depth with AND and OR gates of unbounded fan-in as well as NOT gates, and assume that any such operation can be computed in constant time [27, 7, 8]. Most standard Word RAM instructions can be implemented in the AC0 Word RAM, including addition and subtraction modulo 2_<sup>w</sup>_, bitwise boolean operations, comparisons, and shifts [35, 16]. The only standard operation not supported in this model is multiplication. For wordsize \(w\gg logn\), we explicitly disallow 2_<sup>w</sup>_-size lookup tables, which would allow us to compute _any_ function on _w_ bits: we only allow AC0 functions to be computed on _w_-bit words in constant time.

**Graphs.** Unless otherwise stated, all graphs are undirected and unweighted.

\(\blacktriangleright\) **Theorem 10** (Reiman)**.** _If G is a four-cycle free graph on n nodes, it has at most_ \(\frac{n}{4}\left(1+\sqrt{4n-3}\right)\) _edges._

**Chernoff lower bounds for** _k_**-wise independence.** We will also use the following adaptation of Chernoff bounds to _k_-wise independent random variables:

\(\blacktriangleright\) **Theorem 11** ([34])**.** _Let k be a positive integer, and let X be the sum of_ 0/1 _valued k-wise independent random variables, each with expectation_ \(\mu\)_. For_ \(\delta\ge 1\) _and_ \(k\le\left\lfloor\delta\mu/e^{1/3}\right\rfloor\)_, we have_ \(Pr[X\ge(1+\delta)\mu]\le e^{-k/2}\).

## 3 Compressed List Operations in the AC0-RAM

At a high level, our algorithms use various hashing schemes to reduce triangle and 4-cycle to problems on compressed lists, in particular, equality product, set disjointness, and element distinctness. We then take advantage of word-level parallelism and known techniques for designing AC0 circuits to solve these problems faster, giving us word size factor savings. We begin by detailing these compressed list operations.

\(\blacktriangleright\) **Definition 12** (Compressed list representation)**.** _Let L be a list of k elements from_ \([2^\ell]\)_, where_ \(\ell\le w\)_. We store such L in_ compressed list representation _by packing_ \(\left\lfloor w/\ell\right\rfloor\) _contiguous list elements into a single word, for an overall packed length of_ \(O(k\ell/w)\) _words._

In the following, we let \(\perp\) denote a special character that does not match any valid element. This can be easily implemented in various ways; e.g., we can extend the \(\ell\)-bit encoding of every string to \(\ell+1\) bits, where all "valid" \(\ell\)-bit elements start with a zero, and \(\perp\) equals all-ones (for example).

### 3.1 Sorting Compressed Lists

We begin by describing a sorting algorithm on compressed lists with AC0 word operations, loosely inspired by a work of Chan [13] who allowed _arbitrary_ word operations. Given two compressed sorted lists _L_<sub>0</sub> and _L_<sub>1</sub>, we define the _merge step of L_<sub>0</sub> and _L_<sub>1</sub> to be the task of implementing the standard linear-time merge of _L_<sub>0</sub> and _L_<sub>1</sub> until one of the lists _L<sub>b</sub>_ is empty. The output of a merge step is the merged list obtained so far, along with a \(b\in\{0,1\}\) and the remaining content of the non-empty list _L<sub>b</sub>_. We give a procedure to perform this operation on single words in compressed list representation, which we will use as a subroutine in the

