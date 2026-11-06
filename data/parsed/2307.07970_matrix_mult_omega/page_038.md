_Proof._ Similar to Theorem 5.3, for every set of complete split distributions \(\{\xi_{W,t,i^\prime,j^\prime,k^\prime}^{(r)}\}_{W,t,r,i^\prime,j^\prime,k^\prime}\) that is at most \(\varepsilon\) away in \(L_\infty\) distance from \(\{\beta_{W,t,i^\prime,j^\prime,k^\prime}^{(r)}\}_{W,t,r,i^\prime,j^\prime,k^\prime}\) , we take an independent copy of the input interface tensor, and degenerate it to independent copies of the output interface tensor with the specified complete split distributions. Let

\(\xi_{W,t}^{(r)}=\sum_{i^\prime,j^\prime,k^\prime}\alpha_t^{(r)}(i',j',k')\cdot\left(\xi_{W,t,i^\prime,j^\prime,k^\prime}^{(r)}\times\xi_{W,t,i_t-i^\prime,j_t-j^\prime,k_t-k^\prime}^{(r)}\right)(\forall W\in\{X,Y,Z\},r\in[3],t\in[s'])\) (13)

and \(\xi_{W,t}=A_{t,1}\xi_{W,t}^{(1)}+A_{t,2}\xi_{W,t}^{(2)}+A_{t,3}\xi_{W,t}^{(3)}\) be determined by the considered complete split distributions \(\{\xi_{W,t,i^\prime,j^\prime,k^\prime}\}\). According to Proposition 6.2, an \(\varepsilon\)-interface tensor T with parameter list \(\{(n_t,i_t,j_t,k_t,\xi_{X,t},\xi_{Y,t},\xi_{Z,t})\}_{t\in[s^\prime]}\) can degenerate to \(2^{E_1+E_2+E_3-o(n)-o_{1/\varepsilon}(n)}\) copies of the target interface tensor. Summing up a copy of the outcome tensor for each \(\{\xi_{W,t,i^\prime,j^\prime,k^\prime}^{(r)}\}_{W,t,r,i^\prime,j^\prime,k^\prime}\) will give the output \(\varepsilon\)-interface tensor, so we can get \(2^{E_1+E_2+E_3-o(n)-o_{1/\varepsilon}(n)}\) independent copies of the output tensor in total.

It remains to show that T is a subtensor of the input interface tensor, i.e., a \(3\varepsilon\)-interface tensor with parameters \(\{(n_t,i_t,j_t,k_t,\beta_{X,t},\beta_{Y,t},\beta_{Z,t})\}_{t\in[s^\prime]}\). On the right-hand side of (13), the two complete split distri butions have at most \(\varepsilon\) distance from \(\beta_{W,t,i^\prime,j^\prime,k^\prime}^{(r)}\) and \(\beta_{W,t,i_t-i^\prime,j_t-j^\prime,k_t-k^\prime}^{(r)}\), so their product has \(\le 2\varepsilon\) distance<sup>4</sup> from \(\beta_{W,t,i^\prime,j^\prime,k^\prime}^{(r)}\times\beta_{W,t,i_t-i^\prime,j_t-j^\prime,k_t-k^\prime}^{(r)}\); since the coefficients \(\alpha_t^{(r)}(i',j',k')\) sum up to 1, we know that the left-hand side \(\xi_{W,t}^{(r)}\) has at most \(2\varepsilon\) distance from \(\beta_{W,t}^{(r)}\) as well, and the same holds between \(\xi_{W,t}\) and \(\beta_{W,t}\). Thus the \(\varepsilon\)-interface tensor with complete split distributions \(\{\xi_{W,t}\}_{W,t}\) is contained in the \(3\varepsilon\)-interface tensor with \(\{\beta_{W,t}\}_{W,t}\) as a subtensor. Then we conclude the proof.

The remainder of this section aims to prove Proposition 6.2.

## 6.1 Dividing into Regions

For each of the \(s'\) terms, say the _t_-th term, we pick three real numbers \(A_{t,1},A_{t,2},A_{t,3}\ge 0\) where \(A_{t,1}+A_{t,2}+A_{t,3}=1\), that aims to divide the _t_-th term in the input level-\(\ell\varepsilon\)-interface tensor into three regions of sizes _A_<sub>_t,_1</sub>_n<sub>t</sub>,A_<sub>_t,_2</sub>_n<sub>t</sub>_ and _A_<sub>_t,_3</sub>_n<sub>t</sub>_ respectively. We also pick three different complete split distributions \(\beta_{X,t}^{(1)},\beta_{X,t}^{(2)},\beta_{X,t}^{(3)}\), with the constraint

\(\beta_{X,t}^{(1)}A_{t,1}+\beta_{X,t}^{(2)}A_{t,2}+\beta_{X,t}^{(3)}A_{t,3}=\beta_{X,t}.\) (14)

We also pick \(\beta_{Y,t}^{(r)}\) and \(\beta_{Z,t}^{(r)}\) for \(r\in[3]\) with similar constraints. Similar to Remark 5.2, we assume without loss of generality that, for every _t,r_ and every \(L\in\{0,1,2\}^{2^{\ell-1}}\),

\(\beta_{X,t}^{(r)}(L)=\beta_{Z,t}^{(r)}(\vec{2}-L)\text{if}j_t=0,\beta_{Z,t}^{(r)}(L)=\beta_{Y,t}^{(r)}(\vec{2}-L)\text{if}i_t=0,\beta_{Y,t}^{(r)}(L)=\beta_{X,t}^{(r)}(\vec{2}-L)\text{if}k_t=0\)

where \(\vec{2}\) denotes the length-\((2^{\ell-1})\) vector whose coordinates are all 2, and

\(\beta_{X,t}^{(r)}(L)=0\text{if}\sum_tL_t\neq i_t,\beta_{Y,t}^{(r)}(L)=0\text{if}\sum_tL_t\neq j_t,\beta_{Z,t}^{(r)}(L)=0\text{if}\sum_tL_t\neq k_t.\)

<sup>4</sup>The distance is at most \(2\varepsilon\) for the following reason: first, we change \(\beta_{W,t,i^\prime,j^\prime,k^\prime}^{(r)}\) to \(\xi_{W,t,i^\prime,j^\prime,k^\prime}^{(r)}\), which introduces an additive \(\varepsilon\) error (as the right hand side in Eq. (13) is a weighted average of the entries of \(\xi_{W,t,i^\prime,j^\prime,k^\prime}^{(r)}\)); then we change \(\beta_{W,t,i_t-i^\prime,j_t-j^\prime,k_t-k^\prime}^{(r)}\) to \(\xi_{W,t,i_t-i^\prime,j_t-j^\prime,k_t-k^\prime}^{(r)}\), which introduces another additive \(\varepsilon\) error.

