In Phase 2, each \(|D_j|=\tilde{O}\left(n^{1-(k-j)\frac{x}{[k/3]+2}}\right)\) and \(|E_j|\le O\left(n^{1+(k-j+1)\frac{x}{[k/3]+2}}\right)\). Therefore, each invocation of **Dijkstra** in Phase 2 requires time \(\tilde{O}\left(n^{2+\frac{x}{[k/3]+2}}\right)\). Finally, we balance terms to optimize,

\(\omega\left(1-\frac{\lfloor k/3\rfloor}{\lfloor k/3\rfloor+2}x,1-x,1-\frac{\lfloor k/3\rfloor-1}{\lfloor k/3\rfloor+2}x\right)=2+\frac{x}{\lfloor k/3\rfloor+2}\)

To get the exact expression, we plug in \(k=3\beta-1\) and in particular \(\lfloor k/3\rfloor=\beta-1\).

**Lemma 6.5.** _Let_ \(u\in D_{k_0+3}\) _and_ \(v\in V\) _and P be a shortest path between u,v. Then, after the_ (_k_<sub>0</sub>+3)_-th iteration of Phase 2 of Algorithm 9,_

\(\delta(u,v)\le\hat{\delta}(u,v)\le\delta(u,v)+2\mathsf{wt}(\mathcal{E}_{k_0+3})\)

_for some_ \(\mathcal{E}_{k_0+3}\subset P\) _of size at most 2 and_ \(\mathcal{E}_{k_0+3}\cap E_{k_0+3}=\emptyset\).

_Proof._ We proceed by case analysis.

**Case 1:** \(P\subset E_{k_0+1}\) By Lemma 6.4 and we have \(\hat{\delta}(u,v)\le\delta_{k_0+3}(u,v)\le\delta(u,v)+2\mathsf{wt}(\mathcal{E}_{k_0+3})\) where \(|\mathcal{E}_{k_0+3}|\le|L(P,k_0+3)|\le 2\) and \(\mathcal{E}_{k_0+3}\cap E_{k_0+3}=\emptyset\).

**Case 2:** \(P\unknown\subset E_{k_0+1}\) Finally, suppose _P_ contains some edge not in _E_<sub>_k_<sub>0</sub>+1</sub>. Let _e_<sub>0</sub> be the closest edge in _P_ to _v_ not in _E_<sub>_k_<sub>0</sub>+3</sub> and _w_<sub>0</sub> be the endpoint closer to _v_. Then, both endpoints of _e_<sub>0</sub> have degree at least _s_<sub>_k_<sub>0</sub>+2</sub> so that there is \(w_0^*=r(w_0,D_{k_0+2})\) such that rank_<sub>w</sub>(w_<sub>0</sub>_,w)\<s_<sub>_k_<sub>0</sub>+2</sub> and therefore \(\mathsf{wt}(w_0^*,w)\le\mathsf{wt}(e_0)\).

Note that there is some \(1\le j\le l-1\) such that \(P\subset F_j\backslash F_{j+1}\) as \(t_l=\frac{n}{2^l}\le n^x=s_{k_0}\). Let \(e=(a,b)\in P\) such that \(e\in F_j\backslash F_{j+1}\). Then, \(\mathsf{rank}_a(a,b),\mathsf{rank}_b(a,b)\ge t_j\). Since deg(_a)\>s<sub>j</sub>_, there is vertex _a_<sup>∗</sup>=_r(a,D<sub>j</sub>_) such that rank_<sub>a</sub>(a,a_<sup>∗</sup>)_\<s<sub>j</sub>_ and \((a,a^*)\in F_{j+1}\subset F_j\). Since \(P\subset F_j\), in the _j_-th iteration and \(w_0^*\in D_{k_0+2}\),

\(X_j(a^*,u)\le\mathsf{wt}(a^*,a)+\delta(a,u)\le\delta(a,u)+\mathsf{wt}(a,b)\)<br>
\(X_j(a^*,w_0^*)\le\mathsf{wt}(a^*,a)+\delta(a,w_0)+\mathsf{wt}(w_0,w_0^*)\le\delta(a,w_0)+\mathsf{wt}(a,b)+\mathsf{wt}(e_0)\)

From the **ApproximateMinPlus**, we have,

\(\hat{\delta}(u,w_0^*)\le\left(1+\frac{\varepsilon}{3}\right)\left(\delta(a,u)+\delta(a,w_0)+2\mathsf{wt}(a,b)+\mathsf{wt}(e_0)\right)\le(1+\varepsilon)\delta(u,w_0)+2\mathsf{wt}(a,b)+\mathsf{wt}(e_0)\)

If _e=e_<sub>0</sub>, then we automatically have \(X_j(w_0^*,u)\le\delta(w_0,u)+\mathsf{wt}(w_0^*,w_0)\le\delta(w_0,u)+\mathsf{wt}(e_0)\). Thus, we can assume \(e\neq e_0\).

Then, when we execute **Dijkstra** from _u_ in the (_k_<sub>0</sub>+3)-th iteration, we use the edges \((u,w_0^*)\), \((w_0^*,w_0)\) and the remaining edges in _E_<sub>_k_<sub>0</sub>+3</sub>, so that,

\(\hat{\delta}(u,v)\le\hat{\delta}(u,w_0^*)+\mathsf{wt}(e_0)+\delta(w_0,v)\le(1+\varepsilon)\delta(u,v)+\le(1+\varepsilon)\delta(u,v)+2(\mathsf{wt}(a,b)+\mathsf{wt}(e_0))\)

We claim {(_a,b),e_<sub>0</sub>} satisfies the desired conditions. Clearly E<sub>_k_<sub>0</sub>+3</sub> has size 2. By definition, \(e_0\notin E_{k_0+3}\). Recall \(\mathsf{rank}_a(e),\mathsf{rank}_b(e)\ge t_j\ge t_l\ge\frac{n^x}{4}>s_{k_0+2}\) so that \((a,b)\notin E_{k_0+3}\).

