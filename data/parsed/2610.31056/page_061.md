3.<tbc>

\(\mathbb{P}_\mathbf{a}\left(\mathbf{a}^{(pq)}=\mathbf{x},\mathbf{a}^{(r)}=\mathbf{y}\big|\mathsf{E}^{(\mathsf{U})}\right)\)<br>
\(=\mathbb{P}_\mathbf{a}\left(\mathbf{a}^{(pq)}=\mathbf{x}\big|\mathsf{E}^{(\mathsf{U})}\right)\mathbb{P}_\mathbf{a}\left(\mathbf{a}^{(r)}=\mathbf{y}\big|\mathsf{E}^{(\mathsf{U})}\right)\left(1+\mathcal{O}\left(\frac{npq}{M}\right)\right),\)

_where_ \(\mathsf{E}^{(\mathsf{U})}:=\wedge_{j=1}^n\mathsf{E}_j^{(\mathsf{U})}\).

_Proof._ The proof of parts \[1\] and \[2\] comes directly from equations (15) and (16). Now, we look at the proof of part \[3\]. Let us define

\(\mathsf{P}_\mathsf{i}(x,y):=\mathbb{P}_{a_i}\left(a_i^{(pq)}=x,a_i^{(r)}=y\big|\mathsf{E}_\mathsf{i}^{(\mathsf{U})}\right)\)<br>
\(\mathsf{Q}_\mathsf{i}(x,y):=\mathbb{P}_{a_i}\left(a_i^{(pq)}=x\big|\mathsf{E}_\mathsf{i}^{(\mathsf{U})}\right)\mathbb{P}_{a_i}\left(a_i^{(r)}=y\big|\mathsf{E}_\mathsf{i}^{(\mathsf{U})}\right)\)

We aim to analyze the ratio of P<sub>i</sub>(_x,y_) and Q<sub>i</sub>(_x,y_), denoted by R<sub>i</sub>(_x,y_). This ratio will help us analyze the dependence between the two variables.

**Claim E.0.3.** _For all_ \(0\le x<pq\) _and_ \(0\le y<r\) _such that_ \((x,y)\neq 0\)_, we have the following_<tbc>

\(\Omega\left(\frac{1}{M}\right)=\mathsf{R}_\mathsf{i}(x,y)-1=\mathcal{O}\left(\frac{pq}{M}\right).\)

<tbc>_Proof:_

1. _x_=0, 0_\<y\<r_. In this case, we have<tbc>

<tbc>\(\mathsf{P}_\mathsf{i}(x,y)=\frac{1}{M},\mathsf{Q}_\mathsf{i}(x,y)=\frac{r-1}{M}\cdot\frac{pq}{M}\)<tbc>

<tbc>Hence,<tbc>

\(\mathsf{R}_\mathsf{i}(x,y)=\frac{\frac{1}{M}}{\frac{r-1}{M}\cdot\frac{pq}{M}}\)<br>
\(=1+\frac{pq-s}{pq(r-1)}.\)

Since \(\Omega(1/M)=\frac{pq-s}{pq(r-1)}=\mathcal{O}\left(pq/M\right)\), we get the desired result.<tbc>

2. _x\>_0, \(0\le y<r\). In this case, we have<tbc>

<tbc>\(\mathsf{P}_\mathsf{i}(x,y)=\frac{1}{M},\mathsf{Q}_\mathsf{i}(x,y)=\frac{r}{M}\cdot\frac{pq}{M}\)<tbc>

<tbc>Hence,<tbc>

<tbc>\(\mathsf{R}_\mathsf{i}(x,y)=1+\frac{s}{M}.\)<tbc>

<tbc>Since \(\frac{1}{M}\le 1+\frac{s}{M}<1+\frac{pq}{M}\), we get the desired result.

This completes the proof of the claim.

Now, consider the following

\(\mathbb{P}_\mathbf{a}\left(\mathbf{a}^{(pq)}=\mathbf{x},\mathbf{a}^{(r)}=\mathbf{y}\big|\mathsf{E}^{(\mathsf{U})}\right)\)<br>
\(=\prod_{i=1}^n\mathbb{P}_{a_i}\left(a_i^{(pq)}=x_i,a_i^{(r)}=y_i\big|\mathsf{E}_\mathsf{i}^{(\mathsf{U})}\right)\)<br>
\(=\mathbb{P}_\mathbf{a}\left(\mathbf{a}^{(pq)}=\mathbf{x}\big|\mathsf{E}^{(\mathsf{U})}\right)\mathbb{P}_\mathbf{a}\left(\mathbf{a}^{(r)}=\mathbf{y}\big|\mathsf{E}^{(\mathsf{U})}\right)\left(1+\mathcal{O}\left(\frac{npq}{M}\right)\right).\)

This completes the proof.

