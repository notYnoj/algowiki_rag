Otherwise, if \(|D^*|\ge 3m+1\), let \(D_1^*\) be the set of nodes in _D_<sup>∗</sup> with size strictly less than \(\ell\). Then, using the fact that \(\ell=\lfloor\delta\frac{k}{m}\rfloor>\frac{1}{2}\delta\frac{k}{m}\) since \(m\le\frac{1}{2}\delta k\), we have

\(|D^*\backslash D_1^*|\le\text{Size}(D^*)/\ell\le(\frac{1}{2}\delta k+\ell)/\ell<m+1,\)

which implies that \(|D_1^*|>|D^*|-m-1\ge 2m\).

Each node in \(D_1^*\) is a leaf or has degree at least two, so we now know that _D_<sup>∗</sup> contains more than _m_ leaves or more than _m_ nodes of degree at least two. Either fact implies that the prefix of \(T^\ell\) induced by _D_<sup>∗</sup> contains more than _m_ leaves, which implies \(c^*(T^\ell,D^*)>m\), as desired.

We are now ready to analyze the performance of WSHTreeElim.

**Lemma 40.** WSHTreeElim _performs_ O(_m_) _comparisons, and can be implemented with running time_ O(_k)._

_Proof._ To determine the number of comparisons, we can ignore the preprocessing of _T_ into \(T^\ell\). By lemma 27, the number of comparisons is O(_W(D_)). If the algorithm does not return `FAIL`, we have \(W(D)\le m\) and are done. Suppose it returns `FAIL`. Then \(W(D)\le m\) in the final iteration before we stop, and the last iteration only takes constant time to perform the check \(W(D)+w(Q.\text{\texttt{find-min}}())\le\frac{1}{2}\delta k\).

The running time _without_ preprocessing and maintaining Size(_D_) is still O(_m_) by lemma 28. To achieve the O(_k_) running time bound, we perform the preprocessing only as needed. Whenever the algorithm requests a node, we may need to move down a path of length at most \(\ell\). The running total running time for this is \(\mathcal{O}(m\cdot\ell)=\mathcal{O}(k)\). Finally, maintaining Size(_D_) and computing \(D'\) at the end also takes O(_k_) time.

## Supporting forests.

For simplicity, we have so far only considered input _trees_, but we will need an equivalent of WSHTreeElim for _forests_. This is possible with the following simple extension: Given a forest _F_ along with _k_ and _m_, first check whether the number of roots in _F_ is at least _m_. If that is the case, then \(c^*(F,\emptyset)\ge m\), so we can immediately return `FAIL`. Otherwise, as described at the start of section 5 add a dummy root _r_ to _F_, and add all original roots of _F_ as children to _r_. Then, run WSHTreeElim(_F,k_+1_,m_), and return the result (discarding the dummy root _r_ if necessary). Call this procedure WSHForestElim.

**Lemma 41.** WSHForestElim(_F,k,m_) _takes_ O(_m_) _comparisons and_ O(_k_) _time. It either returns a set_ \(D'\) _of at least_ \(\frac{1}{4}\delta k\) _nodes with rank strictly less than k, or_ `FAIL`_. If it returns_ `FAIL`_, then_ \(c^*(T,\frac{1}{2}k-1)\ge m\).

_Proof._ Follows directly from lemmas 37 to 40; taking into account the dummy root, and using that \(\frac{1}{2}\delta k-1\ge\frac{1}{4}\delta k\).

