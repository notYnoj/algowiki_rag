## 4.4.1. _Uniform Stirling decomposition._

**Lemma 4.2** (Uniform Stirling decomposition)**.** _Let_ \(L\ge 1\) _and_ \(\mu\in\mathcal{M}_L\) _with multiplicities_ \(n_{a,b}:=L\mu(a,b)\)_. Let_ \(D:=\{(a,b):n_{a,b}\ge 1\}\) _and s_:=|_D|. Then_

(4.9) \(log|\mathcal{S}_{L-1}(\mu)|=LH(\mu)+\frac{1}{2}log(2\pi L)-\frac{1}{2}\sum_{(a,b)\in D}log(2\pi n_{a,b})+\rho_L(\mu),\)

_where the remainder satisfies the explicit bounds_

(4.10) \(-\sum_{(a,b)\in D}\frac{1}{12n_{a,b}}\le\rho_L(\mu)\le\frac{1}{12L}.\)

_Proof._ Apply the explicit Stirling bounds (valid for all integers \(k\ge 1\)),

\(\sqrt{2\pi k}\big(\frac{k}{e}\big)^k\le k!\le\sqrt{2\pi k}\big(\frac{k}{e}\big)^ke^\frac{1}{12k},\)

to \(log|\mathcal{S}_{L-1}(\mu)|=logL!-\sum_{(a,b)\in D}log(n_{a,b}!)\), and use \(LlogL-\sum_{a,b}n_{a,b}logn_{a,b}=LH(\mu)\). □

## 4.4.2. _Support bound and subexponential number of types._

For each _M_, we define the alphabet \(\mathcal{A}_M:=\big\{(a,b)\in\mathbb{N}_{>0}^2:1\le b\le a\le N+1\big\}\), with<tbc>

\(K_M:=|\mathcal{A}_M|=\sum_{a=1}^{N+1}a=\frac{(N+1)(N+2)}{2}.\)

<tbc>Let I_<sub>M</sub>_ denote the set of pairs \((L,\mu)\) that appear in (4.7), i.e.,<tbc>

\(\mathcal{I}_M:=\big\{(L,\mu):L\in\{1,\dots,M\},\mu\in\mathcal{M}_L,supp(\mu)\subseteq\mathcal{A}_M,\mathbb{E}_\mu[a]=\frac{N+1}{L},\mathbb{E}_\mu[b]=\frac{M+1}{L}\big\}.\)

<tbc>**Lemma 4.3** (Support bound)**.** _Let_ \((L,\mu)\in\mathcal{I}_M\)_, and write_ \(D:=supp(\mu)\)_. Then_<tbc>

(4.11) \(|D|\le\frac{1}{2}\big(\sqrt{3\sqrt{3(N+1)}}+2\big)^2.\)

<tbc>_Proof._ Each distinct symbol (_a,b_) in _D_ appears at least once, hence

(4.12) \(\sum_{(a,b)\in supp(\mu)}a\le\sum_{k=1}^La_k=N+1.\)

For each \(a\ge 1\) there are exactly _a_ choices of \(b\in\{1,\dots,a\}\), and each such candidate pair (_a,b_) has "cost" _a_. We respectively denote the number of pairs with cost \(\le t\) and the total cost of all of them via<tbc>

\(N(t):=\sum_{a=1}^ta=\frac{t(t+1)}{2};C(t):=\sum_{a=1}^ta^2=\frac{t(t+1)(2t+1)}{6}.\)

<tbc>If _s_=|_D_|, let _t_ be the smallest integer with \(N(t)\ge s\), so that _N(t_-1)_\<s_. Then any set of _s_ pairs has total cost at least _C(t_-1). Hence

\(C(t-1)\le\sum_{(a,b)\in supp(\mu)}a\le^{(4.12)}N+1.\)

Using \(C(u)\ge u^3/3\) for \(u\ge 1\) gives \((t-1)^3/3\le N+1\), so \(t\le\sqrt{3\sqrt{3(N+1)}}+1\). Finally,

\(s\le N(t)=\frac{t(t+1)}{2}\le\frac{(t+1)^2}{2}\le\frac{1}{2}\big(\sqrt{3\sqrt{3(N+1)}}+2\big)^2,\)

producing the desired bound. □

