Now, we make the following crucial observation relating the two random variables C<sup>(int)</sup> and C<sup>(pqr)</sup> as follows<tbc>

\(\mathcal{C}^{(\mathrm{int})}\le\mathcal{C}^{(\mathrm{pqr})}.\)

<tbc>This implies

\(\mathbb{E}_\mathbf{a}\left(\mathcal{C}^{(\mathrm{int})2}\right)\le\mathbb{E}_\mathbf{a}\left(\mathcal{C}^{(\mathrm{pqr})2}\right).\)

In the modular case, we analyzed the second moment of the random variable C<sup>(pqr)</sup> given the random vector **a** is uniformly distributed over the ring Z_<sub>pqr</sub>_.

In the integer case, the input random vector **a** is uniformly distributed over the set [_M]<sup>n</sup>_, here we can observe that the variables \(a_i^{(p)}:=a_imodp\), \(a_i^{(q)}:=a_imodq\), and \(a_i^{(r)}:=a_imodr\) has the following distribution

\(\mathbb{P}_{a_i}\left(a_i^{(p)}=\alpha\right)=\frac{1}{p}\cdot\left(1+\mathcal{O}\left(\frac{p}{M}\right)\right)\)<br>
\(\mathbb{P}_{a_i}\left(a_i^{(q)}=\beta\right)=\frac{1}{q}\cdot\left(1+\mathcal{O}\left(\frac{q}{M}\right)\right)\)<br>
\(\mathbb{P}_{a_i}\left(a_i^{(r)}=\gamma\right)=\frac{1}{r}\cdot\left(1+\mathcal{O}\left(\frac{r}{M}\right)\right),\)

\(\forall 1\le i\le n\), \(\alpha\in\mathbb{Z}_p\), \(\beta\in\mathbb{Z}_q\), and \(\gamma\in\mathbb{Z}_r\). Since, _p,q_, and _r_ are significantly smaller than the input integer _M_, we can safely assume that the random variables **a**<sup>(_p_)</sup>, **a**<sup>(_q_)</sup>, and **a**<sup>(_r_)</sup> are uniformly distributed over the rings Z_<sub>p</sub>_, Z_<sub>q</sub>_, and Z_<sub>r</sub>_ respectively. Now, using the second-moment computation from the modular case, we obtain the desired result.

### 7.1.3 Concentration

Similar to the modular case, we use the Paley-Zygmund inequality to prove that the random variable C<sup>(int)</sup> is concentrated around its mean. Using Lemma 7.0.2 and Lemma 7.0.4 and this inequality, we get the desired success probability of the Algorithm 4. This completes the proof of Lemma 7.0.1.

## 7.2 Complexity Analysis

**Lemma 7.0.5.** _Let M and n be the same as defined in the problem **ACI-RESS**. Then Algorithm 4 runs in expected time_ poly(_n)M_<sup>1/4</sup> _over the random choice of the input vector_ **a**_. Let_ T _be the running time of the algorithm. Then, we also have the following tail bound_

\(\mathbb{P}_\mathbf{a}\left(\mathsf{T}\ge poly(n)\cdot M^{1/4}\right)=\mathcal{O}\left(\frac{1}{poly(n)}\right).\)

_Proof._ Since the filtering algorithm only depends on the lower _pq_ bits of the input variables, and as we observed in Section 7.1.2, the input vector mod _p_ and _q_ is asymptotically uniform over the corresponding support; therefore, the expected sizes of the list generated in the algorithm asymptotically remain the same as in the modular case. Hence, the time complexity in the integer case asymptotically remains the same as the modular case.

