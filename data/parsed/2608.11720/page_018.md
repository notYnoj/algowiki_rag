<tbc>The case _t_=0 holds because \(C_{\kappa,0}(J_s)\) is the trivial event and after tracing out the teleportation registers of B, it follows from the definition of Algorithm B that both A and B have the same initial state on the registers being compared.

Then assume Eq (11) holds for some _t\<T_. We will prove it also holds for round _t_+1. Let _I<sub>s</sub>(t_)=\[_u,v_\] and _I<sub>s</sub>(t_+1)=\[_u_+1_,v_-1\]. We first analyse the R registers, which in A are communicated one step clockwise. In B, the corresponding transfers happening into the interval _I<sub>s</sub>(t_+1) are<tbc>

\(\mathsf{R}_{t+1}(p)\longrightarrow\mathsf{L}_{t+2}(p+1),p\in[u,v-2].\)

<tbc>Let us apply Lemma 6.1 to the interval \[_u,v_-1\]. We identify the registers X,Y,Z in Lemma 6.1 with B’s registers as<tbc>

\(\mathsf{X}(p)=\mathsf{R}_{t+1}(p),\mathsf{Y}(p)=\mathsf{T}_{t+1,R}(p),\mathsf{Z}(p)=\mathsf{L}_{t+2}(p).\)

<tbc>Any registers of B not treated explicitly are assumed to be included in the environment E of Lemma 6.1. In B, after the communication round, the register T<sub>_t_+1_,R_</sub>(_p_)=Y(_p_) is maximally entangled with L<sub>_t_+2</sub>(_p_+1)=Z(_p_+1), as required by the lemma for \(p\in[u,v-2]\). On the event \(C_{\kappa,t+1}(J_s)\), we have

\(k_{t+1,R}(p+1)=k_{t+1,R}(p)=\kappa_{t+1,R},\forall p\in[u,v-2].\)

Thus, the unitary _P_<sub>_k_<sub>_t_+1_,R_</sub>(_p_+1)</sub> applied on L<sub>_t_+2</sub>(_p_+1) is the proper teleportation correction operation. Therefore, by Lemma 6.1, the overall effect is a relabelling \(\mathsf{R}_{t+1}(p)\longrightarrow\mathsf{L}_{t+2}(p+1)\) for \(p\in[u,v-2]\). Since all registers not mentioned above were included in E, the lemma also guarantees this relabelling preserves any correlations with E.

The counter-clockwise transfers of the L registers are treated analogously, by applying Lemma 6.1 to the interval \[_u_+1_,v_\] with the opposite ordering. This gives the relabellings \(\mathsf{L}_{t+1}(p)\longrightarrow\mathsf{R}_{t+2}(p-1)\) for \(p\in[u+2,v]\). Together, these two relabellings reproduce the communication step of A on _I<sub>s</sub>(t_+1)=\[_u_+1_,v_-1\]. Indeed, for each vertex \(p\in I_s(t+1)\), the register L<sub>_t_+2</sub>(_p_) comes from R<sub>_t_+1</sub>(_p_-1), and the register R<sub>_t_+2</sub>(_p_) comes from L<sub>_t_+1</sub>(_p_+1), exactly as in one communication round of A.

Finally, after the communication round _t_+1, A applies _U_<sub>_t_+1</sub> to the three local registers at each vertex. In B, this same unitary is applied at Step (iii) to \(\mathsf{L}_{t+2}(p)\otimes\mathsf{M}(p)\otimes\mathsf{R}_{t+2}(p)\), which by the argument above have the same state as the registers of A in _I<sub>s</sub>(t_+1). This shows that, given the event \(C_{\kappa,t+1}(J_s)\),

\(\rho_{t+1}^{(\mathscr{B})}(I_s(t+1)|C_{\kappa,t+1}(J_s))=\rho_{t+1}^{(\mathscr{A})}(I_s(t+1)).\)

Therefore, by induction, Eq (11) holds for \(0\le t\le T\).

In particular, Eq (11) holds for _t=T_, where the interval _I<sub>s</sub>(T_)=\[_s+T,s+T+r_-1\]. Since _I<sub>s</sub>(T_) has length _r_ and A has no monochromatic block of length _r_ in its support, then for every \(a\in\Sigma\),<tbc>

\(\mathrm{Tr}\big(\Pi_a^{\otimes r}\rho_T^{(\mathscr{A})}(I_s(T))\big)=0,\)

<tbc>where \(\Pi_a\) is a measurement effect (cf. Definition 3.1). Substituting Eq (11) in the previous equation,

\(\mathrm{Tr}\big(\Pi_a^{\otimes r}\rho_T^{(\mathscr{B})}(I_s(T)|C_{\kappa,T}(J_s))\big)=0.\)

This is the probability that all vertices in _I<sub>s</sub>(T_) output _a_ given that \(C_{\kappa,T}(J_s)\) occurs.

Therefore, it is not possible that every vertex in _J<sub>s</sub>_ outputs \(\lambda\) if \(C_{\kappa,T}(J_s)\) occurs. Otherwise, if \(C_{\kappa,T}(J_s)\) does not occur, then, by definition, some teleportation key contained in the output of B differs from the corresponding component of \(\kappa\) in _J<sub>s</sub>_, thus not all vertices in _J<sub>s</sub>_ output \(\lambda\). Since \(\lambda\) was arbitrary, _J<sub>s</sub>_ is monochromatic with probability zero, which concludes the proof.

