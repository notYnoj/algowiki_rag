The proof of this theorem follows by combining the work of Amirkhanyan, Bush, and Croot \[11\] with Sanders’ state-of-the-art bounds \[87\] for the Freiman-Ruzsa theorem. To state these two ingredients, we start with some definitions. A set of the form

\(P=\left\{\sum_{i=1}^d\ell_ia_i:|\ell_i|\le L_i\right\}\)

is called a (centered) _generalized arithmetic progression_. Here, _d_ is called the _dimension_ of the progression. We say that _P_ is _proper_ if each element \(p\in P\) has a unique representation of the form \(\sum_{i=1}^d\ell_ia_i\) for \(|\ell_i|\le L_i\). Then Sanders’ result \[87\] can be stated as follows; see also \[75\] for an exposition of this result.

**Theorem A.1** (Quasi-Polynomial Freiman-Ruzsa \[87\])**.** _Let X be an integer set with_ \(|X+X|\le K|X|\)_. Then X can be covered by_ exp((log_K)_<sup>_O_(1)</sup>) _translates of a proper generalized arithmetic progression with dimension O_((log_K)_<sup>_O_(1)</sup>) _and size at most_ exp((log_K)_<sup>_O_(1)</sup>)|_X|._

The main result from \[11\] can be stated as follows.

**Theorem A.2** (Condensing Lemma \[11\])**.** _Let P be a generalized arithmetic progression of the form_<tbc>

\(P=\left\{\sum_{i=1}^d\ell_ia_i:|\ell_i|\le L_i\right\}\)

<tbc>_such that_<tbc>

\(\left\{\sum_{i=1}^d\ell_ia_i:|\ell_i|\le 4L_i\right\}\)

<tbc>_is also proper. Then there are integers_ \(a'_1,\dots,a'_d\) _such that the map_ \(h:P\rightarrow\mathbb{Z}\) _defined by_

\(h\left(\sum_{i=1}^d\ell_ia_i\right)=\sum_{i=1}^d\ell_ia'_i\)

_is order-preserving, and such that_ \(|h(x)|\le d^{O(d)}|P|\) _for all_ \(x\in P\).

**Proof of Theorem 1.11.** Let \(X\subseteq\mathbb{Z}\) be arbitrary with doubling _K_. From Theorem A.1 it follows that _X_ can be covered by exp((log_K)_<sup>_O_(1)</sup>) translates of a proper generalized arithmetic progression _Q_ with dimension \(d\le O((logK)^{O(1)})\) and size exp((log_K)_<sup>_O_(1)</sup>)|_X|._ We express _Q_ as<tbc>

\(Q=\left\{\sum_{i=1}^d\ell_ix_i:|\ell_i|\le L_i\right\},\)

<tbc>and let<tbc>

\(P=\left\{\sum_{i=1}^d\ell_ix_i:|\ell_i|\le\left\lfloor\frac{L_i}{4}\right\rfloor\right\}.\)

<tbc>Note that _Q_ satisfies the conditions of Theorem A.2, so there are integers \(x'_1,\dots,x'_d\) such that the map \(h':Q\rightarrow\mathbb{Z}\) defined by<tbc>

\(h'\left(\sum_{i=1}^d\ell_ix_i\right)=\sum_{i=1}^d\ell_ix'_i.\)

