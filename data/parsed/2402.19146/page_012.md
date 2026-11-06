We can easily reduce s-CT-MSeq to CT-MSeq. Thus, we only consider the reduction from the OV problem to s-CT-MSeq in the following proof. Let \(A=\{\alpha_1,\dots,\alpha_{n_A}\}\) and \(B=\{\beta_1,\dots,\beta_{n_B}\}\) be the input of the OV problem where \(n_B\le n_A\) and \(\alpha_i,\beta_j\in\{0,1\}^d\) for every \(1\le i\le n_A,1\le j\le n_B\). From _A_ and _B_, we construct an input of CT-MSeq: text \(T_A\in\Sigma^*\) of length \(20n_Ad+8n_A+1\in O(n_Ad)\) and pattern \(P_B\in\Sigma^*\) of length \(4n_Bd+2n_B+1\in O(n_Bd)\) where \(\Sigma=\{0,1,2,3\}\). While our reduction is similar to the reduction from the OV problems to the _episode matching problem_ \[10\], our construction for text and pattern is non-trivial and includes new ideas that exploit properties of Cartesian trees. The key idea of our reduction is to construct pattern _P<sub>B</sub>_ so that the Cartesian tree of _P<sub>B</sub>_ has _comb-like_ structures. To achieve this, we insert characters _c_ between gadget strings in _P<sub>B</sub>_ such that _c_ is smaller than any other character appearing in the gadgets (see also Fig. 5). Thanks to such comb-like structures, we can prevent interference between Cartesian trees of gadget strings.

First, we define the _coordinate gadgets C_<sub>1</sub> and _C_<sub>2</sub>:

\(C_1(a)=\left\{\begin{array}{ c c }
\text{\texttt{2323}} & \text{if}a=0, \\
\text{\texttt{3232}} & \text{if}a=1.
\end{array}\right.\)<br>
\(C_2(b)=\left\{\begin{array}{ c c }
\text{\texttt{323}} & \text{if}b=0, \\
\text{\texttt{222}} & \text{if}b=1.
\end{array}\right.\)

It can be seen that both _C_<sub>2</sub>(0)=`323` and _C_<sub>2</sub>(1)=`222` are CT-subsequences of _C_<sub>1</sub>(0)=`2323`. Also, _C_<sub>2</sub>(0)=`323` is a CT-subsequence of _C_<sub>1</sub>(1)=`3232` but _C_<sub>2</sub>(1)=`222` is not. Thus, we have the following observation:

_Observation 3_ String _C_<sub>2</sub>(_b_) is a CT-subsequence of string _C_<sub>1</sub>(_a_) if and only if \(a\cdot b=0\).

Next, we construct the _vector gadgets_ \(V_1(\alpha)\) and \(V_2(\beta)\) for all \(\alpha\in A\) and \(\beta\in B\):

\(V_1(\alpha)=\text{\texttt{1}}C_1(\alpha[1])\text{\texttt{1}}C_1(\alpha[2])\text{\texttt{1}}\cdots\text{\texttt{1}}C_1(\alpha[d])\text{\texttt{1}}\)<br>
\(V_2(\beta)=\text{\texttt{1}}C_2(\beta[1])\text{\texttt{1}}C_2(\beta[2])\text{\texttt{1}}\cdots\text{\texttt{1}}C_2(\beta[d])\text{\texttt{1}}\)

Note that \(|V_1(\alpha)|=5d+1\) and \(|V_2(\beta)|=4d+1\). Fig. 5 shows an example of \(V_2(\beta)\) and \(CT(V_2(\beta))\) where \(\beta=(0,1,0,0,1)\). The following Lemma 4 holds.

**Lemma 4** _String_ \(V_2(\beta)\) _is a CT-subsequence of string_ \(V_1(\alpha)\) _if and only if_ \(\alpha\) _and_ \(\beta\) _are orthogonal._

_Proof_ For each \(1\le i\le d\), Cartesian trees of \(C_1(\alpha[i])\) and \(C_2(\beta[i])\) belong to the left subtree of the (_i_+1)th character `1` in \(CT(V_1(\alpha))\) and \(CT(V_2(\beta))\), respectively, since \(C_1(\alpha[i])\) and \(C_2(\beta[i])\) consist only of `2` and `3`. Now we consider the following two cases:

1. If \(\alpha\) and \(\beta\) are orthogonal, \(C_2(\beta[i])\) is a CT-subsequence of \(C_1(\alpha[i])\) for all \(1\le i\le d\) by Observation 3. Therefore, by assigning every `1` in \(V_2(\beta)\) to every `1` in \(V_1(\alpha)\), and \(C_2(\beta[i])\) to \(C_1(\alpha[i])\) for each \(1\le i\le d\), we obtain a subsequence of \(V_1(\alpha)\) that CT-matches \(V_2(\beta)\).<tbc>

