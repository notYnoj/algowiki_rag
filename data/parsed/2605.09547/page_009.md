## Storing the Electric Flow _f_ (Sections 4.5 and 4.6):

To argue why we can store each electric circulation \(\delta_x\) in \(\widetilde{O}(n)\) space, we argue the storage of \(g\in\mathbb{R}^E\) and the electric flow separately.

An electric flow _f_ (see (1)) is given by vertex potentials \(\delta_y:=(\mathbf{A}^\top\mathbf{R}_x^{-1}\mathbf{A})^\dagger\mathbf{A}^\top g\in\mathbb{R}^V\) which can easily be stored in \(\widetilde{O}(n)\) space. Then for any edge _e_=(_w,z_), we can compute the electric flow _f<sub>e</sub>_ on that edge via<tbc>

\(f_e=(\mathbf{R}_x^{-1}\mathbf{A}\delta_y)_e=((\delta_y)_z-(\delta_y)_w)/(\mathbf{R}_x)_{e,e}.\)

<tbc>However, this also needs access to (**R**_<sub>x</sub>_)<sub>_e,e_</sub>. To guarantee \(\widetilde{O}(\sqrt{n})\) iterations suffice, these resistances must be

\((\mathbf{R}_x)_{e,e}=\tau_e\cdot\left(\frac{1}{x_e^2}-\frac{1}{(u_e-x_e)^2}\right).\)

Here term \(\tau\in\mathbb{R}^E\) are so called Lewis-weights, which can be interpreted as a measure of importance for each edge _e_, and they are a generalization of effective resistance. Without this \(\tau\), the number of iterations would increase from \(\widetilde{O}(\sqrt{n})\) to \(\widetilde{O}(\sqrt{m})=\widetilde{O}(n)\), and we could no longer guarantee subquadratic space.

The term \(1/x_e^2-1/(u_e-x_e)^2\) is motivated by the resistance (**R**_<sub>x</sub>_)<sub>_e,e_</sub> going towards \(\infty\) when _x<sub>e</sub>_ or (_u<sub>e</sub>-x<sub>e</sub>_) are close to zero. When the resistance is high, then the electric flow will not route a lot of flow through that edge, which is needed to guarantee the capacity constraints \(0\le x+\delta_x\le u\).

Observe that, given edge _e_ and its capacity _u<sub>e</sub>_, we can compute _x<sub>e</sub>_, so we can also compute \(1/x_e^2-1/(u_e-x_e)^2\). If we can also compute \(\tau_e\) and _g<sub>e</sub>_, then we get \((\delta_x)_e\), and our iterative argument for computing \(x_e^t=x_e^{t-1}+(\delta_x^t)_e\) for all \(t=1,\dots,\widetilde{O}(\sqrt{n})\) goes through.

The difficulty is that for any edge _e_, both _g<sub>e</sub>_ and \(\tau_e\) depend not just on _x<sub>e</sub>_, but are a global property depending on the entire flow \(x\in\mathbb{R}^E\). So we need to store additional information.

## Storing Weights \(\tau\in\mathbb{R}^E\) (Section 4.3):

For some \(p=1-1/\Theta(logm)\), the (regularized) \(\ell_p\)-Lewis-weights from \[LS14\] are defined as the scaling \(\tau\in\mathbb{R}_{\ge 0}^E\) that satisfy the recurrence relation

\(\tau=\sigma(\mathbf{T}^{1/2-1/p}\mathbf{V}^{-1/2}\mathbf{A})+\frac{n}{m}\)

for \(\mathbf{V}_{e,e}=1/x_e^2-1/(u_e-x_e)^2\), \(\mathbf{T}_{e,e}=\tau_e\). \[BLL<sup>+</sup>21\] proved that the algorithm still works when the equality is only satisfied as some \((1\pm 1/O(logn))\)-approximation.

Cohen and Peng \[CP15\] proved that, if we start with some bad approximation _w_ of the Lewis-weights, then the following routine improves the approximation quality by a 1-_p/_2≈1/2 factor

\(w\leftarrow(w^{2/p-1}(\sigma(\mathbf{W}^{1/2-1/p}\mathbf{V}^{-1/2}\mathbf{A})+n/m))^{p/2}.\) (2)

Since \(n/m\le\tau\le 1+n/m\), we can start with _w_=all-1-vector, and use some \(\widetilde{O}(1)\) iterations of (2) to get an accurate enough estimate of the Lewis-weight. If we let _w_<sup>(0)</sup>_,w_<sup>(1)</sup>_,...,w_<sup>(_k_)</sup>=: \(\overline{\tau}\) be the sequence of values computed this way, then the final \(\overline{\tau}\) will be a good approximation of the Lewis-weights. We store these values in low space via the recurrence

\(w_e^{(j)}=((w_e^{(j-1)})^{2/p-1}(\sigma((\mathbf{W}^{(j-1)})^{1/2-1/p}\mathbf{V}^{-1/2}\mathbf{A})_e+n/m))^{p/2}\)

which allows us to query \(w_e^{(j)}\) recursively for _j_=1_,...,k_, and thus store \(\overline{\tau}=:w^{(k)}\in\mathbb{R}^E\) in low space, if we can store \(\sigma((\mathbf{W}^{(j-1)})^{1/2-1/p}\mathbf{V}^{-1/2}\mathbf{A})\in\mathbb{R}^E\) in low-space for \(j=1,\dots,k=\widetilde{O}(1)\).

This entire approach still yields an accurate estimate if we only approximately compute \(\sigma(\cdot)\). This is done via the \(\ell_2\)-characterization of \(\sigma(\cdot)\): for any matrix **M** we have<tbc>

\(\sigma(\mathbf{M})_e:=(\mathbf{M}(\mathbf{M}^\top\mathbf{M})^\dagger\mathbf{M}^\top)_{e,e}=\|\mathbf{M}(\mathbf{M}^\top\mathbf{M})^\dagger\mathbf{M}^\top\chi_e\|_2^2\)

<tbc>where \(\chi_e\) is a standard unit-vector. The \(\ell_2\)-norm can be \((1\pm\epsilon)\)-approximated via an \(O(\epsilon^{-2}logn)\times|E|\) Johnson-Lindenstrauss sketching matrix **S**, i.e., we store for _j_=1,2_,...,k_<tbc>

\(\mathbf{P}^{(j)}:=\mathbf{S}^{(j)}(\mathbf{W}^{(j-1)})^{1/2-1/p}\mathbf{V}^{-1/2}\mathbf{A}(\mathbf{A}^\top(\mathbf{W}^{(j-1)})^{1-2/p}\mathbf{V}\mathbf{A})^{-1}\mathbf{A})^\dagger\)

