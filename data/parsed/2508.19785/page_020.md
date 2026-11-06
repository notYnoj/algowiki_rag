<tbc>Proof. When the window size is _w_, each iteration of the for loop at line 6 of Algorithm 2 requires time _O(w_<sup>2</sup>). Since there are \(\lceil\frac{m}{w}\rceil\) iterations, the overall time spent for window size _w_ is _O(mw_). The claim follows by summing the above complexity over all the \(O(log_{1/\rho} w_S)\) considered window sizes, which decrease geometrically. In particular, the window size considered in the _i_-th iteration is at most \(\rho^{i-1}w_S\), and we can upper bound the overall running time with \(\sum_{i=1}^{+\infty} O(m\rho^{i-1}w_S)=O(\frac{m\cdot w_S}{1-\rho})\). □

In the rest of this section, we use _w_ to denote a window size considered by the algorithm and \(\sigma_w(x)\) as a shorthand for pos(_x,S<sub>w</sub>_). The following three lemmas relate the three quantities \(\sigma_w(\cdot)\), \(\tau_w(\cdot)\) and \(\sigma_{\lfloor\rho w\rfloor}(\cdot)\).

Lemma 5.2. _For all elements x,_ \(|\tau_w(x)-\sigma_w(x)|<4w\).

Proof. Fix an element _x_ and let _B<sub>i</sub>_ be the basket containing _x_. We have \(\tau_w(x)=max\{0,i-4\}\cdot w+pos(x,A)\), where pos(_x,A_) is the position of _x_ in _A_. Since _A_ contains at most \(min\{i+3,7\}\cdot w\) elements, we have:<tbc>

\((i-4)\cdot w<\tau_w(x)\le max\{0,i-4\}\cdot w+min\{i+3,7\}\cdot w=(i+3)\cdot w.\)

<tbc>Therefore, using \((i-1)\cdot w<\sigma_w(x)\le i\cdot w\), we have:

\(-4w=(i-4)\cdot w-i\cdot w<\tau_w(x)-\sigma_w(x)<(i+3)\cdot w-(i-1)\cdot w=4w\). □

Lemma 5.3. _For all elements x,_ \(|\sigma_{\lfloor\rho w\rfloor}(x)-\tau_w(x)|<4w\).

Proof. Consider an element _x_. By Lemma 5.2, all elements _y_ with \(\sigma_w(y)\le\tau_w(x)-4w\) satisfy \(\tau_w(y)<\tau_w(x)\), and all elements _z_ with \(\sigma_w(z)\ge\tau_w(x)+4w\) satisfy \(\tau_w(z)>\tau_w(w)\). This shows that there are at least \(\tau_w(x)-4w\) elements _y_ with \(\tau_w(y)<\tau_w(x)\) and at least \(n-\tau_w(x)-4w\) elements _z_ with \(\tau_w(z)>\tau_w(x)\), implying that \(\tau_w(x)-4w<\sigma_{\lfloor\rho w\rfloor}(x)<\tau_w(x)+4w\). □

Lemma 5.4. _For all elements x,_ \(|\sigma_{\lfloor\rho w\rfloor}(x)-\sigma_w(x)|<8w\).

Proof. Using Lemma 5.2, Lemma 5.3, and the triangle inequality, we have:

\(|\sigma_{\lfloor\rho w\rfloor}(x)-\sigma(x)|\le|\sigma_{\lfloor\rho w\rfloor}(x)-\tau_w(x)|+|\tau_w(x)-\sigma(x)|<4w+4w=8w\). □

Lemma 5.5. _For all elements x,_ \(|\sigma_w(x)-\sigma_0(x)|<\frac{8w}{1-\rho}\).

Proof. Let _r_+1 be the number of rounds of BasketSort executed from (and including) the round with window size _w_ to completion and let _w_<sub>0</sub>_,w_<sub>1</sub>_,w_<sub>2</sub>_,...,w<sub>r</sub>_ be the corresponding window sizes so that _w_<sub>0</sub>=_w_, \(w_r\ge 1\), and \(\lfloor\rho w_r\rfloor=0\). Let _w_<sub>_r_+1</sub>=0. By Lemma 5.4, we know that \(|\sigma_{w_i}(x)-\sigma_{w_{i+1}}(x)|<8w_i\) for all _i_=0_,...,r_. Since \(w_i\le\rho^iw\), a repeated application of the triangle inequality yields:

\(|\sigma_w(x)-\sigma_0(x)|=\left|\sum_{i=0}^r\left(\sigma_{w_i}(x)-\sigma_{w_{i+1}}(x)\right)\right|\le\sum_{i=0}^r\left|\sigma_{w_i}(x)-\sigma_{w_{i+1}}(x)\right|\)<br>
\(<\sum_{i=0}^r8w_i<8\sum_{i=0}^{+\infty}\rho^iw=\frac{8w}{1-\rho}.\) □

## 5.2 Analysis of the Maximum Dislocation

We are now ready to analyze the maximum dislocation of the sequence returned by BasketSort.

Given an element \(x\in S\) and a window size _w_, we say that an element is _good_ w.r.t. _w_ if its dislocation in _S<sub>w</sub>_ is at most _w_. We avoid specifying _w_ when it is clear from context. For the analysis of the maximum dislocation, it would suffice to prove that all elements are good w.r.t. all window sizes \(w=\Omega(logm)\) considered by BasketSort with a high enough probability. However, the above<tbc>

