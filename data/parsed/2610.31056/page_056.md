Since _s<sub>j</sub>_ is in the central window, using Corollary 1 we get the desired result as follows

\(\mathbb{P}_{\mathbf{a}^{(pq)}}\left(S_{\mathsf{C},pq,i}=c\right)\)<br>
\(=\sum_{j=0}^{pq-1}\mathbb{P}_{\mathbf{a}^{(pq)}}\left(S_{\mathsf{TS},pq,i}=c\cdot pq+j=s_j\right),\)<br>
\(=\sum_{j=0}^{pq-1}\Theta\left(\frac{1}{\sigma_{pq}\sqrt{w_i}}\right),\)<br>
\(=pq\cdot\Theta\left(\frac{1}{\sigma_{pq}\sqrt{w_i}}\right),\)<br>
\(=\Theta\left(\frac{1}{\sqrt{w_i}}\right).\)

This completes the proof of Property (1). For Property (2), we can observe that the following two events are the same<tbc>

\(\left(S_{\mathsf{TS},i}^{(pq)}=l,S_{\mathsf{C},pq,i}=c\right),\)

<tbc>and<tbc>

\(\left(S_{\mathsf{TS},pq,i}=s=c\cdot pq+l\right).\)

<tbc>Hence, we have

\(\mathbb{P}_{\mathbf{a}^{(pq)}}\left(S_{\mathsf{TS},pq,i}=c\cdot pq+l\right)\)<br>
\(=\mathbb{P}_{\mathbf{a}^{(pq)}}\left(S_{\mathsf{TS},i}^{(pq)}=l,S_{\mathsf{C},pq,i}=c\right),\)<br>
\(=\mathbb{P}_{\mathbf{a}^{(pq)}}\left(S_{\mathsf{TS},i}^{(pq)}=l\big|S_{\mathsf{C},pq,i}=c\right)\cdot\mathbb{P}_{\mathbf{a}^{(pq)}}\left(S_{\mathsf{C},pq,i}=c\right).\)

Using Corollary 1 and part \[1\] of this lemma in the above equation, we get the desired result

\(\mathbb{P}_{\mathbf{a}^{(pq)}}\left(S_{\mathsf{TS},i}^{(pq)}=l\big|S_{\mathsf{C},pq,i}=c\right)\)<br>
\(=\frac{\mathbb{P}_{\mathbf{a}^{(pq)}}\left(S_{\mathsf{TS},pq,i}=c\cdot pq+l\right)}{\mathbb{P}_{\mathbf{a}^{(pq)}}\left(S_{\mathsf{C},pq,i}=c\right)},\)<br>
\(=\frac{\Theta\left(\frac{1}{pq\sqrt{w_i}}\right)}{\Theta\left(\frac{1}{\sqrt{w_i}}\right)},\)<br>
\(=\Theta\left(\frac{1}{pq}\right).\)

It remains to prove Property (3). First, we will split the total sum into the left and right parts

\(S_{\mathsf{TS},pq,i}=S_{\mathsf{LS},pq,i}+S_{\mathsf{RS},pq,i},\)<br>
\(=\mathbf{a}^{(pq)\left(L\right)}\cdot\mathbf{u}_i^{(L)}+\mathbf{a}^{(pq)\left(R\right)}\cdot\mathbf{u}_i^{(R)},\)

and let _w<sub>l,i</sub>_ and _w<sub>r,i</sub>_ be the Hamming weights of the vectors \(\mathbf{u}_i^{(L)}\) and \(\mathbf{u}_i^{(R)}\) respectively. Then, we have _w<sub>i</sub>=w<sub>l,i</sub>+w<sub>r,i</sub>_. Now, we divide the left sum _S_<sub>LS,_pq,i_</sub> by _p_<tbc>

\(S_{\mathsf{LS},pq,i}=Q_{\mathsf{LS},i}^{(p)}\cdot p+S_{\mathsf{LS},i}^{(p)}.\)

