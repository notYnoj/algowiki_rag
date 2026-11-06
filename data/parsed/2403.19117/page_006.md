## 3.2 Large _d_ case via subsampling

In this section we prove Lemma 5. Assume \(2^{n/2}\le\Delta\le d<2^n\), and \(\Delta\) is known. We first use \(d=\sum_{0\le t<2^n}max\{0,f_t-1\}\) (Equation (3)) to show that many subset sums _t_ have large _f<sub>t</sub>_, which then allows us to use subsampling to speed up the modular dynamic programming approach of [1, 3].

\(\blacktriangleright\) **Lemma 8.** _There exists a_ \(j\in\{0,1,\dots,n-1\}\) _such that_ \(\#\{t:f_t>2^j\}>\frac{\Delta}{2^{j+1}n}\).

**Proof.** By definition of _d_ in Equation (3),

\(\Delta\le d=\sum_{t:f_t>1}(f_t-1)\le\sum_{0\le j<n}\#\{t:2^j<f_t\le 2^{j+1}\}\cdot(2^{j+1}-1).\) (9)

If the claimed inequality fails for all _j_, then

\([\text{RHS of Equation}(9)]\le\sum_{0\le j<n}\frac{\Delta}{2^{j+1}n}\cdot(2^{j+1}-1)<\Delta,\)

a contradiction.

Our algorithm enumerates all \(j\in\{0,1,\dots,n-1\}\) (increasing the time complexity by a factor of _n=O_<sup>∗</sup>(1)), and from now on we assume _j_ satisfies the inequality in Lemma 8. Define

\(h:=2^j+1\ge 2,m:=\left[\frac{\Delta}{2^{j+1}n}\right]>\frac{\Delta}{2hn},\text{and}X:=\{t\in[2^n]:f_t\ge h\}.\) (10)

Here we defined the set _X_ of frequent subset sums only for the sake of analysis. By Lemma 8,

\(|X|\ge m.\) (11)

Readers are encouraged to focus on the case of _h_=2 and \(m\ge\Omega^*(\Delta)\) (which is the hardest case for our algorithm) at first read.

We first describe the behavior of our algorithm: Let \(p\in[P,2P]\) be a uniformly random prime (for some parameter \(2\le P\le 2m\) to be determined later in the "Time complexity" paragraph). For each \(r\in\mathbb{Z}_p\), define bin \(B_r:=\{S\subseteq[n]:w(S)\equiv r(modp)\}\). The algorithm picks a random bin index \(r^*\in\mathbb{Z}_p\), and subsamples \(C\subseteq B_{r^*}\) by keeping each \(S\in B_{r^*}\) with probability \(\alpha\) independently (for some \(0<\alpha\le\frac{1}{2h}\) to be determined later in the "Success probability" paragraph). Finally, a pair of distinct \(S,S'\in C\) with \(w(S)=w(S')\) is reported (if exists).

Now we explain how to implement the algorithm above via dynamic programming (DP) similarly to [1, 3]. Build the DP table \(D_{i,r}=\#\{S\subseteq[i]:w(S)\equiv r(modp)\}\) (where \(0\le i\le n\) and \(r\in\mathbb{Z}_p\)) in _O_<sup>∗</sup>(_p_) overall time via the transition \(D_{i,r}=D_{i-1,r}+D_{i-1,(r-w_i)modp}\) with initial values _D_<sub>0_,r_</sub>=**1**[_r_=0]. This DP computes the size of every bin |_B<sub>r</sub>_|=_D<sub>n,r</sub>_. Furthermore, for any bin _B<sub>r</sub>_ and integer \(k\in[|B_r|]\), we can report the rank-_k_ set _S_ in _B<sub>r</sub>_ (in lexicographical order, where larger indices are compared first) by backtracing in the DP table in _O_<sup>∗</sup>(1) time. Then, in order to subsample a collection of sets \(C\subseteq B_{r^*}\) at rate \(\alpha\), we can first subsample their ranks in [|_B_<sub>_r_<sup>∗</sup></sub>|] (in near-linear time in the output size, see e.g., [10]), and then recover the actual sets by backtracing.

