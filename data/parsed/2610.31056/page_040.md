\(\mathsf{F}_{\mathsf{OB},pq,\mathbf{a},i,j}:\left\lfloor\frac{\mathbf{u}_{ij}^{(10)}\cdot\mathbf{a}^{(pq)}}{pq}\right\rfloor=\left\lfloor\frac{\mathbf{u}_{ij}^{(01)}\cdot\mathbf{a}^{(pq)}}{pq}\right\rfloor\)<br>
\(\mathsf{F}_{\mathsf{TS},r,\mathbf{a},i,j}:\mathbf{u}_{ij}^{(10)}\cdot\mathbf{a}^{(r)}=\mathbf{u}_{ij}^{(01)}\cdot\mathbf{a}^{(r)}.\)

**Claim 7.0.1.** _For any_ \(1\le i<j\le N\)_, the following holds_<tbc>

\(\mathcal{C}_{ij}^{(int)}\ge\mathcal{D}_{ij}^{(int)}.\)

<tbc>_Proof:_ Let \(\mathcal{D}_{ij}^{(int)}=1\). Then the events \(\mathsf{F}_{\mathsf{LS},\mathbf{a},10}^{(p)},\mathsf{F}_{\mathsf{LS},\mathbf{a},01}^{(p)},\mathsf{F}_{\mathsf{TS},\mathbf{a},10}^{(p)}\), and \(\mathsf{F}_{\mathsf{TS},\mathbf{a},01}^{(p)}\) trivially implies the survival of the vectors **u**_<sub>i</sub>_ and **u**_<sub>j</sub>_. And, the event F<sub>TS_,r,_**a**_,i,j_</sub> implies collision over the remaining _r_ bits. Since F<sub>OB_,pq,_**a**_,i,j_</sub>=1, and \(\mathbf{u}_{ij}^{(01)}\cdot\mathbf{a}^{(pq)}\equiv_{pq}\mathbf{u}_{ij}^{(10)}\cdot\mathbf{a}^{(pq)}\) we have the following<tbc>

\(\mathbf{u}_{ij}^{(01)}\cdot\mathbf{a}^{(pq)}=\mathbf{u}_{ij}^{(10)}\cdot\mathbf{a}^{(pq)}.\)

<tbc>This gives us the following equality over the carries too

\(\left\lfloor\frac{\mathbf{u}_i\cdot\mathbf{a}^{(pq)}}{pq}\right\rfloor=\left\lfloor\frac{\mathbf{u}_{ij}^{(10)}\cdot\mathbf{a}^{(pq)}+\mathbf{u}_{ij}^{(11)}\cdot\mathbf{a}^{(pq)}}{pq}\right\rfloor\)<br>
\(=\left\lfloor\frac{\mathbf{u}_{ij}^{(01)}\cdot\mathbf{a}^{(pq)}+\mathbf{u}_{ij}^{(11)}\cdot\mathbf{a}^{(pq)}}{pq}\right\rfloor\)<br>
\(=\left\lfloor\frac{\mathbf{u}_j\cdot\mathbf{a}^{(pq)}}{pq}\right\rfloor.\)

This implies that **u**_<sub>i</sub>_ and **u**_<sub>j</sub>_ collides over the carries too, and we have \(\mathcal{C}_{ij}^{(int)}=1\). \(\blacksquare\)

Due to Claim 7.0.1, the task of analyzing the random variable \(\mathcal{C}_{ij}^{(int)}\) reduces to the case of vectors with non-overlapping supports. This reduction simplifies the analysis and allows us to avoid dealing with dependencies arising from overlapping coordinates of the two vectors.

**Lemma 7.0.3.** _Fix_ \(\mathbf{u}_i,\mathbf{u}_j\in\mathsf{A}\) _such that they do not overlap, i.e._ \(\|\mathbf{u}_i\|_1+\|\mathbf{u}_j\|_1=\|\mathbf{u}_i\oplus\mathbf{u}_j\|_1\)_. Let w<sub>i</sub>,w<sub>j</sub>,w<sub>l,i</sub>,w<sub>r,i</sub>,w<sub>l,j</sub>, and w<sub>r,j</sub> denote the Hamming weights of the vectors_ \(\mathbf{u}_i,\mathbf{u}_j,\mathbf{u}_i^{(L)},\mathbf{u}_i^{(R)},\mathbf{u}_j^{(L)}\)_, and_ \(\mathbf{u}_j^{(R)}\) _respectively. Assume that_ \(\alpha n<w_i,w_j<(1-\alpha)n\), \(|w_i-w_j|=\mathcal{O}(\sqrt{n})\) _and_ \(\alpha n/2<w_{l,i},w_{r,i},w_{l,j},w_{r,j}<(1-\alpha)n/2\) _for some constant_ \(1/8\le\alpha<1/4\)_. Then, we have the following_<tbc>

\(\mathbb{E}_\mathbf{a}\left(\mathcal{C}_{ij}^{(\mathsf{int})}\right)=\Omega\left(\frac{1}{np^4q^2r}\right).\)

<tbc>_Proof._ Since **a**<sup>(_pq_)</sup> and **a**<sup>(_r_)</sup> are independent of each other, \(\mathbb{E}_\mathbf{a}\left(\mathcal{C}_{ij}^{(\mathsf{int})}\right)\) is the product of the following two probabilities

\(\mathbb{P}_{\mathbf{a}^{(pq)}}\left(\mathsf{E}_{\mathsf{LS},\mathbf{a},i}^{(p)}\wedge\mathsf{E}_{\mathsf{LS},\mathbf{a},j}^{(p)}\wedge\mathsf{E}_{\mathsf{TS},\mathbf{a},i}^{(pq)}\wedge\mathsf{E}_{\mathsf{TS},\mathbf{a},j}^{(pq)}\wedge\mathsf{E}_{\mathsf{C},pq,\mathbf{a},i,j}\right),\) (8)

and

\(\mathbb{P}_{\mathbf{a}^{(r)}}\left(\mathsf{E}_{\mathsf{TS},r,\mathbf{a},i,j}\right).\)

Now, we analyze the **a**<sup>(_pq_)</sup> and **a**<sup>(_r_)</sup> events separately in the following proposition.

