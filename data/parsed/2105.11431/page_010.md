choices of distinct \(a_1\in\ell_1^\mathrm{far}(r,y),a_2\in\ell_2^\mathrm{far}(r,y),b_1\in\ell_1^\mathrm{far}(x,c),b_2\in\ell_2^\mathrm{far}(x,c)\) that do not share a line with each other or with (_x,y_). Therefore:<tbc>

\(\mathbb{P}[B]\ge\left(|\ell_1^\mathrm{far}(r,y)||\ell_2^\mathrm{far}(r,y)||\ell_1^\mathrm{far}(x,c)||\ell_2^\mathrm{far}(x,c)|-O(n^3)\right)\left(p(1-p)^{4n}\right)^4\)<br>
\(\ge|\ell_1^\mathrm{far}(r,y)||\ell_2^\mathrm{far}(r,y)||\ell_1^\mathrm{far}(x,c)||\ell_2^\mathrm{far}(x,c)|\left(p(1-p)^{4n}\right)^4-O\left(\frac{1}{n}\right).\)

Note that if both _A_ and _B_ occur then \((x,y)\in\mathcal{S}_R(r,c)\). We observe that (_x,y_) is not contained in any of the lines \(\ell_1^\mathrm{far}(r,y),\ell_2^\mathrm{far}(r,y),\ell_1^\mathrm{far}(x,c),\ell_2^\mathrm{far}(x,c)\). Therefore \(\mathbb{P}[B|A]\ge\mathbb{P}[B]\). Hence

\(\mathbb{P}[(x,y)\in\mathcal{S}_R(r,c)]\ge\mathbb{P}\left[A\cap B\right]=\mathbb{P}[A]\mathbb{P}[B|A]\ge\mathbb{P}[A]\mathbb{P}[B]\)<br>
\(\ge p(1-p)^{4n}\left(|\ell_1^\mathrm{far}(r,y)||\ell_2^\mathrm{far}(r,y)||\ell_1^\mathrm{far}(x,c)||\ell_2^\mathrm{far}(x,c)|\left(p(1-p)^{4n}\right)^4-O\left(\frac{1}{n}\right)\right)\)<br>
\(\ge|\ell_1^\mathrm{far}(r,y)||\ell_2^\mathrm{far}(r,y)||\ell_1^\mathrm{far}(x,c)||\ell_2^\mathrm{far}(x,c)|p^5(1-p)^{20n}-O\left(\frac{1}{n^2}\right).\)

□

The preceding calculation suggests that we should consider positions (_x,y_) such that \(|\ell_1^\mathrm{far}(r,y)|,|\ell_2^\mathrm{far}(r,y)|,|\ell_1^\mathrm{far}(x,c)|,|\ell_2^\mathrm{far}(x,c)|,=\Omega(n)\). As we will apply Claim 4.6 with \(p=\Omega(1/n)\), this condition would imply that \(\mathbb{P}[(x,y)\in\mathcal{S}_R(r,c)]=\Omega(1/n)\). This motivates the next definition.

**Definition 4.7.** A position \((x,y)\in[n]^2\) is **balanced** if \(|\ell_1^\mathrm{far}(x,y)|,|\ell_2^\mathrm{far}(x,y)|\ge n/10\).

We will now show that for every \((r,c)\in[n]^2\) there are \(\Omega(n^2)\) positions \((x,y)\in[n]^2\) such that (_r,c_) and (_x,y_) do not share a line and (_r,y_) and (_x,c_) are both balanced. Let \(S\subseteq[n]^2\) be the set of positions (_x,y_) such that neither of

\(x-n/10\le y\le x+n/10,\frac{9}{10}n-x\le y\le\frac{11}{10}n-x\)

holds (see Figure 2).

**Claim 4.8.** _Let_ \((x,y)\in S\)_. Then_ (_x,y_) _is balanced._

_Proof._ For every \((x,y)\in[n]^2\), we have \(|\ell_1^\mathrm{far}(x,y)|=|x+y-(n+1)|\) and \(|\ell_2^\mathrm{far}(x,y)|=|x-y|\).

Let \((x,y)\in S\). Then, by definition, either _y\>x+n/_10 or _x\>y+n/_10. Both imply \(|\ell_2^\mathrm{far}(x,y)|=|x-y|>n/10\). Similarly, either _x+y\>_11_n/_10 or _x+y\<_9_n/_10. In the first case, _x+y_-(_n_+1)_\>n/_10-1. In the second, _x+y_-(_n_+1)_\<-n/_10-1. Both imply \(|\ell_1^\mathrm{far}(x,y)|=|x+y-(n+1)|\ge n/10\). □

**Claim 4.9.** _Each row and each column in_ \[_n_\]<sup>2</sup> _intersects S on at least n/_2 _positions._

_Proof._ Since _S_ is invariant under reflection along the _y=x_ axis it suffices to prove the claim for rows. _S_ is also invariant under the reflection \((r,c)\mapsto(n+1-r,c)\), so it suffices to prove the claim for rows \(r\le(n+1)/2\).

Let \(r\in[n]\) be at most (_n_+1)/2. We will show that row _r_ contains at least _n/_2 positions in _S_. Indeed, if \(1\le r\le n/10\) then for every 2_n/_10_\<c\<_8_n/_10, it holds that \((r,c)\in S\). Otherwise, \(n/10<r\le(n+1)/2\). In this case every _c_ satisfying one of<tbc>

