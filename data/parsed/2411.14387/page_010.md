\(\blacktriangleright\) **Definition 15** (funnel bound)**.** _Let P be a point set with distinct y-coordinates. For each_ \(p\in P\)_, define quantity_

\(f(P,p):=\mathrm{mixValue}(F_\mathsf{L}(P,p).y,F_\mathsf{R}(P,p).y),\)

_which describes how much the left and right funnel of p are interleaved in time._

_Then_

\(\mathsf{Funnel}(P):=\sum_{p\in P}f(P,p).\)

_In addition, for an access sequence X, let_ Funnel(_X_):=Funnel(_G<sub>X</sub>)._

\(\blacktriangleright\) **Definition 16** (amortized bounds)**.** _For any sequence_ \(X\in S^m\)_, define amortized versions of the optimal cost and the Wilber bounds:_

\(\overline{\mathsf{OPT}}(X):=\frac{\mathsf{OPT}(X)}{m},\overline{\mathsf{Alt}}(X):=\frac{\mathsf{Alt}(X)}{m},\overline{\mathsf{Funnel}}(X):=\frac{\mathsf{Funnel}(X)}{m}.\)

\(\blacktriangleright\) **Definition 17** (composed sequence, see \[9\])**.** _Let S_<sub>1</sub>_,...,S<sub>l</sub> be disjoint sets of keys with increasing values (i.e._ \(\forall x\in S_j,x'\in S_{j+1}\)_, we have_ \(x<x'\)_). For each_ \(j\in[l]\)_, let_ \(X^{(j)}\in S_j^{m_j}\) _be an access sequence with keys in S<sub>j</sub>, and let_ \(\widetilde{X}\) _be a sequence with keys in_ \[_l_\] _such that every_ \(j\in[l]\) _appears exactly m<sub>j</sub> times (its total length is_ \(m:=m_1+\cdots+m_l\)_). Then we define the composed sequence_

\(X=\widetilde{X}(X^{(1)},\dots,X^{(l)})\in(S_1\cup\cdots\cup S_l)^m\)

_as the sequence that interleaves X_<sup>(1)</sup>_,...,X_<sup>(_l_)</sup> _according to the order given by_ \(\widetilde{X}\)_: that is,_ \(X_t=X_{\sigma(t)}^{\left(\widetilde{X}_t\right)}\) _where_ \(\sigma(t):=\#\big\{t'\le t\left|\widetilde{X}_{t^\prime}=\widetilde{X}_t\right\}\).

Note that \[6\] defines the _decomposition_ operation, which is the inverse operation of the composition. We will use Definition 17 throughout this paper.

\(\blacktriangleright\) **Definition 18** (_j<sub>x</sub>_)**.** _In the context of Definition 17, for any key_ \(x\in S_1\cup\cdots\cup S_l\)_, let j<sub>x</sub> be the unique index such that_ \(x\in S_{j_x}\).

x
p
x
L
x
L
R
x
R
L
x
x
the funnel of p has 5 points
By increasing y-coordinate: L, R, L, L. The side switches twice, so f(P, p) = 2.
Figure 4 Computing f(P, p) for p = (4, 9) in the geometric view of X = (4,6,3,5,1,7,2,1,4,6,3). Notice how the funnel points form a staircase-like front on either side of p.

