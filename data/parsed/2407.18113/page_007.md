Let _T_ be the function given by these bounds such that<tbc>

\(\vec{V}_n\le T(V_{n-1}^\leftarrow,V_{n-2}^\leftarrow),\) (6)

<tbc>where \(\ge\) is taken component-wise. Moreover, _T_ is _translationally invariant_, that is, for all real _r_,<tbc>

\(T(\vec{v}+r,\vec{v}'+r)=T(v,v')+r,\) (7)

<tbc>where the sum of a vector with a real is taken component-wise. Finally, _T_ is also _monotonic_, that is,

\(\vec{u}\le\vec{u}'\text{and}\vec{v}\le\vec{v}'\Longrightarrow T(u,v)\le T(u',v').\) (8)

We are now ready to prove the main Lemma for the computation of \(\alpha'_k\).

**Lemma 7.** _If there exists a vector_ \(\vec{v}\) _and a real r such that_<tbc>

\(T(\vec{v},\vec{v}-r)\le\vec{v}+r,\) (9)

<tbc>_then there exists a real c such that_

\(\forall n\ge 0,\vec{V}_n\le\vec{v}+nr+c.\) (10)

_In particular, this implies that_ \(\alpha'_k\le r\).

_Proof._ We take any _c_ large enough such that (10) holds for \(n\in\{0,1\}\). We proceed by induction on _n_. The base case is covered by the choice of _c_. For the inductive step, assume that (10) holds for all _i\<n_. Then using (6), the induction hypothesis, (8), (7) and (9), in this order, we obtain

\(\vec{V}_n\le T(V_{n-1}^\leftarrow,V_{n-2}^\leftarrow)\)<br>
\(\le T(\vec{v}+(n-1)r+c,\vec{v}+(n-2)r+c)\)<br>
\(\le T(\vec{v},\vec{v}-r)+(n-1)r+c\)<br>
\(\le\vec{v}+r+(n-1)r+c=\vec{v}+nr+c,\)

which concludes our induction.

## 2.3 Implementation and bounds

If we can find a vector \(\vec{v}\) and real _r_ satisfying (9), this implies \(\alpha_k\le 2r\). We use a computer program to verify the existence of such a vector. To find \(\vec{v}\) and _r_, we simply start with two vectors \(\vec{w}_0=\vec{w}_1=0\), and we iterate \(\vec{w}_n=T(w_{n-1}^\leftarrow,w_{n-2}^\leftarrow)\). It seems to be the case that \(\vec{w}_n-w_{n-1}^\leftarrow\) converges to a uniform vector, but we do not need to prove it. We simply take \(\vec{v}=w_n\) for some _n_ large enough, and we take _r_ to be the largest component of \(w_n-w_{n-1}+\varepsilon\). We then check that (9) is satisfied with this choice of \(\vec{v}\) and _r_.

The implementation relies on fixed point arithmetic (that is, we fix some positive integer _p_, and we work with numbers of the form _a/p_ where \(a\in\mathbb{N}\)). We do all the rounding in the appropriate direction and in particular for the final step, we can formally verify with exact computation that (9) holds with the choice of \(\vec{v}\) and _r_.

