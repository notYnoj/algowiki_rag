_Proof._ refer to Section D.2.

Let the \(\text{rank}(\mathbf{U}_{ijlk}^{(L)})\), \(\text{rank}(\mathbf{U}_{ijlk}^{(R)})\), and rank(**U**_<sub>ijlk</sub>_) are denoted by _t_<sub>1</sub>, _t_<sub>2</sub>, and _t_<sub>3</sub> respectively. Using Claim 6.0.2, we know that \(3\le t_3\le 4\). Since, the vectors **u**_<sub>i</sub>,_**u**_<sub>j</sub>,_**u**_<sub>l</sub>_, and **u**_<sub>k</sub>_ satisfy a relation in the sum _S_<sub>1</sub>, we have _t_<sub>3</sub>=3. And, since \(t_3\ge max\{t_1,t_2\}\), we have \(1\le t_1,t_2\le 3\). Now, we split the sum _S_<sub>1</sub> based on the rank of the matrices \(\mathbf{U}_{ijlk}^{(L)}\) and \(\mathbf{U}_{ijlk}^{(R)}\) and using Lemma 6.0.4<tbc>

\(S_1\le\sum_{i<j,l<k(i,j)\neq(l,k)\mathbf{u}_i-\mathbf{u}_j=\pm(\mathbf{u}_l-\mathbf{u}_k)t_1+t_2\le 5}\frac{1}{p^{t_1}\cdot p^{t_2}\cdot q^3\cdot r}+\sum_{i<j,l<k(i,j)\neq(l,k)\mathbf{u}_i-\mathbf{u}_j=\pm(\mathbf{u}_l-\mathbf{u}_k)t_1=t_2=3}\frac{1}{p^3\cdot p^3\cdot q^3\cdot r}.\)

<tbc>Then, using Proposition 6.0.1 and Proposition 6.0.3, we have

\(S_1<\frac{2^{(t_1+t_2)n/2}}{p^{t_1}\cdot p^{t_2}\cdot q^3\cdot r}+\frac{6^n}{p^3\cdot p^3\cdot q^3\cdot r}=\mathcal{O}\left(1\right)+\mathcal{O}\left(\frac{1}{2^{0.165n}}\right)=\mathcal{O}\left(1\right).\text{(5)}\)

### Upper bound of _S_<sub>2</sub>.

Using similar techniques and arguments, we have

\(S_2\le\frac{2}{r^2}\cdot\sum_{i<j,l<k(i,j)\neq(l,k)\mathbf{u}_i-\mathbf{u}_j\neq\pm(\mathbf{u}_l-\mathbf{u}_k)}\mathbb{P}_{\mathbf{a}^{(pq)}}\left(\mathcal{D}_{ij}=1\wedge\mathcal{D}_{lk}=1\right)\le\frac{2\cdot 2^{(t_1+t_2)n/2}}{p^{t_1}\cdot p^{t_2}\cdot q^{t_3}\cdot r^2}=\mathcal{O}\left(1\right).\text{(6)}\)

Now, combining equations (4), (5) and (6), we get that

\(\mathbb{E}_\mathbf{a}(\mathcal{C}^2)=S_1+S_2+\mathbb{E}_\mathbf{a}\left(\mathcal{C}\right)=\mathcal{O}\left(1\right)+\mathcal{O}(1)+\mathcal{O}\left(1\right)=\mathcal{O}\left(1\right).\)

This complete the proof of Lemma 6.0.3.

## 6.1.3 Concentration

Now, we use the following second-moment concentration bound to prove that the random variable C is concentrated around its mean value.

**Lemma 6.0.5.** (_Paley-Zygmund Inequality, see e.g.,_ \[_Roc24_\] _Section 2.3)_. For any non-negative random variable Z and any_ \(\theta\in[0,1]\),<tbc>

\(\mathbb{P}\left(Z>\theta\mathbb{E}(Z)\right)\ge(1-\theta)^2\cdot\frac{\mathbb{E}(Z)^2}{\mathbb{E}(Z^2)}.\)

