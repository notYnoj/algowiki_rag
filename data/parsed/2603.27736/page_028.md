2.2. _(Popular Entries)_ Let \(C_{g,h}^\mathrm{pop}\) be the restriction of _C<sub>g,h</sub>_ to the popular entries (where we replace all unpopular entries by \(\perp\)). By Observation 4.7 we have that \(|P|\le|S_g||T_h|/(d'/q)\le d'q\), so by construction the instance \((A_g,B_h,C_{g,h}^\mathrm{pop})\) is \(d'q\)-uniform. We trivially reduce that instance further to at most \(((d'q)/d)^3\le t^3q^3\) instances that are _d_-uniform and store the resulting instances in I.<tbc>

<tbc>This completes the description of the reduction. Clearly it is potential-adjusting (with potential functions _u_\[_i_\]=-_s<sub>i,g</sub>_, _v_\[_k_\]=0, and _w_\[_j_\]=-_t<sub>j,h</sub>_).

**Running Time.** The preprocessing step takes time \(\tilde{O}(n_1n_2n_3/t)\) as argued before and leads to _O_(log<sup>2</sup>_n_<sub>2</sub>) instances we have to deal with. The running time of the uniformization step is bounded as follows by summing over all the contributions analyzed before:

\(\tilde{O}\big((n_1n_2+n_1n_3+n_2n_3)d\cdot p^4t^3q^3+\frac{n_1n_2n_3}{t}+\frac{n_1n_2n_3t}{p}+\frac{n_1n_2n_3tp^4}{q}\big).\)

This becomes as claimed by setting the parameters _p=t_<sup>2</sup> and _q=t_<sup>10</sup>. From this choice of parameters it also follows that \(|\mathcal{I}|\le O(\mathrm{log}^2(n_1n_2n_3)\cdot p^4t^3q^3)\le O(t^{41}\mathrm{log}^2(n_1n_2n_3))\) as claimed.

## 4.3 Reduction from Low-Rank to Uniform Regular Exact Triangle

The third step is to reduce to instances that are not only _D_-uniform but also 1_/D-regular_ (i.e., each integer appears in at most a 1_/D_-fraction of the entries of each row and column in all three matrices). This is one of the most technical steps in \[4\]. Roughly, the idea is to show that each _D_-uniform instance can be partitioned into two pieces: a _D_-uniform 1_/D_-regular part, and a remaining part that is \(D'\)-slice-uniform for some \(D'\checkmark D\). The first part is as intended. And the second part can be solved by first applying Lemma 4.5 and then _recursing_ on the polynomially many resulting \(D'\)-uniform instances. By carefully choosing the involved parameters this indeed leads to a subcubic reduction--but with quite bad quantitative bounds. Specifically, the resulting algorithm for \(n^{3-\omega-\epsilon}\)-slice-uniform Exact Triangle runs in time \(n^{3-\epsilon^{O(1)}}\).

Here we propose a twist to the argument in \[4\]: Instead of recursing on polynomially many instances that are \(D'\)-slice-uniform for some \(D'\checkmark D\), it turns out to be possible to recurse on just _O_(1) instances that are _r_-rank for some \(r\checkmark D\). This, in contrast, results in a final running time of \(n^{3-\Omega(\epsilon)}\) as stated in Theorem 4.1.

**Lemma 4.10** (Reduction from Low-Rank to Uniform Regular Exact Triangle)**.** _For any parameter_ \(t\ge 1\) _there is a potential-adjusting reduction from any_ rank-_r Exact Triangle instance to t_<sup>875</sup>(_n_<sub>1</sub>_n_<sub>2</sub>_n_<sub>3</sub>)<sup>_o_(1)</sup> _instances that are each D_-uniform _and_ 1_/D_-regular _for some_ \(D\le r\)_. The reduction runs in deterministic time_ (_n_<sub>1</sub>_n_<sub>2</sub>_n_<sub>3</sub>_/t_+(_n_<sub>1</sub>_n_<sub>2</sub>+_n_<sub>2</sub>_n_<sub>3</sub>+_n_<sub>1</sub>_n_<sub>3</sub>)_rt_<sup>875</sup>)<sup>1+_o_(1)</sup>_. In particular:_

\(\mathrm{ExactTri}(n_1,n_2,n_3|r)\)<br>
\(\le\big(t^{875}\cdot\mathrm{ExactTri}(n_1,n_2,n_3|D\le r;\rho\le 1/D)+\frac{n_1n_2n_3}{t}+(n_1n_2+n_2n_3+n_1n_3)rt^{875}\big)^{1+o(1)}.\)

Running Time: For each unpopular pair (i,j) we spend time O(d') to list all relevant representations, plus time O(d'/q · n2/dA) to enumerate all x,y,k. In total, we repeat this step p4 times, leading to a total time of:
O (p4 · n1n3 · (d'+ -
- -
= O(p4 · n1n3 · (dt+ -
= O(n1n2n3 dtp4 + -
q

Running Time: O(p4t3q3 · n1n2 + n2n3 + n1n3).

