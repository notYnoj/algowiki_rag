• \(S_{\mathsf{C},pq,i}=\left\lfloor\frac{\mathbf{a}^{(pq)}\cdot\mathbf{u}_i}{pq}\right\rfloor=c\).

for some \(k\in[0,p)\), \(l\in[0,pq)\), and _c_=\[0_,w<sub>i</sub>_). The following lemma provides a detailed account of the interdependencies among these three events.

**Lemma 7.1.1.** _Let n, p, q,_ **a**<sup>(_pq_)</sup> _be the same as defined earlier. Fix_ \(\mathbf{u}_i\in\mathsf{A}\)_, let w<sub>i</sub>,w<sub>l,i</sub>, and w<sub>r,i</sub> denote the Hamming weights of the vectors_ \(\mathbf{u}_i,\mathbf{u}_i^{(L)}\)_, and_ \(\mathbf{u}_i^{(R)}\) _respectively. Assume that_ \(\alpha n<w_i<(1-\alpha)n\) _and_ \(\alpha n/2<w_{l,i},w_{r,i}<(1-\alpha)n/2\) _where_ \(1/8\le\alpha<1/4\) _is some constant. Then_

1. _For all_ \(c=w_i/2+\mathcal{O}(\sqrt{w_i})\)_, we have_<tbc>

<tbc>\(\mathbb{P}_{\mathbf{a}^{(pq)}}\left(S_{\mathsf{C},pq,i}=c\right)=\Theta\left(\frac{1}{\sqrt{w_i}}\right).\)<tbc>

<tbc>_2._ _For all_ \(l\in[0,pq)\) _and_ \(c=w_i/2+\Theta(\sqrt{w_i})\)_, we have_<tbc>

<tbc>\(\mathbb{P}_{\mathbf{a}^{(pq)}}\left(S_{\mathsf{TS},i}^{(pq)}=l\middle|S_{\mathsf{C},pq,i}=c\right)=\Theta\left(\frac{1}{pq}\right).\)<tbc>

<tbc>_3._ _For all_ \(k\in[0,p)\), \(l\in[0,pq)\)_, and_ \(c=w_i/2+\Theta(\sqrt{w_i})\)_, we have_

\(\mathbb{P}_{\mathbf{a}^{(pq)}}\left(S_{\mathsf{LS},i}^{(p)}=k,S_{\mathsf{TS},i}^{(pq)}=l,S_{\mathsf{C},pq,i}=c\right)\)<br>
\(=\Theta\left(\frac{1}{p^2q\sqrt{w_i}}\right).\)

_Proof._ Leveraging the smoothness of the sum distributions, we first show that the carry bits converge in distribution to a discrete normal distribution with mean _w<sub>i</sub>/_2 and variance \(\Theta(w_i)\), and henceforth we prove that the total sum modulo _pq_ and the left sum modulo _p_ condition on the carry bits also converge to the uniform distribution, as _n_ tends to infinity. Finally, we show that the following three events are asymptotically independent

• \(\sum_{j=1}^{n/2}a_j^{(pq)}\cdot u_{ij}\equiv_pa\),<tbc>

• \(\mathbf{a}^{(pq)}\cdot\mathbf{u}_i\equiv_pq\) _b,_<tbc>

• \(\left\lfloor\frac{\mathbf{a}^{(pq)}\cdot\mathbf{u}_i}{pq}\right\rfloor=c\).

Refer to Section E.1 for a detailed proof.

## 7.3.1 Proof of Proposition 7.0.1

1. Since **u**_<sub>i</sub>_ and **u**_<sub>j</sub>_ do not overlap, we can split the independent events as follows

\(\mathbb{P}_{\mathbf{a}^{(pq)}}\left(\mathsf{E}_{\mathsf{LS},\mathbf{a},i}^{(p)}\wedge\mathsf{E}_{\mathsf{LS},\mathbf{a},j}^{(p)}\wedge\mathsf{E}_{\mathsf{TS},\mathbf{a},i}^{(pq)}\wedge\mathsf{E}_{\mathsf{TS},\mathbf{a},j}^{(pq)}\wedge\mathsf{E}_{\mathsf{C},pq,\mathbf{a},i,j}\right)\)<br>
\(=\mathbb{P}_{\mathbf{a}^{(pq)}}\left(\mathsf{E}_{\mathsf{LS},\mathbf{a},i}^{(p)}\wedge\mathsf{E}_{\mathsf{LS},\mathbf{a},j}^{(p)}\wedge\mathsf{E}_{\mathsf{TS},\mathbf{a},i}^{(pq)}\wedge\mathsf{E}_{\mathsf{TS},\mathbf{a},j}^{(pq)}\wedge(S_{\mathsf{C},pq,i}=S_{\mathsf{C},pq,j})\right)\)<br>
\(=\sum_c\mathbb{P}_{\mathbf{a}^{(pq)}}\left(\mathsf{E}_{\mathsf{LS},\mathbf{a},i}^{(p)}\wedge\mathsf{E}_{\mathsf{LS},\mathbf{a},j}^{(p)}\wedge\mathsf{E}_{\mathsf{TS},\mathbf{a},i}^{(pq)}\wedge\mathsf{E}_{\mathsf{TS},\mathbf{a},j}^{(pq)}\wedge(S_{\mathsf{C},pq,i}=S_{\mathsf{C},pq,j}=c)\right)\)<br>
\(=\sum_c\mathbb{P}_{\mathbf{a}^{(pq)}}\left(S_{\mathsf{LS},i}^{(p)}=s_0,S_{\mathsf{TS},i}^{(pq)}=\beta,S_{\mathsf{C},pq,i}=c\right)\cdot\mathbb{P}_{\mathbf{a}^{(pq)}}\left(S_{\mathsf{LS},j}^{(p)}=s_0,S_{\mathsf{TS},j}^{(pq)}=\beta,S_{\mathsf{C},pq,j}=c\right)\)<br>
\(>\sum_{c=W^{(C)}}\mathbb{P}_{\mathbf{a}^{(pq)}}\left(S_{\mathsf{LS},i}^{(p)}=s_0,S_{\mathsf{TS},i}^{(pq)}=\beta,S_{\mathsf{C},pq,i}=c\right)\cdot\mathbb{P}_{\mathbf{a}^{(pq)}}\left(S_{\mathsf{LS},j}^{(p)}=s_0,S_{\mathsf{TS},j}^{(pq)}=\beta,S_{\mathsf{C},pq,j}=c\right),\)

