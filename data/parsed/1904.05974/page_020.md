follows from this proof in \[27\] which, in turn, is based on the proof of integrality of the stable matching polytope in \[44\]. We include in the appendix a proof of this theorem for our case, i.e., for the half-integral matching \(\mathbf{q}'\), showing that \(\mathbf{q}'\) can be written as the convex combination of two popular matchings; moreover, these two matchings can be efficiently computed.

Note that this theorem does not hold for the popular half-integral matching **_x_** (which is not a convex combination of popular matchings) in the instance shown in Fig. 2 since **_x_** is not perfect.

**Theorem 11.** _The popular (perfect) half-integral matching_ \(\mathbf{q}'\) _in_ \(G'\) _can be written as_ \(\mathbf{q}'=(I_{M_1}+I_{M_2})/2\) _for popular matchings M_<sub>1</sub> _and M_<sub>2</sub> _in_ \(G'\).

The popularity of matchings _M_<sub>1</sub> and _M_<sub>2</sub> will be shown by defining witnesses of popularity \(\unknown\) and \(\unknown\) as follows. Recall that \(\unknown'\) is the witness of \(\mathbf{q}'\) constructed in the proof of Lemma 5. For any \(u\in A'\cup B'\):

- if \(\alpha'_u\in\{\pm 1\}\) then let \(\beta_u=\gamma_u=\alpha'_u\); else (so \(\alpha'_u=0\))<tbc>

• if \(u\in A'\) then \(\beta_u=-1\) and \(\gamma_u=1\); else (so \(u\in B'\)) \(\beta_u=1\) and \(\gamma_u=-1\).

Thus \(\beta_u,\gamma_u\in\{\pm 1\}\) for every \(u\in A'\cup B'\). Corollary 1 follows from the fact that \(\alpha'_a=\alpha'_b=0\) for \(a\in U_A\subseteq A'\) and \(b\in U_B\subseteq B'\).

**Corollary 1.** _We have_ \(\beta_a=-1\) _and_ \(\gamma_a=1\forall a\in U_A\) _and_ \(\beta_b=1\) _and_ \(\gamma_b=-1\forall b\in U_B\).

Let _N_<sub>1</sub> (resp., _N_<sub>2</sub>) be the matching obtained by deleting edges \((u,u')\) for \(u\in U_A\cup U_B\) from _M_<sub>1</sub> (resp., _M_<sub>2</sub>). Thus _N_<sub>1</sub> and _N_<sub>2</sub> are matchings in _G_. Note that **_q_**=(_I_<sub>_N_<sub>1</sub></sub>+_I_<sub>_N_<sub>2</sub></sub>)/2.

**Lemma 6.** _The matchings N_<sub>1</sub> _and N_<sub>2</sub> _are quasi-popular in G._

_Proof._ In order to prove the quasi-popularity of _N_<sub>1</sub>, it will be useful to partition _A_\\_U<sub>A</sub>_ into \(A_{-1}\cup A_1\) and _B_\\_U<sub>B</sub>_ into \(B_1\cup B_{-1}\) as follows. For \(i=\pm 1\):

- let _A<sub>i</sub>_ be the set of those \(a\in A\backslash U_A\) such that \(\beta_a=i\).<tbc>

**-** let _B<sub>i</sub>_ be the set of those \(b\in B\backslash U_B\) such that \(\beta_b=i\).

Since \(\beta_a+\beta_b=\mathfrak{wt}_{M_1}(a,b)=0\) for every edge \((a,b)\in M_1\), we have \(N_1\subseteq(A_1\times B_{-1})\cup(A_{-1}\times B_1)\). Fig. 6 will be useful. We now define a certificate \(\unknown'\) of _N_<sub>1</sub>’s quasi-popularity.

**-** Let \(\beta'_a=2\) for all \(a\in A_1\) and let \(\beta'_b=-2\) for all \(b\in B_{-1}\). Let \(\beta'_u=0\) for all other vertices _u_.

UA
UB
UA
UB
A-1
B1
A-1
B1
A1
B-1
A1
B-1

**Fig.6.** The figure on left represents \(\beta\)-values and the one on right represents \(\beta'\)-values. On left, elements in blue (resp., red) sets have \(\beta\)-value 1 (resp., -1). We have \(\beta'_a=\beta_a+1\forall a\in A\) and \(\beta'_b=\beta_b-1\forall b\in B\).

