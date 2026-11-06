For a uniform order define \(M_i=\mathbb{E}_x\big[\mathbf{1}_{\{x_i\le r\}}\phi_x\phi_x^\mathsf{T}\big]\).

**Lemma 2.** _Put_ \(\nu=p(n+1)/3\), \(\delta=p\nu h/(3mk)\), \(\tau=p/3\), \(T=\nu+2k\delta=(p/m)\big(v^2+(r^2-1)/3\big)\), \(S=\nu-2\delta\), \(\theta=p\nu/\sqrt{m}\) _and_ \(\eta=\sqrt{m}\delta\)_. In the decomposition_ (13),

\(M_1=\left(\begin{array}{ c c }
p & -\theta \\
-\theta & T
\end{array}\right)\oplus\oplus_{a=1}^k\left(\begin{array}{ c c }
S & \eta \\
\eta & \tau
\end{array}\right)\oplus\tau I_{k(k-1)/2}.\)

_Proof._ Condition on \(x_1=\ell\) and put \(L_\ell=2\ell-n-1\). The signs on edges at label 1 sum to \(L_\ell\), and \(b\wedge\omega=m^{-1/2}\sum_{j\ge 2}e_1\wedge e_j\), so the coordinate along \(b\wedge\omega\) is \(L_\ell/\sqrt{m}\). The sums \(n^{-1}\sum_{\ell\le r}L_\ell=-p\nu\) and \(n^{-1}\sum_{\ell\le r}L_\ell^2=p\big(v^2+(r^2-1)/3\big)\) give the first block. For a unit vector \(w\in W\) use \(g_w=e_1\wedge w\) and \(y_w=w\wedge\omega_o\) with \(\omega_o=m^{-1/2}\sum_{j\ge 2}e_j\). The star signs at label 1 contain \(\ell-1\) plus signs and \(n-\ell\) minus signs, and exchangeability gives \(A_\ell:=\mathbb{E}[\langle g_w,\phi_x\rangle^2|x_1=\ell]=4(\ell-1)(n-\ell)/(mk)\). For a uniform order on _m_ labels the oriented-edge covariance is \((I+D_m^\mathsf{T}D_m)/3\), where _D<sub>m</sub>_ has edge columns _e<sub>i</sub>-e<sub>j</sub>_. The relative order of the other labels is uniform given \(x_1=\ell\), so \(\mathbb{E}[\langle y_w,\phi_x\rangle^2|x_1=\ell]=n/3\). For the cross term, let _Y<sub>j</sub>_ be the relative rank of a label \(j\neq 1\) among the _m_ labels other than 1. This rank is uniform on \[_m_\]. Then \(\mathbb{E}[\mathrm{sgn}(\ell-x_j)(2Y_j-m-1)]=-2(\ell-1)(m-\ell+1)/m\), and since rank scores and the coordinates of _w_ sum to zero, \(\mathbb{E}[\langle g_w,\phi_x\rangle\langle y_w,\phi_x\rangle|x_1=\ell]=-\sqrt{m}A_\ell/2\). Averaging over \(\ell\le r\) gives \(A_0=n^{-1}\sum_{\ell\le r}A_\ell=2p(r-1)(3n-2r-2)/(3mk)\) and the block \(\left(\begin{array}{ c c }
A_0 & -\sqrt{m}A_0/2 \\
-\sqrt{m}A_0/2 & pn/3
\end{array}\right)\). The rotation \(w\wedge\omega=(-g_w+\sqrt{m}y_w)/\sqrt{n}\), \(b\wedge w=(\sqrt{m}g_w+y_w)/\sqrt{n}\) transforms it into the stated block, with _S=A_<sub>0</sub>+_mp/_3, \(\eta=\sqrt{m}(p/3-A_0/2)\) and \(\tau=p/3\). Exchangeability makes these forms proportional to the inner product on _W_, so orthogonal basis vectors give no cross terms. Writing \(\phi_\mathrm{st}\) and \(\phi_\mathrm{int}\) for the star and internal parts of \(\phi_x\), \(\mathbb{E}[\phi_\mathrm{st}\phi_\mathrm{int}^\mathsf{T}|x_1=\ell]=-(A_\ell/2)D_m\). The internal cycle space \(\Lambda^2W\) has zero incidence, covariance _I/_3, and no coupling to the other blocks, which gives the last block.

## A.3 Upper bound

Let \(Q=p+p\nu\zeta/m\), which is the right side of (10), and define<tbc>

\(\xi=T+\frac{p\nu}{\zeta},\ell_C=\tau+\frac{\eta^2}{\xi-S},\mathcal{L}=QP_0+\xi P_V+\ell_CP_C.\)

<tbc>Then \(\xi-T=p\nu/\zeta>0\) and \(\xi-S=p\nu(3k+2h\zeta)/(3k\zeta)>0\). Also \(\theta/(\xi-T)=\rho\), \(\eta/(\xi-S)=\gamma\) and \(Q-p=(\xi-T)\rho^2\), so the blocks of L-_M_<sub>1</sub> factor as<tbc>

\(\left(\begin{array}{ c c }
Q-p & \theta \\
\theta & \xi-T
\end{array}\right)=(\xi-T)\left(\begin{array}{ c }
\rho \\
1
\end{array}\right)\left(\rho 1
\end{array}\right),\left(\begin{array}{ c c }
\xi-S & -\eta \\
-\eta & \ell_C-\tau
\end{array}\right)=(\xi-S)\left(\begin{array}{ c }
1 \\
-\gamma
\end{array}\right)\left(1-\gamma
\end{array}\right),\)

<tbc>and the last block is \((\xi-S)\gamma^2I\unknown 0\). Hence \(\mathcal{L}\unknown M_1\), and covariance under relabeling gives \(\mathcal{L}\unknown M_i\) for every _i_. Each edge has \(\|P_V(e_i\wedge e_j)\|^2=2/n\) and \(\|P_C(e_i\wedge e_j)\|^2=k/n\), so the edge diagonal of L is \((2\xi+k\ell_C)/n\), and

\(nQ-2\xi-k\ell_C=\frac{p\nu}{m\zeta(3k+2h\zeta)}F_{n,r}(\zeta)=0.\)

Every diagonal entry of L in the feature basis therefore equals _Q_.

