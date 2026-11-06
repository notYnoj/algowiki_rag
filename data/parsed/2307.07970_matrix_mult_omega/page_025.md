Here, the differences with Proposition 5.1 are the followings:

• The input becomes multiple independent copies of \(\left(\mathrm{CW}_q^{\otimes 2^{\ell-1}}\right)^{\otimes n}\).<tbc>

• The output tensor becomes independent copies of some level-\(\ell\varepsilon\)-interface tensor, instead of level-\(\ell\) interface tensor in Proposition 5.1.<tbc>

• There is a small \(2^{o_{1/\varepsilon}(n)}\) factor loss in the number of independent copies of the level-\(\ell\varepsilon\)-interface tensor we can keep.

The high-level idea of the proof is the following: for each copy of \(\left(\mathrm{CW}_q^{\otimes 2^{\ell-1}}\right)^{\otimes n}\) in the input, we apply Proposition 5.1 where the target complete split distributions are slightly different in each application (up to \(\varepsilon\) in \(L_\infty\) distance with some specified complete split distributions). Finally, we merge the level-\(\ell\) interface tensors into a level-\(\ell\varepsilon\)-interface tensor.

_Proof of Theorem 5.3._ Let<tbc>

\(\left\{\xi_{W,i,j,k}^{(r)}\right\}_{r\in[3],W\in\{X,Y,Z\},i+j+k=2^\ell}\)

<tbc>be a set of level-\(\ell\) complete split distributions whose \(L_\infty\) distance with<tbc>

\(\left\{\beta_{W,i,j,k}^{(r)}\right\}_{r\in[3],W\in\{X,Y,Z\},i+j+k=2^\ell}\)

<tbc>is at most \(\varepsilon\). Furthermore, we require that all entries of \(\xi_{W,i,j,k}^{(r)}\) are integral multiples of \(\frac{1}{A_r\cdot\alpha(i,j,k)\cdot n}\). Let \(\widetilde{\mathcal{D}}\) be the collection of such sets of complete split distributions. For every _W,i,j,k_, there are _O(n_) choices for the value of each entry in \(\xi_{W,i,j,k}^{(r)}\), and the total number of entries is \(3^{2^{\ell-1}}=O(1)\) as \(\ell\) is a con stant. Thus, the number of \(\xi_{W,i,j,k}^{(r)}\) is bounded by poly(_n_)=2<sup>_o(n_)</sup>, and consequently the number of \(\left\{\beta_{W,i,j,k}^{(r)}\right\}_{r\in[3],W\in\{X,Y,Z\},i+j+k=2^\ell}\) (i.e., the size of \(\widetilde{\mathcal{D}}\)) is also bounded by 2<sup>_o(n_)</sup>. Also, it is not difficult to verify that the level-\(\ell\varepsilon\)-interface tensor with parameter list<tbc>

\(\left\{\left(n\cdot A_r\cdot\alpha^{(r)}(i,j,k),i,j,k,\beta_{X,i,j,k}^{(r)},\beta_{Y,i,j,k}^{(r)},\beta_{Z,i,j,k}^{(r)}\right)\right\}_{r\in[3],i+j+k=2^\ell}\) (2)

<tbc>is the sum of all level-\(\ell\) interface tensors with parameter lists

\(\left\{\left(n\cdot A_r\cdot\alpha^{(r)}(i,j,k),i,j,k,\xi_{X,i,j,k}^{(r)},\xi_{Y,i,j,k}^{(r)},\xi_{Z,i,j,k}^{(r)}\right)\right\}_{r\in[3],i+j+k=2^\ell}\) (3)

over all such \(\left\{\xi_{W,i,j,k}^{(r)}\right\}\in\widetilde{\mathcal{D}}\).

Let _E_<sub>1</sub>_,E_<sub>2</sub>_,E_<sub>3</sub> be defined as in Proposition 5.1 applied to complete split distributions \(\left\{\beta_{W,i,j,k}^{(r)}\right\}\), and let \(E'_1,E'_2,E'_3\) be defined as in Proposition 5.1 but applied to some complete split distributions \(\left\{\xi_{W,i,j,k}^{(r)}\right\}\in\widetilde{\mathcal{D}}\). By Proposition 5.1, each copy of \(\left(\mathrm{CW}_q^{\otimes 2^{\ell-1}}\right)^{\otimes n}\) can be degenerated into \(2^{(A_1E'_1+A_2E'_2+A_3E'_3)n-o(n)}\) independent copies of the level-\(\ell\) interface tensor with parameter list as in (3).

It is not difficult to see that _A_<sub>1</sub>_E_<sub>1</sub>+_A_<sub>2</sub>_E_<sub>2</sub>+_A_<sub>3</sub>_E_<sub>3</sub> is continuous with respect to \(\left\{\beta_{W,i,j,k}^{(r)}\right\}\), and because the \(L_\infty\) distance between \(\left\{\beta_{W,i,j,k}^{(r)}\right\}\) and \(\left\{\xi_{W,i,j,k}^{(r)}\right\}\) is at most \(\varepsilon\), we get that \(A_1E'_1+A_2E'_2+A_3E'_3\ge A_1E_1+A_2E_2+A_3E_3-o_{1/\varepsilon}(1)\).

