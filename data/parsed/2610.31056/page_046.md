where _W_<sup>(_C_)</sup> is the intersection of the Gaussian central windows of the variables _S_C_,pq,i_ and _S_C_,pq,j_. Then, using Lemma 7.1.1, we have the following<tbc>

\(\mathbb{P}_{\mathbf{a}^{(pq)}}\left(\mathsf{E}_{\mathsf{LS},\mathbf{a},i}^{(p)}\wedge\mathsf{E}_{\mathsf{LS},\mathbf{a},j}^{(p)}\wedge\mathsf{E}_{\mathsf{TS},\mathbf{a},i}^{(pq)}\wedge\mathsf{E}_{\mathsf{TS},\mathbf{a},j}^{(pq)}\wedge\mathsf{E}_{\mathsf{C},pq,\mathbf{a},i,j}\right)>\sum_{t=W^{(C)}}\left(\frac{1}{p^2q}\cdot\Theta\left(\frac{1}{\sqrt{n}}\right)\right)^2\)<br>
\(=\sum_{t=W^{(C)}}\Theta\left(\frac{1}{p^4q^2n}\right)\)<br>
\(=\Theta\left(\frac{1}{p^4q^2\sqrt{n}}\right),\)

since the window _W_<sup>(_C_)</sup> has \(\Theta(\sqrt{n})\) many points. This completes the proof of part \[1\].<tbc>

2. Firstly, we observe the following<tbc>

\(\mu_r:=\mathbb{E}\left(a_j^{(r)}\right)=\frac{r-1}{2}=\Theta(r),\)<br>
\(\sigma_r^2:=\mathsf{Var}\left(a_j^{(r)}\right)=\Theta(r^2).\)

Similar to the previous part, since the vectors **u**_<sub>i</sub>_ and **u**_<sub>j</sub>_ do not overlap, we have the following<tbc>

\(\mathbb{P}_{\mathbf{a}^{(r)}}\left(S_{\mathsf{TS},r,i}=S_{\mathsf{TS},r,j}\right)\)<br>
\(=\sum_t\mathbb{P}_{\mathbf{a}^{(r)}}\left(S_{\mathsf{TS},r,i}=t\right)\cdot\mathbb{P}_{\mathbf{a}^{(r)}}\left(S_{\mathsf{TS},r,j}=t\right).\)

Let \(W_i^{(r)}:=w_i\mu_r+\mathcal{O}(\sigma_r\sqrt{w_i})\) and \(W_j^{(r)}:=w_j\mu_r+\mathcal{O}(\sigma_r\sqrt{w_j})\) be the Gaussian central windows of the random variables _S_TS_,r,i_ and _S_TS_,r,j_ respectively. To capture most of the mass, we take the intersection of the two windows. Let \(W^{(r)}:=W_i^{(r)}\cap W_j^{(r)}\), then we have the following<tbc>

\(\mathbb{P}_{\mathbf{a}^{(r)}}\left(S_{\mathsf{TS},r,i}=S_{\mathsf{TS},r,j}\right)\)<br>
\(=\sum_t\mathbb{P}_{\mathbf{a}^{(r)}}\left(S_{\mathsf{TS},r,i}=t\right)\cdot\mathbb{P}_{\mathbf{a}^{(r)}}\left(S_{\mathsf{TS},r,j}=t\right)\)<br>
\(>\sum_{t\in W^{(r)}}\mathbb{P}_{\mathbf{a}^{(r)}}\left(S_{\mathsf{TS},r,i}=t\right)\cdot\mathbb{P}_{\mathbf{a}^{(r)}}\left(S_{\mathsf{TS},r,j}=t\right).\)

Now, using Theorem 7.1 to compute the distributions of the random variables _S_TS_,r,i_ and _S_TS_,r,j_, we have the following<tbc>

\(\mathbb{P}_{\mathbf{a}^{(r)}}\left(S_{\mathsf{TS},r,i}=S_{\mathsf{TS},r,j}\right)=\sum_{t\in W^{(r)}}\Theta\left(\frac{1}{\sigma_r^2\sqrt{w_iw_j}}\right).\)

And, since there are \(\Theta(\sigma_r\sqrt{n})\) many points in the window _W_<sup>(_r_)</sup> and \(w_i,w_j=\Theta(n)\), we have the desired result. This completes the proof of part \[2\].

