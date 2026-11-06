We can apply this theorem to both _V<sub>n</sub>_ and _U<sub>n</sub>_ with _m_=2_n_, _c_=1 and well-chosen values of \(\varepsilon\) that are going to be useful in what follows.

**Lemma 2.** _For all n,_<tbc>

\(\mathbb{P}\left[V_n\le\mathbb{E}\left[V_n\right]+\sqrt{n\mathrm{log}2}\right]\ge\frac{1}{2},\) (3)

<tbc>_and_<tbc>

\(\mathbb{P}\left[U_n\ge\mathbb{E}\left[U_n\right]+\sqrt{n\mathrm{log}(4(n+1)^2)}\right]\le\frac{1}{4(n+1)^2}.\) (4)

<tbc>**Lemma 3.** _For all k,_<tbc>

\(\alpha_k=2\alpha'_k.\)

<tbc>_Proof._ By definition, for all _n_,

\(\frac{\mathbb{E}\left[V_n\right]}{n}\le\frac{\mathbb{E}\left[U_{\left[1,\lceil n/2\rceil\right],\left[1,\lceil n/2\rceil\right]}\right]}{n}\le\frac{\mathbb{E}\left[U_{\left[1,\lceil n/2\rceil\right],\left[1,\lceil n/2\rceil\right]}\right]}{\lceil n/2\rceil}\cdot\frac{\lceil n/2\rceil}{n}.\)

The limit of the right-hand side as _n_ goes to infinity is \(\frac{\alpha_k}{2}\) which implies \(\alpha'_k\le\frac{\alpha_k}{2}\) .

We now focus on proving \(\alpha'_k\ge\frac{\alpha_k}{2}\) . We have from (3),<tbc>

\(\frac{1}{2}\le\mathbb{P}\left[V_n\le\mathbb{E}\left[V_n\right]+\sqrt{n\mathrm{log}2}\right]\le\sum_{i=1}^n\mathbb{P}\left[U_{\left[1,i\right],\left[1,n-i\right]}\le\mathbb{E}\left[V_n\right]+\sqrt{n\mathrm{log}2}\right].\)

<tbc>Hence, there exists _i_ such that<tbc>

\(\mathbb{P}\left[U_{\left[1,i\right],\left[1,n-i\right]}\le\mathbb{E}\left[V_n\right]+\sqrt{n\mathrm{log}2}\right]\ge\frac{1}{2n}.\)

<tbc>Since _U_<sub>\[_i_+1_,n_\],\[_n-i_+1_,n_\]</sub> has the same distribution as _U_<sub>\[1_,i_\],\[1_,n-i_\]</sub>, and they are independent of each others, we have

\(\frac{1}{4n^2}\le\mathbb{P}\left[U_{\left[1,i\right],\left[1,n-i\right]}\le\mathbb{E}\left[V_n\right]+\sqrt{n\mathrm{log}2}\right]\cdot\mathbb{P}\left[U_{\left[i+1,n\right],\left[n-i+1,n\right]}\le\mathbb{E}\left[V_n\right]+\sqrt{n\mathrm{log}2}\right]\)<br>
\(=\mathbb{P}\left[U_{\left[1,i\right],\left[1,n-i\right]}\le\mathbb{E}\left[V_n\right]+\sqrt{n\mathrm{log}2}\text{and}U_{\left[i+1,n\right],\left[n-i+1,n\right]}\le\mathbb{E}\left[V_n\right]+\sqrt{n\mathrm{log}2}\right]\)<br>
\(\le\mathbb{P}\left[U_{\left[1,n\right],\left[1,n\right]}\le 2\mathbb{E}\left[V_n\right]+2\sqrt{n\mathrm{log}2}\right]\)

From (4),<tbc>

\(\mathbb{P}\left[U_n\le\mathbb{E}\left[U_n\right]-\sqrt{n\mathrm{log}(4(n+1)^2)}\right]\le\frac{1}{4(n+1)^2}<\mathbb{P}\left[U_n\le 2\mathbb{E}\left[V_n\right]+2\sqrt{n\mathrm{log}2}\right],\)

<tbc>which implies

\(\mathbb{E}\left[U_n\right]-\sqrt{n\mathrm{log}(4(n+1)^2)}\le 2\mathbb{E}\left[V_n\right]+2\sqrt{n\mathrm{log}2}.\)

This implies \(\mathbb{E}\left[U_n\right]\le 2\mathbb{E}\left[V_n\right]+o(n)\). Taking the limit as _n_ goes to infinity, we get \(\alpha_k\le 2\alpha'_k\) which concludes the proof.

