## 6.1.1 First Moment

**Lemma 6.0.2.** _Let M,n,p, and q be the same as defined in the above problem **ACM-RESS**. Then the following holds for the Algorithm 3_<tbc>

\(\mathbb{E}_\mathbf{a}\left(\mathcal{C}\right)=\Theta\left(1\right).\)

<tbc>_Proof._ Let \(v\in\left\{0,1\right\}^n\backslash\left\{0^n\right\}\), then we observe the following

\(\mathbb{P}_{\mathbf{a}^{\left(p\right)}}\left(\mathbf{v}\cdot\mathbf{a}^{\left(p\right)}\equiv\alpha\mathrm{mod}p\right)=\frac{1}{p},\)<br>
\(\mathbb{P}_{\mathbf{a}^{\left(q\right)}}\left(\mathbf{v}\cdot\mathbf{a}^{\left(q\right)}\equiv\beta\mathrm{mod}q\right)=\frac{1}{q},\)<br>
\(\mathbb{P}_{\mathbf{a}^{\left(r\right)}}\left(\mathbf{v}\cdot\mathbf{a}^{\left(r\right)}\equiv\gamma\mathrm{mod}r\right)=\frac{1}{r},\)

\(\forall\alpha\in\mathbb{Z}_p\), \(\beta\in\mathbb{Z}_q\), and \(\gamma\in\mathbb{Z}_r\).

Since the vectors **a**<sup>(_p_)</sup>, **a**<sup>(_q_)</sup>, and **a**<sup>(_r_)</sup> are mutually independent, we can observe that the following four events are mutually independent

\(\mathsf{E}_{\mathsf{LS},p}^{\left(i\right)}\wedge\mathsf{E}_{\mathsf{LS},p}^{\left(j\right)},\mathsf{E}_{\mathsf{RS},p}^{\left(i\right)}\wedge\mathsf{E}_{\mathsf{RS},p}^{\left(j\right)},\mathsf{E}_{\mathsf{TS},q}^{\left(i\right)}\wedge\mathsf{E}_{\mathsf{TS},q}^{\left(j\right)},\mathsf{E}_{\mathsf{col},r}^{\left(ij\right)}.\) (2)

And, since \(\mathbf{u}_i\neq\mathbf{u}_j\), the events dependent on the vector **u**_<sub>i</sub>_ are independent of the events dependent on the vector **u**_<sub>j</sub>_. Combining this observation with the above equation, we have the following<tbc>

\(\mathbb{E}_\mathbf{a}\left(\mathcal{C}_{ij}\right)=\left\{\begin{array}{ c c }
\frac{1}{p^3q^2r} & \mathbf{u}_i^{\left(L\right)}=\mathbf{u}_j^{\left(L\right)},\mathbf{u}_i^{\left(R\right)}\neq\mathbf{u}_j^{\left(R\right)} \\
\frac{1}{p^3q^2r} & \mathbf{u}_i^{\left(L\right)}\neq\mathbf{u}_j^{\left(L\right)},\mathbf{u}_i^{\left(R\right)}=\mathbf{u}_j^{\left(R\right)} \\
\frac{1}{p^4q^2r} & \mathbf{u}_i^{\left(L\right)}\neq\mathbf{u}_j^{\left(L\right)},\mathbf{u}_i^{\left(R\right)}\neq\mathbf{u}_j^{\left(R\right)}
\end{array}\right..\)

<tbc>Then, we have the following

\(\mathbb{E}_\mathbf{a}\left(\mathcal{C}\right)=\sum_{i<j}\mathbb{E}_\mathbf{a}\left(\mathcal{C}_{ij}\right)=\frac{1}{2}\sum_{i\neq j}\mathbb{E}_\mathbf{a}\left(\mathcal{C}_{ij}\right)=\frac{1}{2}\cdot\left(\frac{2N_1}{p^3q^2r}+\frac{N_2}{p^4q^2r}\right),\) (3)

where

\(N_1=\left(2^{n/2}-1\right)\cdot\left(2^{n/2}-1\right)\cdot\left(2^{n/2}-2\right)=\Theta\left(2^{3n/2}\right),\)

and

\(N_2=\left(\left(2^{n/2}-1\right)\cdot\left(2^{n/2}-2\right)\right)^2=\Theta\left(2^{2n}\right).\)

In the computation of _N_<sub>1</sub> and _N_<sub>2</sub>, we have used the fact that \(\mathbf{u}_i^{\left(L\right)}\), \(\mathbf{u}_i^{\left(R\right)}\), \(\mathbf{u}_j^{\left(L\right)}\), and \(\mathbf{u}_j^{\left(R\right)}\) cannot be equal to 0<sup>_n/_2</sup>.

