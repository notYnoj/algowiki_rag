placed. The particular case of **V**<sub>6</sub> is presented in Figure 7 and this construction is highlighted by the colors.

**Theorem 3.7.** _For_ \(n\ge 4\), -3 _is the least eigenvalue of_ T(_n_) _with multiplicity T(n_-3) _and_ **T**_<sub>n</sub> is a basis for_ E<sub>T(_n_)</sub>(-3).

_Proof._ Applying Theorem 2.2 to T(_n_) considering the edge clique partition where the vertices of each row, column and diagonal of T(_n_) is a clique, it follows that each vector of **T**_<sub>n</sub>_ is an eigenvector of T(_n_) associated with -3.

Now consider that **T**_<sub>n</sub>_ is a set of linearly dependent vectors. Then it exists \(\alpha_{(1,1)},\alpha_{(2,1)},\alpha_{(2,2)},\dots,\alpha_{(n-3,n-4)},\alpha_{(n-3,n-3)}\in\mathbb{R}^{T(n)}\) not simultaneously zero, such that

\(s=\sum_{(i,j)\in[n]\times[1,i]}\alpha_{(i,j)}t_n^{(i,j)}=0.\) (4)

Let \(\ell=T(i-1)+j\) be least integer such that \(\alpha_{(i,j)}\neq 0\). By the construction of **T**_<sub>n</sub>_, \(s_{\ell+1}=\alpha_{(i,j)}\) and so, by the Equation (4), \(s_{\ell+1}=0=\alpha_{(i,j)}\) and we get a contradiction. Thus, **T**_<sub>n</sub>_ is set of linearly independent vectors and \(\mathrm{dim}(\mathcal{E}_{\mathcal{T}(n)}(-3))\ge|\mathbf{T}_n|=T(n-3)\).

Let \(I\subseteq\{(i,j)|i\in[2,n-2],j\in[1,i-1]\}\) be the set of indices (_p,q_) such that _x_<sub>(_p,q_)</sub>, the (_T(p_-1)+_q_)-th component of \(X=(x_{(i,j)})\in\mathcal{E}_{\mathcal{T}(n)}(-3)\) are entirely determined by the entries _x_<sub>(_i,j_)</sub> with \(i\in[2,n-2]\) and \(j\in[i]\).

By Theorem 2.2, we know that the sum of the entries of _x_ by rows, column, and diagonal is zero, then we get that _x_<sub>(1,1)</sub>=_x_<sub>(_n,_1)</sub>=_x_<sub>(_n,n_)</sub>=0 and<tbc>

\(x_{(i,i)}=-\sum_{j=1}^{i-1}x_{(i,j)},\text{for}i\in[2,n-1]\)

<tbc>and so \(\{(i,j)|i\in[2,n-2],j\in[1,i-1]\}\subset I\). Similarly, we can now state that

\(x_{(n-1,1)}=-\sum_{i\in([n-2]\cup\{n\})}x_{(i,1)}\text{and}\)<br>
\(x_{(n-1,n-1)}=-\sum_{i\in([n-2]\cup\{n\})}x_{(i,i)},\)

and so \(\{(n-1,1),(n-1,n-1)\}\subset I\).

Now, considering the parameters \(j_1\in[2,n-1]\) and _j_<sub>2</sub>=\[2_,n_-2\], we can obtain

\(x_{(n,j_1)}=-\sum_{x-y=n-j_1\wedge y\neq j_1}x_{((x,y))}\text{and}\)<br>
\(x_{(n-1,j_2)}=-\sum_{x+y=n-1+j_2\wedge y\neq j_2}x_{(x,y)},\)

0
1
-1
-1
0
1
0
1
-1
0

Figure 6: Vector _t_.

