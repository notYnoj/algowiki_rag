### Lower Bound of E<sub>**a**</sub>(C).

Using equation (3), \(M=pqr=\Theta\left(2^n\right)\), and \(p,q=\Theta\left(M^{1/4}\right)\), we get

\(\mathbb{E}_\mathbf{a}\left(\mathcal{C}\right)=\frac{N_1}{p^3q^2r}+\frac{N_2}{2p^4q^2r}\)<br>
\(=\Theta\left(\frac{2^{3n/2}}{p^2qM}\right)+\Theta\left(\frac{2^{2n}}{p^3qM}\right)\)<br>
\(=\Theta\left(\frac{2^{3n/2}}{2^{7n/4}}\right)+\Theta\left(\frac{2^{2n}}{2^{2n}}\right)\)<br>
\(=\Theta(1).\)

This completes the proof of Lemma 6.0.2.

## 6.1.2 Second Moment

**Lemma 6.0.3.** _Let M,n,p,and q be the same as defined in the above problem **ACM-RESS**. Then the following holds for the Algorithm 3_<tbc>

\(\mathbb{E}_\mathbf{a}\left(\mathcal{C}^2\right)=\mathcal{O}\left(1\right).\)

<tbc>_Proof._

\(\mathbb{E}_\mathbf{a}\left(\mathcal{C}^2\right)=\mathbb{E}_\mathbf{a}\left(\sum_{i<j}\mathcal{C}_{ij}.\sum_{l<k}\mathcal{C}_{lk}\right)\)<br>
\(=\sum_{i<j,l<k}\mathbb{E}_\mathbf{a}\left(\mathcal{C}_{ij}\mathcal{C}_{lk}\right)\)<br>
\(=\sum_S\mathbb{P}_\mathbf{a}\left(\mathcal{C}_{ij}=1\wedge\mathcal{C}_{lk}=1\right)+\mathbb{E}_\mathbf{a}\left(\mathcal{C}\right),\)

where \(S:=\left\{\left(\mathbf{u}_i,\mathbf{u}_j,\mathbf{u}_l,\mathbf{u}_k\right)|i<j,l<k,\left(i,j\right)\neq\left(l,k\right)\right\}\). Hence, we need to analyze the probability that the following events occur simultaneously

1. _Left sum events:_<tbc>

\(\mathsf{E}_{\mathsf{LS},p}^{\left(i\right)}:\mathbf{u}_i^{\left(L\right)}\cdot\mathbf{a}^{\left(p\right)\left(L\right)}\equiv s_0\mathrm{mod}p,\)<br>
\(\mathsf{E}_{\mathsf{LS},p}^{\left(j\right)}:\mathbf{u}_j^{\left(L\right)}\cdot\mathbf{a}^{\left(p\right)\left(L\right)}\equiv s_0\mathrm{mod}p,\)<br>
\(\mathsf{E}_{\mathsf{LS},p}^{\left(l\right)}:\mathbf{u}_l^{\left(L\right)}\cdot\mathbf{a}^{\left(p\right)\left(L\right)}\equiv s_0\mathrm{mod}p,\)<br>
\(\mathsf{E}_{\mathsf{LS},p}^{\left(k\right)}:\mathbf{u}_k^{\left(L\right)}\cdot\mathbf{a}^{\left(p\right)\left(L\right)}\equiv s_0\mathrm{mod}p,\)

2. _Right sum events:_<tbc>

\(\mathsf{E}_{\mathsf{RS},p}^{\left(i\right)}:\mathbf{u}_i^{\left(R\right)}\cdot\mathbf{a}^{\left(p\right)\left(R\right)}\equiv s_1\mathrm{mod}p,\)<br>
\(\mathsf{E}_{\mathsf{RS},p}^{\left(j\right)}:\mathbf{u}_j^{\left(R\right)}\cdot\mathbf{a}^{\left(p\right)\left(R\right)}\equiv s_1\mathrm{mod}p,\)<br>
\(\mathsf{E}_{\mathsf{RS},p}^{\left(l\right)}:\mathbf{u}_l^{\left(R\right)}\cdot\mathbf{a}^{\left(p\right)\left(R\right)}\equiv s_1\mathrm{mod}p,\)<br>
\(\mathsf{E}_{\mathsf{RS},p}^{\left(k\right)}:\mathbf{u}_k^{\left(R\right)}\cdot\mathbf{a}^{\left(p\right)\left(R\right)}\equiv s_1\mathrm{mod}p,\)

