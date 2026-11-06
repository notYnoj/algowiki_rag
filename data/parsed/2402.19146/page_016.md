From Lemmas 5 and 7, we have a reduction from the OV problem to s-CT- MSeq (and thus, to CT-MSeq) such that \(T_A\in O(n_Ad)\), \(P_B\in O(n_Bd)\). If CT-MSeq can be solved in \(O((|T_A||P_B|)^{1-\epsilon})\) time, then the OV problem can be solved in \(O((n_An_Bd^2)^{1-\epsilon})\subseteq O((n_An_B)^{1-\epsilon}\mathsf{poly}(d))\) time. When _n<sub>A</sub>=n<sub>B</sub>_, the result contradicts OVH/SETH, and when \(n_B=\Theta(n_A^\lambda)\) for \(0<\lambda\le 1\) and \(d\le n^{o(1)}\), the result contradicts UOVH/SETH (cf. Section 2.3). Therefore, Theorem 2 holds.

## 5 Longest common CT-subsequence problems

### 5.1 CT-LCS algorithms for general ordered alphabets

In this section, we propose an algorithm for solving CT-LCS for general ordered alphabets. An _O(n_<sup>6</sup>)-time and _O(n_<sup>4</sup>)-space algorithm, which is our main result will be given in Section 5.1.2. We start from explaining an _O(n_<sup>8</sup>)-time and _O(n_<sup>6</sup>)-space algorithm for simplicity (Section 5.1.1).

For each \(c\in\Sigma\), let _P<sub>c</sub>(S_)={_i|S_\[_i_\]=_c_} and let \(S'\) be the string of length |_S_| such that \(S'[i]=(S[i],r_i)\) for \(1\le i\le|S|\), where _r<sub>i</sub>_ is the rank of _i_ in _P_<sub>_S_\[_i_\]</sub>(_S_). For ordered pairs (_c,r_) and \((c',r')\) of characters and integers, let \((c,r)<(c',r')\) iff (1) \(c<c'\) or (2) \(c=c'\) and \(r<r'\). Then, it holds that CT(_S_) and \(\mathsf{CT}(S')\) are isomorphic. Thus, without loss of generality, we can assume that all characters in the string _S_ are distinct. The same assumption applies to the other string _T_, but _S_ and _T_ may share the same characters.

#### 5.1.1 _O(n_<sup>8</sup>)-time and _O(n_<sup>6</sup>)-space algorithm

We refer to a pair \((i,j)\in[n]^2\) of positions in _S_ and _T_ as a _pivot_. Our algorithm in the general case is based on the idea of _pivoted Cartesian-trees_ from Oizumi et al. \[8\] defined as follows.

**Definition 4** (Fixed (longest) common CT-subsequence) Let \((i,j)\in[n]^2\) be a pivot of strings _S_ and _T_. A string _Q_ is said to be a _fixed common CT-subsequence_ (_f-CT-CS_) of _S_ and _T_ with pivot (_i,j_) if there exist subscript sequences \(I,J\in\mathcal{I}_{|Q|}^n\) such that

• CT(_Q_)=CT(_S<sub>I</sub>_)=CT(_T<sub>J</sub>_),<tbc>

• _S_\[_i_\]=min(_S<sub>I</sub>_), and<tbc>

1
2
3
4
5
6
7
8
1
2
3
4
5
6
7
8
S
12
6
3
14
2
9
4
11
T
3
2
5
9
7
12
8
1
2
2
CT(Q)
CT(Q)
1
4
1
4
3
3

**Fig. 7** \(Q=\langle\mathbf{12},\mathbf{6},\mathbf{14},\mathbf{9}\rangle\) is a fixed longest common CT-subsequence of \(S=\langle\mathbf{12},\mathbf{6},\mathbf{3},\mathbf{14},\mathbf{2},\mathbf{9},\mathbf{4},\mathbf{11}\rangle\) and \(T=\langle\mathbf{3},\mathbf{2},\mathbf{5},\mathbf{9},\mathbf{7},\mathbf{12},\mathbf{8},\mathbf{1}\rangle\) with pivot (2,5).

