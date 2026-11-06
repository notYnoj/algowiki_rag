<tbc>scalar and block Toeplitz matrices \[4,5\] motivate our approach. We first derive an incremental recurrence for the needed QR data, with only O(_np_<sup>2</sup>+_p_<sup>3</sup>) arithmetic and O(_np+p_<sup>2</sup>) storage complexity. However, this approach will suffer from numerical cancellation. So we address this cancellation through dynamic generator-refreshing, even though it will add extra computational cost. The dynamic method further motivates us to use the first block row of the orthogonal basis of the Toeplitz matrix as the basis to construct the Arnoldi vectors. Based on this idea, we give a structured representation of the Arnoldi basis. Under an additional split form assumption of _A(s_), we use this structured representation to give the implicitly rebased method, which is both fast and stable in numerical experiments.

The paper is organized as follows. Section 2 reviews infGMRES. Section 3 uses the block Toeplitz structure to derive the incremental and dynamic algorithms. Section 4 further explores the structure of the Arnoldi basis and develops the implicitly rebased method. Section 5 establishes the residual lower bound of infGMRES and explains the effect of scaling. Section 6 applies our algorithms to several numerical experiments to illustrate their performance. Conclusions are given in Section 7.

**2. Review of infGMRES.** We first introduce the infGMRES framework \[6\]. Throughout, assume that \(z\neq 0\), _A_<sub>0</sub>:=_A_(0) is nonsingular, and _A(s_) is analytic near the origin. Its Taylor expansion is<tbc>

\(A(s)=\sum_{j=0}^\infty A_js^j,A_j:=\frac{A^{(j)}(0)}{j!},\) (2.1)

<tbc>and its degree-_q_ truncation is \(A_q(s)=\sum_{j=0}^qA_js^j\). For any _s_ such that _A<sub>q</sub>(s_) is nonsingular, the solution _x<sub>q</sub>(s_) of _A<sub>q</sub>(s)x<sub>q</sub>(s_)=_z_ is equivalent to the first _n_ elements of the solution of<tbc>

\((\mathcal{L}_0-s\mathcal{L}_1)v(s)=\text{vec}_0(z),\text{vec}_0(z):=\left[z^T0\cdots 0\right]^T\in\mathbb{C}^{(q+1)n},\)

<tbc>with<tbc>

