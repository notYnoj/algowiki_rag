small number of connected components. It can also handle directed graphs, but in order to keep the presentation as concise as possible, we will focus on undirected graphs here and mention that just considering the underlying undirected graph allows to extend all results to directed graphs as well. We next state our main theorem, but defer its proof to the end of this section. Note that in the following we consider arbitrary separators, not necessarily cycle separators. We still use the terms _C_<sub>in</sub> and _C_<sub>ex</sub> to refer to the graphs induced by either side of the separation.

**Theorem 3.** _Let_ \(\pi\)-Request _be a computable request variant,_ \(\rho\ge 1\) _be a constant, and_ \(\gamma\) _be a non-decreasing computable function such that_

_R1_ \(\pi\)-Request _has constant locality_ \(\alpha_\pi\)_, that is, for any instance_ \(I=(d,G,B,x,S_\pi)\) _of_ \(\pi\)- Request_, any request_ \(r\in R_\pi(d,G,B,\mathcal{M},S_\pi)\)_, and any BFS layering V_<sub>1</sub>_,V_<sub>2</sub>_,V_<sub>3</sub>_,...,V<sub>i</sub> of G with_ \(i>\alpha_\pi d\)_, the following holds. Let V<sup>j</sup> be the union of all sets_ \(V_\ell\) _with_ \(\ell\equiv_{\alpha_\pi d+1}j\) _for each_ \(j\in[\alpha_\pi d+1]\) _and let_ \(I'_j=(d,G'=G[V\backslash V^j],B[G'],x,S_\pi[G'])\) _be the instance where all vertices from V<sub>j</sub> are removed. Then, the output for instance I and request r is equal to either the maximum or the minimum of the outputs for all_ \(I'_j\) _and r containing all vertices in_ M.<tbc>

_R2_ \(R_\pi(d,G,B,\mathcal{M},S_\pi)\) _can be computed in_ \(\mathcal{O}(\gamma(d)n^\rho)\) _time._<tbc>

_R3_ _Given a separator C,_ \(S_\pi[C_\mathrm{in}]\) _and_ \(S_\pi[C_\mathrm{ex}]\) _can be computed in_ \(\mathcal{O}(\gamma(d)n^\rho)\) _time._<tbc>

_R4_ _There is an algorithm that given a separator C_=(_C_<sub>he</sub>_,C_<sub>li</sub>_,C_<sub>di</sub>) _such that_ (_C,_1) _is measured for d and_ \(\alpha_\pi\)_, a pebble set_ M _for_ \((B,d,\alpha_\pi,x)\)_, and the solutions for instances_

\((d,C_\mathrm{in},((B_\mathrm{he}\cup C_\mathrm{he})[C_\mathrm{in}],(B_\mathrm{li}\cup C_\mathrm{li})[C_\mathrm{in}],(B_\mathrm{di}\cup C_\mathrm{di})[C_\mathrm{in}]),x+1,S_\pi[C_\mathrm{in}])\text{\textit{and}}\)<br>
\((d,C_\mathrm{ex},((B_\mathrm{he}\cup C_\mathrm{he})[C_\mathrm{ex}],(B_\mathrm{li}\cup C_\mathrm{li})[C_\mathrm{ex}],(B_\mathrm{di}\cup C_\mathrm{di})[C_\mathrm{ex}]),x+1,S_\pi[C_\mathrm{ex}]),\)

_can compute the solutions for instance I for all requests_ \(r\in R_\pi(d,G,B,\mathcal{M},S_\pi)\) _in_ \(\mathcal{O}(\gamma(d)n^\rho)\) _time that do not intersect C_<sub>di</sub> _and intersect C_<sub>li</sub> _in at most_ \(20\alpha_\pi\sqrt{d}\mathrm{log}(d)\) _vertices._

_Then,_ \(\pi\)-Request _can be solved in_ \(2^{\tilde{\mathcal{O}}(\sqrt{d})}\gamma(d)n^{\mathrm{max}(2.49,\rho+\varepsilon)}\) _time for any_ \(\varepsilon>0\).

The rest of this section is structured as follows. First, we present three algorithms that recursively call one another to solve the problem. One of them (`solve-\(\pi\)-`r`) is the main algorithm, one (`red-portals`) is for the special case in which the portal set _B_ becomes too large, and the final (`base-case`) handles the base cases when the parameter becomes small enough. We then show that a number of invariants are maintained throughout all algorithm calls. In the following three subsections, we analyze each of the three algorithms. There, we give an informal description of the respective algorithm and prove that it works correctly. This will yield the correctness proof of Theorem 3 in the end. In the next section, we will show how to apply this theorem to different problems.

## 3.1 Algorithms and Invariants

We start by formally stating the three aforementioned algorithms: `solve-\(\pi\)-`r` (Algorithm 1), `red-portals` (Algorithm 2), and `base-case` (Algorithm 3). We present the algorithms for the case where \(\pi\)-Request is a maximization problem, but the minimization version can be solved by essentially the same algorithms. The aforementioned invariants are summarized in the following lemma.

**Lemma 8.** _Throughout all calls of `solve-`\(\pi\)**`-r`, `red-portals`, and `base-case`, the following invariants are maintained._

