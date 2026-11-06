<tbc>**Theorem 4.1.** _Let H be the unweighted graph obtained by joining a new vertex to every vertex of C_<sub>5</sub>_. Then the Max-Cut semidefinite relaxation of H has a unique optimal solution of rank three and optimal value_ \((23+4\varphi)/4\)_, where_ \(\varphi=(1+\sqrt{5})/2\).

_Proof._ Write _h_ for the hub, label the cycle vertices 0_,...,_4 in cyclic order, and put<tbc>

\(\varphi=\frac{1+\sqrt{5}}{2},b=\varphi+2,a=b^{-1},s=\sqrt{1-a^2}.\)

<tbc>Assign the hub the unit vector _u<sub>h</sub>_=(0,0,1) and assign the cycle vertices

\(u_j=(scos\theta_j,ssin\theta_j,-a),\theta_j=\frac{4\pi j}{5}(0\le j\le 4).\)

The five cycle vectors lie on a circle below the hub vector, with consecutive cycle vertices separated by an angle of \(4\pi/5\) around that circle. To see the choice of height, replace _a_ by \(t\in[0,1]\) in this representation. The sum of the edge inner products is \(\frac{5}{2}((\varphi+2)t^2-2t-\varphi)\), minimized at _t=a_. We next certify that this representation is optimal among all feasible Gram matrices. Let \(U\in\mathbb{R}^{6\times 3}\) have the displayed rows. Its columns are independent, so \(X^*=UU^\top\) is feasible and has rank three.

Let _A<sub>C</sub>_ be the adjacency matrix of _C_<sub>5</sub> and consider, in the vertex order _h,_0_,...,_4, the matrix<tbc>

\(S=\left(\begin{array}{ c c }
5/b & \mathbf{1}^\top \\
\mathbf{1} & A_C+\varphi I
\end{array}\right).\)

<tbc>The eigenvalues of _A<sub>C</sub>_ are \(2cos(2\pi k/5)\), \(0\le k\le 4\). On the nonconstant cycle eigenspaces, _S_ therefore has eigenvalues 0 and \(\sqrt{5}\), each twice. On the remaining subspace, with the constant cycle vector normalized to unit length, it is represented by

\(\left(\begin{array}{ c c }
5/b & \sqrt{5} \\
\sqrt{5} & b
\end{array}\right).\)

This matrix has determinant zero and trace 5_/b+b_=5. Thus \(S\unknown 0\) and dimker_S_=3.

The identity \(2cos(4\pi/5)=-\varphi\) shows that _S_ annihilates the first two columns of _U_. For the third column, the hub equation is 5_/b_-5_a_=0 and each cycle equation is \(1-(2+\varphi)a=0\). Hence _SU_=0 and ker_S_=range_U_.

Let _A<sub>H</sub>_ be the adjacency matrix of _H_. Since _S_ and _A<sub>H</sub>_ have the same off-diagonal entries, every \(X\in\mathcal{E}_6\) satisfies

\(\langle A_H,X\rangle=\langle S,X\rangle-5/b-5\varphi\ge-5/b-5\varphi.\)

Equality holds for _X_<sup>∗</sup> because _SU_=0. Minimizing \(\langle A_H,X\rangle\) is equivalent to maximizing the Max-Cut objective, so _X_<sup>∗</sup> is optimal. For any optimum _X_, equality gives _SX_=0, and therefore \(rangeX\subseteq kerS=rangeU\).

The graph has ten edges, so the optimal value is \(5+(5/b+5\varphi)/4=(23+4\varphi)/4\approx 7.368\). Its maximum cut has value 7: if _k_ cycle vertices lie opposite the hub, at most \(k+2min\{k,5-k\}\le 7\) edges cross the cut, and equality is attained by placing cycle vertices 0,2,4 opposite the hub.

It remains to show that the diagonal equations allow no other optimum. By Lemma 2.2, write \(X=UMU^\top\) with \(M\in Sym(\mathbb{R}^3)\) positive semidefinite. The hub equation gives _M_<sub>33</sub>=1. The equation \(u_j^\top Mu_j=1\) at each cycle vertex becomes

\(0=\frac{s^2}{2}(M_{11}+M_{22}-2)\)<br>
\(+\frac{s^2}{2}(M_{11}-M_{22})cos(2\theta_j)+s^2M_{12}sin(2\theta_j)\)<br>
\(-2asM_{13}cos\theta_j-2asM_{23}sin\theta_j.\)

The five functions \(1,cos\theta,sin\theta,cos2\theta,sin2\theta\) are linearly independent when evaluated at the five angles \(\theta_j\). Indeed, multiplying a vanishing linear combination by \(e^{2i\theta}\) gives a polynomial of degree at

