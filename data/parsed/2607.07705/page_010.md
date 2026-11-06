### 3.4 Remaining profits

While the basic concept of profits clearly suggests to look for a profitable enough tree edge set, it does not really allow us to construct a such a tree set iteratively.

Assume, for example, that \(A=\emptyset\) and that we guess correctly that an edge \(e_1\in E(T)\) is not a part of the solution. We know that if we remove _e_<sub>1</sub> from _T_ and add all its inverse edges, we gain **p**(_e_<sub>1</sub>) profit from this. Afterwards, we move on to guessing the second edge _e_<sub>2</sub> that should be removed from _T_. But the profits are not "up-to-date" anymore, since it might be the case that \(\mathrm{Inv}(e_1)\cap\mathrm{Inv}(e_2)\neq\emptyset\), and we gain less profit than **p**(_e_<sub>2</sub>) from removing _e_<sub>2</sub>.

We introduce the concept of _remaining profit_, which is aimed to support the additive edge removal and represent the actual profit when some edges are already removed from _T_.

**Definition 5** (Remaining profits)**.** Let (_G,_**w**) be a weakly-connected digraph with positive edge weights. For a tree edge \(e\in E(T)\), and for a tree edge set \(S\subseteq E(T)\), we denote by

\(\mathbf{rp}(G,\mathbf{w},S,e)=\mathbf{w}(\mathrm{Inv}(e)\backslash\mathrm{Inv}(S))-\mathbf{w}(e)\)

the _remaining profit_ of _e_ in (_G,_**w**) with respect to _S_. As usual, we shorten this to **rp**(_S,e_).

The following properties of remaining profits are straightforward from the definition.

**Observation 5.** _Let_ (_G,_**w**) _be a weakly-connected digraph with positive edge weights, let_ \(e\in E(T)\)_, let_ \(S\subseteq E(T)\) _and let_ \(e_1,e_2,\dots,e_q\in E(T)\) _such that_ \(e_i\neq e_j\) _for_ \(i\neq j\)_. Then_

• \(\mathbf{rp}(S,e)\le\mathbf{p}(e)\).<tbc>

• \(\mathbf{p}(\{e_1,\dots,e_q\})=\sum_{i=1}^q\mathbf{rp}(\bigcup_{j=1}^{i-1}\{e_j\},e_i)\).

In the following observation, we highlight that picking _k_ edges from _E(T_) consecutively, each time with positive remaining profit, is a winning strategy for MAS/MaxST.

**Observation 6.** _Let_ I=(_G,_**w**_,k_) _be an instance of MAS/MaxST. If there exist_ \(e_1,e_2,\dots,e_k\in E(T)\) _with_ \(\mathbf{rp}(\bigcup_{j=1}^{i-1}\{e_j\},e_i)\ge 1\) _for each_ \(i\in[k]\)_, then_ I _is a yes-instance._

_Proof._ Straightforward from the second point of Observation 5 and the first point of Observation 4.

For \(A=\emptyset\), solving an instance is equivalent to finding a set \(S\subseteq E(T)\) with \(\mathbf{p}(S)\ge k\).

## 4 FPT-algorithm for integral edge weights

In this section, we provide four major blocks of the proof of Theorem 1, each block corresponds to a lemma.

### 4.1 Limiting allowed edges

In Section 3 we gave a lot of insight on blocked edges. Allowed edges, if given in instance without inverse edges, are somewhat simpler to deal with, even for rational weights. We are able to show an algorithm that constructs a solution if their total weight is at least 3_k_.

