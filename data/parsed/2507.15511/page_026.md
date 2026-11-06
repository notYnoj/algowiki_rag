which is asymptotically equivalent to the sum form \(O\big((U_0+U_1)\cdot n^2\big)\) and \(O\big((U_0+U_1)\cdot n\big)\) stated in Theorem 4. Space is \(O\big((U_0+U_1)\cdot n\big)\) for storing canonical bitmasks.

### With Controlled Aliasing (CNF).

Let _E<sub>i</sub>_ be the number of _expanded_ states on half _i_ under CNF. By Lemma 9, \(E_i\le\frac{3}{4}\cdot 2^{|\ell_i|}=\frac{3}{4}\cdot 2^{n/2}\) in the worst case. Substituting _E<sub>i</sub>_ for _U<sub>i</sub>_ in the same accounting yields

\(T_\mathrm{det}(n)=O\big(\mathrm{max}(E_0,E_1)\cdot n^2\big)=O^*\big(2^{n/2-\mathrm{log}_2(4/3)}\big),\)<br>
\(\mathbb{E}\big[T_\mathrm{rand}(n)\big]=O\big(\mathrm{max}(E_0,E_1)\cdot n\big)=O^*\big(2^{n/2-\mathrm{log}_2(4/3)}\big),\)

matching Theorem 6. Space remains _O_<sup>∗</sup>(2<sup>_n/_2</sup>), since each aliased key stores up to two canonical masks (one per lane \(\chi\in\{0,1\}\)).

### Optimality (Conditional).

Under Conjecture 1, the randomized solver is optimal up to constants in the local deduplicating model, achieving \(\Theta(U\cdot n)\) expected time (Theorem 3). The deterministic \(O(U\cdot n^2)\) bound leaves a polynomial gap, whose removal would require a deterministic sublinear-time canonicality test per extension.

_Summary._ The interleaved double-meet-in-the-middle framework, combined with (i) lex-minimal canonicalization with suppression-on-overwrite and (ii) the CNF expansion gate under Controlled Aliasing, yields (a) certificate-sensitive runtimes scaling with _U_<sub>0</sub>_,U_<sub>1</sub> and (b) a strict worst-case improvement below 2<sup>_n/_2</sup> on _all_ inputs.

## C Compositional Sum Lemmas and Complement Check

These lemmas govern how partial sums are combined across recursive calls and meet-in-the-middle partitions. They apply to both aliasing and non-aliasing regimes and are invoked by all canonical certificate routines to ensure uniqueness and correctness.

Let \(\ell_0,\ell_1\) be the two halves of a split of _S_, and write \(\Sigma(\ell_i)\) for the set of distinct subset sums produced by the enumerator on side _i_.

_Lemma_ 1 (Direct Match in One Half). _A subset_ \(A\subseteq\ell_i\) _is a witness to_ (_S,t_) _if_<tbc>

\(\sigma(A)=t.\)

<tbc>_Lemma_ 2 (Self-Complement Match). _A subset_ \(A\subseteq\ell_i\) _solves_ (_S,t_) _if_<tbc>

\(\sigma(\ell_i\backslash A)=\sigma(\ell_i)-t.\)

<tbc>_Lemma_ 3 (Cross-Half Direct Match). _For subsets_ \(A\subseteq\ell_0\) _and_ \(B\subseteq\ell_1\),<tbc>

\(\sigma(A)+\sigma(B)=t\Longleftrightarrow t-\sigma(A)\in\Sigma(\ell_1).\)

<tbc>_Lemma_ 4 (Double Complement Match). _If subsets_ \(A\subseteq\ell_0\) _and_ \(B\subseteq\ell_1\) _satisfy_<tbc>

\(\sigma(\ell_0\backslash A)+\sigma(\ell_1\backslash B)=\sigma(S)-t,\)

<tbc>_then_ \(S\backslash(A\cup B)\) _is a witness (i.e., sums to t). Equivalently,_<tbc>

\(\sigma(\ell_0\backslash A)+\sigma(\ell_1\backslash B)=\sigma(S)-t\Longleftrightarrow\sigma(A)+\sigma(B)=t.\)

