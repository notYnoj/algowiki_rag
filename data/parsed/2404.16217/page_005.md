max-flow(_s,v<sub>j</sub>,_G\(\backslash F\)) = \(\lambda\), there must exists a path, say _Q_, from _s_ to _v<sub>j</sub>_ in H\(\backslash F\) passing through _r_<sub>_i_<sub>0</sub></sub>. Such a path _Q_ must pass through \(\ell(x_{i_0})\) as well as a vertex in _Y_<sub>_i_<sub>0</sub></sub>, say _y_<sub>_i_<sub>0</sub>_,W_</sub>. This implies that the edge (_y_<sub>_i_<sub>0</sub>_,W_</sub>_,v<sub>j</sub>_) lies in H, and so by definition of _S_<sub>_i_<sub>0</sub></sub>, the set _W_ lies in _S_<sub>_i_<sub>0</sub></sub>. Moreover _W_ contains the element _x_ as \((\ell(x_{i_0}),y_{i_0,W})\) is an edge in G. This proves that element \(x\in U\) is covered by _S_<sub>_i_<sub>0</sub></sub>, and thus _S_<sub>_i_<sub>0</sub></sub> is a valid solution to \(\langle U,\mathfrak{F}\rangle\). \(\blacktriangleleft\)

\(\blacktriangleright\) **Lemma 11.** _Any solution S of the SET-COVER instance_ \(\langle U,\mathfrak{F}\rangle\)_, can be used to construct a solution_ H _of_ \((\lambda,k)\)_-FT-BFP instance satisfying_ \(|\mathrm{in}(v_j,\mathcal{H})|=\lambda(|S|+k)\)_, for each_ \(j\in[1,N]\).

**Proof.** Let _S_ be a solution of the SET-COVER instance \(\langle U,\mathfrak{F}\rangle\). Consider the sets

\(A_i=\{y_{i,W}|W\in S\}\cup Z_i,\text{for}i\unknown\lambda,\text{and}A=\bigcup_{i=1}^\lambda A_i.\)

We will show that

\(\mathcal{H}=\mathcal{G}\backslash\cup_{j=1}^N\mathrm{In}\text{-Edges}(v_j)+\cup_{j=1}^N(A\times v_j).\)

is a \((\lambda,k)\)-FT-BFP of G.

Let us assume, to the contrary, that H is not a \((\lambda,k)\)-FT-BFP of G. Then there must exist an edge set _F_ of size at most _k_ and an index \(j\in[1,N]\) satisfying max-flow(_s,v<sub>j</sub>,_G\(\backslash F\)) is greater than max-flow(_s,v<sub>j</sub>,_H\(\backslash F\)). Observe that each path from _s_ to _v<sub>j</sub>_ must pass through a vertex _r<sub>i</sub>_, for some \(i\in[1,\lambda]\), and each _r<sub>i</sub>_ only allows a unit flow to pass through it.

Since max-flow(_s,v<sub>j</sub>,_G\(\backslash F\))_\>_max-flow(_s,v<sub>j</sub>,_H\(\backslash F\)), there must exist an index \(i\in[1,\lambda]\) satisfying that there exists a path from _s_ to _v<sub>j</sub>_ in G\(\backslash F\) _passing through r<sub>i</sub>_, but no such corresponding path exists in H\(\backslash F\).

Let \(R=\{x_i^0,x_i^1,\dots,x_i^\alpha\}\) be the set of leaf nodes in tree _B<sub>i</sub> reachable_ from _s_ in G\(\backslash F\). There exist at least min(_k_+1,|_R_|) vertex-disjoint paths from _R_ to _v<sub>j</sub>_ in H, namely,

\((\{x_i^0,\ell(x_i^0),y_{i,W},v_j)\text{, where}W\in\mathfrak{F}\text{is the set in}S\text{that contains the element}x^0\in U.\)

\((\{x_i^c,r(x_i^c),z_i^c,v_j)\text{, for}c=1\text{to min}(k,|R|-1).\)

S
r
Yi
Zi
Vj

\(\blacksquare\)

**Figure 1** Depiction of a \((\lambda,k)\)-FT-BFP instance obtained from a SET-COVER instance \(\langle U,\mathfrak{F}\rangle\).

