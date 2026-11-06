factories, and they want to route all their products to facilities on the right satisfying the following constraints: 1) each edge can route only 1 product; and 2) each facility can receive at most _d/_8 products. The ProposeAcceptFinalize algorithm described below finds a set of edges _M_ to enable such routing, also called a feasible route as explained earlier.

Notice that for a facility \(v\in R\), the proposals it receives in iteration _i_+1 is a subset of the proposals it receives in iteration _i_. Therefore, once _v_ starts accepting in some iteration _i_, it will also accept all proposals received in future rounds _i_+1_,i_+2_,..._ too, if any proposals are received. Moreover, the total number of product _v_ receives will not exceed _d/_8. Pippenger \[Pip96\] and Asharov et al. \[AKL<sup>+</sup>20b\] showed the following fact:

**Fact 8.2** (Pippenger \[Pip96\] and Asharov et al. \[AKL<sup>+</sup>20b\])**.** _There exist an appropriate constant_ \(\epsilon\in(0,1)\) _and a bipartite expander graph family_ \(\{G_{\epsilon,m}\}_{m\in\mathbb{N}}\) _where each vertex has d edges for a constant_ \(d:=d(\epsilon)\) _assumed to be a multiple of_ 8_, such that for any_ \(m\in\mathsf{SQ}\subseteq\mathbb{N}\)_, at the end of the above_ ProposeAcceptFinalize _procedure which runs for_ iter _iterations (and assuming it is instantiated with the family of graphs_ \(\{G_{\epsilon,m}\}_{m\in\mathbb{N}}\)_), the following must hold:_

1. _at most m/_2iter _vertices in L remain unsatisfied;_<tbc>

2. _every satisfied vertex in_ \(u\in L\) _has at least d/_2 _edges in the output matching M;_<tbc>

_3._ _for every vertex in_ \(v\in R\)_, the output matching M has at most d/_8 _edges incident to v._

Given the ProposeAcceptFinalize subroutine, we can realize a 1/log_<sup>c</sup>n_-lossy loose compaction as follows where _c\>_1 denotes a constant.

\begin{tabular}{cc}
\multicolumn{2}{c}{ProposeAcceptFinalize subroutine} \\
\multicolumn{2}{c}{Initially, each productive factory is _unsatisfied_ and each unproductive factory is _satisfied_. For a productive factory \(u\in L\), we use notation load(_u_) to denote the number of products it has (corresponding to the number of real elements in the chunk).} \\
\multicolumn{2}{c}{**Algorithm:** Repeat the following for iter times and output the resulting matching _M_ at the end:} \\
(a) & _Propose_: Each unsatisfied factory sends a proposal (i.e., the bit 1) to each one of its neighbors. Each satisfied factory sends 0 to each one of its neighbors. \\
(b) & _Accept_: If a facility \(v\in R\) received no more than _d/_8 proposals, it sends an acceptance message to each one of its _d_ neighbors; otherwise, it sends a reject message along each of its _d_ edges. \\
(c) & _Finalize_: Each currently unsatisfied factory \(u\in L\) checks if it received at least \(\frac{d}{2}\) acceptance messages. If so, add the set of edges over which acceptance messages are received to the matching _M_. At this moment, this factory becomes satisfied. \\
\end{tabular}

\begin{tabular}{cc}
\multicolumn{2}{c}{1/(log_n)<sup>c</sup>_**-Lossy Loose Compaction**} \\
\multicolumn{2}{c}{**Input:** An input array **I** of _n_ elements, in which at most _n/_128 are real and the rest are dummies.} \\
\multicolumn{2}{c}{**Assumption**: Without loss of generality, we assume that _d_ is a multiple of 8. Further, we assume that _m_ is a perfect square and that _n_ is a multiple of _d/_2; henceforth let _m_:=_n/(d/_2)=2_n/d_. The algorithm can be easily generalized to any choice of _n_ -- see Remark 3.} \\
\end{tabular}

