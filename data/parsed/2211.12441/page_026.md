proof of the Sensitivity Lemma. Whereas a bound on deterministic complexity Q follows purely from the number of execution traces D, here, the execution traces are weighted by their depth and their probability of occurring.

Recall that _g_ in the statement of the Strong Sensitivity Lemma denotes any convex function \(g:[1,\infty)\rightarrow\mathbb{R}\) with _g(x_)=_x_! for \(x\in[n]\); for deriving the Sensitivity Lemma from the Strong Sensitivity Lemma we also need _g_ to be nondecreasing. One such function is \(g(x)=\Gamma(x+1)\). To prove a lower bound on the zero-error distributional complexity, we need the function _g_ to be not only convex, but _log-convex_, i.e., log<sub>2</sub>_g(x_) needs to be convex. The function \(g(x)=\Gamma(x+1)\) satisfies this constraint as well.

**Proposition 40.** _Let_ \(\Pi\) _be a problem in the comparison-query model with n items,_ D _the uniform distribution on the inputs_ \(\rho\)_, and_ \(g:[1,\infty)\rightarrow\mathbb{R}\) _a nondecreasing log-convex function with g(x_)=_x! for_ \(x\in[n]\).<tbc>

\(\mathrm{Dist}\mathrm{Q}_0(\Pi,\mathcal{D})\ge\mathrm{log}_2(g(s(\Pi)+1)/n)\)

<tbc>_Proof._ Let _k_ be the number of distinct execution traces of a deterministic algorithm _A_ for \(\Pi\), and let _R_<sub>1</sub>_,...,R<sub>k</sub>_ denote the corresponding sets of rankings. Interpreting _A_ as a binary decision tree, let _d(R<sub>i</sub>_) be the depth of the execution trace corresponding to _R<sub>i</sub>_. By Kraft’s inequality,<tbc>

\(\sum_{i=1}^k2^{-d(R_i)}\le 1.\)

<tbc>Let \(f(x)=\frac{1}{n}\frac{g(x+1)}{n!}\) and define the weight function \(w(\rho)=f(\mathrm{deg}_\overline{H}(\rho))\), where <o>_H_</o> refers to the notation of the Strong Sensitivity Lemma: <o>_H_</o> denotes the subgraph of the full permutahedron that only consists of the bichromatic edges when the vertices are colored with their execution trace under _A_. By Claim 19, the sum of the weights of all rankings \(\rho\) in _R<sub>i</sub>_ is at most 1. Therefore,<tbc>

\(\sum_\rho 2^{-d(\rho)}w(\rho)\le 1.\)

<tbc>Dividing both sides by _n_! and taking the logarithm of both sides, we get that<tbc>

\(\mathrm{log}_2\mathbb{E}\left[2^{-d(\rho)}w(\rho)\right]\le\mathrm{log}_2(1/n!),\) (18)

<tbc>where the expectation is with respect to a uniform distribution over the inputs \(\rho\). By Jensen’s inequality, since log is concave, we get<tbc>

\(\mathrm{log}_2\mathbb{E}\left[2^{-d(\rho)}w(\rho)\right]\ge\mathbb{E}\left[\mathrm{log}_2\left(2^{-d(\rho)}w(\rho)\right)\right]=\mathbb{E}[-d(\rho)]+\mathbb{E}[\mathrm{log}_2w(\rho)],\)

<tbc>which, in combination with (18), implies<tbc>

\(\mathbb{E}[\mathrm{log}_2w(\rho)]\le\mathbb{E}[d(\rho)]+\mathrm{log}_2(1/n!).\)

<tbc>Note that since _g_ is log-convex, so is _f_. By applying Jensen’s inequality again,<tbc>

\(\mathbb{E}[\mathrm{log}_2w(\rho)]=\mathbb{E}[\mathrm{log}_2f(\mathrm{deg}_\overline{H}(\rho))]\ge\mathrm{log}_2f(\mathbb{E}[\mathrm{deg}_\overline{H}(\rho)]),\)

<tbc>implying<tbc>

\(\mathrm{log}_2\left(\frac{1}{n}\cdot\frac{g(\mathbb{E}[\mathrm{deg}_\overline{H}(\rho)]+1)}{n!}\right)\le\mathbb{E}[d(\rho)]+\mathrm{log}_2(1/n!),\)

