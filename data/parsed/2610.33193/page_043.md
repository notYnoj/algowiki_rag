where for the last inequality we use the fact that \(1/4\le(1-1/k)^k\) for all \(k\ge 2\).

Using the arithmetic geometric mean inequality,

\(\left|\mathcal{A}_I^{s-2^{k_\ell}}\right|+\left|\mathcal{A}_I^{s+2^{k_\ell}}\right|\ge 2\sqrt{\left|\mathcal{A}_I^{s-2^{k_\ell}}\right|\left|\mathcal{A}_I^{s+2^{k_\ell}}\right|}.\)<br>
\(\ge 2(1/4)^{2c}\left|\mathcal{A}_I^s\right|=(2/\alpha)\left|\mathcal{A}_I^s\right|,\)

where the constant \(\alpha\) is 4<sup>2_c_</sup>. We have now proven (10) in all cases, Let _C(x_<sub>1</sub>_,x_<sub>2</sub>) denote the number of choices of set _A_ such that _g_ will receive input (_x_<sub>1</sub>_,x_<sub>2</sub>). Then:<tbc>

\(C(x_1,x_2)=\sum_{s,I\mathcal{A}_I^s\text{gives input}(x_1,x_2)}\left|\mathcal{A}_I^s\right|\le(\alpha/2)\sum_{s,I\mathcal{A}_I^s\text{gives input}(x_1,x_2)}\left|\mathcal{A}_I^{s-2^{k_\ell}}\right|+\left|\mathcal{A}_I^{s+2^{k_\ell}}\right|\le\alpha C(x_2,x_1),\)

<tbc>where the last inequality comes from the fact that this sum is counting each possible _A_ at most twice. By symmetry the same argument gives that \(C(x_2,x_1)\le\alpha C(x_1,x_2)\). Since every equipartition is equally likely we can conclude that:

\(1/\alpha\le\frac{C(x_2,x_1)}{C(x_1.x_2)}=\frac{Pr_\mathcal{D}[(x_2,x_1)]}{Pr_\mathcal{D}[(x_1,x_2)]}\le\alpha\)

as desired.

## Thermodynamic bounds

Now that we have proven Lemma 5.11, we are ready to prove our thermodynamic bounds.

**Lemma 5.12.** _Let D be an ordered set and_ D _be the distribution resulting from picking n elements of D without replacement uniformly at random. Let n be sufficiently large so that Lemma 5.11 applies. Any gate in Batcher’s odd-even mergesort where Lemma 5.11 can be applied must release_ \(\Omega(1)\) _expected heat._

_Proof._ Assume for now that _D_={0_,...,n_-1}. By (5) and Lemma 5.11 we know that the optimal heat function for such a gate with induced marginal input distribution D is given by \(Q(x_1,x_2)=log(1+\frac{Pr_\mathcal{D}[(x_2,x_1)]}{Pr_\mathcal{D}[(x_1,x_2)]})\ge log(1+1/\alpha)=\Omega(1)\). Since this applies to every input pair _x_<sub>1</sub>_,x_<sub>2</sub>, the expected heat dissipation is \(\Omega(1)\). This lower bound also applies to arbitrary sets _D_ due to Lemma 5.5.

**Theorem 5.13.** _Let D be an ordered set and_ D _be the distribution resulting from picking n elements of D without replacement uniformly at random. Batcher’s odd-even mergesort must release_ \(\Omega(nlog^2n)\) _expected heat on input distribution_ D_. When using the optimal heat function for each gate, this value is_ \(\Theta(nlog^2n)\).

_Proof._ We do this by counting the number of gates where we can apply Lemma 5.12. Let _C(n_) denote the count of such gates in the circuit of size _n_. In the non recursive step, when _n_ is sufficiently large, the admissible gates are those in layers \(\ell>\lceil(logn)/2\rceil+1\) that are central. As in the proof of Lemma 5.11, let \(k_\ell=(logn)-\ell\) be the width of gates in layer \(\ell\). There are at least _n/_4 choices of _i_ such that \(3n/8\le i\le 5n/8\). By (4), at least half of these _i_ have the correct value of \(\left\lfloor i/2^{k_\ell}\right\rfloor\) to be either the top or the bottom node of a gate. Of these _n/_8 potential gates, at most \(2^{k_\ell}\) of them<tbc>

