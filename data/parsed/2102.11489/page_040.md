**Fact 10.4.** _Assume the same assumptions as in Theorem 10.1, and moreover n is divisible by f(n). The lossy loose compaction algorithm above can be realized with a circuit consisting of_ \(C_\mathrm{sp}\cdot n\cdot(f(f(n))+1)+O(n)\) _generalized boolean gates,_ \(2C_\mathrm{sp}\cdot n\) _number of w-selector gates, and of depth D_<sub>sp</sub>(_n)+D_<sub>sp</sub>(_f(n_))+_O_(log_f(n_)).

**When** _n_ **is not divisible by** _f(n_)**.** When _n_ is not divisible by _f(n_), we can pad the last chunk with filler elements to a length of a multiple _f(n_). After the padding the total number of elements is upper bounded by _n+f(n_). As long as _n_ is greater than an appropriately large constant, even with the aforementioned padding, we would have the following fact:

**Fact 10.5.** _Assume the same assumptions as in Theorem 10.1. Then, for sufficiently large n, the above lossy loose compaction algorithm can be realized with a circuit consisting of_ \(2.07C_\mathrm{sp}\cdot n\cdot f(f(n))+O(n)\) _generalized boolean gates,_ \(2.07C_\mathrm{sp}\cdot n\) _number of w-selector gates, and in depth_ 2.07_D_<sub>sp</sub>(_n)+O_(log_f(n_)).

## 11 Linear-Sized, Low-Depth \(1/\mathsf{polylog}(\cdot)\)-Lossy Loose Compactor

In this section, we shall prove the following theorem.

**Theorem 11.1** (Linear-sized loose compactor)**.** _Let_ \(\widetilde{C}>1\) _be an arbitrary constant. There exists a circuit in the indivisible model that solves_ \((1/\mathrm{log}\widetilde{C}(n),n,w)\)_-lossy loose compaction, and moreover the circuit depth is O_(log<sup>0.5</sup>_n), the total number of generalized boolean gates is upper bounded by_ \(O(n\cdot w)\cdot\mathrm{max}\left(1,\mathsf{polylog}^*n-\mathrm{log}^*w\right)\)_, and the number of w-selector gates is upper bounded by_ \(O(n)\cdot\mathrm{max}\left(1,\mathsf{polylog}^*n-\mathrm{log}^*w\right)\).

_As a direct corollary, for any arbitrarily large constant_ \(c\ge 1\)_, if_ \(w\ge\mathrm{log}^{(c)}n\)_, it holds that the number of generalized boolean gates is upper bounded by O(nw), and the number of w-selector gates is upper bounded by O(n)._

The case when _w\>_loglog_n_ is easier (see  8), so in the remainder of this section, unless otherwise noted, we shall assume that \(w\le\mathrm{loglog}n\).

**Proof of Theorem 11.1:** We will construct tight compaction through repeated bootstrapping and boosting. Without loss of generality, we may assume that _n_ is greater than an appropriately large constant. We have two steps:

• \(\mathbf{LC}_i\Longrightarrow\mathbf{SP}_{i+1}\) **(Theorem 9.3):** from lossy loose compactor to approximate splitter. Due to Theorem 9.1 and Theorem 9.3, we get the following, where we use different subscripts in the big-O notations to hide different constants.

Assuming \((\alpha,n,w)\)-lossy loose compactor with:<tbc>

\(\text{\# generalized boolean gates :}B_\mathrm{lc}(n)\)<br>
\(\text{\# selector gates :}S_\mathrm{lc}(n)\)<br>
\(\text{depth :}D_\mathrm{lc}(n)\)

<tbc>Then, for any \(\beta\in(0,1/4]\), there exists \((8\alpha,\beta,n,w)\)-approximate splitter with:<tbc>

\(\text{\# generalized boolean gates :}2.5B_\mathrm{lc}(n)+10S_\mathrm{lc}(n)+O_1(n)\)<br>
\(\text{\# selector gates :}5S_\mathrm{lc}(n)+O_2(n)\)<br>
\(\text{depth :}2.4\mathrm{log}\frac{1}{\alpha}\cdot(D_\mathrm{lc}(n)+O_3(1))\)

