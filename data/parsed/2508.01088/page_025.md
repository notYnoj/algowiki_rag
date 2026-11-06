(_a)_ _The graph_ \(G_{3,H}^2\) _is formed by K_<sub>1,3</sub>_, with vertex bipartition_ ({_a},{b,c,d_})_, K_<sub>2,2</sub>_, with vertex bipartition_ ({_e,f},{g,h_})_, K_<sub>3,1</sub>_, with vertex bipartition_ ({_i,j,k},{l_}) _and K_<sub>4,0</sub>_, with vertex bipartition_ (\(\{m,n,o,p\},\varnothing\));<tbc>

(_b)_ _The graph_ \(G_{3,V}^2\) _is formed by K_<sub>1,3</sub>_, with vertex bipartition_ ({_p},{d,h,l_})_, K_<sub>2,2</sub>_, with vertex partition_ ({_o,k},{g,c_})_, K_<sub>3,1</sub>_, with vertex partition_ ({_n,j,f},{b_}) _and K_<sub>4,0</sub>_, with vertex partition_ (\(\{m,i,e,a\},\varnothing\)).<tbc>

<tbc>_Each complete bipartite graph appears as represented by its adjacency matrix in_ \(A(G_{3,H}^2)\) _and_ \(A(G_{3,V}^2)\)_, where they are square diagonal submatrices. It is assumed that K_<sub>4,0</sub> _has no edges._<tbc>

<tbc>_Since_ \(\sigma(A(G_{3,H}^2)=\sigma(A(G_{3,V}^2)\) _it follows that_

\(\sigma(A(G_{3,X}^2)=\sigma(K_{1,3})\cup\sigma(K_{2,2})\cup\sigma(K_{3,1})\cup\sigma(K_{4,0})\)<br>
\(=\{\sqrt{3},0^{[2]},-\sqrt{3}\}\cup\{2,0^{[2]},-2\}\cup\{\sqrt{3},0^{[2]},-\sqrt{3}\}\cup\{0^{[4]}\}\)<br>
\(=\{2,\sqrt{3}^{[2]},0^{[10]},-\sqrt{3}^{[2]},-2\},\) (37)

_for X=H and X=V._

_Therefore,_ \(A(G_3^2)=A(G_{3,H}^2)+A(G_{3,V}^2)\) _and the adjacency matrix of G_<sub>3</sub>_, is_

\(A(G_3)=A(G_3^1)+\underbrace{A(G_{3,H}^2)+A(G_{3,V}^2)}_{A(G_3^2)}.\) (38)

_Taking into account_ (38)_, we obtain_

\(A(\mathcal{Q}(4))=A(G_{1,2})+A(G_3)\)<br>
\(=A(G_{1,2})+\big(A(G_3^1)+\big(A(G_{3,H}^2)+A(G_{3,V}^2)\big)\big).\) (39)

## 4.2 Lower and upper bounds on the eigenvalues of Q(_n_)

In this section, we apply the Weyl’s inequalities to the splitting (39), which corresponds to the graph decomposition of Q(_n_), to determine lower and upper bounds for the eigenvalues of Q(_n_).

**Theorem 4.4.** (Weyl, 1912) \[12\]<br>
_For Hermitian matrices_ \(A,B\in\mathbb{C}^{n\times n}\)_, considering the eigenvalues in non-increasing order,_ \(\lambda_1(X)\ge\lambda_2(X)\ge\cdots\ge\lambda_n(X)1\le i,j\le n\),

\(\lambda_{i+j-1}(A+B)\le\lambda_i(A)+\lambda_j(B),i+j\le n+1,\) (40)

\(\lambda_i(A)+\lambda_j(B)\le\lambda_{i+j-n}(A+B).i+j\ge n+1.\) (41)

As direct consequence of Theorem 4.2, we may apply the Weyl’s inequalities (40)-(41), taking into account the matrix equation (35). First, let us determine the spectrum of the graphs _G_<sub>1,2</sub>, \(G_3^1\), \(G_{3,H}^2\) and \(G_{3,V}^2\).

• **Spectrum of** _G_<sub>1,2</sub>**.** Since _G_<sub>1,2</sub> has two components, one isomorphic to T(_n_) and other isomorphic to T(_n_-1), it follows that<tbc>

<tbc>\(\sigma(G_{1,2})=\sigma(\mathcal{T}(n))\bigcup_\text{with repetitions}\sigma(\mathcal{T}(n-1)).\)<tbc>

<tbc>Then, from Theorem 3.19 (Theorem 6.3.20 in \[6\]), we have the following:<tbc>

