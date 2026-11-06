• _S is an_ inclusion-wise minimal separator _if none of its proper subset is a minimal separator._

_We denote by_ \(\Delta_G\) _the collection of minimal separators of a graph G._

As a first remark, two vertices _a_ and _b_ can be vertex-separated if they are not adjacent, since an (_a,b_)-separator cannot contain any of them. Observe also that two inclusion-wise minimal separators cannot be subsets of each other, by definition. However, we can have \(S'\unknown S\) such that both \(S'\) and _S_ are minimal separators: in this case, \(S'\) is a minimal separator for some pair of vertices - say \((a',b')\) - and _S_ is a minimal separator of another pair \((a,b)\neq(a',b')\). Set _S_ also separates \((a',b')\) but not minimally.

Naturally, the set \(\Delta_G\) can be of exponential size compared to _n_=|_V(G_)|: as an example, consider some _melon graph_ which consists in \(p(n)=\frac{n-2}{2}\) disjoint paths of length 3 between two vertices _a_ and _b_. There are exactly 2<sup>_p(n_)</sup> minimal (_a,b_)-separators in such graph. Minimal separators of a graph _G_ can be enumerated in polynomial delay \[1, 28\], while the list of inclusion-wise minimal separators of _G_ cannot be produced in output-polynomial time \[8\] unless _P=NP_.

**Lemma 1** (Enumeration of minimal separators \[1\])**.** _All minimal separators of G can be enumerated with a delay of O(n_<sup>3</sup>)_, providing a global running time of_ \(O(n^3|\Delta_G|)\).

Plenty of folklore statements exist on minimal separators. We will recall some of them which will be useful for our results.

**Lemma 2** (Minimal separators and full components \[6\])**.** _For any graph G with_ \(a,b\in V(G)\) _and some set_ \(S\subseteq V(G)\backslash\{a,b\}\)_, S is a minimal_ (_a,b)-separator if and only if (iff) a and b belong to two different full components for S._

_As a consequence, for each_ \(s\in S\)_, there is a path from a to b intersecting S only in s._

Another folklore notion, present in many papers dealing with minimal separators, is the relationship between two minimal separators of the same pair: either they are _crossing_ or _parallel_. We need some property on parallel separators for the remainder.

**Definition 9** (Parallel separators)**.** _Two minimal_ (_a,b)-separators S and_ \(S'\) _of a graph G are_ parallel_, if either_ \(C_G(a,S)\subseteq C_G(a,S')\) _or_ \(C_G(a,S')\subseteq C_G(a,S)\).

It is equivalent to state that two parallel (_a,b_)-separators satisfy respectively either \(C_G(b,S')\subseteq C_G(b,S)\) or \(C_G(b,S)\subseteq C_G(b,S')\). The following lemma is a direct consequence of Lemma 2.

**Lemma 3.** _Let S and_ \(S'\) _be two parallel minimal_ (_a,b)-separators,_ \(S\neq S'\)_, and let us say w.l.o.g. that_ \(C_G(a,S)\unknown C_G(a,S')\).

_For any vertex_ \(x\in S\)_, there exists a path P<sub>x</sub> from x to some_ \(y\in S'\) _whose internal vertices do not belong to_ \(S\cup S'\cup\{a,b\}\).

_Proof._ We distinguish two cases. If \(x\in S\cap S'\), then trivially there exists a one-vertex path _P<sub>x</sub>_={_x_} without internal vertices and whose arrival (identical to departure, _y=x_) belongs to \(S'\). Thus, we focus on the case \(x\in S\backslash S'\).

According to Lemma 2, there exists a path from _a_ to _b_ passing through _x_, hence we can consider its subpath from _x_ to _b_. We denote by _P_ this subpath. From Lemma 2 again, _C(a,S_) is full component for _S_, so \(x\in N(C(a,S))\). But \(C(a,S)\subseteq C(a,S')\) and \(x\in S'\), so<tbc>

