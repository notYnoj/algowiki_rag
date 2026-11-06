<tbc>**Lemma 5.1.** _For all_ \(n\ge 4\), \(|u\rangle\in H\backslash\{0\}\)_, there exists a conjugate-linear map_6\(L:H\rightarrow\mathrm{Mat}_{d^2}(\mathbb{C})\) _and a Hilbert space_ \(V\subseteq\mathrm{Mat}_d(\mathbb{C})\) _with_ \(0<\mathrm{dim}(V)\le d\) _such that_<tbc>

\(\mathrm{im}(L)=(V\otimes\mathrm{Mat}_d(\mathbb{C}))P\text{\textit{where}}\forall\alpha,\beta\in\mathbb{C}^d\text{\textit{we have}}P(\alpha\otimes\beta)=\beta\otimes\alpha,\)

<tbc>_and for all_ \(v_1,\dots,v_n\in H\)_, we have that_<tbc>

\(\langle v_1,v_2,\dots,v_n|C|u,\dots,u\rangle=\mathrm{Tr}\left(\prod_{p=1}^nL(v_p)\right).\)

<tbc>_Proof._ For clarity, let L, M and R be three _d_ dimensional Hilbert spaces and \(H=\mathsf{L}\otimes\mathsf{M}\otimes\mathsf{R}\). Using the Schmidt decomposition (see, e.g., \[Wat18, Eq. 1.164\]) of \(|u\rangle\) w.r.t. M and \(\mathsf{L}\otimes\mathsf{R}\), we get an _orthonormal_ family \(\{m_1,\dots,m_r\}\subseteq\mathsf{M}\) and an _orthogonal_ \(\{T_1,\dots,T_r\}\subseteq\mathsf{L}\otimes\mathsf{R}\) for which<tbc>

\(|u\rangle=\sum_{i=1}^r|m_i\rangle_\mathsf{M}\otimes|T_i\rangle_{\mathsf{L},\mathsf{R}}.\)

<tbc>Define _V_=span{_T_<sub>1</sub>_,...,T<sub>r</sub>_}, which we see as a subspace of Mat_<sub>d</sub>_(C) of dimension at most \(r\le d\). For each \(i\in[r]\) and vector \(|v\rangle\in H\), define \(B_i(v)\in\mathrm{Mat}_d(\mathbb{C})\) as \((B_i(v))_{a,b}=\langle v|a,i,b\rangle\), where \(m_i=|i\rangle_\mathsf{M}\) for succintness. Now we can define the map _L_ as

\(L(v)=\left(\sum_{i=1}^rT_i\otimes B_i(v)\right)P,\)

which is clearly conjugate-linear and \(\mathrm{im}(L)\subseteq(V\otimes\mathrm{Mat}_d(\mathbb{C}))P\). Conversely, the orthonormality of the _m<sub>i</sub>_ gives that _B<sub>i</sub>(v_)=_E<sub>j,k</sub>_ when _v_=|_j,i,k_〉. Since the _T<sub>i</sub>_ span _V_ and the _E<sub>j,k</sub>_ span Mat_<sub>d</sub>_(C), we get that \(\mathrm{im}(L)=(V\otimes\mathrm{Mat}_d(\mathbb{C}))P\). So what remains to prove is the trace property.

First, rewrite \(|u\rangle=\sum_i|m_i\rangle_\mathsf{M}\otimes|T_i\rangle_{\mathsf{L},\mathsf{R}}\) as an element of \(\mathsf{L}\otimes\mathsf{M}\otimes\mathsf{R}\) as follows<tbc>

\(|u\rangle=\sum_{i=1}^r\sum_{j,k\in[d]}(T_i)_{j,k}|j,i,k\rangle_{\mathsf{L},\mathsf{M},\mathsf{R}}.\)

<tbc>Therefore, if we have _p_ copies of this state |_u_〉 in registers L(_p),_M(_p),_R(_p_) (using cyclic indices _k_<sub>0</sub>=_k<sub>n</sub>_ and _j_<sub>_n_+1</sub>=_j_<sub>1</sub>), after the communication round the global state can be written as

\(C|u,\dots,u\rangle=C\left(\sum_{i_1,\dots,i_n\in[r]}\sum_{j_1,\dots,j_n\in[d]}\sum_{k_1,\dots,k_n\in[d]}\left(\prod_{p=1}^n(T_{i_p})_{j_p,k_p}\right)\otimes_{p=1}^n|j_p,i_p,k_p\rangle_{\mathsf{L}(p),\mathsf{M}(p),\mathsf{R}(p)}\right)\)<br>
\(=\sum_{i_1,\dots,i_n\in[r]}\sum_{j_1,\dots,j_n\in[d]}\sum_{k_1,\dots,k_n\in[d]}\left(\prod_{p=1}^n(T_{i_p})_{j_p,k_p}\right)\otimes_{p=1}^n|k_{p-1},i_p,j_{p+1}\rangle_{\mathsf{L}(p),\mathsf{M}(p),\mathsf{R}(p)}\)

Consider any vectors \(|v_1\rangle,\dots,|v_n\rangle\in H\) and note that \(\langle v_1,v_2,\dots,v_n|C|u,u,\dots,u\rangle\) can be written as

\(\sum_{i_1,\dots,i_n\in[r]}\sum_{j_1,\dots,j_n\in[d]}\sum_{k_1,\dots,k_n\in[d]}\left(\prod_{p=1}^n(T_{i_p})_{j_p,k_p}\right)\otimes_{p=1}^n\langle v_p|k_{p-1},i_p,j_{p+1}\rangle_{\mathsf{L}(p),\mathsf{M}(p),\mathsf{R}(p)}\)<br>
\(=\sum_{i_1,\dots,i_n\in[r]}\sum_{j_1,\dots,j_n\in[d]}\sum_{k_1,\dots,k_n\in[d]}\prod_{p=1}^n(T_{i_p})_{j_p,k_p}(B_{i_p}(v_p))_{k_{p-1},j_{p+1}}\)

6a conjugate-linear map \(f:U\rightarrow V\) between complex vector spaces is additive, i.e., _f(x+y_)=_f(x_)+_f(y_) for all vectors \(x,y\in U\), but conjugates the scalar factors, i.e., \(f(\lambda x)=\overline{\lambda}f(x)\) for all \(x\in U\) and \(\lambda\in\mathbb{C}\)

