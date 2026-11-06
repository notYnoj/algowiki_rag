component in _C_\\_T_ (first item) - in this case, return _S_ - or we can augment _S_ into a larger minimal separator \(S'\unknown\Omega\). Restart the same process on \(S'\) and future augmented separators while the lemma property is not satisfied. The process necessarily stops since each separator is augmented by at least one vertex at each step meanwhile being included into \(\Omega\).

The previous lemma allows us to define what is a _shy decomposition_ of a PMC \(\Omega\), _i.e._ the bi-partition between some \(\Omega\)-shy separator and the remainder of the PMC. Such shy decomposition can be obtained by picking any minimal separator of \(\Omega\) and then applying the procedure of Lemma 15 until obtaining an \(\Omega\)-shy separator _S_ with regard to the component containing \(\Omega\backslash S\).

**Definition 19** (Shy decomposition)**.** _Given a graph G and one of its PMCs_ \(\Omega\)_, a pair_ (_S,T_) _is a_ shy decomposition _of_ \(\Omega\) _if it satisfies the following properties:_

• (_S,T_) _is a partition of_ \(\Omega\): \(S\cup T=\Omega\) _and_ \(S\cap T=\emptyset\),<tbc>

• _S is a minimal separator of G which is_ \(\Omega\)_-shy with regard to C, where C=C<sub>G</sub>(t,S_) _with_ \(t\in T\).

Lemma 15 guarantees that each PMC admits at least one shy decomposition. Before going further on PMC Superset, we state an important connection between the concepts of shy separators and active separators. The following result is used in Section 4.

**Lemma 16.** _Consider a graph G with a PMC_ \(\Omega\) _which admits an active separator S. Let C be the connected component of G_\\_S containing_ \(T=\Omega\backslash S\)_. Then, separator S is_ \(\Omega\)_-shy with regard to C._

_Proof._ Assume by way of contradiction that _S_ is not \(\Omega\)-shy with regard to _C_. There exists a connected component \(B\unknown C\) in \(G\backslash\Omega\) which is full for _S_: \(S\subseteq N(B)\). Hence, for any pair \(x,y\in S\), set _T_ does not separate pair (_x,y_) in graph \(G[C\cup\{x,y\}]\): indeed, there is a (_x,y_)-path whose internal vertices belong to _B_, as both \(x,y\in N(B)\). This contradicts the fact that _S_ is active (Definition 15).

## 3.3 A characterization of PMC supersets

The presence of a shy separator is the key witness to assess whether some shy set is a PMC superset. We begin with "if" part: if some set _X_ is a PMC superset, then there is necessarily a shy separator \(S\unknown X\). The formal statement is provided below.

**Theorem 6.** _Let_ \(X\subseteq V(G)\) _be a shy set. If X is a PMC superset, then there exists a triplet_ (_a,b,S_) _satisfying the following properties:_

• _a and b are two distinct vertices and in particular_ \(a\in X\),<tbc>

• _S is the X-close_ (_a,b)-separator,_<tbc>

• _S is an X-shy separator with regard to C<sub>G</sub>(a,S)._<tbc>

