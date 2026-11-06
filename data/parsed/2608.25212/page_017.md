_Proof._ By Theorem 33, C has bounded versatile symmetric difference. Thus, by Corollary 20, we compute an sd-degeneracy sequence of _G_ of constant width in time O(_n_<sup>2</sup>). By Lemma 13, we get an interval biclique partition of _G_ with O(_n_) bicliques in further O(_n_log_n_+|_E(G_)|)=O(_n_<sup>2</sup>) time. We finally invoke Theorem 5 from every vertex as source, and conclude.

**Theorem 7.** _For every graph class_ C _of linear neighborhood complexity, there is an_ O<sub>C</sub>(_n_<sup>2</sup>)_-time algorithm that, given any adjacency matrix M of an n-vertex graph of_ C_, yields a data structure that computes the matrix-vector product MX in time_ O<sub>C</sub>(_n_) _for any n-vector X._

_In particular, the product MN can be computed in_ O<sub>C</sub>(_n_<sup>2</sup>) _time for any_ \(n\times n\) _matrix N._

_Proof._ As in the proof of Theorem 6, we obtain an interval biclique partition of _G_ with O(_n_) bicliques in O(_n_<sup>2</sup>) time. We conclude with Lemma 14.

## 6 Finding an sd-degeneracy sequence in randomized linear time

In this section, we prove Theorem 4: we show how to compute an sd-degeneracy sequence of width \(\mathcal{O}(n^{1-1/\rho})\) in expected linear time in graphs of VC density \(\rho\). In particular, this yields an expected linear-time algorithm that outputs sd-degeneracy sequences of constant width in classes of linear neighborhood complexity (Theorem 2). The proof relies on a result in learning theory and VC- combinatorics related to Haussler’s packing lemma (Theorem 32).

A _set system_ on a domain _D_ is a set F of subsets of _D_. For \(A\subseteq D\), denote<tbc>

\(\mathcal{F}\unknown_A:=\{F\cap A:F\in\mathcal{F}\}.\)

<tbc>The _shatter function_ of a set system F is the function \(\pi_\mathcal{F}:\mathbb{N}\rightarrow\mathbb{N}\) defined by

\(\pi_\mathcal{F}(m):=max\{|\mathcal{F}\unknown_A|:A\subseteq D,|A|\le m\}.\)

The _VC dimension_ of a set system F is the largest integer _d_ such that there exists a subset \(A\subseteq D\) of size _d_ with F\(\unknown_A=2^A\).

Given a finite domain _X_, an _s-sample_ is a tuple \(S=(x_1,\dots,x_s)\in X^s\) of _s_ elements of _X_. We will consider _s_-samples of _X_ drawn uniformly at random, that is, each element _x<sub>i</sub>_ of _S_ is drawn independently and uniformly at random from _X_. (Note that an _s_-sample can contain the same element multiple times.)

Given a set _F_ and an _s_-sample _S_=(_x_<sub>1</sub>_,...,x<sub>s</sub>_), denote \(F\cap S:=F\cap\{x_1,\dots,x_s\}\). For a set system F on a domain _X_ and integer \(s\ge 1\), denote

\(\mathcal{F}\unknown_s:=\{(S,F\cap S)|S\in X^s,F\in\mathcal{F}\},\)

that is, the set of all restrictions of sets in F to all possible samples of size _s_. The next lemma originates in \[38, Lemma 9\] as part of a proof of Haussler’s packing lemma. It is in the spirit of the classical PAC learning model, and states that sets from a set system of bounded VC dimension can be learned from a small random sample.

**Lemma 25** (\[38\])**.** _Let_ F _be a set system on a finite domain X of VC dimension at most d. For any_ \(\varepsilon>0\) _and integer_ \(s\ge 1\)_, there exists a map_ \(f:\mathcal{F}\unknown_s\rightarrow 2^X\) _such that for every_ \(F\in\mathcal{F}\),

\(\mathbb{P}_{S\sim X^s}\left(|F\triangle f(S,F\cap S)|<\frac{d}{\varepsilon s}\cdot|X|\right)\ge 1-\varepsilon,\)

_where S∼X<sup>s</sup> denotes that S is an s-sample of X, drawn uniformly at random._

