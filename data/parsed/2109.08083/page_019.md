<tbc>Let _f(n_) and _g(n_) be functions of _n_. Then we say that,

(i) _f(n_)=_o(g(n_)) (as \(n\rightarrow\infty\)) if for every \(\alpha>0\), there exists _n_<sub>0</sub>_\>_0 such that \(|f(n)|\le\alpha|g(n)|\) for every \(n\ge n_0\).<tbc>

(ii) We write that _f(n_)=_O(g(n_)) (as \(n\rightarrow\infty\)) if there exist _M,n_<sub>0</sub>_\>_0 such that \(|f(n)|\le M|g(n)|\) for every \(n\ge n_0\).<tbc>

(iii) We write that \(f(n)=\omega(g(n))\) (as \(n\rightarrow\infty\)) if _g(n_)=_o(f(n_)).<tbc>

(iv) We write that \(f(n)=\Omega(g(n))\) (as \(n\rightarrow\infty\)) if _g(n_)=_O(f(n_)).<tbc>

(v) \(f(n)=\Theta(g(n))\) (as \(n\rightarrow\infty\)) if _f(n_)=_O(g(n_)) and \(f(n)=\Omega(g(n))\).

Throughout we shall also write \(f(n)\checkmark g(n)\) to mean that _f(n_)=_o(g(n_)) and naturally also \(f(n)\gg g(n)\) to mean that _g(n_)=_o(f(n_)).

## 2.2. Inequalities and Bounds

It will be convention to omit floor and ceiling signs unless crucial to an argument. We write \(x=a\pm b\) to mean that \(x\in[a-b,a+b]\) when \(b\ge 0\), and \(x\in[a+b,a-b]\) when _b\<_0.

The following inequalities and bounds are used in various places throughout.

Proposition 2.1. _For all_ \(x\in(-1,\infty]\), \(\mathrm{log}(1+x)\le x\).

Proposition 2.2. _Take n sufficiently large and let_ \(p(i):=1-\frac{i}{n}\)_. Then for every_ \(1>\alpha>0\), \(\sum_{i=0}^{n-n^{1-\alpha}-1}\mathrm{log}(p(i))=n(-1+O(n^{-\alpha}\mathrm{log}(n)))\).

Proof. We have that

\(\int_{n^{-\alpha}}^1\mathrm{log}(x)\mathrm{d}x\le\frac{1}{n}\sum_{i=0}^{n-n^{1-\alpha}-1}\mathrm{log}(p(i))\le\int_{n^{-\alpha}+n^{-1}}^{1+\frac{1}{n}}\mathrm{log}(x)\mathrm{d}x\)<br>
\(\le\int_{n^{-\alpha}+n^{-1}}^1\mathrm{log}(x)\mathrm{d}x+O(n^{-2}).\)

Then

\(\frac{1}{n}\sum_{i=0}^{n-n^{1-\alpha}-1}\mathrm{log}(p(i))=\int_{n^{-\alpha}}^1\mathrm{log}(x)\mathrm{d}x\pm\left(\int_{n^{-\alpha}}^{n^{-\alpha}+n^{-1}}\mathrm{log}(x)\mathrm{d}x+O(n^{-2})\right)\)<br>
\(=\int_{n^{-\alpha}}^1\mathrm{log}(x)\mathrm{d}x+O(n^{-\alpha}\mathrm{log}(n))=-1+O(n^{-\alpha}\mathrm{log}(n)).\)

Rearranging gives the result. □

**2.2.1. Probabilistic bounds.** Various results rely on probabilistic arguments requiring knowledge of the following bounds. We say that an event _A_ holds _with high probability_ (_whp_) if there exists some \(\alpha>0\) such that \(\mathbb{P}(A)=1-e^{-\Omega(n^\alpha)}\) as \(n\rightarrow\infty\). Note that this is not the usual definition, but a stronger statement. In the following lemma, _B(n,p_) is the binomial distribution with parameters _n_ and _p_.

Lemma 2.3. (Chernoff’s inequality, e.g. \[**28**, Remark 2.8\]) _Suppose that_ \(X\in B(n,p)\)_. Then,_

\(\mathbb{P}(|X-\mathbb{E}(X)|\ge t)\le 2\mathrm{exp}\left(-\frac{2t^2}{n}\right)\)

_for every_ \(t\ge 0\).

