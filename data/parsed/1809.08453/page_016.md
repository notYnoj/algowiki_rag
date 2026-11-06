<tbc>A polynomial time 2-approximation algorithm can be obtained by rounding an optimal solution of \(\widehat{\mathcal{P}}\). The 2-approximation algorithm writes as follows:

ROUNDING ALGORITHM

1. Solve \(\widehat{\mathcal{P}}\) and let \((\hat{\mathbf{d}},\hat{\mathbf{x}},\hat{\mathbf{y}})\) denote an optimal solution to \(\widehat{\mathcal{P}}\);<tbc>

2. For each \(\rho\in P\), set \(y(\rho)=1\) if \(\hat{y}(\rho)\ge 0.5\), and \(y(\rho)=0\) otherwise;<tbc>

3. Return the stable marriage **x** obtained from **y** by using constraints 13-15 in P.

**Example 8** _Coming back to Example 1, assume that the weights of the GGI operator are defined by Equation 4 and that the disutility function is defined by d(i_)=_i. Then, an optimal solution_ \((\hat{\mathbf{d}},\hat{\mathbf{x}},\hat{\mathbf{y}})\) _to_ \(\widehat{\mathcal{P}}\) _is characterized by_ \(\hat{y}(\rho_1)=\hat{y}(\rho_2)=0.75\) _and_ \(\hat{y}(\rho_3)=0\) _(for a GGI value of_ 4.3075_). For this instance, by_ ROUNDING ALGORITHM_, the obtained vector_ **y** _is therefore_ \(y(\rho_1)=y(\rho_2)=1\) _and_ \(y(\rho_3)=0\)_. This corresponds to stable marriage_ **x**<sup>4</sup>_, which is in fact an optimal solution._

Steps 2 and 3 of the algorithm can obviously be performed in polynomial time. In step 1, solving \(\widehat{\mathcal{P}}\) can also be performed in polynomial time by using one of the linearizations of the GGI operator proposed by Ogryczak and Śliwiński \[2003\]. The following lemma ensures that the returned solution is a 2-approximation of an optimal solution of P:

**Lemma 2** _For any feasible solution_ \((\hat{\mathbf{d}},\hat{\mathbf{x}},\hat{\mathbf{y}})\) _of_ \(\widehat{\mathcal{P}}\)_, the feasible solution_ (**d**,**x**,**y**) _of_ P _ob tained by setting_

\(y(\rho)=\left\{\begin{array}{ c c }
1 & \text{\textit{if}}\hat{y}(\rho)\ge 0.5, \\
0 & \text{\textit{otherwise}}
\end{array}\right.\)

_is such that_ \(\hat{\mathbf{d}}\ge\frac{1}{2}\mathbf{d}\) _where_ \(\ge\) _is taken componentwise._

_Proof_ In order to establish the result stated in the lemma, we introduce the notion of man and woman _weights_ of a rotation. Given a rotation \(\rho=(m_{i_0},w_{i_0}),\dots,(m_{i_{r-1}},w_{i_{r-1}})\) we define the _m<sub>i</sub>_-weight of that rotation by:

\(\omega_i^m(\rho)=\left\{\begin{array}{ c c }
d(\mathsf{rk}(m_{i_k},w_{i_k}))-d(\mathsf{rk}(m_{i_k},w_{i_{(k+1)\mathsf{mod}r}})) & \text{if}i\in\{i_0,\dots,i_{r-1}\}\text{and}i=i_k \\
0 & \text{otherwise}.
\end{array}\right.\)

Similarly, we define the _w<sub>j</sub>_-weight of that rotation by:

\(\omega_j^w(\rho)=\left\{\begin{array}{ c c }
d(\mathsf{rk}(w_{i_k},m_{i_k}))-d(\mathsf{rk}(w_{i_k},m_{i_{(k-1)\mathsf{mod}r}})) & \text{if}j\in\{i_0,\dots,i_{r-1}\}\text{and}j=i_k \\
0 & \text{otherwise}.
\end{array}\right.\)

Note that a man weight of a rotation will always be negative while a woman weight of a rotation will always be positive.

Assume that \(\rho\) is a rotation that is exposed in a stable marriage **x**, and let \(\mathbf{x}'\) be the stable marriage obtained from **x** by eliminating \(\rho\). Then:<tbc>

\(d(m_i,\mathbf{x}')=d(m_i,\mathbf{x})-\omega_i^m(\rho),d(w_j,\mathbf{x}')=d(w_j,\mathbf{x})-\omega_j^w(\rho).\)

<tbc>Consequently, if **x** is the stable marriage obtained from the man-optimal stable marriage **x**_<sup>m</sup>_ by eliminating rotations \(\rho_1,\dots,\rho_t\), then:<tbc>

\(d(m_i,\mathbf{x})=d(m_i,\mathbf{x}^m)-\sum_{k=1}^t\omega_i^m(\rho_k),d(w_j,\mathbf{x})=d(w_j,\mathbf{x}^m)-\sum_{k=1}^t\omega_j^w(\rho_k).\)

