_Case 1:_ This case considers \(|\sigma_w(z)-x|>(\frac{15}{1-\rho}\rho+8)w\). Using the triangle inequality, the fact that _y_ is good w.r.t. _w_, \(|\tau_w(y)-y|\le\rho\frac{w}{2}\) , and the definition on _Y_ , we have:

\(|\sigma_w(y)-x|\le|\sigma_w(y)-y|+|y-\tau_w(y)|+|\tau_w(y)-x|\)<br>
\(\le w+\rho\frac{w}{2}+\left(\frac{15}{1-\rho}\rho+4\right)w=\left(\frac{15}{1-\rho}\rho+\frac{\rho}{2}+5\right)w.\)

Then, all elements _z_ with \(\sigma_w(z)<x-(\frac{15}{1-\rho}\rho+8)w\) (resp. \(\sigma_w(z)>x+(\frac{15}{1-\rho}\rho+8)w\)) are necessarily smaller than (resp. larger than) _y_. Indeed, \(\sigma_w(z)<x-(\frac{15}{1-\rho}\rho+8)w\le\sigma_w(y)-(3-\frac{\rho}{2})w<\sigma_w(y)-2w\) (resp. \(\sigma_w(z)>x+(\frac{15}{1-\rho}\rho+8)w\ge\sigma_w(y)+(3-\frac{\rho}{2})w>\sigma_w(y)+2w\)), and the fact that _y_ is happy w.r.t. _w_ implies _z\<y_ (resp. _z\>y_).

From the above discussion, we know that if \(z<y-\rho w\), then we must have \(\sigma_w(z)<x-(\frac{15}{1-\rho}\rho+8)w\) (since if \(\sigma_w(z)>x+(\frac{15}{1-\rho}\rho+8)w\), then _z\>y_). Using Lemma 5.2, we obtain \(\tau_w(z)<\sigma_w(z)+4w<x-(\frac{15}{1-\rho}\rho+4)w\le\tau_w(y)\), implying that \(\sigma_{\lfloor\rho w\rfloor}(z)<\sigma_{\lfloor\rho w\rfloor}(y)\). Symmetrically, if \(z>y+\rho w\), we must have \(\sigma_w(z)>x+(\frac{15}{1-\rho}\rho+8)w\), which implies \(\tau_w(z)>\sigma_w(z)-4w>x+(\frac{15}{1-\rho}\rho+4w)\ge\tau_w(y)\) and hence \(\sigma_{\lfloor\rho w\rfloor}(z)>\sigma_{\lfloor\rho w\rfloor}(y)\).

_Case 2:_ This case considers \(|\sigma_w(z)-x|\le(\frac{15}{1-\rho}\rho+8)w\). Notice that \(z\in Y\) and hence \(|\tau_w(z)-z|\le\rho\frac{w}{2}\) . If \(z<y-\rho w\), then \(\tau_w(z)\le z+\rho\frac{w}{2}<y-\rho\frac{w}{2}\le\tau_w(y)\), where the last inequality holds since \(|\tau_w(y)-y|\le\rho\frac{w}{2}\) . Using \(\tau_w(z)<\tau_w(y)\), we have \(\sigma_{\lfloor\rho w\rfloor}(z)<\sigma_{\lfloor\rho w\rfloor}(y)\) as desired. Symmetrically, if \(z>y+\rho w\), then \(\tau_w(z)\ge z-\rho\frac{w}{2}>y+\rho\frac{w}{2}\ge\tau_w(y)\), which implies \(\sigma_{\lfloor\rho w\rfloor}(z)>\sigma_{\lfloor\rho w\rfloor}(y)\) as desired. □

Lemma 5.14. _Let x be an element that satisfies_ (⋆) _w.r.t. w and assume that all elements z with_ \(|\sigma_w(z)-z|\le x-(\frac{15}{1-\rho}\rho+8)w\) _satisfy_ \(|\tau_w(z)-z|\le\rho\frac{w}{2}\) _. Then, x satisfies_ (⋆) _w.r.t._ \(\lfloor\rho w\rfloor\).

Proof. By Lemma 5.13, _x_ satisfies condition (a) of (⋆) w.r.t. \(\lfloor\rho w\rfloor\), and therefore we only need to prove that _x_ also satisfies condition (b).

Let _T_ be the set of all elements _y_ with \(|\sigma_{\lfloor\rho w\rfloor}(y)-x|\le(\frac{15}{1-\rho}-3)\lfloor\rho w\rfloor\). For any element \(y\in T\), we have \(|\sigma_w(y)-\sigma_{\lfloor\rho w\rfloor}(y)|\le 8w\) (see Lemma 5.4), and thus \(|\sigma_w(y)-x|\le(\frac{15}{1-\rho}-3)\rho w+8w\le(\frac{15}{1-\rho}-3)w\), implying that _y_ is both happy and good w.r.t. _w_ (since _x_ satisfies (⋆)).

Focus on an element \(y\in T\). We want to show that any element _z_ such that \(\sigma_{\lfloor\rho w\rfloor}(z)<\sigma_{\lfloor\rho w\rfloor}(y)-2\lfloor\rho w\rfloor\) (resp. \(\sigma_{\lfloor\rho w\rfloor}(z)>\sigma_{\lfloor\rho w\rfloor}(y)+2\lfloor\rho w\rfloor\)) must be smaller (resp. larger) than _y_ (w.r.t. the true order of the elements). This immediately implies that _y_ is happy w.r.t. \(\lfloor\rho w\rfloor\), hence the claim follows.

In the rest of the proof, we only argue about elements _z_ such that \(\sigma_{\lfloor\rho w\rfloor}(z)<\sigma_{\lfloor\rho w\rfloor}(y)-2\lfloor\rho w\rfloor\) as symmetric arguments hold for \(\sigma_{\lfloor\rho w\rfloor}(z)>\sigma_{\lfloor\rho w\rfloor}(y)-2\lfloor\rho w\rfloor\).

We start with some preliminary observations: first of all, recall that all elements \(y'\) with \(|\sigma_{\lfloor\rho w\rfloor}(y')-x|\le\frac{15}{1-\rho}\lfloor\rho w\rfloor\) are good w.r.t. \(\lfloor\rho w\rfloor\) by Lemma 5.13, and, since the set of these elements is a su perset of _T_, _y_ is good w.r.t. \(\lfloor\rho w\rfloor\). Moreover, we can upper bound \(\sigma_{\lfloor\rho w\rfloor}(z)\) by writing \(\sigma_{\lfloor\rho w\rfloor}(z)<\sigma_{\lfloor\rho w\rfloor}(y)-2\lfloor\rho w\rfloor\le x+(\frac{15}{1-\rho}-5)\lfloor\rho w\rfloor\), and thus all _z_ with \(|\sigma_{\lfloor\rho w\rfloor}(z)-x|\le\frac{15}{1-\rho}\lfloor\rho w\rfloor\) immediately satisfy _z\<y_. Indeed, any such _z_ is good w.r.t. \(\lfloor\rho w\rfloor\) as _x_ satisfies condition (a) of (⋆), and thus \(z\le\sigma_{\lfloor\rho w\rfloor}(z)+\lfloor\rho w\rfloor<\sigma_{\lfloor\rho w\rfloor}(y)-\lfloor\rho w\rfloor\le y\).

As a consequence, it remains to analyze the case \(|\sigma_{\lfloor\rho w\rfloor}(z)-x|>\frac{15}{1-\rho}\lfloor\rho w\rfloor\), and we henceforth further restrict ourselves to the elements _z_ for which \(\sigma_{\lfloor\rho w\rfloor}(z)<x-\frac{15}{1-\rho}\lfloor\rho w\rfloor\).<sup>6</sup><tbc>

<sup>6</sup>Since \(y\in T\), we have \(\sigma_{\lfloor\rho w\rfloor(y)}+3\lfloor\rho w\rfloor\le x+\frac{15}{1-\rho}\lfloor\rho w\rfloor\). Thus, any element _z_ with \(\sigma_{\lfloor\rho w\rfloor}(z)>x+\frac{15}{1-\rho}\lfloor\rho w\rfloor\) satisfies \(\sigma_{\lfloor\rho w\rfloor}(z)\ge\sigma_{\lfloor\rho w\rfloor(y)}+3\lfloor\rho w\rfloor>\sigma_{\lfloor\rho w\rfloor(y)}-2\lfloor\rho w\rfloor\), and does not need to be considered.

