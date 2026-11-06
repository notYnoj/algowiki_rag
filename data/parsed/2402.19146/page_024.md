## 5.3 Conditional lower bound for CT-LCS

In this section, we prove the following theorem.

**Theorem 6** _If there is an_ \(\epsilon>0\) _such that CT-LCS for an alphabet of size_ 5 _can be solved in_ \(O((|S||T|)^{1-\epsilon})\) _time, then OVH and SETH are false._

We extend the LCS reduction \[11\] to our CT-subsequence version using a similar idea as described in Section 4.2. Let \(A=\{\alpha_1,\dots,\alpha_{n_A}\}\) and \(B=\{\beta_1,\dots,\beta_{n_B}\}\) be the input of the OV problem where \(n_B\le n_A\) and \(\alpha_i,\beta_j\in\{0,1\}^d\) for every \(1\le i\le n_A,1\le j\le n_B\). From _A_ and _B_, we construct an input of CT-LCS: string \(S_A\in\Sigma^+\) of length 240_n<sub>A</sub>d_<sup>2</sup>+56_n<sub>A</sub>d_+100_d_<sup>2</sup>+16_n<sub>A</sub>_\(\in O(n_A\mathsf{poly}(d))\) and string \(T_B\in\Sigma^+\) of length 400_n<sub>A</sub>d_<sup>2</sup>+25_n<sub>B</sub>d_<sup>2</sup>+100_d_<sup>3</sup>+14_n<sub>B</sub>d_+100_d_<sup>2</sup>+4_n<sub>B</sub>_\(\in O((n_A+n_B)\mathsf{poly}(d))\), where \(\Sigma=\{0,1,2,3,4\}\).

First, we define the _coordinate gadgets C_<sub>1</sub> and _C_<sub>2</sub>:

\(C_1(a)=\left\{\begin{array}{ c c }
\text{3434} & \text{if}a=0, \\
\text{4433} & \text{if}a=1.
\end{array}\right.\)<br>
\(C_2(b)=\left\{\begin{array}{ c c }
\text{4343} & \text{if}b=0, \\
\text{3333} & \text{if}b=1.
\end{array}\right.\)

We can see that ct\_lcs(_C_<sub>1</sub>(0)_,C_<sub>2</sub>(0))=ct\_lcs(_C_<sub>1</sub>(0)_,C_<sub>2</sub>(1))=ct\_lcs(_C_<sub>1</sub>(1)_,C_<sub>2</sub>(0))=3 and ct\_lcs(_C_<sub>1</sub>(1)_,C_<sub>2</sub>(1))=2 hold. Next, we construct _vector gadgets_ \(V_1(\alpha)\) and \(V_2(\beta)\) for all \(\alpha\in A\) and \(\beta\in B\):

\(V_1(\alpha)=\mathsf{2}^sC_1(\alpha[1])\mathsf{2}^sC_1(\alpha[2])\mathsf{2}^s\cdots\mathsf{2}^sC_1(\alpha[d])\mathsf{2}^s\mathsf{3434}\mathsf{2}^s,\)<br>
\(V_2(\beta)=\mathsf{2}^sC_2(\beta[1])\mathsf{2}^sC_2(\beta[2])\mathsf{2}^s\cdots\mathsf{2}^sC_2(\beta[d])\mathsf{2}^s\mathsf{3333}\mathsf{2}^s,\)

where _s_=5_d_. Note that \(|V_1(\alpha)|=|V_2(\beta)|=5d^2+14d+4\). The following Lemma 10 holds.

**Lemma 10** \(\mathsf{ct}\text{\_lcs}(V_1(\alpha),V_2(\beta))=D+1\) _holds if_ \(\alpha\) _and_ \(\beta\) _are orthogonal, and otherwise_ \(\mathsf{ct}\text{\_lcs}(V_1(\alpha),V_2(\beta))\le D\) _holds, where D=s(d_+2)+3(_d_+1)-1.

_Proof_ For each \(1\le i\le d\), Cartesian trees of \(C_1(\alpha[i])\) and \(C_2(\beta[i])\) belong to the left subtree of the (_i_+1)th substring 2_<sup>s</sup>_ in \(CT(V_1(\alpha))\) and \(CT(V_2(\beta))\), respectively, since \(C_1(\alpha[i])\) and \(C_2(\beta[i])\) consist only of 3 and 4. Now we consider the following two cases:

1. If \(\alpha\) and \(\beta\) are orthogonal, \(\mathsf{ct}\text{\_lcs}(C_1(\alpha[i]),C_2(\beta[i]))=3\) holds for all \(1\le i\le d\). Therefore, by assigning every 2_<sup>s</sup>_ in \(V_2(\beta)\) to every 2_<sup>s</sup>_ in \(V_1(\alpha)\), and \(C_2(\beta[i])\) to \(C_1(\alpha[i])\) for each \(1\le i\le d\), we obtain a common CT-subsequence of length _D_+1. Assume on the contrary that there exists a common CT-subsequence _S_ of \(V_1(\alpha)\) and \(V_2(\beta)\) with \(|S|\ge D+2\). Since the total number of 3’s and 4’s in \(V_1(\alpha)\) (or \(V_2(\beta)\)) is 4(_d_+1), any subsequence of \(V_1(\alpha)\) (or \(V_2(\beta)\)) that CT-matches _S_ contains at least _D_+2-4(_d_+1)=<tbc>

