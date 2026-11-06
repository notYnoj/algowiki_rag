By Lemma 5.4, we have that \(\sigma_w(z)<\sigma_{\lfloor\rho w\rfloor}(z)+8w<x-(\frac{15}{1-\rho}\rho-8)w\). To conclude the proof we separately consider three cases depending on the value of \(\sigma_w(z)\).

_Case 1:_ The first case considers \(\sigma_w(z)<x-\frac{15}{1-\rho}w\). From \(\sigma_w(y)\ge x-(\frac{15}{1-\rho}-3)w\), we have \(x-\frac{15}{1-\rho}\le\sigma_w(y)-3w\), i.e., \(\sigma_w(z)<\sigma_w(y)-3w\), which implies _z\<y_ since _y_ is happy.

_Case 2:_ The second case considers \(x-\frac{15}{1-\rho}w\le\sigma_w(z)<x-(\frac{15}{1-\rho}\rho+1)w\). In this case, _z_ is good w.r.t. _w_, as ensured by condition (a) of (<tbc>

<tbc>⋆) from the hypothesis of this lemma and by \(\frac{15}{1-\rho}>\frac{15}{1-\rho}\rho+1\). Thus, we have \(z\le\sigma_w(z)+w<x-\frac{15}{1-\rho}\rho w\le x-(\frac{15}{1-\rho}-3)\rho w-\lfloor\rho w\rfloor\le\sigma_{\lfloor\rho w\rfloor}(y)-\lfloor\rho w\rfloor\le y\), where we relied on the definition of _T_ and the fact that _y_ is good w.r.t. \(\lfloor\rho w\rfloor\).

_Case 3:_ The third and final case considers \(x-(\frac{15}{1-\rho}\rho+1)w\le\sigma_w(z)<x-(\frac{15}{1-\rho}\rho-8)w\). By condition (a) of (<tbc>

<tbc>⋆), _z_ is good w.r.t. _w_, and thus \(x-(\frac{15}{1-\rho}\rho+2)w\le z<x-(\frac{15}{1-\rho}\rho-9)w\). Moreover, by the assumption of the lemma, \(x-(\frac{15}{1-\rho}\rho+2+\frac{\rho}{2})w\le\tau_w(z)\le x-(\frac{15}{1-\rho}\rho-9-\frac{\rho}{2})w\), and further by Lemma 5.13, _z_ is good w.r.t. \(\lfloor\rho w\rfloor\), implying that \(|\sigma_{\lfloor\rho w\rfloor}(z)-z|\le\lfloor\rho w\rfloor\). Since \(|\sigma_{\lfloor\rho w\rfloor}(y)-y|\le\lfloor\rho w\rfloor\) (as explained before) and \(\sigma_{\lfloor\rho w\rfloor}(z)<\sigma_{\lfloor\rho w\rfloor}(y)-2\lfloor\rho w\rfloor\), we have that \(z\le\sigma_{\lfloor\rho w\rfloor}(z)+\lfloor\rho w\rfloor<\sigma_{\lfloor\rho w\rfloor}(y)-\lfloor\rho w\rfloor\le y\). □

Lemma 5.15. _Let w and w_<sup>∗</sup> _be two window sizes satisfying_ \(\frac{4}{\kappa(p,q,\rho)}\cdot ln\lfloor\rho w\rfloor\le w^*\le w\) _and_ \(w\ge 4\)_. If_ (<tbc>

<tbc>⋆) _holds for an element x w.r.t. w, then_ (<tbc>

<tbc>⋆) _holds for x w.r.t. all window sizes that are at least w_<sup>∗</sup> _and at most w with probability at least_ \(1-\frac{69120}{(1-\rho)^3w^2}\).

Proof. Suppose that (<tbc>

<tbc>⋆) holds for _x_ w.r.t. a generic window size \(w'\) such that \(w^*\le w'\le w\). The probability that (<tbc>

<tbc>⋆) fails for _x_ w.r.t. \(\lfloor\rho w'\rfloor\) is at most the probability that the hypothesis of Lemma 5.14 does not hold, i.e., the probability \(P(w')\) that there exists an element _y_ with \(\sigma_{w^\prime}(y)\in[x-(\frac{15}{1-\rho}\rho+8)w',x+(\frac{15}{1-\rho}\rho+8)w']\) such that \(|\tau_{w^\prime}(y)-y|>\rho\frac{w'}{2}\) .

Recall the definition of _B<sub>i</sub>_, _B_ and _B_<sup>+</sup> in Section 5.1 and Section 5.2. In order to apply Lemma 5.9, we consider the basket _B<sub>i</sub>_ of \(\sigma_{w^\prime}\) that contains _y_, i.e., \(max\{(i-1)\cdot w',0\}+1\le\sigma_{w^\prime}(y)\le min\{i\cdot w',m\}\). Lemma 5.9 requires that the up to \(7w'\) elements in _B_ are happy w.r.t. \(w'\) and that the up to \(13w'\) elements in _B_<sup>+</sup> are good w.r.t. \(w'\). By the definition of _B_ and _B_<sup>+</sup>, any element _z_ in _B_ satisfies \(|\sigma_{w^\prime}(z)-\sigma_{w^\prime}(y)|\le 4w'\) and any element \(z'\) in _B_<sup>+</sup> satisfies \(|\sigma_{w^\prime}(z')-\sigma_{w^\prime}(y)|\le 7w'\). Since \(\sigma_{w^\prime}(y)\in[x-(\frac{15}{1-\rho}\rho+8)w',x+(\frac{15}{1-\rho}\rho+8)w']\) and \([x-(\frac{15}{1-\rho}\rho+8+7)w',x+(\frac{15}{1-\rho}\rho+8+7)w']=[x-\frac{15}{1-\rho}w',x+\frac{15}{1-\rho}w']\), the fact that (<tbc>

<tbc>⋆) holds w.r.t. \(w'\) immediately implies that the hypotheses of Lemma 5.9 are met.

Therefore, by Lemma 5.9, Lemma 5.14, and by using the union bound over the (at most) \(2\left(\frac{15}{1-\rho}\rho+8\right)w'+1\) elements _y_ with \(\sigma_{w^\prime}(y)\in[x-(\frac{15}{1-\rho}\rho+8)w',x+(\frac{15}{1-\rho}\rho+8)w']\), we have:

\(P(w')\le\left(2\left(\frac{15}{1-\rho}\rho+8\right)w'+1\right)\cdot 9w'exp(-w'\cdot\kappa(p,q,\rho))\)<br>
\(\le\left(2\left(\frac{15}{1-\rho}\rho+8\right)w'+1\right)\cdot 9w'exp(-4ln\lfloor\rho w\rfloor)\)<br>
\(\le\frac{18\left(\frac{15}{1-\rho}\rho+9\right)(w')^2}{\lfloor\rho w\rfloor^4}<\frac{256\cdot 18\left(\frac{15}{1-\rho}\right)(w')^2}{w^4}=\frac{69120(w')^2}{(1-\rho)w^4},\)

where \(\frac{15}{1-\rho}\rho+9<\frac{15}{1-\rho}\) and \(\lfloor\rho w\rfloor^4\le(\rho w-1)^4\le\frac{\rho^4w^4}{16}\le\frac{w^4}{256}\) since \(\lfloor\rho w\rfloor\ge\lfloor\frac{4}{2}\rfloor=2\).

Let _r_ denote the number of iterations of BasketSort having a window size between _w_ (included) and _w_<sup>∗</sup> (excluded). The probability that condition (<tbc>

<tbc>⋆) fails for _x_ w.r.t. at least one such window<tbc>

