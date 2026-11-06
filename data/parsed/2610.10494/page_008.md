Lemma 5.1 give \(P'_{ij}(t)\ge L_i\) and \(P_{ij}(t)\le L_i(t+c_{ij})\). Homogeneity gives _g(r,s_)=_rP<sub>ij</sub>(s/r)<sup>p<sub>i</sub></sup>_, so, also interchanging the inputs,

\(\frac{\partial_sg(r,s)}{g(r,s)}=\frac{p_i}{r}\frac{P'_{ij}(s/r)}{P_{ij}(s/r)}\ge\frac{p_i}{s+c_{ij}r},\)<br>
\(\frac{\partial_rg(r,s)}{g(r,s)}=\frac{p_j}{s}\frac{P'_{ji}(r/s)}{P_{ji}(r/s)}\ge\frac{p_j}{r+c_{ji}s}.\)

Differentiating _g(tr,ts_)=_tg(r,s_) at _t_=1 gives<tbc>

\(r\frac{\partial_rg(r,s)}{g(r,s)}+s\frac{\partial_sg(r,s)}{g(r,s)}=1.\)

<tbc>Substituting the two lower bounds yields

\(1\ge\frac{p_is}{s+c_{ij}r}+\frac{p_jr}{r+c_{ji}s}(r,s>0).\) (23)

Appendix G obtains the same inequality using finite increments, without assuming differentiability. Clearing denominators gives a quadratic in _r/s_. Its nonnegativity for every positive ratio implies

\(\sqrt{c_{ij}c_{ji}}\ge\left(\sqrt{p_ip_j}-\sqrt{(1-p_i)(1-p_j)}\right)_+,\) (24)

where (_z_)<sub>+</sub>=max{_z,_0}.

For nonnegative _x_<sub>1</sub>_,x_<sub>2</sub>_,x_<sub>3</sub>, AM-GM and (21) give

\(\sum_{i<j}2\sqrt{c_{ij}c_{ji}}x_ix_j\le\sum_{i<j}(c_{ij}x_i^2+c_{ji}x_j^2)\le\sum_ix_i^2.\) (25)

Put \(\theta_i=arccos\sqrt{p_i}\) and suppose \(S=\theta_1+\theta_2+\theta_3<\pi/2\). Take \(x_i=cos\theta_i>0\). Then (24) gives \(\sqrt{c_{ij}c_{ji}}\ge cos(\theta_i+\theta_j)\). Using the product-to-sum identities, we get

\(cos(\theta_i+\theta_j)x_j+cos(\theta_i+\theta_k)x_k=cos\theta_i+\frac{cos(\theta_i+2\theta_j)+cos(\theta_i+2\theta_k)}{2}\)<br>
\(=x_i+cosScos(\theta_j-\theta_k)>x_i.\)

The extra term is positive: cos_S\>_0 and \(cos(\theta_j-\theta_k)>0\), since \(|\theta_j-\theta_k|\le S<\pi/2\). Multiplying by _x<sub>i</sub>_ and summing contradicts (25). Appendix G contains the complete proof, including the quadratic calculation.

## 6. From character bounds to running times

We can now turn the parameter constraint into matrix-multiplication algorithms. The other ingredients are the matrix-tensor formula (11) and Strassen’s spectral theorem (Theorem 3.2). For a given matrix shape, we bound a weighted sum of the three parameters for every character; the theorem then bounds asymptotic rank. We first show how this rank bound gives a running-time bound, then apply the angular constraint from Proposition 5.2 to obtain the general-shape bound and the rectangular curve.

**Lemma 6.1** (Character bounds give algorithms)**.** _Fix_ \(\mathbf{h}=(h_X,h_Y,h_Z)\ge 0\)_. If the dot- product parameters of every tensor character satisfy_ \(\sum_ih_ip_i\le E\)_, then_ \(\omega(h_Y,h_Z,h_X)\le E\).

