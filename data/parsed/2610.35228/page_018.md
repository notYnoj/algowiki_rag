<tbc>Set \(m:=\lfloor L_N/2\rfloor\), and take _N_ sufficiently large that \(m\ge 1\). For every \(Q\subseteq V\) with \(|Q|\le 2m\), define<tbc>

\(\mu(Q):=\langle u_Q,u_\emptyset\rangle.\)

<tbc>The required vectors are available because \(2m\le L_N\). Normalization gives \(\mu(\emptyset)=1\). For \(|A|,|B|\le m\), consistency gives

\(\mu(A\cup B)=\langle u_{A\cup B},u_\emptyset\rangle=\langle u_A,u_B\rangle.\)

The first step follows from the definition of \(\mu\), and the second step follows from consistency. Thus the level-_m_ moment matrix is the Gram matrix of the vectors _u<sub>A</sub>_ with \(|A|\le m\) and is therefore positive semidefinite.

It remains to verify that the moments of sets containing an edge vanish. Let \(e=\{v,w\}\in E\). Consistency and the edge constraint give<tbc>

\(\|u_e\|^2=\langle u_{\{v\}},u_{\{w\}}\rangle=0.\)

<tbc>The first step follows from consistency, and the second step follows from the edge constraint. Hence _u<sub>e</sub>_=0. If \(e\subseteq Q\) and \(|Q|\le 2m\), consistency again gives

\(\mu(Q)=\langle u_Q,u_\emptyset\rangle=\langle u_Q,u_e\rangle=0.\)

The first step follows from the definition of \(\mu\), the second step follows from consistency and \(Q\cup e=Q\), and the third step uses _u<sub>e</sub>_=0. Therefore \(\mu\) is a level-_m_ pseudo-distribution. Its objective is preserved: for each _v_, we have \(\mu(v)=\langle u_{\{v\}},u_\emptyset\rangle=\|u_{\{v\}}\|^2\). The first step follows from the definition of \(\mu\), and the second step follows from consistency. Summing over _v_ gives the objective _B_.

Choose _c_:=_c_<sub>0</sub>/2. Integer rounding gives \(m\ge 2^{c_0q_N}/2-1\). For all sufficiently large _N_, this lower bound is at least 2<sup>_c_<sub>0</sub>_q<sub>N</sub>/_2</sup>, because \(q_N\rightarrow\infty\). After discarding finitely many graph sizes, we may therefore assume \(m\ge\lfloor 2^{cq_N}\rfloor=R_N\). Restricting \(\mu\) to any level \(1\le r\le R_N\) preserves its objective, and hence

\(\mathrm{Las}_r(G)\ge B\ge\alpha(G)N2^{-s}.\)

The first step follows because restriction preserves feasibility and the objective; the second step follows from Eq. (19). Also \(B\le N\), because each singleton marginal of a feasible pseudo-distribution is at most 1. Combining this with Eq. (19) gives \(\alpha(G)\le 2^s\).

Take \(T:=\lfloor s\rfloor+1\) and _C_:=_C_<sub>0</sub>+1. Since \(N\ge 4\) implies \(q_N\ge 1\), we have<tbc>

\(1\le T\le s+1\le Cq_N.\)

<tbc>The first step follows from _s\>_0, the second step uses \(\lfloor s\rfloor\le s\), and the third step uses _s=C_<sub>0</sub>_q<sub>N</sub>_ and \(q_N\ge 1\). Since \(N\ge 4\), we have \(\alpha(G)\ge 1\). Therefore, for every \(1\le r\le R_N\),

\(\mathrm{Las}_r(G)\ge\alpha(G)N2^{-s}\ge N2^{-s}>N2^{-T},\alpha(G)\le 2^s<2^T.\)

In the first chain, the first step follows from the objective bound above, the second step uses \(\alpha(G)\ge 1\), and the third step uses _T\>s_. In the second chain, the first step follows by combining \(B\le N\) with Eq. (19), and the second step uses _T\>s_. This proves Eq. (18).

To state the consequence precisely, let \(t_\mathrm{max}(N)\ge 1\) and \(r(N,t)\ge 1\) be integer-valued functions. Suppose that, for every \(N\ge 4\), every graph _G_ on _N_ vertices and every integer \(1\le t\le t_\mathrm{max}(N)\), one has<tbc>

\(\mathrm{Las}_{r(N,t)}(G)\ge 2^{-t}N\Longrightarrow\alpha(G)\ge 2^t.\)

