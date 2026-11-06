The designation triangular graph in some publications is used for graphs with distinct properties, as it is the case of the one introduced by Hoffman in \[9\], in the context of the study of the uniqueness of the triangular association scheme. These graphs are also referred in the book of Brualdi and Ryser \[3, p. 152\], where _T(m_) denotes a triangular graph which is defined as being the line graph of the complete graph _K<sub>m</sub>_, \((m\ge 4)\). Thus the vertices of _T(m_) may be identified as the 2-subsets of {1,2_,...,m_} and two vertices are adjacent in _T(m_) if and only if the corresponding 2-subsets have a nonempty intersection. As it is referred in \[3\], these graphs are strongly regular graphs on the parameters \((n,d,\lambda,\mu)=(\frac{m(m-1)}{2},2(m-2),m-2,4)\). Therefore, since T(_n_) is not strongly regular, this graph is not isomorphic to _T(n_). However, both graphs have some close parameters, as it can be seen in  1.

In this paper the results of Section 3 follow part of the ones introduced in \[6, Chapter 6\]. Even so, for the reader’s convenience, some proofs are herein recalled. The properties of triangular graphs of order \(\frac{n(n+1)}{2}\) , T(_n_), are explored and applied to the decomposition of the _n_-Queens’ graph into graphs belonging to three families - a family of a single graph whose components are two triangular graphs, T(_n_) and T(_n_-1), a family of a single graph whose components are cliques and a family of complete bipartite graphs. Finally, using the Weyl’s inequalities, some techniques to determine lower and upper bounds on the eigenvalues of the _n_-Queens’ graph are introduced. The notation used throughout the text, with the exception of very specific cases, is the one that is followed in \[2\] and \[7\].

## 2 Triangular board and triangular graph T(_n_)

Let T_<sub>n</sub>_ be the board of \(\frac{n(n+1)}{2}\) points in a triangular shape with _n_ dots on each side. For _n_=1,2,3,4, such arrangement is represented in Figure 1. The rows of T_<sub>n</sub>_ are labeled from 1 to _n_, from the top to the bottom and, in the _i_<sup>th</sup> row, its dots are labeled from 1 to _i_, from the left to the right. Then, the _j_<sup>th</sup> entry (dot) of the _i_<sup>th</sup> row of T(_n_) is identified by the ordered pair (_i,j_).

Note that, for \(n\in\mathbb{N}\), the number of dots of T_<sub>n</sub>_ is the _n<sup>th</sup> triangular number_ \(T(n)=\frac{n(n+1)}{2}\) .

Let us define the _n_<sup>th</sup> triangular graph as T(_n_)=(_V,E_) with<tbc>

\(V=\{(i,j)|i\in[n]\wedge j\in[i]\}\)

<tbc>and<tbc>

\(E=\left\{((i,j),(k,\ell))\in V^2|(i=k\vee j=\ell\vee i-j=k-\ell)\wedge(i,j)\neq(k,\ell)\right\}.\)

\begin{tabular}{ccc}
 & Triangular graph T(_m_) & Triangular graph \(T(m),m\ge 4\) \\
order & \(n=\frac{m(m+1)}{2}\) & \(n=\frac{m(m-1)}{2}\) \\
degree & _d_=2(_m_-1) & _d_=2(_m_-2) \\
diameter & _D_=2, for \(m\ge 3\) & _D_=2 \\
\end{tabular}

1: Some parameters of the graphs T(_m_) and _T(m_).

