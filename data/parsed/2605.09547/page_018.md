<tbc>For convenient of writing proofs, we define a local variable **B** (a weighted version of **A**, only used in this proof) and the respective \(\mathbf{Q}:=\mathbf{B}^\top\mathbf{B}\),

\(\mathbf{B}:=\overline{\mathbf{T}^{1/2-1/p}}\Phi''(x)^{-1/2}\mathbf{A},\)<br>
\(\mathbf{Q}:=\mathbf{A}^\top\Phi''(x)^{-1/2}\overline{\mathbf{T}^{1-2/p}}\Phi''(x)^{-1/2}\mathbf{A}.\)

To see why matrix **P** allows us to represent the leverage scores \(\overline{\sigma}\) in small space, recall we wanted \(\overline{\sigma}\approx_{\epsilon_\tau/10}\sigma(\overline{\mathbf{T}^{1/2-1/p}}\Phi''(x)\mathbf{A})\). Indeed,

\(\sigma(\overline{\mathbf{T}^{1/2-1/p}}\Phi''(x)^{-1/2}\mathbf{A})_{e,e}\)<br>
\(=\sigma(\mathbf{B})_{e,e}\)<br>
\(=\chi_e^\top\mathbf{B}(\mathbf{B}^\top\mathbf{B})^{-1}\mathbf{B}^\top\chi_e\)<br>
\(=\chi_e^\top\mathbf{BQ}^{-1}\mathbf{B}^\top\chi_e\)<br>
\(=\chi_e^\top\mathbf{BQ}^{-1}\mathbf{QQ}^{-1}\mathbf{B}^\top\chi_e\)<br>
\(=\chi_e^\top\mathbf{BQ}^{-1}\mathbf{B}^\top\mathbf{BQ}^{-1}\mathbf{B}^\top\chi_e\)<br>
\(=\|\mathbf{BQ}^{-1}\mathbf{B}^\top\chi_e\|_2^2\)<br>
\(\approx_{\epsilon_\sigma/2}\|\mathbf{BM}^{-1}\mathbf{B}^\top\chi_e\|_2^2\)<br>
\(\approx_{\epsilon_\sigma/2}\|\mathbf{R}\overline{\mathbf{T}^{1/2-1/p}}\Phi''(x)^{-1/2}\mathbf{A}\mathbf{M}^{-1}\mathbf{B}^\top\chi_e\|_2^2.\)

where the first step follows from definition of **B**, the second step follows from definition of leverage score, the third step follows from \(\mathbf{Q}=\mathbf{B}^\top\mathbf{B}\), the fourth step follows from **QQ**<sup>-1</sup>=_I_, the fifth step follows from definition of the \(\mathbf{Q}=\mathbf{B}^\top\mathbf{B}\) norm, the seventh step follows from definition of \(\ell_2\) norm, the eighth follows from **M** being a \((1\pm\epsilon_\sigma/2)\)-spectral sparsifier of **Q**, the last step follows from JL property.

#### Initial \(\overline{\tau}\) for refinement

The above procedure allows us to improve some \(\overline{\tau}\), but we need a starting candidate. Since \(1+n/m\ge\tau(x)\ge\frac{n}{m}\), we can simply take \(\overline{\tau}=1\), which is a (_m/n_)-approximation. Then by Lemma 4.9, to get a \(\overline{\tau}\approx_{\epsilon_\tau}\sigma(\overline{\mathbf{T}^{1/2-1/p}}\mathbf{A})+\frac{m}{n}\), we simply need to calculate the update (14) a total of \(log_{|1-p/2|}((m/n)(\epsilon_\tau/2)^{-1})=\widetilde{O}(1)\) times (where our approximation of the leverage scores \(\epsilon_\sigma\) is negligibly small). Finally, by Lemma 4.10, we have \(\overline{\tau}\approx_{\epsilon_\tau}\tau(x)\).

#### Query Complexity

We now analyze the query complexity per edge. Throughout this process we store all the **P**s that we have used to get from 1 to our final \(\overline{\tau}\). For every edge _e_, we only need to calculate \(\|\mathbf{PA}\Phi''(x)_{ee}^{-1/2}\overline{\mathbf{T}}_{ee}^{\prime 1/2-1/p}\chi_e\|_2^2\) where \(\overline{\tau'}\) is the previous \(\overline{\tau}\) calculated. We can temporarily save \(\Phi''(x)_{ee}^{-1/2}\) when calculating this edge, so to calculate this we only need to track back to every \(\overline{\tau_e}\) we have seen, of which there are \(\widetilde{O}(1)\) of. This takes \(T_x+\widetilde{O}(1)\) time.

#### Construction Complexity

We now analyze resource usage. We take \(\widetilde{O}(1)\) steps. In each step we use 1 pass through the stream, and query the previous \(\overline{\tau}\), which as above takes \(\widetilde{O}(T_x)\) time per edge and \(\widetilde{O}(mT_x)\) time total. We solve for **M** using Lemma 2.1, where querying the weight on each edge takes time \(T_x+\widetilde{O}(1)\), for a total of \(\widetilde{O}(mT_x)\). Thus in total we use \(\widetilde{O}(1)\) passes through the stream and \(\widetilde{O}(mT_x+\epsilon_\tau^{-2})\) runtime. For storage, we store \(\widetilde{O}(1)\) variations of our matrix **P**, which takes \(\widetilde{O}(n\epsilon_\tau^{-2})\) space, completing the proof.

## 4.4 Implicit Representation of _g_

Our next step is to find the direction we should move our new point _x_ to, which is given by a gradient in the direction that maximizes centrality. Recall that centrality is defined as

\(v=\frac{s+\mu\tau(x)\phi'(x)}{\mu\tau(x)\sqrt{\phi''(x)}}.\)

The goal of this subsection is to show the following.

