<tbc>A mathematical programming formulation of the GGISM problem reads as follows:<tbc>

\(\mathcal{P}\left\{\begin{array}{ c c }
min_{\mathbf{d},\mathbf{x},\mathbf{y}}\mathtt{GGI}_\unknown(\mathbf{d}) &  \\
d_i^m=\sum_{(i,j)\in\Gamma} x_{ij}d(\mathbf{rk}(m_i,w_j)), & \forall i\in\{1,\dots,n\} \\
d_j^w=\sum_{(i,j)\in\Gamma} x_{ij}d(\mathbf{rk}(w_j,m_i)), & \forall j\in\{1,\dots,n\} \\
x_{ij}=1-y(\rho_\mathtt{break}(i,j)), & \forall(i,j)\in\Gamma\text{s.t.}x_{ij}^m=1 &  \\
x_{ij}=y(\rho_\mathtt{get}(i,j)), & \forall(i,j)\in\Gamma\text{s.t.}x_{ij}^w=1 &  \\
x_{ij}=y(\rho_\mathtt{get}(i,j))-y(\rho_\mathtt{break}(i,j)), & \forall(i,j)\in\Gamma\text{s.t.}x_{ij}^m=x_{ij}^w=0 &  \\
y(\rho')-y(\rho)\le 0, & \forall(\rho,\rho')\text{s.t.}\rho<\rho' &  \\
d_i^m\ge 0, & \forall i\in\{1,\dots,n\} \\
d_j^w\ge 0, & \forall j\in\{1,\dots,n\} \\
x_{ij}\ge 0, & \forall(i,j)\in\Gamma \\
y(\rho)\in\{0,1\}, & \forall\rho\in P
\end{array}\right.\) (13)

<tbc>where \(d_i^m\) (resp. \(d_j^w\)) represents the disutility of _m<sub>i</sub>_ (resp. _w<sub>j</sub>_), \(\mathbf{d}=(d_1^m,\dots,d_n^m,d_1^w,\dots,d_n^w)\), and as usual:

- _x<sub>ij</sub>_=1 (resp. 0) if (_m<sub>i</sub>,w<sub>j</sub>_) is (resp. is not) in the stable marriage **x**,<tbc>

**-** \(y(\rho)=1\) (resp. 0) if \(\rho\) belongs (resp. does not) to the set of rotations characterizing **x**,<tbc>

**-** _P_ is the set of all rotations.

Let us denote by \(\widehat{\mathcal{P}}\) the linear programming relaxation of P where \(y(\rho)\in\{0,1\}\) is replaced by \(0\le y(\rho)\le 1\). Importantly, note that variables \(y(\rho)\) in an optimal solution to \(\widehat{\mathcal{P}}\) are not necessarily integer because the objective function is non-linear (and therefore there does not necessarily an optimal vertex in the solution polytope).

\begin{tabular}{ccc}
\((m,w)\in\Gamma\) & \(\rho_\mathtt{get}(m,w)\) & \(\rho_\mathtt{break}(m,w)\) \\
(_m_<sub>1</sub>_,w_<sub>1</sub>) & & \\
(_m_<sub>2</sub>_,w_<sub>2</sub>) & & \\
(_m_<sub>3</sub>_,w_<sub>3</sub>) & & \\
(_m_<sub>4</sub>_,w_<sub>7</sub>) & & \(\rho_1\) \\
(_m_<sub>4</sub>_,w_<sub>6</sub>) & \(\rho_1\) & \\
(_m_<sub>5</sub>_,w_<sub>6</sub>) & & \(\rho_1\) \\
(_m_<sub>5</sub>_,w_<sub>7</sub>) & \(\rho_1\) & \\
(_m_<sub>6</sub>_,w_<sub>4</sub>) & & \(\rho_2\) \\
(_m_<sub>6</sub>_,w_<sub>5</sub>) & \(\rho_2\) & \\
(_m_<sub>7</sub>_,w_<sub>5</sub>) & & \(\rho_2\) \\
(_m_<sub>7</sub>_,w_<sub>4</sub>) & \(\rho_2\) & \\
(_m_<sub>8</sub>_,w_<sub>8</sub>) & & \(\rho_3\) \\
(_m_<sub>8</sub>_,w_<sub>10</sub>) & \(\rho_3\) & \\
(_m_<sub>9</sub>_,w_<sub>10</sub>) & & \(\rho_3\) \\
(_m_<sub>9</sub>_,w_<sub>9</sub>) & \(\rho_3\) & \\
(_m_<sub>10</sub>_,w_<sub>9</sub>) & & \(\rho_3\) \\
(_m_<sub>10</sub>_,w_<sub>8</sub>) & \(\rho_3\) & \\
\end{tabular}

2: Rotations \(\rho_\mathtt{get}(m,w)\) and \(\rho_\mathtt{break}(m,w)\) in Example 1.

