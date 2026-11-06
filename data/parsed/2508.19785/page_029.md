<tbc>Overall, the expected dislocation of _x_ is at most:

\(\frac{1152}{\kappa(p,q,\rho)^2(1-\rho)}+\frac{8640\cdot 18}{(1-\rho)^4}\sum_{i=1}^z2^{i-z}<\frac{1152}{\kappa(p,q,\rho)^2(1-\rho)}+\frac{311040}{(1-\rho)^4}.\) □

## 5.3.2 A linear upper bound with high probability.

After proving that the expected dislocation of each element is constant, we additionally prove that the total dislocation is linear with high probability. To this end, we first prove that the final position of an element only depends on its nearby elements and on the outcome of their comparisons. For a window size _w_, let \(C_w(h,\ell)\) denote a collection of data including (i) the set of all elements _z_ for which \(|\sigma_w(z)-h|\le\ell\), (ii) their positions in _S<sub>w</sub>_, and (iii) the (random variables denoting the) results of the comparisons between them.

Lemma 5.18. _For any element x and any window size w,_ \(\sigma_0(x)\) _is a function of_ \(C_w(\sigma_w(x),\frac{36}{1-\rho}w)\).

Proof. Let _w_ be a window size considered by BasketSort and define \(w'=\lfloor\rho w\rfloor\). Consider a generic element _y_ belonging to basket _B<sub>j</sub>_ in the round corresponding to window size _w_. The value \(\tau_w(y)\) is a function of _j_, of the elements in the baskets _B_<sub>_j_-3</sub>_,...,B_<sub>_j_+3</sub> (if they exist), of their order in _S<sub>w</sub>_,<sup>7</sup> and of the comparison results between _y_ and these elements. Let _B<sub>i</sub>_ be the basket containing _x_. The position \(\sigma_{w^\prime}(x)\) is a function of _i_, of the elements _y_ belonging to the baskets _B<sub>j</sub>_ with \(|j-i|\le 8\) in the iteration corresponding to window size _w_, and of their values \(\tau_w(y)\). Indeed, for any element \(y'\) that belongs to some basket _B<sub>j</sub>_ with _j\<i_-8 we have \(\sigma_w(y')<\sigma_w(x)-8w\) and Lemma 5.2 ensures that \(y'\) precedes _x_ in \(S_{w^\prime}\) since \(\tau_w(y')<\sigma_w(y')+4w<\sigma_w(x)-4w<\tau_w(x)\). A symmetric argument shows that if _j\>i_+8 then \(y'\) must follow _x_ in \(S_{w^\prime}\).

Since all elements _y_ in _B_<sub>_i_-11</sub>_,...,B_<sub>_i_+11</sub> satisfy \(|\sigma_w(y)-\sigma_w(x)|\le 12w\), \(\sigma_{w^\prime}(x)\) is a function of \(C_w(\sigma_w(x),12w)\). Moreover, using \(|\sigma_w(y)-\sigma_{w^\prime}(y)|<8w\) (see Lemma 5.4), we also obtain that \(\sigma_{w^\prime}\) is a function of \(C_w(\sigma_{w^\prime}(x),20w)\).

Let \(w_k=w,w_{k-1}=\lfloor\rho w\rfloor,w_{k-2},\dots,w_1\) be the window sizes considered by BasketSort from the round corresponding to window size _w_ to termination, and let _w_<sub>0</sub>=0. Notice that, unlike the proof of Section 5.3.1, here the window sizes _w<sub>i</sub>_ increase with _i_. We now prove by induction on _i_=0_,...,k_ that \(\sigma_0(x)\) is a function of \(C_{w_i}(\sigma_0(x),\frac{28}{1-\rho}w_i)\). The base case _i_=0 is trivial, since \(C_0(\sigma_0(x),0)\) includes the position \(\sigma_0(x)\) of _x_ in _S_<sub>0</sub>. Assume then that the inductive claim holds up to some _i\<k_. By induction hypothesis, \(\sigma_0(x)\) is a function of \(C_{w_i}(\sigma_0(x),\frac{28}{1-\rho}w_i)\), and, by Lemma 5.4 and triangle inequality, all elements \(x'\) considered in \(C_{w_i}(\sigma_0(x),\frac{28}{1-\rho}w_i)\) satisfy \(|\sigma_{w_{i+1}}(x')-\sigma_0(x)|\le|\sigma_{w_{i+1}}(x')-\sigma_{w_i}(x')|+|\sigma_{w_i}(x')-\sigma_0(x)|<8w_{i+1}+\frac{28}{1-\rho}w_i\). By the discussion above, the position \(\sigma_{w_{i+1}}(x')\) of any such element \(x'\) is a function of \(C_{w_{i+1}}(\sigma_{w_i}(x'),20w_{i+1})\), and hence the position \(\sigma_{w_{i+1}}(x')\) of _all_ the elements \(x'\) is a function of \(C_{w_{i+1}}(\sigma_0(x),28w_{i+1}+\frac{28}{1-\rho}w_i)\). Using \(w_i\le\rho w_{i+1}\), we have \(28w_{i+1}+\frac{28}{1-\rho}w_i\le(28+\frac{28\rho}{1-\rho})w_{i+1}=\frac{28}{1-\rho}w_{i+1}\).

To conclude the proof, observe that, for any window size _w_, the elements in \(C_w(\sigma_0(x),\frac{28}{1-\rho}w)\) are a subset of those in \(C_w\left(\sigma_w(x),\left(\frac{28}{1-\rho}+\frac{8}{1-\rho}\right)w\right)\), as guaranteed by Lemma 5.5. □

We now combine Lemma 5.11, Lemma 5.17, and Lemma 5.18, to prove that our linear upper bound on the total dislocation of the sequence returned by BasketSort also holds with high probability.

Lemma 5.19. _The total dislocation of S_<sub>0</sub> _is at most_ \(\left(\frac{1152}{\kappa(p,q,\rho)^2(1-\rho)}+\frac{311040}{(1-\rho)^4}+1\right)\cdot m\) _with probability at least_ \(1-O\left(\frac{lnm}{(1-\rho)\kappa(p,q,\rho)}\right)\cdot exp\left(-\Omega\left(\frac{m(1-\rho)^3\kappa(p,q,\rho)}{ln^3m}\right)\right)-O\left(\frac{logm}{m^4log\frac{1}{\rho}}\right)\).

<sup>7</sup>The order of the elements is used, e.g., to break ties in the sorting steps of BasketSort.

