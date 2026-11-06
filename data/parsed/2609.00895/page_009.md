## 2.3 An explicit cofactor formula

For \(j\in[2q]\), let<tbc>

\(R_j:=[2q]\backslash\{j\},\)

<tbc>equipped with the natural order inherited from \[2_q_\]. Define the order isomorphism<tbc>

\(\rho_j:R_j\rightarrow[2q-1]\)

<tbc>by<tbc>

\(\rho_j(i):=\left\{\begin{array}{ c c }
i, & i<j, \\
i-1, & i>j.
\end{array}\right.\)

<tbc>For a subset<tbc>

\(T=\{t_1<\cdots<t_s\}\subseteq R_j,s=|T|,\)

<tbc>let<tbc>

\(T':=R_j\backslash T.\)

<tbc>We define the shuffle sign \(\varepsilon_j(T)\) by

\(\varepsilon_j(T):=(-1)\sum_{k=1}^s(\rho_j(t_k)-k)=(-1)^{\#\{(u,t)\in T^\prime\times T:u<t\}}.\)

Equivalently, \(\varepsilon_j(T)\) is the sign of the shuffle permutation of the ordered set _R<sub>j</sub>_ that places the elements of _T_ before the elements of \(T'\), while preserving the natural order within each set.

For any index set<tbc>

\(S=\{s_1<\cdots<s_d\}\subseteq[2q]\)

<tbc>and exponent set<tbc>

\(E=\{e_1<\cdots<e_d\}\subset\mathbb{N}_0,\)

<tbc>we denote the generalized Vandermonde matrix by<tbc>

\(V_S^E:=\left(x_{s_i}^{e_k}\right)_{1\le i,k\le d}.\)

<tbc>For variables _y_<sub>1</sub>_,...,y<sub>d</sub>_, let<tbc>

\(e_r(y_1,\dots,y_d)=\sum_{1\le i_1<\cdots<i_r\le d}y_{i_1}\cdots y_{i_r}\)

<tbc>denote the elementary symmetric polynomial of degree _r_, with the conventions

\(e_0=1,e_r=0\text{for}r<0\text{or}r>d.\)

For \(T\subseteq[2q]\), we write

\(e_r((x_t)_{t\in T})\)

for the elementary symmetric polynomial of degree _r_ in the variables _x<sub>t</sub>_, \(t\in T\).

We also adopt the standard convention that empty products and determinants of \(0\times 0\) matrices equal 1.

For _r_=1_,...,q_, set<tbc>

\(E_r:=\{0,1,\dots,q-1\}\backslash\{r-1\}.\)

<tbc>For \(1\le j,m\le 2q\), let _M<sub>j,m</sub>_ denote the minor obtained from \(\Lambda\) by deleting row _j_ and column _m_. If \(det(\Lambda)\neq 0\), then the standard cofactor formula gives<tbc>

\((\Lambda^{-1})_{m,j}=\frac{(-1)^{j+m}}{det(\Lambda)}M_{j,m}.\)

