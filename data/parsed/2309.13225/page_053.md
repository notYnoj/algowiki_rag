where \(\mathcal{E}_l\subset P_{u,w}\cup(w,w^*)\), \(|\mathcal{E}_l|\le|L(P_{u,w}\cup(w,w^*),l)|\) and \(\mathcal{E}_l\cap E_l=\emptyset\). Note since \((w,w^*)\in E_l\), \(L(P_{u,w},l)=L(P_{u,w}\cup(w,w^*),l)\).

Now, in the _j_-th iteration, we use the path (_u,w_<sup>∗</sup>),(_w_<sup>∗</sup>_,w_) and the remaining sub-path \(P_{w,v}\subset E_j\) so that,

\(\hat{\delta}_j(w^*,u)\le\mathsf{wt}(P_{u,w})+2\mathsf{wt}(\mathcal{E}_l)+2\mathsf{wt}(w^*,w)+\mathsf{wt}(P_{w,v})\le\mathsf{wt}(P)+2\mathsf{wt}(\mathcal{E}_l)+2\mathsf{wt}(e_0)\)

Note \(e_0\subset E_l\) so that \(e_0\notin\mathcal{E}_l\) and we can define \(\mathcal{E}_j=\mathcal{E}_l\cup\{e_0\}\). Finally, it is easy to check \(|\mathcal{E}_j|=|\mathcal{E}_l|+1\le|L(P_{u,w},l)|+1\le|L(P,j)|\) as \(l\in L(P,j)\backslash L(P_{u,w},l)\).

We are now ready to prove Theorem 6.3.

_Proof._ (Correctness)

Recall that \(\beta\ge 2\). We prove the following for all \(j\ge k_0+3\). Let \(\hat{\delta}_j\) be the estimate \(\hat{\delta}\) after the _j_-th iteration of Phase 2 in Algorithm 9. For \(u\in D_j,v\in V\) and _P_ a shortest path from _u_ to _v_,

\(\hat{\delta}_j(u,v)\le\delta(u,v)+2\mathsf{wt}(\mathcal{E}_j)\)

where \(\mathcal{E}_j\subset P\), \(\mathcal{E}_j\cap E_j=\emptyset\) and \(|\mathcal{E}_j|\le j-(k_0+1)\). From Lemma 6.5, we have proved the base case for _j=k_<sub>0</sub>+3. Let _j\>k_<sub>0</sub>+3 and _e_=(_a,b_) be the closest edge in _P_ to _v_ not in _E<sub>j</sub>_ and _b_ the endpoint closer to _v_.

Then, \(\mathsf{rank}_a(e),\mathsf{rank}_b(e)\ge s_{j-1}\) and \(j\ge k_0+3\). In particular, \(\mathsf{deg}(b)\ge s_{j-1}\) so there is a vertex _b_<sup>∗</sup>=_r(b,D_<sub>_j_-1</sub>) satisfying rank_<sub>b</sub>(b,b_<sup>∗</sup>)_\<s_<sub>_j_-1</sub> and therefore \(\mathsf{wt}(b,b^*)\le\mathsf{wt}(e)\) and \((b^*,b)\in E_j\). By induction,<tbc>

\(\hat{\delta}_{j-1}(b^*,u)\le\delta(b^*,u)+2\mathsf{wt}(\mathcal{E}_{j-1})\)

<tbc>Then,<tbc>

\(\hat{\delta}_j(u,v)\le\hat{\delta}_{j-1}(b^*,u)+\mathsf{wt}(b^*,b)+\delta(b,v)\le\delta(u,b)+\delta(b,v)+2\mathsf{wt}(\mathcal{E}_{j-1})+2\mathsf{wt}(b,b^*)\)

<tbc>Thus, define \(\mathcal{E}_j=\mathcal{E}_{j-1}\cup\{(b,b^*)\}\) which satisfies the desired conditions since \((b,b^*)\in E_j\subset E_{j-1}\) and is therefore not in E<sub>_j_-1</sub>. Furthermore, with induction, \(|\mathcal{E}_j|\le j-(k_0+1)\). In particular, for _j=k_, since _D<sub>k</sub>=V_ ,

\(\hat{\delta}(u,v)\le\delta(u,v)+2\mathsf{wt}(\mathcal{E}_k)\le\delta(u,v)+2\overline{h}(P,\lfloor k/3\rfloor+1)=\delta(u,v)+2\overline{h}(P,\beta)\)

as desired, since \(k-(k_0+1)=\lfloor k/3\rfloor+1\).

_Proof._ (Time Complexity)

Phase 0 requires _O(m_) time, as `Decompose` requires _O(k(m+n_))-time.

We now examine Phase 1. Each \(|C_i|=\tilde{O}\left(\frac{n}{t_i}\right)=\tilde{O}(2^i)\) Each graph _F<sub>i</sub>_ has _O(nt<sub>i</sub>_) edges. Thus, each `Dijkstra` requires \(\tilde{O}(n^2)\)-time. Over _k_ iterations, this is again \(\tilde{O}(n^2)\)-time.

Now, \(|D_{k_0+2}|=\tilde{O}\left(\frac{n}{s_{k_0+2}}\right)=\tilde{O}\left(\frac{n}{s_{k-\lfloor k/3\rfloor}}\right)=\tilde{O}\left(n^{1-\frac{\lfloor k/3\rfloor}{\lfloor k/3\rfloor+2}x}\right)\). Similarly, we can upper bound the size of _D_<sub>_k_<sub>0</sub>+3</sub> as \(|D_{k_0+3}|=\tilde{O}\left(\frac{n}{s_{k-(\lfloor k/3\rfloor-1)}}\right)=\tilde{O}\left(n^{1-\frac{\lfloor k/3\rfloor-1}{\lfloor k/3\rfloor+2}x}\right)\). Finally, \(|C_i|=\tilde{O}(2^l)=\tilde{O}(n^{1-x})\). Thus, each `ApproximateMinPlus` requires time,<tbc>

\(\frac{1}{\varepsilon}n^{\omega\left(1-\frac{\lfloor k/3\rfloor}{\lfloor k/3\rfloor+2}x,1-x,1-\frac{\lfloor k/3\rfloor-1}{\lfloor k/3\rfloor+2}x\right)}\)

