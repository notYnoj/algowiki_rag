However, this transformation increases the universe size from _u_ to (roughly) _un_. In this section, we show that a converse transformation exists, from monotone to non-monotone, that reduces the universe size by a factor _n_. In particular, this shows that Min-Plus Convolution over the universe \[_u_\] is _equivalent_ to Monotone Min-Plus Convolution over the universe \[_nu_\].

**Lemma 5.6** (Universe Reduction for Monotone Min-Plus Convolution)**.** _If Min-Plus Convolution over the universe_ \[_u_\] _can be solved in time_ \(O(n^{2-\epsilon})\) _for some constant_ \(\epsilon>0\)_, then Monotone Min- Plus Convolution of the universe_ \[_un_\] _can be solved in time_ \(O(n^{2-\epsilon^\prime})\) _for some constant_ \(\epsilon'>0\)_. Moreover, the resulting algorithm can provide a witness for each output entry of the Monotone Min-Plus Convolution instance._

A major part of the proof of Lemma 5.6 follows the ideas of Chan and Lewenstein \[CL15\]: We impose a coarse-grained grid on the 2-dimensional index set of the given sequences, inducing a partition into cells. For each cell we select some representative point, apply the BSG theorem on these representatives, and may therefore assume that the representatives form a low-doubling set. From then on, our reduction differs, relying on additive hashing rather than sparse convolutions.

Specifically, it is convenient to use on the following covering version of the BSG theorem with an algorithmic proof due to Chan and Lewenstein \[CL15\]:

**Theorem 5.7** (BSG Covering \[CL15\])**.** _Let_ \(0<\alpha<1\)_, let_ \(t\ge 1\)_, let A,B be sets of size at most n, and let C be a set of size at most tn. There are subsets_ \(A_1,\dots,A_m\subseteq A\) _and_ \(B_1,\dots,B_m\subseteq B\) _and a remainder set_ \(R\subseteq A\times B\) _such that:_

(_i)_ \(\{(a,b)\in A\times B:a+b\in C\}\subseteq R\cup\bigcup_{i=1}^m(A_i\times B_i)\),<tbc>

(_ii)_ \(m=O(\alpha^{-1})\)_, and for all_ \(1\le i\le m\), \(|A_i+B_i|\le O(\alpha^{-5}t^3n)\)_, and_<tbc>

_(iii)_ \(|R|\le O(\alpha n^2)\).

_Moreover, the sets A_<sub>1</sub>_,...,A<sub>m</sub>,B_<sub>1</sub>_,...,B<sub>m</sub> and R can be computed in time_ \(\widetilde{O}(n^2)\) _by a randomized algorithm._

**Proof of Lemma 5.6.** Let (_A,B_) denote the given Monotone Min-Plus Convolution instance over the universe \[_un_\] (where both _A,B_ are monotone), and rewrite these two sequences as

\(A[i]=A_1[i]\cdot u+A_0[i],\)<br>
\(B[j]=B_1[j]\cdot u+B_0[j],\)

where _A_<sub>0</sub>_,B_<sub>0</sub> have entries at most _u_ and _A_<sub>1</sub>_,B_<sub>1</sub> have entries at most _n_. In fact, we may assume without loss of generality that _A_<sub>0</sub>\[_i_\]_,B_<sub>0</sub>\[_j_\]_\<u/_2 (by splitting both sequences into two subsequences, splitting the entries that are less than _u/_2 from the other entries, and computing their four pairwise min-plus convolutions).

Toward computing _A∗B_ we maintain a sequence _C_, initialized with \(\perp\). Over the course of the algorithm we will modify _C_ by updates of the form \(C[k]\leftarrow min\{C[k],A[i]+B[j]\}\) (so that we never underestimate an output), claiming that, when the algorithm terminates, we have _A∗B=C_. This also means that our algorithm can provide a witness _i_ for each entry _C_\[_k_\] in the final output, as desired.

Let \(\delta>0\) be a constant to be determined, let \(\Delta_X=\lceil n^\delta\rceil\) and let \(\Delta_Y=\lceil n^{2\delta}\rceil\). Let _X_ denote the multiples of \(\Delta_X\) in the range \[0_,n_\], and let _Y_ denote the multiples of \(\Delta_Y\) in the range \[0_,n_\].<tbc>

