<tbc>_n/_10+_r\<c\<_9_n/_10-_r_, _c\<r-n/_10, or _c\>_11_n/_10-_r_ will also satisfy \((r,c)\in S\). In any case, there are more than _n/_2 elements \(c\in[n]\) such that \((r,c)\in S\). □

**Claim 4.10.** _For every_ \((r,c)\in[n]^2\) _there are at least n_<sup>2</sup>/5 _positions_ \((x,y)\in[n]^2\) _such that_ (_r,y_) _and_ (_x,c_) _are balanced and_ (_r,c_) _and_ (_x,y_) _do not share a line._

_Proof._ Let \((r,c)\in[n]^2\). Let \(S_r:=\{y:(r,y)\in S,y\neq c\}\) and \(S_c:=\{x:(x,c)\in S,x\neq r\}\). By Claim 4.9, \(|S_r|,|S_c|\ge n/2-1\). Now, let

\(S_{(r,c)}:=(S_c\times S_r)\backslash(\ell_1(r,c)\cup\ell_2(r,c)).\)

We note that \(|S_{(r,c)}|\ge(n/2-1)^2-2n\ge n^2/5\). Also, by definition, if \((x,y)\in S_{(r,c)}\) then it does not share a line with (_r,c_). Next, we argue that for every \((x,y)\in S_{(r,c)}\), it holds that (_r,y_) and (_x,c_) are both balanced. Indeed, if \((x,y)\in S_{(r,c)}\), then (again by definition) \(x\in S_c\). Therefore \((x,c)\in S\) and so by Claim 4.9 is balanced. Similarly, \((r,y)\in S\) and hence is balanced as well. □

In order to prove Lemma 4.3 we will use the following bounded-differences inequality.

**Theorem 4.11** (\[14\] Corollary 1.4)**.** _Let X_<sub>1</sub>_,...,X<sub>N</sub> be i.i.d. Bernoulli random variables with_ P\[_X_<sub>1</sub>=1\]=_p. Assume that for K\>_0 _the function_ \(f:\{0,1\}^N\rightarrow\mathbb{R}\) _satisfies the Lipschitz condition_ \(|f(\omega)-f(\omega')|\le K\) _whenever_ \(\omega,\omega'\in\{0,1\}^N\) _differ by a single coordinate. Then, for all t\>_0:<tbc>

\(\mathbb{P}\left[|f(X_1,\dots,X_N)-\mathbb{E}\left[f(X_1,\dots,X_N)\right]|\ge t\right]\le 2exp\left(-\frac{t^2}{2N(1-p)pK^2+2Kt/3}\right).\)



Figure 2. Roughly speaking, _balanced_ means not too close to the main diagonals. In the \(20\times 20\) array above the set _S_ of balanced positions is

shaded.

