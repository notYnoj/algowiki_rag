_Proof._ Without loss of generality, suppose _B_ is _sorted in increasing order_, and let <o>_B_</o> denote the average over its elements. We will show that we can satisfy the inequality by setting \(\gamma_{1\dots M/2}\) to -1 and \(\gamma_{(M/2+1)\dots M}\) to +1. Namely,<tbc>

\(2\sum_{1\le i\le M/2}\left(b_{M-i+1}-b_i\right)\ge\sum_i\left|b_i-\overline{B}\right|.\)

<tbc>Let _t_ be the smallest index such that \(b_t\ge\overline{B}\). Due to symmetry, we can assume that \(t-1\le M/2\). Let \(s:=\sum_{1\le i\le M}\left|b_i-\overline{B}\right|\), \(s^-:=\sum_{1\le i\le t-1}\left(\overline{B}-b_i\right)\), and \(s^+:=\sum_{t\le i\le M}\left(b_i-\overline{B}\right)\). Then we have _s=s_<sup>-</sup>+_s_<sup>+</sup>. Moreover, since <o>_B_</o> is the mean of _B_, we must have _s_<sup>+</sup>-_s_<sup>-</sup>=0. Therefore, _s_<sup>-</sup>=_s_<sup>+</sup>=_s/_2. Thus

\(2\sum_{1\le i\le M/2}\left(b_{M-i+1}-b_i\right)\ge 2\sum_{1\le i\le t-1}\left(b_{M-i+1}-b_i\right)\)<br>
\(\ge 2\sum_{1\le i\le t-1}\left(\overline{B}-b_i\right)\)<br>
\(=2s^-\)<br>
\(=s.\)

Now we are ready to prove Lemma 4.1:

_Proof of Lemma 4.1._ For every scale-_s_ interval (_l,r_\], by Claim 4.2 we can find a vector<tbc>

\(\left(\gamma_{(m_0,m_1]},\gamma_{(m_1,m_2]},\cdots,\gamma_{(m_{M-1},m_M]}\right)\)

<tbc>such that<tbc>

\(\mathrm{TD}_M(A_{(l,r]})\le 2\sum_{i=1}^M\gamma_{(m_{i-1},m_i]}A_{\Sigma(m_{i-1},m_i]}.\)

<tbc>For each index \(x\in(l,r]\), let _g<sub>x,s</sub>_ denote the sign of \(\gamma_{(m_{i-1},m_i]}\) corresponding to the sub-interval \((m_{i-1},m_i]\unknown x\). We have

\(\mathrm{TD}_M(A_{(l,r]})\le 2\sum_{x\in(l,r]}g_{x,s}a_x.\) (3)

Let \(g_x:=\sum_{s\in[S]}g_{x,s}\) denote the sum of the signs for index _x_ across all scales. By taking the sum of (3) over every recursion interval, we get

\(\includegraphics{}\mathrm{TD}_{M,S}(A)\le 2\sum_xg_xa_x\le 2\sum_x|g_x||a_x|.\) (4)

We bound \(\sum_x|g_x||a_x|\) with a probabilistic argument bounding **E**_<sub>x</sub>_\[|_g<sub>x</sub>||a<sub>x</sub>_\]. Namely, we randomly sample an index \(x\in[n]\). As a warm-up, let us ignore the |_a<sub>x</sub>_| term for now. Notice that for any scale-_s_ interval _A_<sub>(_l,r_\]</sub>, the values of \(g_{x,s^\prime}\) for \(s'>s\) are identical for all \(x\in(l,r]\) since those values depend on \(\gamma_{(l^\prime,r^\prime]}\) of larger intervals \((l',r']\supseteq(l,r]\). Furthermore, _g<sub>x,s</sub>_ is +1 (respectively -1) for exactly half of the \(x\in(l,r]\). Hence _g<sub>x</sub>_ is distributed identical to the sum of _S_ i.i.d. \(\pm 1\) coin flips. Therefore we have \(\mathbf{E}_x\left[|g_x|\right]\le\sqrt{S}\).

Similarly, bringing back |_a<sub>x</sub>_|, we essentially need to bound the \(\sum_x|a_x|\)-tail of a distribution of _S_ i.i.d. \(\pm 1\) coin flips. Formally, we say that an index _x_ is in the "tail" if |_g<sub>x</sub>|\>S_<sup>0.51</sup>, and we want to bound the sum of |_a<sub>x</sub>_| for every _x_ in the tail, which is no more than max_<sub>x</sub>|a<sub>x</sub>_| times the number of _x_’s in the tail. By<tbc>

