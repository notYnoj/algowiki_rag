The algorithm we use to obtain an \(O(\sqrt{logn})\)-approximation in Section 5 can be stated in its generality as follows.

**Theorem 23.** _Let f be a lower bound function. Assume that f is subadditive and that there exists an algorithm for_ MinGMConn _that costs at most O_(log_s)f(P,D_) _for any s-thin instance_ (_P,D). Then, there exists an efficient_ \(O(\sqrt{logn})\) _approximation algorithm for_ MinGMConn.

## F.2 Complete k-partite Demands

In this section, we consider the special case of instances (_P,D_) where the demands _D_ form a complete k-partite graph. This means, we can partition _P_ into disjoint subsets _S_<sub>1</sub>_,S_<sub>2</sub>_,...,S<sub>k</sub>_ such that \(D=S_i\times S_j\) for \(i,j\in\{1,\dots,k\}\) and \(i\neq j\). Again, we allow that points share _x_-coordinates but we assume that all points have distinct _y_-coordinates.

**Lemma 24.** _Let_ (_P,D_) _be an instance with complete k-partite demands and k-partition_ \(S_1\dot{\cup}S_2\dot{\cup},\dots,\dot{\cup}S_k\)_. Then there exists an efficient algorithm that computes a complete k-partite instance_ \((\tilde{P},\tilde{D})\) _such that_

1. \(\tilde{P}\subseteq P\) _and_ \(\tilde{D}\) _is the complete k-partite demand set on k-partition_ \(S_1\cap\tilde{P},S_2\cap\tilde{P},\dots,S_k\cap\tilde{P}\)<tbc>

2. _any feasible solution Q to_ \((\tilde{P},\tilde{D})\) _is feasible for_ (_P,D_) _as well, and_<tbc>

_3._ \(|\tilde{P}|=O(\mathsf{IS}(\tilde{P},\tilde{D}))\).

_Proof._ An _essential demand_ is a pair \((s_i,s_j)\in\tilde{D}\) where \(s_i\in S_i\) and \(s_j\in S_j\) with \(x(s_i)\neq x(s_j)\), such that the vertical side of the rectangle _R(s<sub>i</sub>,s<sub>j</sub>_) containing _s<sub>i</sub>_ does not contain any other point from _P_\\_S<sub>j</sub>_, and such that the vertical side of _R(s<sub>i</sub>,s<sub>j</sub>_) containing _s<sub>j</sub>_ does not contain any other point from _P_\\_S<sub>i</sub>_.

A point is called essential if there exists some essential demand pair involving this point. A point that is not essential is called _redundant_. Removing a redundant point from the instance is safe in the sense that any feasible solution _Q_ to the reduced instance is also feasible to the original solution. To see this, let \(s_i\in S_i\) be a redundant point and let _Q_ be a feasible solution to the reduced instance with point set _P_\\{_s<sub>i</sub>_}. Let \(s_j\in S_j\) and assume w.l.o.g. that _x(s<sub>i</sub>)\<x(s<sub>j</sub>_) and _y(s<sub>i</sub>)\<y(s<sub>j</sub>_). Since _s<sub>i</sub>_ is redundant there exists a point \(s\neq s_i,s\in P\backslash S_j\) on \(\lambda(s_i,s_j)\) or a point \(s'\neq s_j,s'\in P\backslash S_i\) on \(\rho(s_i,s_j)\). Consider first the case that there exists a point \(s\neq s_i,s\in P\backslash S_j\) on \(\lambda(s_i,s_j)\). Since _Q_ is feasible for _P_\\{_s<sub>i</sub>_} there exists a Manhattan path in \((P\backslash\{s_i\})\cup Q\) from _s_ to _s<sub>j</sub>_. This path can be extended to a Manhattan path from _s<sub>i</sub>_ to _s<sub>j</sub>_ in \(P\cup Q\) by adding _s<sub>i</sub>_ as a prefix. This establishes feasibility of _Q_ for _P_. Now consider the second case that there exists a point \(s'\neq s_j,s'\in P\backslash S_i\) on \(\rho(s_i,s_j)\) but no point \(s\neq s_i,s\in P\backslash S_j\) on \(\lambda(s_i,s_j)\). Let \(s''\in P\backslash S_i\) be the lowest point on \(\rho(s_i,s_j)\). Then \((s_i,s'')\) is an essential demand contradicting the assumption that _s<sub>i</sub>_ was redundant.

Our algorithm iteratively removes redundant points until we arrive at a subset \(\tilde{P}\subseteq P\) in which every point is essential. Thus for each point \(p\in\tilde{P}\) there exists an essential demand pair. Assign the vertical side of the corresponding demand rectangle that contains _p_ as _witness_ to _p_.

The intersection graph of the witnesses is an interval graph. We claim that it has clique size at most 4. Assume to the contrary that there exists some point _q_ (not necessarily a demand point) that is contained in 5 witnesses (each of which has an associated demand point). W.l.o.g. assume that at least 3 of the associated demand points lie below _q_. Then there exists a witness (with corresponding demand point _s<sub>i</sub>_ and demand pair (_s<sub>i</sub>,s<sub>j</sub>_)) that contains two points (possibly including _s<sub>i</sub>_) such that they belong to a different partition than \(s_j\in S_j\). This contradicts the fact that the demand pair (_s<sub>i</sub>,s<sub>j</sub>_) corresponding to this witness is essential. This implies that there exists an independent set of witnesses of size at least \(|\tilde{P}|/4\) and thus a boundary independent set of size at least \(|\tilde{P}|/8\).

