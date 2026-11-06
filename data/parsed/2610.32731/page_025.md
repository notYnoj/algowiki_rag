Observe that lemmas 21, 26 to 28 and 36 still hold for WSHTreeElim with respect to \(T^\ell\), since we essentially only changed exit conditions. We now analyze WSHTreeElim, starting with the non-`FAIL` case.

**Lemma 37.** _If_ WSHTreeElim _returns a set_ \(D'\) _(and not_ `FAIL`_), then at the end_ \(|D'|>\frac{1}{2}\delta k\) _as well as_ \(W(C\cup D)<\frac{1}{2\delta}m\) _and_ \(\mathrm{Size}(C\cup D)<\frac{1}{2}k\).

_Proof._ Let _D_ be the set of _m_ nodes deleted from _Q_, and let _C_ be the set of corrupted elements in _Q_ at the end. Observe that \(|D'|=\mathrm{Size}(D)\). After the last loop iteration, we have \(\mathrm{Size}(D)>\frac{1}{2}\delta k\), which immediately implies the first part of the lemma.

Since the algorithm did not return `FAIL`, we have \(W(D)\le 7m\). By lemma 26, we have \(W(C)\le 2W(D)\), so \(W(C\cup D)\le 3\cdot 7m<\frac{1}{2\delta}m\), as desired. Since each node has weight at least one and size at most \(\ell\), we have

\(\mathrm{Size}(C\cup D)\le\ell(|C|+|D|)\le\ell(W(C)+W(D))<\ell\cdot\frac{1}{2\delta}m\le\frac{1}{2}k.\)

**Lemma 38.** _If_ WSHTreeElim _returns a set_ \(D'\) _(and not_ `FAIL`_), then every node in_ \(D'\) _has rank strictly less than k._

_Proof._ Take some node \(v'\in D'\). By definition, there exists a node \(v\in D\) with \(v'\prec v\). Now lemma 36 implies that _v_ smaller than all nodes in \(X=V(T^\ell)\backslash(C\cup D)\). That means a node \(u'\) can only be smaller than _v_ if it is not a descendant of any \(x\in X\). This means that \(u'\in P(u)\) for some \(u\in C\cup D\cup\mathrm{Children}(C\cup D)\). We distinguish two possible cases.

• If \(u\in C\cup D\), then there are at most \(\mathrm{Size}(C\cup D)<\frac{1}{2}k\) such nodes \(u'\) by lemma 37.<tbc>

• Suppose now \(u\in\mathrm{Children}(T^\ell,C\cup D)\backslash(C\cup D)\). Observe that \(|\mathrm{Children}(T^\ell,C\cup D)|\le W(C\cup D)\). Thus, by lemma 37, there strictly less than \(\frac{1}{2\delta}m\) such nodes _u_, and \(\ell\le\delta\frac{k}{m}\) times as many such nodes \(u'\), for a total of less than \(\frac{1}{2}k\) nodes \(u'\).

With this case distinction, we have shown that all but _k_-1 nodes are smaller than _v_, so _v_ (and thus \(v'\)) has rank strictly less than _k_.

We now show that if the algorithm returns `FAIL`, then _m_ was chosen too small.

**Lemma 39.** _If_ WSHTreeElim _returns_ `FAIL`_, then_ \(c^*(T,\frac{1}{2}k-1)>m\).

_Proof._ Let _D_ be the set of deleted nodes, and consider the node _x_ chosen in the last iteration (note that we stop right before deleting _x_ from _Q_). Let \(D^*=D\cup\{x\}\), and let \(D'=\bigcup_{u\in D^*}P(u)\). We have _W(D_<sup>∗</sup>)_\>_7_m_. Since we did _not_ stop in the second-to-last iteration, we have \(\mathrm{Size}(D)\le\frac{1}{2}\delta k\). Since \(\mathrm{size}(x)\le\ell\), we have \(\mathrm{Size}(D^*)=\mathrm{Size}(D\cup\{x\})\le\frac{1}{2}\delta k+\ell\).

Observe that _D_<sup>∗</sup> is a prefix of \(T^\ell\) by lemma 21, and thus \(D'\) is a prefix of _T_. We will show that \(c^*(T^\ell,D^*)>m\). This clearly implies that \(c^*(T,D')>m\), which in turn implies the lemma since \(|D'|=\mathrm{Size}(D)\le\frac{1}{2}\delta k+\ell\le(\frac{1}{2}\delta+\delta)k<\frac{1}{2}k\).

Observe that \(W(D^*)=|D^*|+\sum_{v\in D^*}\mathrm{deg}(T,v)=|D^*|+|D^*|-1+c(T^\ell,D^*)\), so \(c(T^\ell,D^*)>W(D^*)-2|D^*|+1>7m-2|D^*|+1\). If \(|D^*|\le 3m\), we are done.

