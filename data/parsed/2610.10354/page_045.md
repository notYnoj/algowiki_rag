**Claim 6.2.** _Let_ \((i_0,j_0,k_0)\in[0,n]^3\) _be a triple with i_<sub>0</sub>+_j_<sub>0</sub>=_k_<sub>0</sub>_, and let_ \(\Delta=B[j_0]-A[i_0]\)_. Then, A_\[_i_<sub>0</sub>\]+_B_\[_j_<sub>0</sub>\]=_C_\[_k_<sub>0</sub>\] _holds if and only if both_ \(2C_\Delta[k_0]=C[k_0]+\Delta\) _and_ \(A_\Delta[i_0]=B_\Delta[j_0]=C_\Delta[k_0]\) _hold._

**Proof.** We first show the forward direction. By definition,

\(2C_\Delta[k_0]=2min_{i+j=k_0A_\Delta[i]=B_\Delta[j]}B_\Delta[j]=min_{i+j=k_0A[i]+\Delta=B[j]}\{A[i]+\Delta+B[j]\}\)<br>
\(\ge min_{i+j=k_0}\{A[i]+\Delta+B[j]\}=C[k_0]+\Delta.\)

Additionally, since \(A_\Delta[i_0]=A[i_0]+\Delta=B[j_0]=B_\Delta[j_0]\),

\(2C_\Delta[k_0]\le 2B_\Delta[j_0]=A[i_0]+\Delta+B[j_0]=C[k_0]+\Delta.\)

Hence, we have \(2C_\Delta[k_0]=C[k_0]+\Delta\). Moreover, we have \(C_\Delta[k_0]=B_\Delta[j_0]\) since the above inequality is tight, so \(A_\Delta[i_0]=B_\Delta[j_0]=C_\Delta[k_0]\) holds as claimed.

Now we consider the reverse direction. From the assumptions \(2C_\Delta[k_0]=C[k_0]+\Delta\) and \(A_\Delta[i_0]=B_\Delta[j_0]=C_\Delta[k_0]\), we have

\(C[k_0]+\Delta=2C_\Delta[k_0]=A_\Delta[i_0]+B_\Delta[j_0]=A[i_0]+\Delta+B[j_0],\)

so _A_\[_i_<sub>0</sub>\]+_B_\[_j_<sub>0</sub>\]=_C_\[_k_<sub>0</sub>\] holds as claimed.

Consider the following algorithm. We enumerate \(\Delta\in\{-\sqrt{n},\dots,\sqrt{n}\}\), create \(A_\Delta\) and \(B_\Delta\), and compute \(C_\Delta=\text{Min-Equal}(A_\Delta,B_\Delta)\) using A in \(O(n^{1.5-\epsilon})\) time per \(\Delta\). By standard sampling-based approaches (Lemma 2.14), we can further list \(n^{2\epsilon/3}\) witnesses for every \(C_\Delta\) in \(\widetilde{O}(n^{1.5-\epsilon/3})\) time using A as a black-box. This step takes \(\widetilde{O}(\sqrt{n}\cdot n^{1.5-\epsilon/3})=\widetilde{O}(n^{2-\epsilon/3})\) over all \(\Delta\).

What remains to consider are those \(C_\Delta[k]\) that have more than \(n^{2\epsilon/3}\) witnesses and \(2C_\Delta[k]=C[k]+\Delta\). We call such a pair \((\Delta,k)\) heavy. By Claim 6.2, the set of witnesses for \(C_\Delta[k]\) is exactly the set of (_i,j_) where _A_\[_i_\]+_B_\[_j_\]=_C_\[_k_\] and _B_\[_j_\]-_A_\[_i_\]=\(\Delta\). Since the values of _C_\[_k_\] and \(\Delta\) are both known, we can determine the value _A_\[_i_\]=_u_ and _B_\[_j_\]=_v_ where \(u=(C[k]-\Delta)/2,v=(C[k]+\Delta)/2\). After simple linear time preprocessing, we can enumerate elements in the set \(S_v=\{j\in[n]:B[j]=v\}\) in \(O(n^{1/2+\epsilon/3})\) time (recall each element can appear at most \(O(n^{1/2+\epsilon/3})\) times in _B_). Once we have this set, we can compute the exact set of witnesses for \(C_\Delta[k]\) in \(O(n^{1/2+\epsilon/3})\) time, simply by checking if \(A_\Delta[k-j]=B_\Delta[j]\) and compare them with \(C_\Delta[k]\) for \(j\in S_v\). Since we only need to list up to _n_<sup>1/2</sup> witness per _C_\[_k_\], we only need to resolve \(n^{1/2-2\epsilon/3}\) heavy pairs for a particular value of _k_ before we find enough witnesses for _C_\[_k_\]. Hence, we only need to handle \(O(n^{3/2-2\epsilon/3})\) heavy pairs, and thus the overall running time for this case is \(O(n^{2-\epsilon/3})\).

## 6.3 Bounded Monotone Min-Plus Convolution

In order to show the hardness for Bounded Monotone Min-Plus Convolution, we first show the hardness of another problem in the following:

**Lemma 6.3.** _Let_ \(A\in[\sqrt{n}]^{[0,n]}\) _and_ \(B\in[\sqrt{n}]^{[0,\sqrt{n}]}\)_. Computing the Min-Plus Convolution between A and B requires n_<sup>1.5-_o_(1)</sup> _time, under the Strong Min-Plus Convolution Hypothesis._

