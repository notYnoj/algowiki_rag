_Proof._ Since the standard deviations of both random variables _S_<sub>LS_,pq,i_</sub> and _S_<sub>RS_,pq,i_</sub> are \(\Theta(pq\sqrt{n})\) and \(\Delta\le pq\), a shift of magnitude \(\Delta\) keeps us within the central region of the distribution. Consequently, the density function _f<sub>pq,i</sub>(y_) varies smoothly under a displacement of size \(\Delta\) and its value remains stable up to constant factors when evaluated at \(f_{pq,i}(y+\Delta)\).

Now, for any \(k\in\mathbb{Z}_p\), let us define a set _A<sub>k</sub>_ that contains elements congruent to _k_ modulo _p_ in the window \(W_{pq}^{(L)}\) as follows<tbc>

\(A_k:=\{y|y=W_{pq}^{(L)},y\equiv k\mathrm{mod}p\}.\)

<tbc>Since almost the entire mass of a Gaussian is in the central window, we have the following

\(\sum_yf_{pq,i}(y)=\Theta\left(\sum_{y=W_{pq}^{(L)}}f_{pq,i}(y)\right).\) (13)

Now, using the above equation for any \(k\in[0,p)\), we have the following

\(\sum_{y\equiv k\mathrm{mod}p}f_{pq,i}(y)=\Theta\left(\sum_{y\in A_k}f_{pq,i}(y)\right).\) (14)

Now, we combine the above two observations and get the following averaging argument

**Claim E.0.2.** _For any_ \(k\in[0,pq)\)_, we have_<tbc>

\(\sum_{y=W_{pq}^{(L)}}f_{pq,i}(y)=p\cdot\Theta\left(\sum_{y\in A_k}f_{pq,i}(y)\right).\)

<tbc>_Proof._ Consider \(k'\in[0,pq)\) and the corresponding set \(A_{k^\prime}\). Then, for any element in \(A_{k^\prime}\), say \(y'=k'+mp\), there exists a unique element in _A<sub>k</sub>_, _y=k+mp_, such that \(|y'-y|=|k'-k|<p\). Let \(\Delta_{k^\prime}:=k'-k\). Using this observation, we get the following

\(\sum_{y^\prime\in A_{k^\prime}} f_{pq,i}(y')=\sum_{y^\prime\in A_{k^\prime}} f_{pq,i}(k'+kp)\)<br>
\(=\sum_{y\in A_k}f_{pq,i}(y+\Delta_{k^\prime})\)<br>
\(=\Theta\left(\sum_{y\in A_k}f_{pq,i}(y)\right).\)

This implies the \(\sum_{y^\prime\in A_{k^\prime}} f_{pq,i}(y')\) corresponding to any residue class \(k'\) is in the neighborhood of \(\sum_{y\in A_k}f_{pq,i}(y)\). So, taking the average will give us the desired result.

\(\sum_yf_{pq,i}(y)=\sum_{k^\prime=0}^{p-1}\sum_{y\in A_{k^\prime}} f_{pq,i}(y)=p\cdot\Theta\left(\sum_{y\in A_k}f_{pq,i}(y)\right).\)

