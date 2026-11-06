# OPTIMAL SOLUTION RANKS IN THE MAX-CUT SEMIDEFINITE RELAXATION

AVINASH BHARDWAJ AND VISHNU NARAYANAN

Abstract. For every _n_ and _r_ with \(1\le r\) and \(\genfrac(){pt}{2}{r+1}{2}\le n\), we construct a connected unweighted graph on _n_ vertices whose Max-Cut semidefinite relaxation has a unique optimal solution of rank _r_. The main examples are the Kneser graphs _K(m,_2), whose unique optima have rank _m_-1. A six-vertex wheel supplies rank three, and attaching pendant vertices preserves both rank and uniqueness. For dense random graphs, we also prove a polynomial lower bound on the optimal rank.

### 1. Introduction

The semidefinite relaxation of Max-Cut replaces the two signs defining a cut by unit vectors. This raises a natural question: how many dimensions can a graph force an optimal representation to use? We show that connected unweighted graphs can require every dimension allowed by the general rank bound, even with a unique optimal Gram matrix.

Let _G_ be a graph on the vertex set [_n_] with symmetric nonnegative weight matrix _A_=(_a<sub>ij</sub>_), zero diagonal, and Laplacian _L_=Diag(_A_**1**)-_A_. We denote the Goemans–Williamson relaxation [9] by SDP(_G_) and its optimal value by sdp(_G_):

\(\mathrm{sdp}(G)=\mathrm{max}\big\{\frac{1}{4}\langle L,X\rangle:X\in\mathcal{E}_n\big\},\)<br>
\(\mathcal{E}_n=\{X\in\mathbb{R}^{n\times n}:X\unknown 0,\mathrm{diag}X=\mathbf{1}\},\)

where E_<sub>n</sub>_ is the elliptope. A point of E_<sub>n</sub>_ is the Gram matrix of a family of unit vectors, and its rank is the dimension of the space they span. Rank one is the integral case: \(X\in\mathcal{E}_n\) has rank one exactly when \(X=xx^\top\) with \(x\in\{\pm 1\}^n\), a cut. Let _F(G_) be the set of optimal solutions of SDP(_G_), which is a face of E_<sub>n</sub>_, and define the _optimal rank_

\(\rho(G)=\mathrm{min}\{\mathrm{rank}X:X\in F(G)\}.\)

Thus \(\rho(G)\) measures the dimension needed by the best optimal representation, and \(\rho(G)=1\) exactly when the relaxation is exact. Bhardwaj [4] shows that recognising exactness is NP-hard even for unweighted graphs. Optimal ranks have been studied from several angles [12, 15], and low-rank formulations also underlie heuristics for Max-Cut [5]. Here we ask how large \(\rho(G)\) can be as a function of the number of vertices.

An upper bound on \(\rho(G)\) comes from general theory. _F(G_) is a nonempty compact face of E_<sub>n</sub>_, so it has an extreme point, which is an extreme point of E_<sub>n</sub>_; and by the theorem of Barvinok [2] and Pataki [18], an extreme point of a spectrahedron defined by _n_ linear equations has rank _r_ with \(\genfrac(){pt}{2}{r+1}{2}\le n\). Thus an optimal solution of SDP(_G_) attains a rank satisfying this bound, and hence

\(\rho(G)\le r_\mathrm{BP}(n):=\mathrm{max}\big\{r:\genfrac(){pt}{2}{r+1}{2}\le n\big\}=\big\lfloor\frac{\sqrt{8n+1}-1}{2}\big\rfloor.\) (1)

The question we answer is whether equality in (1) is attained for every _n_, even by connected unweighted graphs.

2020 _Mathematics Subject Classification._ 90C22, 90C27, 05C50, 15B48. _Key words and phrases._ maximum cut, semidefinite programming, rank of optimal solutions, elliptope, Barvinok- Pataki bound, Kneser graphs.

