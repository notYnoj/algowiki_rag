**Theorem 3.** _Let_ \(\pi\)-Request _be a computable request variant,_ \(\rho\ge 1\) _be a constant, and_ \(\gamma\) _be a non-decreasing computable function such that_

_R1_ \(\pi\)-Request _has constant locality_ \(\alpha_\pi\)_, that is, for any instance_ \(I=(d,G,B,x,S_\pi)\) _of_ \(\pi\)- Request_, any request_ \(r\in R_\pi(d,G,B,\mathcal{M},S_\pi)\)_, and any BFS layering V_<sub>1</sub>_,V_<sub>2</sub>_,V_<sub>3</sub>_,...,V<sub>i</sub> of G with_ \(i>\alpha_\pi d\)_, the following holds. Let V<sup>j</sup> be the union of all sets_ \(V_\ell\) _with_ \(\ell\equiv_{\alpha_\pi d+1}j\) _for each_ \(j\in[\alpha_\pi d+1]\) _and let_ \(I'_j=(d,G'=G[V\backslash V^j],B[G'],x,S_\pi[G'])\) _be the instance where all vertices from V<sub>j</sub> are removed. Then, the output for instance I and request r is equal to either the maximum or the minimum of the outputs for all_ \(I'_j\) _and r containing all vertices in_ M.<tbc>

_R2_ \(R_\pi(d,G,B,\mathcal{M},S_\pi)\) _can be computed in_ \(\mathcal{O}(\gamma(d)n^\rho)\) _time._<tbc>

_R3_ _Given a separator C,_ \(S_\pi[C_\mathrm{in}]\) _and_ \(S_\pi[C_\mathrm{ex}]\) _can be computed in_ \(\mathcal{O}(\gamma(d)n^\rho)\) _time._<tbc>

_R4_ _There is an algorithm that given a separator C_=(_C_<sub>he</sub>_,C_<sub>li</sub>_,C_<sub>di</sub>) _such that_ (_C,_1) _is measured for d and_ \(\alpha_\pi\)_, a pebble set_ M _for_ \((B,d,\alpha_\pi,x)\)_, and the solutions for instances_<tbc>

\((d,C_\mathrm{in},((B_\mathrm{he}\cup C_\mathrm{he})[C_\mathrm{in}],(B_\mathrm{li}\cup C_\mathrm{li})[C_\mathrm{in}],(B_\mathrm{di}\cup C_\mathrm{di})[C_\mathrm{in}]),x+1,S_\pi[C_\mathrm{in}])\text{\textit{and}}\)<br>
\((d,C_\mathrm{ex},((B_\mathrm{he}\cup C_\mathrm{he})[C_\mathrm{ex}],(B_\mathrm{li}\cup C_\mathrm{li})[C_\mathrm{ex}],(B_\mathrm{di}\cup C_\mathrm{di})[C_\mathrm{ex}]),x+1,S_\pi[C_\mathrm{ex}]),\)

_can compute the solutions for instance I for all requests_ \(r\in R_\pi(d,G,B,\mathcal{M},S_\pi)\) _in_ \(\mathcal{O}(\gamma(d)n^\rho)\) _time that do not intersect C_<sub>di</sub> _and intersect C_<sub>li</sub> _in at most_ \(20\alpha_\pi\sqrt{d}\mathrm{log}(d)\) _vertices._

_Then,_ \(\pi\)-Request _can be solved in_ \(2^{\tilde{\mathcal{O}}(\sqrt{d})}\gamma(d)n^{\mathrm{max}(2.49,\rho+\varepsilon)}\) _time for any_ \(\varepsilon>0\).

_Proof._ We first show that `solve-\(\pi\)-r` solves the instance \((d,G,x,B=(B_\mathrm{he},B_\mathrm{li},B_\mathrm{di}),S_\pi)\) of \(\pi\)- Request it is given as input. We will later show that `solve-\(\pi\)-r` terminates after a finite number of recursive calls. We can therefore show the claim by induction and assume that all recursive subcalls of `solve-\(\pi\)-r` indeed solve the corresponding instance of \(\pi\)-Request correctly. For the sake of notational convenience, we will assume that \(\rho\ge 2\).

If Line 1 is reached, then the computation is correct as we assume \(\pi\)-Request to be computable. If Line 1 is reached, then the computation is correct by Lemma 9. If Line 1 is reached, then Lemma 10 shows that the solution is correctly computed.

So assume that Line 1 is reached and let _C_ be the cycle separator computed in Line 1 and let S be the set of cycle separators computed in Line 1. Let M be a pebble set for (_B,x_) and let \(r\in R_\pi(d,G,B,\mathcal{M},S_\pi)\) be a request. If the (unknown) solution _Z_ that determines the optimal value for request _r_ intersects _C_ in at most \(20\sqrt{d}\mathrm{log}(d)\) vertices, then Requirement R4 guarantees that the solution is computed correctly in Line 1 as the solutions res<sub>1</sub> and res<sub>2</sub> are correct by the induction hypothesis. Moreover, as we only update res with valid solutions, the result is not overwritten in a later iteration of Line 1. If _Z_ and _C_ intersect in more than \(20\sqrt{d}\mathrm{log}(d)\) vertices, then both the strict interior and the strict exterior of _C_ contain at most \(d-20\sqrt{d}\mathrm{log}(d)\) vertices of _Z_, that is, _C_ is \(\frac{|Z|-20\sqrt{d}\mathrm{log}(d)}{|Z|}\)-balanced with respect to the weight function that assigns weight 1/|_Z_| to each vertex in _Z_ and zero to all other vertices. By Lemma 6, there exists a \(\frac{|Z|-20\sqrt{d}\mathrm{log}(d)}{|Z|}\)-balanced cycle separator \(C'\in\mathcal{S}\) (computed in Line 1) whose intersection with _Z_ is of size at most

\(40\sqrt{2\alpha_\pi d+3}+\frac{11|Z|\mathrm{log}(\alpha_\pi d)}{2\sqrt{2\alpha_\pi d+3}}\le 40\sqrt{\frac{5d\alpha_\pi}{2}}+\frac{11d\mathrm{log}(d^2)}{2\sqrt{2d}}\)<br>
\(\le 40\sqrt{\frac{5d\mathrm{log}(d)}{14}}+\frac{11d\mathrm{log}(d)}{\sqrt{2d}}\)

