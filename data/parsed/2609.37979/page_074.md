### Rabin games.

A similar distinction arises for Rabin games. A Rabin game is equipped with a family of pairs (_E_<sub>1</sub>_,F_<sub>1</sub>)_,...,(E<sub>r</sub>,F<sub>r</sub>_), where \(E_i,F_i\subseteq V\) , and Player 1 wins if there exists an index \(i\in[r]\) such that _E<sub>i</sub>_ is visited only finitely often and _F<sub>i</sub>_ is visited infinitely often. If the pairs come with fixed identifiers, we may label every vertex _v_ by

\(w(v):=\big(\{i\in[r]|v\in E_i\},\{i\in[r]|v\in F_i\}\big).\)

The Rabin condition is then a Borel objective on the resulting label sequence, so Theorem A.2 also applies to this representation.

As in the generalized Büchi case, however, this encoding requires isomorphisms to preserve every set _E<sub>i</sub>_ and _F<sub>i</sub>_ individually. Under the more natural notion of isomorphism, the Rabin pairs may be permuted, while the pairing and the roles of their two components are preserved. More precisely, one requires a game-graph isomorphism \(\varphi\) and a permutation \(\pi\) of \[_r_\] such that

\(\varphi(E_i)=E'_{\pi(i)}\text{and}\varphi(F_i)=F'_{\pi(i)}\)

for every \(i\in[r]\). Encoding the pairs and their two types of membership using auxiliary vertices and incidence edges allows this symmetry to be represented. However, the same obstacle remains: our current shadow-play construction does not provide a single globally consistent correspondence between the Rabin pairs, and therefore does not establish preservation of the Rabin objective in this representation.

### Open questions.

Under the natural notions of isomorphism described above, we leave open whether the Isomorphic-Priors model admits algorithms with _O_(poly(_k,n_)) preprocessing time and

1. _O(n_<sup>2.99</sup>) query time for generalized Büchi games, when the Büchi sets may be arbitrarily permuted; and<tbc>

2. _O_(poly(_n_)) query time for Rabin games, when the Rabin pairs may be arbitrarily permuted.

## A.3 The Replacement Path Problem

The work of Vassilevska Williams and Williams \[VW10\] is widely regarded as an early landmark in fine-grained complexity. In particular, they showed that a number of fundamental problems with best known subcubic algorithms are tightly related via subcubic reductions, yielding an equivalence web among path, matrix, and triangle problems.

In this appendix, we show that, in our model, Replacement Path can be solved in _O_((_n+m_)log_n_) time.

**Definition A.4** (Replacement Path)**.** An instance of Replacement Path is defined by a tuple _G_=(_V,E,c,P_), where

• (_V,E_) is a finite directed graph,<tbc>

• \(c:E\rightarrow\mathbb{R}\) is a cost function assigning a non-negative cost to each edge,<tbc>

• _P=v_<sub>1</sub>_v_<sub>2</sub>_...v<sub>k</sub>_ is a shortest path.

The solution for Replacement Path is a vector _OPT_=(_OPT_<sub>1</sub>_,...,OPT_<sub>_k_-1</sub>), where for each \(i\in\{1,\dots,k-1\}\), _OPT<sub>i</sub>_ denotes the cost of the shortest _v_<sub>1</sub>_,v<sub>k</sub>_-path in _G<sub>i</sub>_=(_V,E_\\{(_v<sub>i</sub>,v_<sub>_i_+1</sub>)}).

_Remark_ A.5. We may assume without loss of generality that _G_ contains no negative cycles reachable from _v_<sub>1</sub> and to _v<sub>k</sub>_. Indeed, since _P_ is a shortest path, the distance between its endpoints is finite.

