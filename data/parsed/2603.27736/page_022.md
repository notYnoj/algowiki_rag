**Proof of Theorem 4.1.** Combining Lemmas 4.2 and 4.3 we obtain that, for any parameter \(K\ge 1\),

\(\mathrm{ExactTri}(n,n,n|r)=\left(K\cdot\mathrm{ExactTri}(n,n,n|D\le r;K)+\frac{n^3}{K^{1/98000}}+n^2rK\right)^{1+o(1)}\)<br>
\(=\left(K\cdot n^\omega rK+\frac{n^3}{K^{1/98000}}+n^2rK\right)^{1+o(1)}\)<br>
\(=\left(n^\omega rK^2+\frac{n^3}{K^{1/98000}}\right)^{1+o(1)}.\)

We pick \(K=(n^{3-\omega}/r)^{98/200}\) and argue that then the running time is as claimed. Indeed, the second term is clearly \(n^{3+o(1)}(r/n^{3-\omega})^{1/200000}\). The first term can be rewritten as \(n^{3+o(1)}(r/n^{3-\omega})(n^{3-\omega}/r)^{98/100}\) which is at most \(n^{3+o(1)}(r/n^{3-\omega})^{2/100}\) and thus dominated by the second term.

For the remainder of this section, we focus on the proof of Lemma 4.2. The reduction can be split into four individual steps, which we treat in Sections 4.1 to 4.4. See Figure 2 for an outline. Step 1 is new and can be regarded as one of the key technical parts of this paper. Steps 2 and 4 are already established in \[4\] and can be taken almost without modifications; we provide full proofs here for the sake of completeness and because we need appropriately generalized statements throughout (such as a rectangular version, and the assertion that all reductions are potential-adjusting). Step 3 could be taken as in \[4\], but we give an alternative proof that significantly improves the parameters (otherwise we would get the weaker statement that \(n^{3-\omega-\epsilon}\)-rank Exact Triangle can be solved in time \(O(n^{3-\Omega_\epsilon(1)})\) where the hidden dependence on \(\epsilon\) is worse than \(\Omega(\epsilon)\)).

Throughout, we will consider the rectangular case of size \(n_1\times n_2\times n_3\). Moreover, we will often implicitly assume that the parameter in question (_r,d_ or _D_) satisfies that \(r\le n_1,n_2,n_3\). This is without loss of generality, as all algorithms we consider spend time at least \(\Omega(r\cdot(n_1n_2+n_1n_3+n_2n_3))\), and hence if the assumption was violated we could alternatively solve the instance naively in time _O(n_<sub>1</sub>_n_<sub>2</sub>_n_<sub>3</sub>).

## 4.1 Reduction from Low-Rank to Slice-Uniform Exact Triangle

The following lemma captures the first step in our chain of reductions. An important ingredient for its proof is the previously established Lemma 3.6.

**Lemma 4.4** (Reduction from Low-Rank to Slice-Uniform Exact Triangle)**.** _For any parameter_ \(t\ge 1\) _there is a potential-adjusting reduction from any_ rank-_r Exact Triangle instance to O(t_<sup>2</sup>log_r_) _r_-slice-uniform _instances. The reduction runs in deterministic time_ \(\tilde{O}(n_1n_2n_3/t+(n_1n_2+n_2n_3+n_1n_3)rt^2)\)_. In particular:_<tbc>

\(\mathrm{ExactTri}(n_1,n_2,n_3|r)\le\tilde{O}\big(t^2\cdot\mathrm{ExactTri}(n_1,n_2,n_3|d\le r)+\frac{n_1n_2n_3}{t}+(n_1n_2+n_2n_3+n_1n_3)rt^2\big).\)

Low-Rank
Slice-Uniform
Uniform
Uniform
Uniform
Low-Doubling
r < n3-w-E
d < n3-w-E
D < n3-w-E
Regular
D < n3-w-E
D < n3-w-E
Section 4.1
Section 4.2 [4]
p < 1/D
K < n e'
Section 4.3
Section 4.4 [4]

**Figure 2.** Illustrates the four steps in the reduction from Low-Rank Exact Triangle to Uniform Low- Doubling Exact Triangle. (The dashed arrow symbolizes a recursive dependence; see Section 4.3.)

