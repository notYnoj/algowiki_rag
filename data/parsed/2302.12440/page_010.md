**Algorithm 2**

procedure SortInversion\((n,(a_i)_{i\in[n]},p,\sigma)\)<br>
   for \(i=1\rightarrow n\) do<br>
   for \(j=i\rightarrow 2\) do<br>
   if LessThan\((a_j,a_{j-1},\sigma)\) then<br>
Swap<br>
_a<sub>j</sub>_<br>
and<br>
_a_<br>
<sub>_j_-1</sub><br>
   else<br>
   break<br>
   return \((a_i)_{i\in[n]}\)

_Proof._ Consider Algorithm 2, which is essentially insertion sort.

By union bound, with probability \(\ge 1-(n-1+t)\sigma\), the first (_n_-1+_t_) calls to LessThan all return correctly. Conditioned on this happening, the algorithm acts exactly like a normal insertion sort, which halts after the first (_n_-1+_t_) calls to LessThan, which takes \((n-1+t)f(\sigma)\) noisy comparisons in expectation.

With probability \(\le(n-1+t)\sigma\), the algorithm does not run correctly, but the algorithm still halts in at most \(\genfrac(){pt}{2}{n}{2}f(\sigma)\le n^2f(\sigma)\) queries in expectation.

Next, we use Lemma 16 to construct the following subroutine. It is ultimately used to sort some small sets of elements in the main algorithm.

**Lemma 17.** _Fix any parameter_ \(\delta\in(0,1)\) _which can depend on n. There is a randomized algorithm for_ NoisySorting(_n_) _with error probability at most_ \(\delta\) _using_ \(O(n\mathrm{log}n)+nf(\delta/n)+n^2\delta f(\delta/n)\) _noisy comparisons in expectation, and using O(n_log_n_) _random bits always._

_Proof._ We first use Corollary 12 with error probability \(P_e\le n^{-2}\), then use Lemma 16 with error probability \(\sigma=\delta/n\).

After the first step, the expected number of inversion pairs is

\(\mathbb{E}[t]\le P_en^2\le 1,\)

so the second step uses at most \(nf(\delta/n)+n^2\delta f(\delta/n)\) queries in expectation.

The overall error probability is at most \(\mathbb{E}[(n-1+t)\sigma]\le n\sigma=\delta\).

The following lemma allows us to construct algorithms with guaranteed tail behavior for the number of queries. This will be helpful for concentration bounds.

**Lemma 18.** _Suppose we have an algorithm_ A _(solving a certain task) that has error probability_ \(\le\delta\) _and number of queries_ \(\tau\) _with_ \(\mathbb{E}[\tau]\le m\)_, and uses_ \(\le r\) _random bits always. Then we can construct an algorithm_ B _solving the same task satisfying the following properties:_

• B _has error probability_ \((1+o_m(1))\delta\);<tbc>

• _Let_ \(\rho\) _be the number of queries algorithm_ B _uses. Then_<tbc>

\(\mathbb{E}[\rho]\le(1+o_m(1))m,\)<br>
\(\mathbb{E}[\rho^2]=O(m^3).\)

