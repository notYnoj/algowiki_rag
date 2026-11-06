## 2.1 The extreme coefficient at depth two

Fix an edge _e_={_u,v_} of a graph _G_. Set \(\gamma_1=\gamma_2=\phi\), \(\beta_1=\beta\), \(\beta_2=\pi/4\), and define

\(H_e(e^{\mathrm{i}\phi},\beta):=\langle\psi_2(\phi,\phi;\beta,\pi/4)|Z_uZ_v|\psi_2(\phi,\phi;\beta,\pi/4)\rangle.\) (14)

For \(a,b\in\{\pm 1\}\) let \(K_\beta^\pm(a,b)=\langle a|e^{\pm\mathrm{i}\beta X}|b\rangle\). Writing \(c=\mathrm{cos}\beta\) and \(s=\mathrm{sin}\beta\) we have

\(K_\beta^\pm(a,b)=\left\{\begin{array}{ c c }
c, & a=b, \\
\pm\mathrm{is}, & a\neq b,
\end{array}\right.\) (15)

Let _T<sub>e</sub>_ operate on an assignment string so as to flip the two vertex spins in _e_. The next lemma rewrites the edge correlator as a sum of powers of the phase factor, which lets us analyze its coefficients. The proof uses a sum-over-paths expansion over intermediate computational-basis states, as in earlier analyses of QAOA circuits \[5, 25, 27\].

**Lemma 2.2** (Reduced path sum)**.** _For_ \(z=e^{\mathrm{i}\phi}\),

\(H_e(z;\beta)=-2^{-N}\sum_{x,y,t\in\{\pm 1\}^{V(G)}}y_uy_vz^{\mathrm{c}_G(x)-\mathrm{c}_G(t)+\mathrm{c}_G(y)-\mathrm{c}_G(T_ey)}\)<br>
\(\times\prod_{w\in V(G)}K_\beta^+(x_w,y_w)K_\beta^-((T_ey)_w,t_w).\) (16)

_Hence_ \(H_e(z;\beta)\) _is a Laurent polynomial in z._

_Proof._ Write \(|s\rangle\) for the computational-basis state labeled by a spin string \(s\in\{\pm 1\}^{V(G)}\), and insert \(I=\sum_s|s\rangle\langle s|\) between successive operators in the QAOA expectation value. Label the strings at the first and second cost layers on the bra (complex-conjugate) side by _x,y_, and on the ket side by \(t,\bar{y}\), respectively. Here \(\bar{y}\) is an independent label, not the spin complement of _y_. Let _q_ label the basis state at the observable _Z<sub>u</sub>Z<sub>v</sub>_, whose eigenvalue is _q<sub>u</sub>q<sub>v</sub>_. The diagonal cost layers supply the four cut-value phases below; the two overlaps with the uniform initial state supply 2<sup>-_N_</sup>. Since \(B=\sum_wX_w\), the mixer matrix elements factor over vertices, giving

\(H_e(z;\beta)=2^{-N}\sum_{x,y,\bar{y},t,q\in\{\pm 1\}^{V(G)}}q_qu_vz^{\mathrm{c}_G(x)-\mathrm{c}_G(t)+\mathrm{c}_G(y)-\mathrm{c}_G(\bar{y})}\)<br>
\(\times\prod_{w\in V(G)}K_\beta^+(x_w,y_w)K_\bar{\beta}^-(\bar{y}_w,t_w)\prod_{w\in V(G)}K_{\pi/4}^+(y_w,q_w)K_{\pi/4}^-(q_w,\bar{y}_w).\)

Summing over the intermediate spins adjacent to the final mixer gives, for \(w\notin e\),

\(\sum_{q_w}K_{\pi/4}^+(y_w,q_w)K_{\pi/4}^-(q_w,\bar{y}_w)=\delta_{y_w,\bar{y}_w},\) (17)

and, for \(w\in e\),

\(\sum_{q_w}q_wK_{\pi/4}^+(y_w,q_w)K_{\pi/4}^-(q_w,\bar{y}_w)=-\mathrm{i}y_w\delta_{\bar{y}_w,-y_w}.\) (18)

The two endpoint factors multiply to (-i_y<sub>u</sub>_)(-i_y<sub>v</sub>_)=-_y<sub>u</sub>y<sub>v</sub>_. The Kronecker deltas enforce \(\bar{y}=T_ey\), giving (16).

Define the largest possible cut-value decrease from flipping both endpoints of _e_:

\(R_e=\mathrm{max}_y\big[\mathrm{c}_G(y)-\mathrm{c}_G(T_ey)\big].\) (19)

