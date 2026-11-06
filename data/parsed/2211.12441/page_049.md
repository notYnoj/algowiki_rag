_Proof._ By definition, the condition that \(\ell\in N(A)\) is that any \(\ell\)-interval _J_ is contained in some _k_-interval for some \(k\in A\). By condition (2) in Proposition 71, this is equivalent to saying Int(_J_) is contained in some _k_-interval, where Int(_J_) is the interior of _J_. This is true if and only if any open subinterval _I_ of Int(_J_) is contained in some _k_-interval. Equivalently, if _I_ is an open interval that is not contained in any _k_-interval, then _I_ is not contained in any \(\ell\)-interval. Using condition (3) in Proposition 71, this is finally equivalent to the condition that if _I_ contains a fraction of denominator _k_ for every \(k\in A\), then _I_ contains a fraction of denominator \(\ell\).

The characterization in Claim 70 allows us to prove the following key claim about _N(A_).

**Claim 72.** _If_ \(\ell_1,\ell_2\in N(A)\)_, then_ \(\ell_1+\ell_2\in N(A)\).

_Proof._ By Claim 70, any interval _I_ that contains a fraction of denominator _k_ for every \(k\in A\) must also contain two fractions \(x/\ell_1\) and \(y/\ell_2\). For positive integers _a,b,c,d_, define the _mediant_ of _a/b_ and _c/d_ to be (_a+c)/(b+d_). Then the mediant is always between the two fractions. In other words, if \(a/b\le c/d\),

\(\frac{a}{b}\le\frac{a+c}{b+d}\le\frac{c}{d}.\)

This fact can be proven with elementary algebra, as both sides are equivalent to \(a/b\le c/d\).

From this, we see that the mediant \((x+y)/(\ell_1+\ell_2)\) is contained in _I_, as it is between two elements of _I_. As this applies to every such _I_, we can use Claim 70 to conclude that \(\ell_1+\ell_2\in N(A)\).

Note that \(x/\ell_1\) and \(y/\ell_2\) do not have to be distinct. \(\ell_1\) and \(\ell_2\) might be equal, or \(x/\ell_1=y/\ell_2\).

As _k_ encloses _k_ for every _t_, we have that \(A\subseteq N(A)\). Let Sums(_A_) be the set of positive integers that can be written as the sum of not necessarily distinct elements of _A_. Claim 72 implies that \(\mathrm{Sums}(A)\subseteq N(A)\).

**Claim 73.** _For nonnegative integers n,_

\(|\mathrm{Sums}(A)\cap\{n+1,\dots,n+a\}|\ge|A|.\)

_Proof._ Let _m_=max(_A_). Because \(A\subseteq\mathrm{Sums}(A)\), Sums(_A_) contains every positive integer congruent to an element of _A_ modulo _m_, since we can repeatedly add _m_ to any element of _A_. As \(a\ge m\), the set {_n_+1_,...,n+a_} contains at least one element for every residue mod _m_. Therefore, Sums(_A_) contains at least |_A_| elements of {_n_+1_,...,n+a_}.

Putting it all together, we have that

\(|A|\le|\mathrm{Sums}(A)\cap\{b+1,\dots,b+a\}|\le|N(A)\cap\{b+1,\dots,b+a\}|\le|N_t(A)|,\)

which proves Lemma 67 by our previous reasoning. To finish, we need to show that this implies Lemma 65.

**Claim 74.** _Lemma 67 implies Lemma 65._

_Proof._ We prove the following more general claim. Let \(f:\mathbb{R}\rightarrow\mathbb{R}\) be a function that has period 1, and additionally, _f_ is concave on \[0,1\] and _f_(0)=_f_(1)=0. For \(t\in[0,1]\), let \(\beta_t\) be a bijection that satisfies the conditions of Lemma 67. Then for any \(k\in\{1,\dots,a\}\), let \(\ell=\beta_t(k)\). We seek to prove that<tbc>

\(\frac{f(kt)}{k}\ge\frac{f(\ell t)}{\ell}\)

