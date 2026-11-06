Then, we have the following<tbc>

\(\mathbb{P}_{\mathbf{a}^{(pq)\left(L\right)}}\left(S_{\mathsf{LS},i}^{(p)}=k\right)=\sum_{y\equiv pk}\mathbb{P}_{\mathbf{a}^{(pq)\left(L\right)}}\left(S_{\mathsf{LS},pq,i}=y\right).\)

<tbc>We aim to analyze the following event<tbc>

\(\left(S_{\mathsf{LS},i}^{(p)}=k,S_{\mathsf{TS},i}^{(pq)}=l,S_{\mathsf{C},pq,i}=c\right)\)

<tbc>To do so, we split this event into the left and right sums as follows

\(\mathbb{P}_{\mathbf{a}^{(pq)}}\left(S_{\mathsf{LS},i}^{(p)}=k,S_{\mathsf{TS},i}^{(pq)}=l,S_{\mathsf{C},pq,i}=c\right)\)<br>
\(=\mathbb{P}_{\mathbf{a}^{(pq)}}\left(S_{\mathsf{LS},pq,i}\equiv kmodp,S_{\mathsf{TS},pq,i}=s=c\cdot pq+l\right),\)<br>
\(=\sum_{y\equiv pk}\mathbb{P}_{\mathbf{a}^{(pq)}}\left(S_{\mathsf{LS},pq,i}=y,S_{\mathsf{RS},pq,i}=s-y\right).\)

Now, let us define the following function<tbc>

\(f_{pq,i}(y,s):=\mathbb{P}_{\mathbf{a}^{(pq)}}\left(S_{\mathsf{LS},pq,i}=y,S_{\mathsf{RS},pq,i}=s-y\right).\)

<tbc>Since _s_ is fixed in our analysis, we will omit it and denote the above function by _f<sub>pq,i</sub>(y_). Firstly, we can observe the following

\(\sum_{y\equiv pk}f_{pq,i}(y)=\sum_{y\equiv pk}\mathbb{P}_{\mathbf{a}^{(pq)}}\left(S_{\mathsf{LS},pq,i}=y,S_{\mathsf{RS},pq,i}=s-y\right)\)<br>
\(=\mathbb{P}_{\mathbf{a}^{(pq)}}\left(S_{\mathsf{LS},i}^{(p)}=k,S_{\mathsf{TS},i}^{(pq)}=l,S_{\mathsf{C},pq,i}=c\right),\)

and

\(\sum_yf_{pq,i}(y)=\sum_y\mathbb{P}_{\mathbf{a}^{(pq)}}\left(S_{\mathsf{LS},pq,i}=y,S_{\mathsf{RS},pq,i}=s-y\right)\)<br>
\(=\mathbb{P}_{\mathbf{a}^{(pq)}}\left(S_{\mathsf{TS},pq,i}=s=c\cdot pq+l\right).\)

Now, we aim to compare the above two sums. To do so, we will prove a Gaussian smoothness result for the function _f<sub>pq,i</sub>(y_).

Let \(W_{pq}^{(L)}:=(w_{l,ip}q)/2+\mathcal{O}(pq\sqrt{w_{l,i}})\) is the central Gaussian window of the random variable _S_LS_,pq,i_. Since \(s=c\cdot pq+l\), where \(c=w_i/2+\mathcal{O}(\sqrt{w_i})\) and \(0\le l<pq\), thecrefore \(s=(w_ipq)/2+\mathcal{O}(pq\sqrt{w_i})\) and we have the following<tbc>

\(s-W_{pq}^{(L)}=(w_{r,ip}q)/2+\mathcal{O}(pq\sqrt{w_{r,i}}).\)

<tbc>Then, using Theorem 7.1 for the left and right sums, for any \(y=W_{pq}^{(L)}\) and \(y'=s-W_{pq}^{(L)}\) we have

\(\mathbb{P}_{\mathbf{a}^{(pq)}}\left(S_{\mathsf{LS},pq,i}=y\right)=\Theta\left(\frac{1}{\sigma_{pq}\sqrt{w_{l,i}}}\right),\)<br>
\(\mathbb{P}_{\mathbf{a}^{(pq)}}\left(S_{\mathsf{RS},pq,i}=y'=s-y\right)=\Theta\left(\frac{1}{\sigma_{pq}\sqrt{w_{r,i}}}\right).\)

**Claim E.0.1.** _For any_ \(y=W_{pq}^{(L)}\) _and_ \(|\Delta|\le pq\)_, we have_

\(f_{pq,i}(y+\Delta)=\Theta(f_{pq,i}(y)).\) (12)

