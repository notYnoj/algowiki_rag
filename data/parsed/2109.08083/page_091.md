<tbc>Also as in the proof of Corollary 6.4, \(e(H')\le De(H)\le Dexp(\Delta^{\epsilon^2/4})\le exp(D^{\epsilon^2/4})\). In addition, we have that<tbc>

\(\delta(H')\ge min_{v\in V(H)}\sum_{e\unknown v}\lfloor Dw(e)\rfloor\ge(1-\Delta^{-1})D\delta_w(H)\ge D^{1-\psi/2}.\)

<tbc>Now for a fixed \(l\in[L]\) and function _p<sub>l</sub>_ we define weight function \(p'_l:\genfrac(){pt}{2}{V(H^\prime)}{l}\rightarrow\mathbb{R}_{\ge 0}\) via<tbc>

\(p'_l(\bar{v})=p_l(\bar{v})\)

<tbc>for every \(\bar{v}\in\genfrac(){pt}{2}{V(H^\prime)}{l}\). Then<tbc>

\(\sum_{\bar{v}\in\genfrac(){pt}{2}{V(H^\prime)}{l}}p'_l(\bar{v})\ge 2r^lD^\eta max_{v\in V(H^\prime)}p'_l(\{v\}).\)

<tbc>It follows from Theorem 6.6 with parameters \(\eta/2,r,L\), and assuming \(\Delta\) sufficiently large, that with high probability _M_ in \(H'\) satisfies<tbc>

\(p'_l(M)=(1\pm\frac{2D^{-\epsilon/2}}{3})\sum_{\bar{v}\in\genfrac(){pt}{2}{V(H^\prime)}{l}}p'_l(\bar{v})\prod_{v\in\bar{v}}\frac{d_{H^\prime}(v)}{D}.\)

<tbc>Furthermore, _M_ is a distribution on matchings in (_H,w_) and, by construction, \(\frac{d_{H^\prime}(v)}{D}=(1\pm\Delta^{-1})d_w(v)\). Hence

\(p_l(M)=(1\pm\Delta^{-\epsilon})\sum_{\bar{v}\in\genfrac(){pt}{2}{V(H)}{l}}p_l(\bar{v})\prod_{v\in\bar{v}}d_w(v).\)

Taking a union bound yields that there exists a matching _M_ in _H_ such that the conclusion holds simultaneously for polynomially many \(q\in\mathcal{Q}\) and \(p_l\in\mathcal{P}_l\) for each \(l\in[L]\), proving the theorem. □

## 6.2. The weight shuffle

In this section we list some key properties of (_H_<sub>1</sub>_,w_<sub>1</sub>) and describe the process to reach (_H_<sub>1∗</sub>_,w_<sub>1∗</sub>), as well as listing out the key properties of (_H_<sub>1∗</sub>_,w_<sub>1∗</sub>) resulting from this process. From (_H_<sub>1</sub>_,w_<sub>1</sub>) as given in Theorem 6.1, we perform the weight shuffle as described in Section 6.1.1. We give more details of this process in the following algorithm.

Algorithm 6.9.<br>
_i_=1, _w_<sub>(1_,c<sub>g</sub>_)</sub>:=_w_<sub>1</sub>

**Initialise:** _i_=1, _w_<sub>(1_,c<sub>g</sub>_)</sub>:=_w_<sub>1</sub>, where _w_<sub>(1_,c<sub>g</sub>-i_+1)</sub> is an almost-perfect fractional matching for _H_<sub>1</sub> such that _w_<sub>(1_,c<sub>g</sub>-i_+1)</sub>(_e_)=0 for all (_c<sub>g</sub>-j_+1)-bad edges and all _j\<i_.

**Step 1:** Find all (_c<sub>g</sub>-i_+1)-bad edges with weight \(w_{(1,c_g-i+1)}\neq 0\). For each \(z\in\mathcal{Z}_{c_g-i+1,H_1}^2\), transfer the weight \(w(z):=\frac{1}{p_\text{gr}^{15}j_{c_g-i+1}t_1^2}\), from the edges all with the same sign as any (_c<sub>g</sub>-i_+1)-bad edge to edges with the opposite sign.

**Step 2:** For each (_c<sub>g</sub>-i_+1)-bad edge _e_ and \(z_e\in\mathcal{Z}_{c_g-i+1,e,H_1}^+(\text{bad})\backslash Z_{c_g-i+1,H_1}^2\), define

\(w(z_e):=\frac{w_{(1,c_g-i+1)}(e)-\sum_{z\in\mathcal{Z}_{c_g-i+1,e,H_1}^2}w(z)}{|\mathcal{Z}_{c_g-i+1,e,H_1}^+(\text{bad})\backslash\mathcal{Z}_{c_g-i+1,H_1}^2|},\)

