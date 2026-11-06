Taking into account that an eigenvalue of the adjacency matrix of a graph _G_ is also simple called the eigenvalue of _G_, that is, \(\lambda_k(A(G))=\lambda_k(G)\), let us introduce the following theorem.

**Theorem 4.5.** _Consider the graph decomposition described in Theorem 4.2 and the corresponding matrix splitting_ (34)-(35)_. Then we obtain lower and upper bounds on the eigenvalues of_ Q(_n_) _as follows.<br>
Assume that_ \(1\le i_k,j_k,r_k,s_k\le n^2\), \(i_k+j_k\le n^2+1\) _and_ \(r_k+s_k\ge n^2+1\)_, for each_ \(k\in\{1,2,3\}\).

\(\lambda_{i_1+j_1-1}\left(\mathcal{Q}(n)\right)\le\lambda_{p_1}\left(G_{1,2}\right)+\lambda_{q_1}\left(G_3\right)\le\lambda_{r_1+s_1-n^2}\left(\mathcal{Q}(n)\right)\)<br>
\(\underbrace{\lambda_{i_2+j_2-1}}_{\lambda_{j_1}}\left(G_3\right)\le\lambda_{p_2}\left(G_3^1\right)+\lambda_{q_2}\left(G_3^2\right)\le\underbrace{\lambda_{r_2+s_2-n^2}}_{\lambda_{s_1}}\left(G_3^2\right)\)<br>
\(\underbrace{\lambda_{i_3+j_3-1}}_{\lambda_{j_2}}\left(G_3^2\right)\le\lambda_{p_3}\left(G_{3,H}^2\right)+\lambda_{q_3}\left(G_{3,V}^2\right)\le\underbrace{\lambda_{r_3+s_3-n^2}}_{\lambda_{s_2}}\left(G_3^2\right),\)

_where p<sub>k</sub>=i<sub>k</sub> and q<sub>k</sub>=j<sub>k</sub> for the lower bounds and p<sub>k</sub>=r<sub>k</sub> and q<sub>k</sub>=s<sub>k</sub> for the upper bounds._

_Proof._ Let us apply Theorem 4.4 to the matrix splitting (34)-(35), considering starting values for the indices _i_<sub>1</sub>, _i_<sub>2</sub>, _i_<sub>3</sub> and _j_<sub>3</sub> and also for the indices _r_<sub>1</sub>, _r_<sub>2</sub>, _r_<sub>3</sub> and _s_<sub>3</sub>.

1. Consider the indices \(1\le i_3,j_3,r_3,s_3\le n^2\) such that _i_<sub>3</sub>+_j_<sub>3</sub>-1=_j_<sub>2</sub> and _r_<sub>3</sub>+_s_<sub>3</sub>-_n_<sup>2</sup>=_s_<sub>2</sub>.<tbc>

\(\underbrace{\lambda_{i_3+j_3-1}}_{\lambda_{j_2}}\left(G_3^2\right)\le\lambda_{i_3}\left(G_{3,H}^2\right)+\lambda_{j_3}\left(G_{3,V}^2\right),\text{for}i_3+j_3\le n^2+1\)<br>
\(\lambda_{r_3}\left(G_{3,H}^2\right)+\lambda_{s_3}\left(G_{3,V}^2\right)\ge\underbrace{\lambda_{r_3+s_3-n^2}}_{\lambda_{s_2}}\left(G_3^2\right),\text{for}r_3+s_3\ge n^2+1,\)

were \(\lambda_{i_3}\left(G_{3,H}^2\right),\lambda_{j_3}\left(G_{3,V}^2\right),\lambda_{r_3}\left(G_{3,H}^2\right)\) and \(\lambda_{s_3}\left(G_{3,V}^2\right)\) can be obtained from (45).<tbc>

2. Consider the indices \(1\le i_2,j_2,r_2,s_2\le n^2\) such that _i_<sub>2</sub>+_j_<sub>2</sub>-1=_j_<sub>1</sub> and _r_<sub>2</sub>+_s_<sub>2</sub>-_n_<sup>2</sup>=_s_<sub>1</sub>.<tbc>

\(\underbrace{\lambda_{i_2+j_2-1}}_{\lambda_{j_1}}\left(G_3\right)\le\lambda_{i_2}\left(G_3^1\right)+\lambda_{j_2}\left(G_3^2\right),\text{for}i_2+j_2\le n^2+1\)<br>
\(\lambda_{r_2}\left(G_3^1\right)+\lambda_{s_2}\left(G_3^2\right)\ge\underbrace{\lambda_{r_2+s_2-n^2}}_{\lambda_{s_1}}\left(G_3\right),\text{for}r_2+s_2\ge n^2+1,\)

were \(\lambda_{i_2}\left(G_3^1\right)\) and \(\lambda_{r_2}\left(G_3^1\right)\) can be obtained from (44).<tbc>

3. Consider the indices \(1\le i_1,j_1,r_1,s_1\le n^2\).<tbc>

\(\lambda_{i_1+j_1-1}\left(\mathcal{Q}(n)\right)\le\lambda_{i_1}\left(G_{1,2}\right)+\lambda_{j_1}\left(G_3\right),\text{for}i_1+j_1\le n^2+1\)<br>
\(\lambda_{r_1}\left(G_{1,2}\right)+\lambda_{s_1}\left(G_3\right)\ge\lambda_{r_1+s_1-n^2}\left(\mathcal{Q}(n)\right),\text{for}r_1+s_1\ge n^2+1,\)

were \(\lambda_{i_1}\left(G_{1,2}\right)\) and \(\lambda_{r_1}\left(G_{1,2}\right)\) can be obtained from (42) when _n_ is odd and from (43) when _n_ is even.<tbc>

