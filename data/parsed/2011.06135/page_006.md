obtain. Another interesting direction is to show the quantitative hardness of other computational problems assuming Conjecture 1.5 since \(\mathsf{SVP}_\infty^{\{0,1\}}\) is itself a natural problem which encapsulates the difficulty of canonical problems such as _k_-SAT and Subset Sum. Additional motivation for this direction is given by \[BGSD17; Agg+21\], who remark that the concrete lower bound for general \(\mathsf{SVP}_\infty\) may in fact be 3_<sup>n</sup>_ since the kissing number in the \(\ell_\infty\) norm is 3_<sup>n</sup>_-1. Since it is not at all clear whether a 3_<sup>n</sup>_ lower bound for \(\mathsf{SVP}_\infty\) can be deduced from SETH, it may make sense to directly assume the quantitative hardness of \(\mathsf{SVP}_\infty\) or \(\mathsf{SVP}_\infty^{\{0,1\}}\).

### Acknowledgments.

We thank Noah Stephens-Davidowitz and Oded Regev for helpful comments.

## 2 Preliminaries

We present two reductions that show hardness of \(\gamma\)-ANN. Our first reduction reduces a special case of the Shortest Vector Problem to \(\gamma\)-ANN. Our second reduction reduces the Subset Query problem to \(\gamma\)-ANN. Both reductions involve an intermediate problem, referred to as the Bichromatic Closest Pair problem in \[Rub18\]. In this section, we present formal definitions of these problems and their lower bounds assuming SETH.

### 2.1 Complexity Assumptions

**Definition 2.1** (Strong Exponential Time Hypothesis \[IP99\])**.** _For any_ \(\varepsilon>0\)_, there exists_ \(k=k(\varepsilon)\) _such that k_-SAT _on n variables cannot be solved in_ \(2^{(1-\varepsilon)n}\) _time._

Orthogonal Vectors (OV) is an intermediate problem commonly used to show fine-grained hardness results in P \[Wil05; Wil07\]. Note that SETH implies the Orthogonal Vectors Conjecture, which states that Orthogonal Vectors cannot be solved in subquadratic time. For recent developments in fine-grained complexity assuming the Orthogonal Vectors Conjecture, we refer the reader to the survey \[Wil17\] and references therein.

**Definition 2.2** (Orthogonal Vectors)**.** _Given two sets_ \(A,B\subset\{0,1\}^d\)_, decide whether there exists a pair_ \((a,b)\in A\times B\) _such that_ \(\langle a,b\rangle=0\).

**Conjecture 2.3** (Orthogonal Vectors Conjecture)**.** _For every_ \(\delta>0\)_, there exists a constant_ \(c=c(\delta)\) _such that given two sets_ \(A,B\subset\{0,1\}^d\) _each of cardinality N, deciding if there is a pair_ \((a,b)\in A\times B\) _such that_ \(\langle a,b\rangle=0\) _cannot be solved in_ \(O(N^{2-\delta})\) _time on instances with d=c_log_N._

### 2.2 Nearest Neighbor Search Problems

**Definition 2.4** (Approximate Nearest Neighbor Search)**.** _The_ \(\gamma\)_-Approximate Nearest Neighbor Search problem (_\(\gamma\)_-ANN) under the_ \(\ell_p\) _norm is defined as follows. Let_ \(A\subset\mathbb{R}^d\) _be a set of N vectors. Given numbers_ \(\gamma>1\)_, r\>_0_, and a vector_ \(x\in\mathbb{R}^d\)_, distinguish between the following two cases after preprocessing A:_

• _(YES) There exists_ \(a\in A\) _such that with_ \(\left\|a-x\right\|_p\le r\).<tbc>

• _(NO) For all_ \(a\in A\), \(\left\|a-x\right\|_p\ge\gamma r\).

**Definition 2.5** (Approximate Bichromatic Closest Pair)**.** _The_ \(\gamma\)_-approximate Bichromatic Closest Pair problem under the_ \(\ell_p\) _norm is defined as follows. Let_ \(A,B\subset\mathbb{R}^d\) _each be a set of size N. Given numbers_ \(\gamma>1\) _and r\>_0_, distinguish between the following two cases:_

