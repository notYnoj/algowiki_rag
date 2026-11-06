Splay is only _approximately_ monotone. Let _T_ be a left spine with integer keys 1 to 2_<sup>k</sup>_-1 for _k\>_3, let \(Y=\oplus_{i=0}^{k-1}(2^i)\) be the geometric sequence ascending in powers of two, let \(Y'\) be the reversal of _Y_ and let \(X=Y'\oplus Y\) . Splaying the first half of _X_ efficiently brings the requested keys close to the root and ensures cost(_X,T_)=2_<sup>k</sup>_+4_k_-5. Meanwhile, splaying each request in _Y_ only halves the depth of the next requested key, so cost(_Y,T_)=2<sup>_k_+1</sup>-3. Hence the limit of Splay’s subsequence overhead, as tree size increases, is at least two.

Our simulation embedding is designed for minimalism. A more careful analysis can reduce the constant factor. Two prior works construct simulation embeddings for binary search tree algorithms. Harmon builds a simulation embedding for the geometric version of Greedy \[34, Chapter 2.3.4\], while Russo’s simulation embedding for Splay uses rotation-based executions and potential-based analysis \[58\]. Neither work treats simulation embeddings as mathematical objects in their own right. Subsequent to the publication of our SODA paper \[46\], Chalermsook and Jiamjitrak constructed simulation embeddings for a class of template-like algorithms using potential-based methods \[16\]. Reddmann examines several algorithms’ competitive overheads numerically \[56\].

## 4 Startup Overhead

In principle, an algorithm may need to execute many requests in order to bring a poorly structured initial tree into a good state before it can behave optimally. Formally, an algorithm A is _eventually optimal_ if there exists a positive constant _b_ and _startup overhead g_ mapping starting trees to integers such that \(\mathrm{cost}_\mathcal{A}(X,T)\le b\mathrm{OPT}(X,T)+g(T)\) for all request sequences _X_ and corresponding initial trees _T_. Similarly, if \(\mathrm{cost}_\mathcal{A}(Y,T)\le b\mathrm{cost}_\mathcal{A}(X,T)+g(T)\) for all instances (_X,T_) and subsequences _Y_ of _X_ then A is _eventually monotone_. (Eventual optimality implies eventual monotonicity.)

Some works do not distinguish between eventual and dynamic optimality, but Sleator and Tarjan were more optimistic. They made no allowance for startup overhead in their original statement of the dynamic optimality conjecture \[61\]. As we shall show, their optimism was well-placed: if Splay is eventually optimal then it is dynamically optimal. Our proof bounds startup overhead by averaging execution cost over many repetitions of a request sequence. A _repeater_ F for algorithm A is a mapping from integer-instance pairs to request sequences for which there exists positive constants _a_ and _c_ such that \(k\mathrm{cost}_\mathcal{A}(X,T)\le a\mathrm{cost}_\mathcal{A}(\mathcal{F}(k,X,T),T)\) and \(\mathrm{OPT}(\mathcal{F}(k,X,T),T)\le ck\mathrm{OPT}(X,T)\) for all _k\>_0, request sequences _X_, and starting trees _T_. If a repeater exists, then A is _repeatable_.

**Theorem 4.1.** _Eventually optimal repeatable binary search tree algorithms are dynamically optimal._

_Proof._ Repeatability and eventual optimality imply positive constants _a_, _b_ and _c_ and startup overhead _g_ such that \(k\mathrm{cost}_\mathcal{A}(X,T)\le a\mathrm{cost}_\mathcal{A}(\mathcal{F}(k,X,T),T)\le ab\mathrm{OPT}(\mathcal{F}(k,X,T),T)+ag(T)\le(abc)k\mathrm{OPT}(X,T)+ag(T)\) for all request sequences _X_, starting trees _T_ and _k\>_0. Choose \(k\ge g(T)/\mathrm{OPT}(X,T)\) to absorb the overhead and obtain \(\mathrm{cost}_\mathcal{A}(X,T)\le a(bc+1)\mathrm{OPT}(X,T)\). \(\square\)

**Theorem 4.2.** _Eventually monotone repeatable coercible algorithms are dynamically optimal._

_Proof._ These properties imply there exists a simulation embedding S, constant _b_ and startup overhead _g_ for which \(\mathrm{cost}_\mathcal{A}(X,T)\le b\mathrm{cost}_\mathcal{A}(\mathcal{S}(E),T)+g(T)\le b\mathrm{OPT}(X,T)+g(T)\) for all instances (_X,T_) and corresponding optimal executions _E_. Apply Theorem 4.1. \(\square\)

**Theorem 4.3.** _If Splay is eventually monotone then it is dynamically optimal._

_Proof._ We show Splay is repeatable. Let _X_ be a request sequence with initial tree _T_. Let _V_ be the final tree in Splay’s execution of _X_ starting from _T_, and define the extended sequence \(U=X\oplus W\), where _W_ is the sequence described in Theorem 3.4 that induces Splay to transform<tbc>

