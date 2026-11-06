Note that \(1\le\mathrm{size}(v)\le\ell\) for each \(v\in V(T^\ell)\). For convenience, if \(U\subset V(T^\ell)\), we write \(\mathrm{Size}(U)=\sum_{u\in U}\mathrm{size}(u)\).

**Observation 35.** _Each node in_ \(T^\ell\) _with exactly one child has size exactly_ \(\ell\).

## 7.2 An elimination algorithm

We now adapt WSHTreeSelect to use as a subroutine. (In the following, WSHTreeSelect always refers to the improved algorithm of lemma 28, with O(_k_+OPT) running time.) Recall that our strategy is to iteratively remove a subset of low-rank nodes. It turns out WSHTreeSelect achieves this quite naturally, as we show now.

**Lemma 36.** _After some iteration of the main loop of_ WSHTreeSelect_, let D be the set of elements deleted from Q and let C be the set of corrupted elements currently in Q. Then each node in D is smaller than each node outside of_ \(D\cup C\).

_Proof._ Consider a node \(v\in D\), and the time it was removed from _Q_. Then _v_ is smaller than all nodes in \(V(T)\backslash(C\cup D)\) by lemma 22. Since \(D\cup C\) only grows over time, this concludes the proof.

We now describe a variant of WSHTreeSelect, which we call WSHTreeElim. For the sake of readability, let \(\delta=1/43\) in the following. WSHTreeElim receives an additional integer parameter _m_, which must be at least 2 and at most \(\frac{1}{2}\delta k\). Let \(\ell=\lfloor\delta\frac{k}{m}\rfloor\). We construct \(T^\ell\), and then run WSHTreeSelect on \(T^\ell\), with the following changes.

• We maintain a set _D_ of elements removed from the priority queue, and the values Size(_D_) and _W(D_).<tbc>

• Instead of repeating the main loop _k_-1 times, we repeat it as long as \(\mathrm{Size}(D)\le\frac{1}{2}\delta k\) and \(W(D)\le 7m\).<tbc>

• At the end, we do not call Select(_S,k_). Instead, we return \(D'=\bigcup_{u\in D}P(u)\) if still \(W(D)\le 7m\) (so we stopped due to \(\mathrm{Size}(D)>\frac{1}{2}\delta k\)), or return a special value `FAIL` if we stopped due to _W(D)\>_7_m_.<tbc>

• To ensure the desired running time even in certain degenerate cases, the algorithm needs to stop _before_ the `delete`(_x_) call would cause _W(D)\>_7_m_ (algorithm 1, line 10). This can be done by adding a check \(W(D)+w(x)\le 7m\) before `delete`(_x_).<tbc>

3
2
2
1
3
1
2

Figure 5: Contracting a tree _T_ (left) into a tree _T_<sup>3</sup> (right). Red vertices and edges are being contracted. The numbers for _T_<sup>3</sup> indicate node sizes.

