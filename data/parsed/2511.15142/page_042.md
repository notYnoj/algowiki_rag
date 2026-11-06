This insight extends naturally to the matroid intersection setting, where shortest augmenting paths must also be minimal (i.e., having fewest arcs among paths of equal weight), a property standard algorithms like Bellman-Ford already ensure. We show that the path-finding steps can again be carried out using only comparisons of common independent sets. The details appear below:

## E.3 Generalization to Matroid Intersection

We now extend the concepts from bipartite matching to matroid intersection. Let M<sub>1</sub>=(_E,_I<sub>1</sub>) and M<sub>2</sub>=(_E,_I<sub>2</sub>) be matroids over a common ground set _E_, and let \(Y\in\mathcal{I}_1\cap\mathcal{I}_2\) be a common independent set. Define the _exchange graph H_(M<sub>1</sub>,M<sub>2</sub>_,Y_) as a directed bipartite graph with color classes _Y_ and _E_\\_Y_ . For \(y\in Y\) and \(x\in E\backslash Y\) :

\((y,x)\in H\Longleftrightarrow Y-y+x\in\mathcal{I}_1,\)<br>
\((x,y)\in H\Longleftrightarrow Y-y+x\in\mathcal{I}_2.\)

Let _H_(M<sub>1</sub>_,Y),H_(M<sub>2</sub>_,Y_) be the subgraphs of _H_ with edges corresponding to M<sub>1</sub>,M<sub>2</sub> respectively.

We know the following lemma (see \[Sch90, Section 10.4\]):

**Lemma E.6** (Matching lemmas)**.** _For_ \(Y\in\mathcal{I}_1\)_, let H_<sub>1</sub>=_H_(M<sub>1</sub>_,Y_).

(_a)_ _If_ \(Z\in\mathcal{I}_1\) _with_ |_Y_|=|_Z|, then H_<sub>1</sub> _contains a perfect matching on_ \(Y\Delta Z\).<tbc>

_(b)_ _If_ \(Z\subseteq E\) _such that H_<sub>1</sub> _contains a unique perfect matching on_ \(Y\Delta Z\)_, then_ \(Z\in\mathcal{I}_1\).

Let \(X_1:=\{x\in E\backslash Y:Y+x\in\mathcal{I}_1\}\) and \(X_2:=\{x\in E\backslash Y:Y+x\in\mathcal{I}_2\}\). Given a weight function \(w:E\rightarrow\mathbb{R}\), define the length of any path (or cycle) _P_ in _H_ by:

\(\ell(P):=-\sum_{e\in P\cap Y}w_e+\sum_{e\in P\backslash Y}w_e.\)

A common independent set \(Y\in\mathcal{I}_1\cap\mathcal{I}_2\) is _extreme_ if it minimizes weight among all common independent sets of the same size. We know the following lemmas (see Theorem 10.7, Theorem 10.11, Theorem 10.12 in \[Sch90\])

**Lemma E.7.** _The subset_ \(Y\in\mathcal{I}_1\cap\mathcal{I}_2\)_, is a maximum cardinality common independent set iff there is no directed path from X_<sub>1</sub> _to X_<sub>2</sub> _in H._

**Lemma E.8.** _Consider a common independent set_ \(Y\in\mathcal{I}_1\cap\mathcal{I}_2\).

(_i)_ _Y is extreme if and only if H_(M<sub>1</sub>,M<sub>2</sub>_,Y_) _contains no directed cycle of negative length._<tbc>

_(ii)_ _If Y is extreme, and P is a shortest (minimal-hop) path from X_<sub>1</sub> _to X_<sub>2</sub> _in H, then_ \(Y\triangle P\) _is also extreme._

To mimic the Bellman-Ford algorithm, we generalize the notion of augmenting paths using _minimal paths and cycles_, defined with respect to both weight and hop-count.

### Minimal Cycles and Paths.

A cycle _C_ in _H_ is _minimal_ if no proper subcycle \(C'\) satisfies \(\ell(C')\le\ell(C)\). Similarly, for \(y\in Y\) , define P(_y,t_) to be the set of directed paths from _X_<sub>1</sub> to _y_ in _H_ using at most 2_t_-1 arcs. A path \(P\in\mathcal{P}(y,t)\) is _minimal_ if it is lexicographically minimal with respect to length and number of arcs:

\(\text{For all}P'\in\mathcal{P}(y,t),(\ell(P'),|P'|)\unknown(\ell(P),|P|).\)

In the following lemma, we prove our main observation that augmenting an extreme common independent by a minimal path gives a common independent set.

