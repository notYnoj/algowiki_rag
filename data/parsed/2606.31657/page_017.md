<tbc>and<tbc>

\(\mathcal{I}'^{(0)}:=\mathcal{I}_C(m'),\mathcal{I}'^{(j)}:=\mathcal{I}'^{(j-1)}-c'_j.\)

<tbc>Removing these constraints leaves the same residual instance, so \(\mathcal{I}^{(t)}=\mathcal{I}'^{(t)}\). Each I<sup>(_j_)</sup> is satisfied by _f(m_) and every \(\mathcal{I}'^{(j)}\) is satisfied by \(f(m')\). Applying the triangle inequality along the two chains,<tbc>

\(\mathsf{EMD}_{\delta_\mathrm{H}}\big(\mathcal{A}(\mathcal{I}_C(m)),\mathcal{A}(\mathcal{I}_C(m'))\big)\le\sum_{j=1}^t\mathsf{EMD}_{\delta_\mathrm{H}}\big(\mathcal{A}(\mathcal{I}^{(j-1)}),\mathcal{A}(\mathcal{I}^{(j)})\big)+\sum_{j=1}^t\mathsf{EMD}_{\delta_\mathrm{H}}\big(\mathcal{A}(\mathcal{I}'^{(j-1)}),\mathcal{A}(\mathcal{I}'^{(j)})\big).\)

<tbc>Combining this inequality with the lower bound above and recalling \(t\le\theta\), there exists an index _j<sup>⋆</sup>_ such that<tbc>

\(\mathrm{max}\big\{\mathsf{EMD}_{\delta_\mathrm{H}}\big(\mathcal{A}(\mathcal{I}^{(j^\star-1)}),\mathcal{A}(\mathcal{I}^{(j^\star)})\big),\mathsf{EMD}_{\delta_\mathrm{H}}\big(\mathcal{A}(\mathcal{I}'^{(j^\star-1)}),\mathcal{A}(\mathcal{I}'^{(j^\star)})\big)\big\}\ge\frac{1}{2\theta}\left(\delta\left(1-\frac{p}{p-1}\frac{\varepsilon}{r\kappa}\right)-\frac{2\varepsilon}{\kappa}-\frac{1}{n}\right).\)

<tbc>In either case we obtain a satisfiable instance together with the deletion of a single constraint that witnesses the required sensitivity gap. Because \(\delta_\mathrm{H}=d_\mathrm{H}/n\), multiplying by _n_ converts this to the unnormalized Hamming metric. Hence there exists a satisfiable instance witnessing worst-case sensitivity at least

\(\frac{n}{2\theta}\left(\delta\left(1-\frac{p}{p-1}\frac{\varepsilon}{r\kappa}\right)-\frac{2\varepsilon}{\kappa}\right)-\frac{1}{2\theta},\)

completing the proof.

## 4 Sensitivity Lower Bounds from Explicit LTCs

This section instantiates the abstract sensitivity framework developed in Section 3. We plug explicit families of locally testable codes into Theorem 1.1 to derive sensitivity lower bounds for Max E3LIN2 and Max Cut.

### 4.1 LRCC s and Max E3LIN2

In this section, we present our construction of a systematic LTC whose local tests are parity constraints on constantly many variables. Our construction is based on the _left-right Cayley complex (LRCC) code_ introduced by \[12\], with the concrete construction as in Sections 5 and 6 in \[12\].

**Lemma 4.1** (Theorem 1.1 in \[12\])**.** _For every_ 0_\<r\<_1_, there exist_ \(\delta,\kappa>0\), \(q\in\mathbb{Z}_0\)_, and an infinite family of LTCs_ {_C<sub>n</sub>_} _with rate r, distance_ \(\delta\)_, detection probability_ \(\kappa\)_, and query complexity q._

**Remark 4.2.** Section 5 of \[12\] shows that the codes in Lemma 4.1 are linear over the binary field F<sub>2</sub>.

For completeness we recall the notation surrounding the left-right Cayley complex associated with the codes _C<sub>n</sub>_. Given such a code, let _X_ denote its LRCC, a 2-dimensional simplicial complex. We write \(X(\ell)\) for the set of \(\ell\)-faces of _X_, so _X_(0) is the set of vertices, _X_(1) the edges, and _X_(2) the 2-faces. For any vertex \(g\in X(0)\), the local view \(X_g\subseteq X(2)\) consists of the 2-faces that contain _g_. The LRCC construction equips each local view _X<sub>g</sub>_ with a small code _C<sub>g</sub>_ obtained by restricting the global code to the coordinates indexed by _X<sub>g</sub>_. With this terminology in place, the local testability guarantee established in \[12\] can be stated as follows:

