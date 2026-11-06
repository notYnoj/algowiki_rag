<tbc>written in local coordinates, has no eigenvalue with zero real part. A closed trajectory \(\gamma\) is _hyperbolic_ if the differential at \(p\in\gamma\) of the Poincaré return map has no eigenvalue of absolute value 1.

**Definition 2.3.** A point \(y\in M\) is an \(\omega\)-limit (\(\alpha\)-limit) point of \(x\in M\) if there is a sequence \(t_i\rightarrow+\infty\) (\(t_i\rightarrow-\infty\)) such that \(\varphi_{t_i}(x)\rightarrow y\). The set of all such points is the \(\omega\)-limit (\(\alpha\)-limit) set \(\omega(x)\) (\(\alpha(x)\)).

**Definition 2.4.** The _stable_ and _unstable manifolds_ of a critical element _c_ are

\(W^s(c)=\{x\in M|\omega(x)=c\},W^u(c)=\{x\in M|\alpha(x)=c\}.\)

For a singular point _p_ this means \(lim_{t\rightarrow+\infty}\varphi_t(x)=p\) and \(lim_{t\rightarrow-\infty}\varphi_t(x)=p\), respectively; in particular \(p\in W^s(p)\cap W^u(p)\).

**Definition 2.5.** A point \(p\in M\) is _wandering_ for _X_ if there are a neighborhood _V_ of _p_ and _T\>_0 such that \(X_t(V)\cap V=\emptyset\) for all |_t|\>T_; otherwise _p_ is _non-wandering_. The set of non-wandering points is denoted by \(\Sigma(X)\).

**Definition 2.6.** A vector field _X_ on a compact surface _M_ is a _Morse-Smale vector field_ if (1) _X_ has finitely many critical elements, all hyperbolic; (2) \(\Sigma(X)\) is the union of the critical elements; (3) the stable and unstable manifolds of critical elements intersect transversally.

Hyperbolic singular points of a flow on a surface are of three types: _sinks_, _saddles_ and _sources_. With the convention _X_=-grad_f_ for a Morse function _f_, they correspond to critical points of index 0, 1 and 2, respectively. Transversality excludes trajectories going from one saddle to another (saddle connections), since such a trajectory would lie in both _W<sup>u</sup>_ and _W<sup>s</sup>_ with the same tangent direction.

**Definition 2.7.** A Morse-Smale flow is a _Morse flow_ if it has no closed trajectories. A Morse flow on a closed surface _M_ is _optimal_ if it has the minimal number of singular points among all Morse flows on _M_.

**Theorem 2.8.** _Let M be a closed connected surface. Then:_

(_a)_ _a Morse flow on M is optimal if and only if it has exactly one sink and exactly one source;_<tbc>

_(b)_ _an optimal Morse flow has_ \(k=2-\chi(M)\) _saddles; thus k_=2_g if M is orientable of genus g, and k=h if M is non-orientable of genus h._

_Optimal Morse flows exist on every closed connected surface._

_Proof._ Let _a,b_, _k_ be the numbers of sources, sinks and saddles of a Morse flow. The sum of the indices of the singular points is \(\chi(M)\) (Poincaré-Hopf), and a source or sink has index +1, a saddle -1; hence \(a+b-k=\chi(M)\) and the total number of singular points is \(a+b+k=2(a+b)-\chi(M)\). Since \(\Sigma(X)\) is the finite set of singular points, \(\omega(x)\) is a single singular point _p_ for every _x_. Take _x_ outside the one-dimensional stable manifolds of the saddles and outside the singular points; then _p_ is not a saddle, and not a source (as _W<sup>s</sup>(p_)={_p_} for a source), hence a sink. So \(b\ge 1\), and by time reversal \(a\ge 1\). Therefore \(a+b\ge 2\) with equality exactly when _a=b_=1, which gives (a) and \(k=2-\chi(M)\). Existence is shown in Kybalko et al. (2018) (equivalently, via a Morse function with one maximum and one minimum).

## 2.2 Topological equivalence

**Definition 2.9.** Two vector fields _X,Y_ on _M_ are _topologically (trajectory) equivalent_, _X∼Y_ , if there is a homeomorphism \(h:M\rightarrow M\) that maps trajectories of _X_ onto trajectories of _Y_ and preserves the direction of motion along them. The homeomorphism _h_ is not required to preserve an orientation of _M_.

The time parametrization is ignored. The _inverse_ of _X_ is the field -_X_, with the same trajectories traversed in the opposite direction. In general \(X\unknown-X\), so the relation "_X_∼-_Y_" is a different, weaker condition; both occur in Section 5.

**Theorem 2.10.** _Let h be a topological equivalence of X and Y. Then p is a singular point of X iff h(p_) _is a singular point of Y ; a trajectory of X is closed iff its image is closed; and h maps the_ \(\alpha\)_-limit (_\(\omega\)_-limit) set of every trajectory onto the_ \(\alpha\)_-limit (_\(\omega\)_-limit) set of the image trajectory._

**Definition 2.11.** A vector field \(X\in\mathcal{X}^r(M)\), \(r\ge 1\), is _structurally stable_ if it has a neighborhood _U(X_) in the _C<sup>r</sup>_-topology such that _Y∼X_ for all \(Y\in U(X)\).

On closed surfaces the structurally stable fields are exactly the Morse-Smale fields Peixoto (1973); Oshemkov and Sharko (1998); Kibkalo and Yokoyama (2022); in particular, optimal Morse flows are structurally stable, and their classification up to ∼ is the object of this paper.

