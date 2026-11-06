for _c_<sub>11</sub>. This polynomial identity thus records the linear combinations and products to be formed, as well as the combinations that assemble the outputs from them.

We will next present Schönhage’s identity in the same way. Recall that the **_outer product_** of two vectors (_x_<sub>1</sub>_,x_<sub>2</sub>_,x_<sub>3</sub>) and (_y_<sub>1</sub>_,y_<sub>2</sub>_,y_<sub>3</sub>) consists of the nine numbers _x<sub>i</sub>y<sub>j</sub>_, and the **_inner product_** of two vectors (_p_<sub>11</sub>_,p_<sub>12</sub>_,p_<sub>21</sub>_,p_<sub>22</sub>) and (_q_<sub>11</sub>_,q_<sub>12</sub>_,q_<sub>21</sub>_,q_<sub>22</sub>) is the single number \(\sum_{i,j=1}^2p_{ij}q_{ij}\). These are special cases of matrix products: the outer product is multiplying a \(3\times 1\) matrix times a \(1\times 3\) matrix, and the inner product is multiplying a \(1\times 4\) matrix times a \(4\times 1\) matrix. (We index the _p_ and _q_ variables with \(\{1,2\}\times\{1,2\}\) rather than {1,2,3,4} to set up nicer notation for \(\hat{p}\) and \(\hat{q}\) in Lemma 6 below.)

Separately computing the inner product and outer product would use 9+4=13 multiplications. However, Schönhage \[Sch81, §6, eq. (6.3), with _k=n_=3\] showed that they can be computed (along with some error terms that will turn out to be harmless) using only 10 multiplications. The fact that this is possible even when the inner and outer products are on disjoint sets of variables is surprising, and refuted a border rank version of the "direct sum conjecture for tensor rank" \[Str73\].

We call _x_<sub>1</sub>_,x_<sub>2</sub>_,x_<sub>3</sub>_,p_<sub>11</sub>_,p_<sub>12</sub>_,p_<sub>21</sub>_,p_<sub>22</sub> the seven **_left variables_** and _y_<sub>1</sub>_,y_<sub>2</sub>_,y_<sub>3</sub>_,q_<sub>11</sub>_,q_<sub>12</sub>_,q_<sub>21</sub>_,q_<sub>22</sub> the seven **_right variables_**. We will also use ten output variables _z<sub>ij</sub>_ (for \(1\le i,j\le 3\)) and _z_<sub>0</sub>, one for each of the ten quantities we aim to compute, namely, the coefficients of the output variables in the polynomial<tbc>

\(G:=\sum_{i,j=1}^3x_iy_jz_{ij}+\left(\sum_{i,j=1}^2p_{ij}q_{ij}\right)z_0.\)

<tbc>As a notational helper to state the identity, we introduce two \(3\times 3\) matrices \(\hat{p}\) and \(\hat{q}\) of linear forms. These are formed by starting with the \(2\times 2\) matrices of the _p_’s and of the _q_’s, then extending them to \(3\times 3\) matrices so that every column of \(\hat{p}\) and every row of \(\hat{q}\) sums to zero:

\(\hat{p}=\left(\begin{array}{ c c c }
p_{11} & p_{12} & 0 \\
p_{21} & p_{22} & 0 \\
-p_{11}-p_{21} & -p_{12}-p_{22} & 0
\end{array}\right),\hat{q}=\left(\begin{array}{ c c c }
q_{11} & q_{12} & -q_{11}-q_{12} \\
q_{21} & q_{22} & -q_{21}-q_{22} \\
0 & 0 & 0
\end{array}\right).\)

Notice that \(\sum_{i,j=1}^3\hat{p}_{ij}\hat{q}_{ij}=\sum_{i,j=1}^2p_{ij}q_{ij}\) is the desired inner product.

Schönhage’s identity has ten **_terms_**, which we name _P<sub>ij</sub>_ (for \(1\le i,j\le 3\), corresponding to the entries of \(\hat{p}\) and \(\hat{q}\)) and _P_<sub>0</sub>. Each term \(\lambda\) is the product of a linear form \(\varphi_\lambda\) in the left variables, a linear form \(\psi_\lambda\) in the right variables, and a linear form \(\chi_\lambda\) in the output variables. These linear forms are as follows:

\(\varphi_{P_{ij}}=x_i+\hat{p}_{ij},\psi_{P_{ij}}=y_j+\hat{q}_{ij},\chi_{P_{ij}}=z_{ij}+z_0,\)<br>
\(\varphi_{P_0}=-(x_1+x_2+x_3),\psi_{P_0}=y_1+y_2+y_3,\chi_{P_0}=z_0.\)

**Lemma 6.** _Summing over the ten terms,_<tbc>

\(\sum_\lambda\varphi_\lambda\psi_\lambda\chi_\lambda=G+E,\text{\textit{where}}E:=\sum_{i,j=1}^3\left(x_i\hat{q}_{ij}+\hat{p}_{ij}y_j+\hat{p}_{ij}\hat{q}_{ij}\right)z_{ij}.\)

<tbc>_Proof._ We compute the coefficient of each output variable on the left-hand side. The coefficient of _z<sub>ij</sub>_ comes only from the term _P<sub>ij</sub>_, and it is \(\varphi_{P_{ij}}\psi_{P_{ij}}=(x_i+\hat{p}_{ij})(y_j+\hat{q}_{ij})=x_iy_j+(x_i\hat{q}_{ij}+\hat{p}_{ij}y_j+\hat{p}_{ij}\hat{q}_{ij})\). The coefficient of _z_<sub>0</sub> is \(\sum_{i,j=1}^3(x_i+\hat{p}_{ij})(y_j+\hat{q}_{ij})-(x_1+x_2+x_3)(y_1+y_2+y_3)\).<tbc>

