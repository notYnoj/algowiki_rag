integer and \(0\le p\le 1\). For \(0\le\beta\le 1\), we have

\(Pr\big(|Z-pk|\ge\beta pk\big)\le 2exp\big(-\frac{\beta^2pk}{3}\big).\) (1)

(See Janson et al. [18, Corollary 2.3] for a proof.)

Let \(0<\delta\le 1/2\), \(0<\epsilon\le 1\), and \(\Delta\ge 3\) be given. For the purpose of analysis, set _w(e_)=1 for all \(e\in E\). We estimate the size of the stable matching \(M_\infty\) in G using a randomised algorithm that queries the preference oracle for G. We assume that the number of nodes, _n_, is given as input to the algorithm.

Let us first relate |_M<sub>j</sub>_| to \(|M_\infty|\). We have \(|M_j|\le|M_\infty|\) because every blue node, once matched, remains matched. Furthermore, \(|M_\infty|\le|M_j|+f_j(R)\) because every red node \(r\in R\) with empty _C<sub>j</sub>(r_) will be unmatched in \(M_\infty\). Let<tbc>

\(\gamma=\frac{\epsilon}{8\Delta},j\ge 1+\frac{2\Delta-2}{\epsilon}=1+\frac{\Delta-1}{4\Delta\gamma}.\) (2)

<tbc>Note that \(\gamma<1\). By _w<sub>j</sub>(B_)=|_M<sub>j</sub>_| and Lemma 6 we have

\(|M_j|\le|M_\infty|\le(1+4\Delta\gamma)|M_j|\le|M_j|+\frac{\epsilon}{2}\cdot|M_\infty|.\) (3)

It thus suffices to have an estimate for |_M<sub>j</sub>_|.

Because G has no isolated nodes, \(|R|\le\Delta|B|\) and \(|B|\le\Delta|R|\). Because a stable matching is maximal and there are no isolated nodes,

\(\Delta|M_\infty|\ge|R|,\) (4)

\(\Delta|M_\infty|\ge|B|.\) (5)

By (3) we have \(|M_\infty|\le 2|M_j|\) and thus

\(\frac{|R|}{2\Delta}\le|M_j|\le|R|.\) (6)

Since _n_=|_R_|+|_B_|, we have<tbc>

\(\frac{n}{\Delta+1}\le|R|\le n.\) (7)

<tbc>Let

\(N_0=\frac{6(\Delta+1)}{\gamma^2}ln\frac{6}{\delta},N\ge N_0.\) (8)

We use the following procedure to estimate |_M<sub>j</sub>_|. First, select _N_ nodes uniformly at random and query the oracle for their colour. Denote by _X_ the number of red nodes among the _N_ nodes. Then, select _N_ red nodes uniformly at random; that is, select \(2(\Delta+1)N\) nodes uniformly at random and select the first _N_ red nodes among those (if not enough red nodes occur,<tbc>

