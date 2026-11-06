The Sensitivity Lemma follows from Lemma 17 because the coloring with execution traces of an algorithm _A_ for \(\Pi\) is a refinement of the coloring with \(\Pi\), so every edge of the permutahedron that is bichromatic under \(\Pi\) is also bichromatic under _A_, and

\(s(\Pi)\doteq\mathbb{E}(\mathrm{deg}_{\overline{G}(\Pi)}(\rho))\le\mathbb{E}(\mathrm{deg}_\overline{H}(\rho))\doteq\mathrm{deg}_\mathrm{avg}(\overline{H}).\)

Provided _g_ is nondecreasing, it follows that \(\mathrm{D}(\Pi)\ge g(\mathrm{deg}_\mathrm{avg}(\overline{H})+1)/n\ge g(s(\Pi)+1)/n\).

In the Sensitivity Lemma we set \(g(x)=\Gamma(x+1)\). An optimal (but less elegant) choice for _g_ is the piece-wise linear function that interpolates the prescribed values at the integral points in \[_n_\], namely

\(g(x)\doteq(x-\lfloor x\rfloor)\cdot(\lceil x\rceil!)+(1-(x-\lfloor x\rfloor))\cdot(\lfloor x\rfloor!).\)

For the proof of Lemma 17 we take intuition from a similar result in the Boolean setting \[O’D14, Exercise 8.43\], where the hypercube plays the role of the permutahedron in our setting.

**Fact 18.** _Let A be a query algorithm on binary strings of length n. Color each vertex of the n- dimensional hypercube by its execution trace under A, and let <o>H</o> denote the subgraph with the same vertex set but only containing the bichromatic edges. Then the number of distinct execution traces is at least_ 2deg<sub>avg</sub>(_H)._

One way to argue Fact 18 is to think of assigning a weight _w(x_) to each \(x\in\{0,1\}^n\) so as to maximize the total weight on all inputs, subject to the constraint that the total weight on each individual execution trace is at most 1. Then the number of distinct execution traces must be at least the sum of all the weights. If the weight only depends on the degree, i.e., if we can write _w(x_)=_f_(deg<sub><o>_H_</o></sub>(_x_)) for some function \(f:[0,\infty)\rightarrow\mathbb{R}\), then we can lower bound the number _k_ of distinct execution traces as follows:

\(k\ge\sum_xw(x)=\sum_xf(\mathrm{deg}_\overline{H}(x))\ge 2^n\cdot f(\mathbb{E}(\mathrm{deg}(x)))=2^n\cdot f(\mathrm{deg}_\mathrm{avg}(\overline{H})),\) (1)

where the last inequality holds provided _f_ is convex.

In the Boolean setting, the set _R_ of inputs \(x\in\{0,1\}^n\) with a particular execution trace forms a subcube of dimension \(n-\ell\), where \(\ell\) denotes the length of the execution trace, i.e., the number of queries. Each \(x\in R\) has degree \(\ell\) in _H_; this is because a change in a single queried position results in a different execution trace, and a change in an unqueried position does not. Therefore, a natural choice for the weight of \(x\in R\) is \(w(x)=f(\ell)\) where \(f(x)=1/2^{n-\ell}\). It satisfies the constraint that the total weight on _R_ is (at most) one, and _f_ is convex. We conclude by (1) that the number of distinct execution traces is at least \(2^n\cdot f(\mathrm{deg}_\mathrm{avg}(\overline{H}))=2^{\mathrm{deg}_\mathrm{avg}(\overline{H})}\), as desired.

_Proof of Lemma 17._ Let _k_ denote the number of distinct execution traces of _A_, and let _R_<sub>1</sub>_,...,R<sub>k</sub>_ denote the corresponding sets of rankings. Following a similar strategy, we want to find a convex function \(f:[0,\infty)\rightarrow\mathbb{R}\) such that the weight function \(w(\rho)=f(\mathrm{deg}_\overline{H}(\rho))\) does not assign weight more than 1 to any one of the sets _R<sub>i</sub>_. The following claim, to be proven later, is the crux of this.

**Claim 19.** _Let R denote the set of all rankings_ \(\rho\) _that follow a particular execution trace on A, and let_ \(d\in\{0,\dots,n-1\}\)_. The number of rankings_ \(\rho\in R\) _with_ \(\mathrm{deg}_\overline{H}(\rho)=d\) _is at most_ \(\frac{n!}{(d+1)!}\).

