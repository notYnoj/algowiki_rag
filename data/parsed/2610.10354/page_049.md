**Proof.** Let _j=k-i_. Since _i_ is a witness for _C_\[_k_\], we must have \(B[j]\neq\perp\) and hence _B_\[_j_\]=0, and _A_\[_i_\]=_C_\[_k_\]. By definition, clearly \(A'_{x,y}[f_{x,y}(i)]=1\), and \(B'_{x,y}[(x\cdot k+2y)-f_{x,y}(i)]=B'_{x,y}[f_{x,y}(j)]=1\). Hence, _f<sub>x,y</sub>(i_) is a witness in the Boolean convolution between \(A'_{x,y}\) and \(B'_{x,y}\). It remains to show that it is the minimum such index.

Suppose for the sake of contradiction that there exists _t\<f<sub>x,y</sub>(i_) where \(A'_{x,y}[t]=B'_{x,y}[(x\cdot k+2y)-t]=1\). By definition, these imply<tbc>

\(A_{x,y}[t]=\lfloor t/N^{2/3}\rfloor\text{and}B_{x,y}[(x\cdot k+2y)-t]=0.\)

<tbc>Because _f<sub>x,y</sub>_ is invertible, there exists \(i'\in\mathbb{F}_N\) such that \(f_{x,y}(i')=t\), and correspondingly \(f_{x,y}(k-i')=(x\cdot k+2y)-t\). Hence, we further obtain

\(A[i']=\lfloor t/N^{2/3}\rfloor\text{and}B[k-i']=0.\) (9)

By the fact \(f_{x,y}(i)\in S_{x,y}\), we have \(A_{x,y}[f_{x,y}(i)]=\lfloor f_{x,y}(i)/N^{2/3}\rfloor\ge\lfloor t/N^{2/3}\rfloor=A[i']\). Since _A_\[_i_\]=_A<sub>x,y</sub>_\[_f<sub>x,y</sub>(i_)\], we have \(A[i']\le A[i]=C[k]\). By Equation (9), this means \(i'\in I_k\) and \(A[i']=A[i]=C[k]\). Since \(f_{x,y}(i')\in S_{x,y}\) holds, this contradicts the fact that _i_ is the unique element in _I<sub>k</sub>_ where \(f_{x,y}(i)\in S_{x,y}\), as \(i'\) is also such an element.

By Claim 6.5, as long as we can guarantee that there is a unique witness \(i\in I_k\) satisfying \(f_{x,y}(i)\in S_{x,y}\), we are able to recover it from the result of Min-Witness\((A'_{x,y},B'_{x,y})\). The next Claim 6.6 shows this happens with probability \(\Omega(1/N^{1/3})\). Since we initially assumed \(|I_k|\le n^{1/3}\), it thus takes only \(\widetilde{O}(N^{1/3})\) repetitions to recover all elements in _I<sub>k</sub>_, in total \(\widetilde{O}(n^{1/3}T(n))\) time as desired. It thus remains to show Claim 6.6 to finish the proof.

**Claim 6.6.** _Let I<sub>k</sub> be the set of witnesses for C_\[_k_\] _in the Min-Plus Convolution C=A∗B where_ \(|I_k|\le n^{1/3}\)_, and let_ \(i_0\in I_k\) _be an arbitrary element. Then the probability that i_<sub>0</sub> _is the unique element in I<sub>k</sub> that satisfies_ \(f_{x,y}(i)\in S_{x,y}\) _is_ \(\Omega(1/N^{1/3})\).

**Proof.** Note that every \(i\in I_k\) has the same value _A_\[_i_\]. Let us denote this value by _u_. Then, for \(i\in I_k\), the condition \(f_{x,y}(i)\in S_{x,y}\) can be equivalently written as<tbc>

\(f_{x,y}(i)\in[u\cdot N^{2/3},(u+1)\cdot N^{2/3}).\)

<tbc>Let _X<sub>i</sub>_ denote the above event. Note that {_f<sub>x,y</sub>}<sub>x,y</sub>_ is a nearly 2-wise independent hash family. Hence,

\(\mathbb{P}\left[X_{i_0}\wedge\wedge_{i\in I_k\backslash\{i_0\}}\neg X_i\right]=\mathbb{P}\left[X_{i_0}\right]-\mathbb{P}\left[X_{i_0}\wedge\vee_{i\in I_k\backslash\{i_0\}}X_i\right]\)<br>
\(\ge\frac{N^{2/3}-1}{N}-\sum_{i\in I_k\backslash\{i_0\}}\mathbb{P}\left[X_{i_0}\wedge X_i\right]\)<br>
\(\ge\frac{N^{2/3}-1}{N}-n^{1/3}\cdot\left(\frac{N^{2/3}+1}{N}\right)^2\)<br>
\(=\Omega(N^{-1/3}),\)

where the final step holds because \(n\le N/2\).

