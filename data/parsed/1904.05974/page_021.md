We need to show that \(\beta'\) obeys the three constraints given below, see (LP3)-(LP4).

\(\beta'_a+\beta'_b\ge g_{N_1}(a,b)\forall(a,b)\in E\) (16)

\(\beta'_u\ge g_{N_1}(u,u)\forall u\in A\cup B\) (17)

\(\sum_{u\in A\cup B}\beta'_u=0,\) (18)

where \(g_{N_1}(\cdot)\) is defined as in (15), with _M=N_<sub>1</sub>. For any \(u\in A\cup B\), _g_<sub>_N_<sub>1</sub></sub>(_u,u_)=0 if _u_ is unmatched in _N_<sub>1</sub> and _g_<sub>_N_<sub>1</sub></sub>(_u,u_)=-2 if _u_ is matched in _N_<sub>1</sub>.

_Constraint_ (16). For any edge (_a,b_), we have \(\beta'_a+\beta'_b=\beta_a+\beta_b\): this is because \(\beta'_a=\beta_a+1\) for \(a\in A\) and \(\beta'_b=\beta_b-1\) for \(b\in B\). We have \(\beta'_a+\beta'_b=\beta_a+\beta_b\ge\mathsf{wt}_{M_1}(a,b)\ge g_{N_1}(a,b)\) for all edges \((a,b)\in E\),<sup>6</sup> where \(\beta_a+\beta_b\ge\mathsf{wt}_{M_1}(a,b)\) holds for each edge \((a,b)\in E\) due to the popularity of _M_<sub>1</sub> in \(G'\) with witness \(\beta\).

_Constraint_ (17). It follows from Corollary 1 that \(\beta_a=-1\) for \(a\in U_A\) and \(\beta_b=1\) for \(b\in U_B\), so \(\beta'_u=0=g_{N_1}(u,u)\) for an unmatched vertex _u_. We also have \(\beta'_u\ge-2=g_{N_1}(u,u)\) for a matched vertex _u_. Thus \(\beta'_u\ge g_{N_1}(u,u)\) for all vertices _u_.

_Constraint_ (18). For every edge \((a,b)\in N_1\), observe that \(\beta'_a+\beta'_b=\beta_a+\beta_b=\mathsf{wt}_{M_1}(a,b)=0\). We also observed above that \(\beta'_u=0\) for every unmatched vertex _u_. So \(\sum_{u\in A\cup B}\beta'_u=0\). Thus constraints (16)-(18) are satisfied. We conclude that _N_<sub>1</sub> is quasi-popular in _G_.

The quasi-popularity of _N_<sub>2</sub> in _G_ can be shown similarly. \(\square\)

Thus both _N_<sub>1</sub> and _N_<sub>2</sub> are quasi-popular matchings in _G_. Since **_q_**=(_I_<sub>_N_<sub>1</sub></sub>+_I_<sub>_N_<sub>2</sub></sub>)/2, one of _N_<sub>1</sub>_,N_<sub>2</sub> has cost at most cost(**_q_**). Since **_q_** can be computed in polynomial time and _N_<sub>1</sub>_,N_<sub>2</sub> can be efficiently obtained from **_q_** (see the proof of Theorem 11), we can conclude the following theorem.

**Theorem 12.** _Given a marriage instance_ \(G=(A\cup B,E)\) _with a function_ \(\mathsf{cost}:E\rightarrow\mathbb{R}\)_, there is a polynomial time algorithm to compute a quasi-popular matching N such that_ \(\mathsf{cost}(N)\le\mathsf{cost}(\mathbf{q})\)_, where **q** is a min-cost popular fractional matching in G._

## 5 Hardness of Finding a Min-Cost Quasi-Popular Matching

We prove Theorem 1 in this section. We show a reduction from 3SAT. Given a 3SAT formula \(\psi\) on _n_ variables, we construct a marriage instance \(G_\psi\) and a cost function on the edges. At a high level, this construction resembles the structure of the instance used in \[10\] to show the hardness of deciding if a marriage instance admits a stable matching that is also dominant. However, our proof is much more involved, and requires the introduction of new tools.

In fact, the hardness reductions from \[10\] heavily rely on the combinatorial characterizations of stable/popular matchings in terms of certain forbidden induced structures. As mentioned in Section 1, such a characterization is not known for quasi-popular matchings. Recall from Section 4.1 that a matching is quasi-popular if and only if it admits a witness in \(\{0,\pm 1,\pm 2\}^n\). We will use such witnesses in our reduction.

### 5.1 Our Reduction from 3SAT

As done in \[10\], it will be useful to perform a simple transformation of the 3SAT formula \(\psi\) so that the transformed formula has a unique occurrence of each negative literal. This property is easily accomplished: let _X_<sub>1</sub>_,...,X<sub>n</sub>_ be the _n_ variables in \(\psi\). For each _i_, replace all occurrences of \(\neg X_i\) in \(\psi\) with _X_<sub>_n+i_</sub>, i.e., a single new variable. The clauses \(X_i\vee X_{n+i}\) and \(\neg X_i\vee\neg X_{n+i}\) are added to capture \(\neg X_i\Longleftrightarrow X_{n+i}\).

<sup>6</sup> If wt<sub>_M_<sub>1</sub></sub>(_a,b_)=0 then \(g_{N_1}(a,b)\in\{0,-1\}\); if wt<sub>_M_<sub>1</sub></sub>(_a,b_)=-2 then _g_<sub>_N_<sub>1</sub></sub>(_a,b_)=-4; if wt<sub>_M_<sub>1</sub></sub>(_a,b_)=2 then _g_<sub>_N_<sub>1</sub></sub>(_a,b_)=2.

