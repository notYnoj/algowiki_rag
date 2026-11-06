Equation (3) gives \(Z_1\equiv AP_1(\mathrm{mod}\varepsilon)\): the final endpoint product does not reach this range, and the contribution from _Q_ is divisible by \(\varepsilon\).

Once _Z<sub>j</sub>_ is known, subtract _W<sub>j</sub>_, discard the first _t_ coefficients, and take the next _s_ coefficients. In formulas, define the length-_s_ polynomial _Z_<sub>_j_+1</sub> by<tbc>

\([z^k]Z_{j+1}=[z^{k+t}](Z_j-W_j),0\le k<s,1\le j\le c.\)

<tbc>To verify this step, suppose \(Z_j\equiv AP_j(\mathrm{mod}\varepsilon)\). Then

\(Z_j-W_j=Z_j-AP_j+z^tAP_{j+1}-\varepsilon z^bAQ^{(j)}\)<br>
\(\equiv z^tAP_{j+1}(\mathrm{mod}\varepsilon).\)

Reading coefficients _t,...,t+s_-1 therefore recovers every coefficient of _AP_<sub>_j_+1</sub> modulo \(\varepsilon\). Induction yields \(Z_j\equiv AP_j(\mathrm{mod}\varepsilon)\) for all \(1\le j\le c+1\).

The encoding is linear in the right inputs. Every decoding step is a shift, a sum, a coefficient extraction, or multiplication by \(\varepsilon^{-1}\), so the combined decoder is linear in _W_<sub>1</sub>_,...,W<sub>c</sub>_. All _Z<sub>j</sub>_ are polynomial in \(\varepsilon\), since their recovery uses no division by \(\varepsilon\), and the middle output is exact. Hence the decoded map has no negative powers and equals the requested target modulo \(\varepsilon\). The left input is unchanged, and the only products computed are the _c_ sources _W<sub>j</sub>_.

For _c_=1 and _t=a_+2_b_-1, this specializes to the three-for-one degeneration of \[Ope26a, Lemma 4.2\]. We next transpose the packing to reverse the counts: _c_ middle products will compute _c_+1 middle products and one full product.

**Lemma 2.5** (Dual packing)**.** _Under the hypotheses of Lemma 2.4, there is a same-left packing modulo_ \(\varepsilon\) _of_

\(\big((\mathrm{Mid}_{a,b}(A,Q_i))_{i=1}^{c+1},\mathrm{Full}_{a,b}(A,P)\big)\)

_using c copies of_ Mid<sub>_a,b+t_</sub>_, with the same coefficient sizes_ \(p\times q,q\times r\).

_Proof._ Set \(\widetilde{A}(z)=\sum_{i=0}^{a-1}A_i^\mathsf{T}z^{a-1-i}\). For a fixed _A_, coefficient extraction gives, for every length \(\lambda\),

\(\mathrm{Full}_{a,\lambda}(\widetilde{A},\cdot)^\mathsf{T}=\mathrm{Mid}_{a,\lambda}(A,\cdot),\mathrm{Mid}_{a,\lambda}(\widetilde{A},\cdot)^\mathsf{T}=\mathrm{Full}_{a,\lambda}(A,\cdot).\)

Here transpose is taken over all scalar entries of the coefficient lists. For example, the _j_th coefficient of the first transpose is \(\sum_iA_iQ_{a-1+j-i}\). Apply the primal packing to \(\widetilde{A}\) and transpose its map from the entire list of right inputs to the entire list of outputs. That target map is block diagonal, with _c_+1 Full blocks and one Mid block. The displayed identities exchange each block and each source, for \(\lambda=b\) and _b+t_. Lemma A.1 swaps the encoder and decoder by transposition and preserves correctness modulo \(\varepsilon\).

## 2.3 Packing across variables

We now combine the two gadgets to amplify their gain. We first allow the positions of the full and middle ranges to depend on the target; the next subsection will put all targets into one common form.

Use 2_d_ variables _z_<sub>1</sub>_,...,z_<sub>2_d_</sub>. For \(I\subseteq[2d]\), let _F_<sub>_a,b,I_</sub>(_A,B_) compute the coefficients of _AB_ that are full in the variables indexed by _I_ and middle in the others. Precisely, _A_ has length _a_ in every variable, _B_ has length _b_ on _I_ and _s_ outside _I_, and the output consists of<tbc>

\(\big([\mathbf{z}^\unknown](AB)\big)_{\nu_k\in\{0,\dots,s-1\}(k\in I),\nu_k\in\{a-1,\dots,s-1\}(k\notin I)}.\)

