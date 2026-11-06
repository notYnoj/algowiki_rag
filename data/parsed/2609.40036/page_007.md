## 2 Decoded Quantum Interferometry with imperfect decoding

Let \(B\in\unknown_q^{m\times n}\) have rows **b**_<sub>i</sub>_, and fix target sets **C**=(_C_<sub>1</sub>_,...,C<sub>m</sub>_) with \(C_i\subseteq\unknown_q\) and |_C<sub>i</sub>_|=_r_, where 0_\<r\<q_. The Max-LINSAT objective is<tbc>

\(s(\mathbf{x}):=\sum_{i=1}^m\unknown_{C_i}(\mathbf{b}_i\cdot\mathbf{x}),\mathbf{x}\in\unknown_q^n.\) (5)

<tbc>Writing \(\rho=r/q\), define the centered, normalized target indicators<tbc>

\(g_i(x):=\frac{\unknown_{C_i}(x)-\rho}{\sqrt{q\rho(1-\rho)}}.\) (6)

<tbc>For \(q=\ell_0^\nu\) with \(\ell_0\) prime, use the additive character<tbc>

\(\chi_q(t):=\mathrm{exp}\left(\frac{2\pi i}{\ell_0}\mathrm{Tr}_{\unknown_q/\unknown_{\ell_0}}(t)\right),\mathrm{Tr}_{\unknown_q/\unknown_{\ell_0}}(t):=\sum_{j=0}^{\nu-1}t^{\ell_0^j}.\) (7)

<tbc>It satisfies \(\chi_q(s+t)=\chi_q(s)\chi_q(t)\), \(\overline{\chi_q(t)}=\chi_q(-t)\), and<tbc>

\(\sum_{\mathbf{x}\in\unknown_q^d}\chi_q(\mathbf{a}\cdot\mathbf{x})=q^d\unknown_\mathbf{0}(\mathbf{a}).\) (8)

<tbc>Thus the Fourier transform with entries \((\mathsf{F}_q)_{a,x}=\chi_q(ax)/\sqrt{q}\) is unitary. Set<tbc>

\(\widetilde{g}_i(a):=\frac{1}{\sqrt{q}}\sum_{x\in\unknown_q}\chi_q(ax)g_i(x),\) (9)

<tbc>so that \(\widetilde{g}_i(0)=0\) and \(\sum_a|\widetilde{g}_i(a)|^2=1\). For an error word \(\mathbf{y}\in\unknown_q^m\), define

\(\widetilde{g}_\mathbf{C}(\mathbf{y}):=\prod_{i:y_i\neq 0}\widetilde{g}_i(y_i),\) (10)

with the empty product equal to one.

DQI prepares an error state specified by a normalized amplitude vector \(\mathbf{w}=(w_0,\dots,w_m)\in\unknown^{m+1}\):<tbc>

\(|\Gamma\rangle:=\sum_{\mathbf{y}\in\unknown_q^m}\phi_\mathbf{C}(\mathbf{y})|\mathbf{y}\rangle,\phi_\mathbf{C}(\mathbf{y}):=\frac{w_{|\mathbf{y}|}}{\sqrt{\genfrac(){pt}{2}{m}{|\mathbf{y}|}}}\widetilde{g}_\mathbf{C}(\mathbf{y}).\) (11)

<tbc>Since<tbc>

\(\sum_{|\mathbf{y}|=k}|\widetilde{g}_\mathbf{C}(\mathbf{y})|^2=\genfrac(){pt}{2}{m}{k},\) (12)

<tbc>this state is normalized and assigns probability |_w<sub>k</sub>_|<sup>2</sup> to errors of weight _k_. For state preparation, let \(|D_k^m\rangle\propto\sum_{\mathbf{z}\in\{0,1\}^m:|\mathbf{z}|=k}|\mathbf{z}\rangle\) be the normalized Dicke state. Applying \(U=\otimes_iU_i\) to \(|\mathbf{w}\rangle:=\sum_kw_k|D_k^m\rangle\) gives \(|\Gamma\rangle\), where _U<sub>i</sub>_ are the isometries into \(\unknown^q\) given by<tbc>

\(U_i|0\rangle=|0\rangle,U_i|1\rangle=\sum_{a\in\unknown_q^\times}\widetilde{g}_i(a)|a\rangle.\) (13)

