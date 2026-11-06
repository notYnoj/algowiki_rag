<tbc>size is at most:

\(\sum_{i=0}^{r-1}\frac{69120(\rho^iw)^2}{(1-\rho)w^4}\le\frac{69120}{(1-\rho)w^2}\cdot\sum_{i=0}^\infty\rho^{2i}=\frac{69120}{(1-\rho)(1-\rho^2)w^2}=\frac{69120}{(1-\rho)^3w^2}.\) □

## 5.3.1 A linear upper bound in expectation.

We prove a linear upper bound on the expected total dislocation by proving a constant upper bound on the expected dislocation of each element _x_.

Within this subsection, we assume that \(w_S\ge 4\) (since otherwise Lemma 5.5 ensures that the dislocation of _x_ is at most \(3+\frac{24}{1-\rho}\)). We define _w_<sub>0</sub>=_w<sub>S</sub>_, and for an integer \(i\ge 1\), we let \(w_i=\frac{4}{\kappa(p,q,\rho)}\cdot lnw_{i-1}\). Moreover, let _z_ be the smallest index for which _w_<sub>_z_+1</sub>_\<_4 or \(w_{z+1}>\frac{w_z}{2}\) , i.e., \(\frac{4}{\kappa(p,q,\rho)}lnw_z>\frac{w_z}{2}\) . Notice that we have \(w_i\ge 2w_{i+1}\) for _i_=0_,...,z_-1, \(w_z\ge 4\), and \(\frac{4}{\kappa(p,q,\rho)}lnw_z\ge\frac{w_z}{2}\) . Therefore, \(w_z\le\frac{8}{\kappa(p,q,\rho)}lnw_z\le\frac{8}{\kappa(p,q,\rho)}\sqrt{w_z}\), and hence \(w_z\le\frac{64}{\kappa(p,q,\rho)^2}\).

We group the rounds of `BasketSort` into _z_+1 phases as follows: phase 0 consists of the sole round with window size _w<sub>S</sub>_, while phase \(i\in\{1,\dots,z\}\) consists of all rounds that consider a window size that is smaller than _w_<sub>_i_-1</sub> and at least _w<sub>i</sub>_. Since \(\rho\ge\frac{1}{2}\), our choice of _w<sub>i</sub>_ ensures that each phase contains at least one round.

Given an element _x_, we say that _x_ satisfies (<tbc>

<tbc>⋆) _until phase i_ if _x_ satisfies (<tbc>

<tbc>⋆) w.r.t. all window sizes _w_ with \(w\ge w_i\). Notice that, since the dislocation of the input sequence is at most _w<sub>S</sub>_, all elements are both good and happy w.r.t. _w_<sub>0</sub>=_w<sub>S</sub>_ and hence _x_ always satisfies (<tbc>

<tbc>⋆) until phase 0. We say that _x violates_ (<tbc>

<tbc>⋆) in phase \(i\ge 1\) if _x_ does not satisfy (<tbc>

<tbc>⋆) until phase _i_ but it _x_ satisfies (<tbc>

<tbc>⋆) until phase _i_-1.<tbc>

<tbc>Lemma 5.16. _The probability that an element x violates_ (<tbc>

<tbc>⋆) _in phase_ \(i\in\{1,\dots,z\}\) _is at most_ \(\frac{69120}{w_{i-1}^2}\).

Proof. If _x_ violates (<tbc>

<tbc>⋆) in phase _i_, then _x_ satisfies (<tbc>

<tbc>⋆) until phase _i_-1. Therefore, we let _w_ be the smallest window size with \(w\ge w_{i-1}\), and we assume that _x_ satisfies (<tbc>

<tbc>⋆) w.r.t. _w_. Observe that our choice of _w_ ensures that \(\rho w<w_{i-1}\). Let _w_<sup>∗</sup> be the smallest window size such that \(w^*\ge w_i\). We have \(w^*\ge w_i\ge\frac{4}{\kappa(p,q,\rho)}\cdot logw_{i-1}\ge\frac{4}{\kappa(p,q,\rho)}\cdot ln\lfloor\rho w\rfloor\).

Then, Lemma 5.15 ensures that _x_ satisfies (<tbc>

<tbc>⋆) w.r.t. all window sizes between _w_ and _w_<sup>∗</sup> with probability at least \(1-\frac{69120}{(1-\rho)^2w^2}\ge 1-\frac{69120}{(1-\rho)^2w_{i-1}^2}\). □

Lemma 5.17. _The expected dislocation of each element x in S_<sub>0</sub> _is at most_ \(\frac{1152}{\kappa(p,q,\rho)^2(1-\rho)}+\frac{311040}{(1-\rho)^4}\).

Proof. Consider a phase \(i\in\{0,\dots,z\}\), let _w_ be the smallest window size such that \(w\ge w_i\), and observe that \(w\le\frac{w_i}{\rho}\le 2w_i\). If _x_ satisfies (<tbc>

<tbc>⋆) until phase _i_, then _x_ is good w.r.t. _w_. Hence, \(|x-\sigma_w(x)|\le w\) and, by Lemma 5.5 and the triangle inequality, we have:<tbc>

\(|x-\sigma_0(x)|\le|x-\sigma_w(x)|+|\sigma_w(x)-\sigma_0(x)|<w+\frac{8w}{1-\rho}<\frac{9w}{1-\rho}\le\frac{18w_i}{1-\rho}.\)

<tbc>Recall that _x_ satisfies (<tbc>

<tbc>⋆) in phase 0. Then, either _x_ satisfies (<tbc>

<tbc>⋆) until phase _z_, or it violates (<tbc>

<tbc>⋆) in some phase \(i\in\{1,\dots,z\}\). In the former case, we have \(|x-\sigma_0(x)|\le\frac{18w_z}{1-\rho}\le\frac{18\cdot 64}{\kappa(p,q,\rho)^2(1-\rho)}=\frac{1152}{\kappa(p,q,\rho)^2(1-\rho)}\). In the latter case, Lemma 5.16 ensures that the probability that _x_ violates (<tbc>

<tbc>⋆) in phase _i_ is at most:<tbc>

\(\frac{69120}{(1-\rho)^3w_{i-1}^2}\le\frac{8640}{(1-\rho)^3w_{i-1}}\cdot 2^{i-z},\)

<tbc>where \(w_{i-1}\ge 2^{z-i+3}\) follows from \(w_z\ge 4\) and \(w_i\ge 2w_{i+1}\). Moreover, we have \(|x-\sigma_0(x)|\le\frac{18w_{i-1}}{1-\rho}\) since _x_ satisfies (<tbc>

<tbc>⋆) until phase _i_-1.<tbc>

