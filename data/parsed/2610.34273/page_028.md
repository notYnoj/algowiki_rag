Let _s,w_ be two more variables. For every integer \(e\ge 0\), define<tbc>

\(U_e=\{Fs+Gw:F,G\in V_e\}.\)

<tbc>We use the ordered basis _u_<sup>_e-i_</sup>_v<sup>i</sup>s,u_<sup>_e-i_</sup>_v<sup>i</sup>w_, first in increasing _i_ and then in the displayed order within each pair. The tensor \(\mathcal{C}_n(a_1,\dots,a_{n-2},b)\otimes_KE_{n-1,n}^{(2)}\) represents the multilinear map

\(V_{a_1-1}\times\cdots\times V_{a_{n-2}-1}\times U_{b-1}\longrightarrow U_{S+b-1},\)<br>
\((f_1,\dots,f_{n-2},F)\longmapsto\left(\prod_{j=1}^{n-2}f_j\right)F.\)

Indeed, the edge tensor preserves the choice of _s_ or _w_ from the last input to the output, while C_<sub>n</sub>_ multiplies the coefficient polynomials. This changes only the indexing of the last two legs. The other _n_-2 inputs remain separate legs.

We now construct bases of the last input and output spaces that work for every choice of the shared inputs. Put _D=uw-vs_. For every integer \(e\ge 1\), define the linear map

\(\rho_e:U_e\longrightarrow V_{e+1},\rho_e(Fs+Gw)=uF+vG.\)

For integers \(0\le i\le e\), put _q<sub>e,i</sub>=u_<sup>_e-i_</sup>_v<sup>i</sup>s_, and put _q_<sub>_e,e_+1</sub>=_v<sup>e</sup>w_. Their images under \(\rho_e\) are, in order, all the monomials _u_<sup>_e_+1-_i_</sup>_v<sup>i</sup>_ with \(0\le i\le e+1\). Hence \(\rho_e\) is surjective.

Multiplication by _D_ is injective on _V_<sub>_e_-1</sub>, since _D_ is nonzero and the polynomial ring C\[_u,v,s,w_\] has no zero divisors. Also, \(\rho_e(Dg)=0\) for every \(g\in V_{e-1}\). The kernel has dimension (2_e_+2)-(_e_+2)=_e_, which equals dim_V_<sub>_e_-1</sub>. Thus multiplication by _D_ identifies _V_<sub>_e_-1</sub> with the entire kernel, giving the exact sequence<tbc>

\(0\longrightarrow V_{e-1}-\rightarrow^{g\mapsto Dg}U_e-\rightarrow^{\rho_e}V_{e+1}\longrightarrow 0.\)

<tbc>In particular, an ordered basis of _U<sub>e</sub>_ consists of the vectors _q_<sub>_e,_0</sub>_,...,q_<sub>_e,e_+1</sub>, followed by

\(k_{e,j}=Du^{e-1-j}v^j(0\le j<e).\)

For completeness, apply \(\rho_e\) to a linear relation among these vectors. The coefficients of all _q<sub>e,i</sub>_ vanish because their images form a basis of _V_<sub>_e_+1</sub>. Injectivity of multiplication by _D_ then forces the coefficients of all _k<sub>e,j</sub>_ to vanish. There are (_e_+2)+_e_=2_e_+2=dim_U<sub>e</sub>_ vectors, so they form a basis.

Use these bases with _e=b_-1 and _e=S+b_-1. Both are at least one because \(b\ge 2\) and \(S\ge 0\). Fix any tuple of shared input forms \(f_j\in V_{a_j-1}\), for \(1\le j\le n-2\), and put \(f=\prod_{j=1}^{n-2}f_j\in V_S\). Multiplication by _f_ respects both the quotient and the kernel:

\(\rho_{S+b-1}(fF)=f\rho_{b-1}(F)(F\in U_{b-1}),\)<br>
\(f(Dg)=D(fg)(g\in V_{b-2}).\)

We spell out what these two identities say about the coefficients. Write<tbc>

\(f=\sum_{t=0}^Sc_tu^{S-t}v^t,c_t=0(t\in\mathbb{Z}\backslash\{0,\dots,S\}).\)

<tbc>For an input quotient lift _q_<sub>_b_-1_,i_</sub>, where \(0\le i\le b\), its image under \(\rho_{b-1}\) is _u_<sup>_b-i_</sup>_v<sup>i</sup>_. Thus the output quotient coordinates of _fq_<sub>_b_-1_,i_</sub> are _c_<sub>_r-i_</sub> for \(0\le r\le S+b\). Subtracting the corresponding<tbc>

