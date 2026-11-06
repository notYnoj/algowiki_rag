Note that the analysis of §2 requires a deterministic, syndrome-consistent output for every valid syndrome, whereas the LP decoder declares failure in certain scenarios. To make it a valid DQI decoder, we modify it as follows. When the LP declares failure, return a solution of _H_**y**=**s** found by Gaussian elimination, with free coordinates set to zero in a fixed order. This defines a polynomial-time map _D_LP with _D_LP(0)=0. The word-error probability of the resulting decoder is at most \(P_\mathrm{W}^\mathrm{LP}\), since declared failures were already counted as errors, so it inherits (86).

For a fixed-target DQI instance with \(\ell=\lfloor pm\rfloor\) and \(p<p_\mathrm{LP}^\mathrm{cert}\), the fixed-weight version makes the failure probability in Theorem 1 tend to zero, uniformly over weights through \(\ell\). Consequently the optimized satisfaction fraction tends to _F<sub>r/q</sub>_(min{_p,_1-_r/q_}) for arbitrary target sets of size _r_.

## 4.1 MaxCut and Max-_k_-Cut

Having established a firm connection between decoding LS cycle codes and DQI performance, we turn to our first application of interest: the well-known problem of MaxCut and its generalization, Max-_k_-Cut.

**Definition 5** (Max-_k_-Cut)**.** _Let G_=(_V,E_) _be a simple graph. Max-k-Cut asks for an assignment_ \(\mathbf{x}:V\rightarrow[k]\) _maximizing the number of edges_ \(\{u,v\}\in E\) _with_ \(x_u\neq x_v\)_. The cut fraction is this number divided by m_=|_E|. MaxCut is Max-2-Cut._

As the name suggests, MaxCut admits a visualization as the number of edges "cut" by a bipartition of the vertices. More generally, Max-_k_-Cut can be understood as a vertex coloring problem in which, given a fixed number of colors _k_, one seeks to color the vertices to minimize the number of adjacent vertices with the same color.

Max-_k_-Cut is an instance of Max-2-LINSAT when _k=q_ is a prime power. We identify the labels with F_<sub>q</sub>_ and orient the edges. The constraints are \(x_v-x_u\in\unknown_q\backslash\{0\}\), so _B<sup>T</sup>_ is an oriented incidence matrix, _r=q_-1, and (18) gives \(\theta(a)=1/(q-1)\). Thus the semicircle formula is

\(b_q(p):=F_{(q-1)/q}(p)=\frac{\left(\sqrt{(q-1)(1-p)}+\sqrt{p}\right)^2}{q}.\) (90)

It increases from the random-assignment fraction (_q_-1)_/q_ to 1 on \(0\le p\le 1/q\).

Write \(F_{q,D}^\mathrm{DQI}\) for the optimal asymptotic cut fraction among the reliably decoded cutoff families of Corollary 3 on the Linial-Simkin ensemble. For this Max-_k_-Cut comparison, take _q\<D_, as in  3. Here \(\delta_\mathrm{cyc}(D,q)<1/(D-1)\le 1/q\). Substituting the ML decoding threshold bound (78) into the semicircle formula (90) gives<tbc>

\(F_{q,D}^\mathrm{DQI}\le U_q(D):=b_q\big(\delta_\mathrm{cyc}(D,q)\big).\) (91)

<tbc>For \(q/D^{2/3}\le 1/32\), the same corollary gives the lower bound \(b_q\big((1-16q/D^{2/3})\delta_\mathrm{cyc}(D,q)\big)\). Conse quently, for _q=o(D_<sup>2/3</sup>),

\(F_{q,D}^\mathrm{DQI}=\frac{q-1}{q}\left(1+\frac{1}{D-1}\right)+o(D^{-1}).\) (92)

For MaxCut, the exact binary threshold in (79) gives the exact reliable-decoding value

\(F_{2,D}^\mathrm{DQI}=\frac{1}{2}+\sqrt{\delta_\mathrm{cyc}(D,2)(1-\delta_\mathrm{cyc}(D,2))}=\frac{1}{2}+\frac{1}{2(D-1)}.\) (93)

