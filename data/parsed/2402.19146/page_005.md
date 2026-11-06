Fig. 1 shows CT(_S_) for a string \(S=\langle 5,8,2,6,4,7,4\rangle\) and CT(_S<sub>b</sub>_) for a binary string \(S_b=\langle 1,0,0,1,0,1,0\rangle\). As shown in Fig. 1, the Cartesian tree recursively splits the string based on the smallest character without considering the ordering of characters between the left and right subtrees, thereby expressing a flexible ordering structure of the characters.

For two strings _S_ and _T_ of equal length, the two Cartesian-trees CT(_S_) and CT(_T_) are _isomorphic_ if they have the same tree topology as ordered trees \[19\], which are tree data structures where the children of each node are ordered. We denote it by CT(_S_)=CT(_T_). We say that two strings _S_ and _TCT-match_ if CT(_S_)=CT(_T_).

**Definition 2** (CT-subsequence) A string _P_ is said to be a _CT-subsequence_ of a string _T_ if there is a subsequence _Q_ of _T_ such that CT(_Q_)=CT(_P_).

**Definition 3** (CT-occurrence interval) An interval \([\ell,r]\) in _T_ is said to be a _CT- occurrence interval_ for _P_ if there is a subsequence \(T[i_1]\cdots T[i_{|P|}]\) of \(T[\ell..r]\) such that \(\mathsf{CT}(T[i_1]\cdots T[i_{|P|}])=\mathsf{CT}(P)\), where \(\ell\le i_1\le\cdots\le i_{|P|}\le r\).

A CT-occurrence interval \([\ell,r]\) for _P_ in _T_ is said to be _minimal_ if no proper sub-interval of \([\ell,r]\) is a CT-occurrence interval for _P_ in _T_.

Our first problem is the following:

_Problem 1_ (CT-subsequence matching problem (CT-MSeq) \[8\]) Given two strings _T_ and _P_, find all minimal CT-occurrence intervals for _P_ in _T_.

Fig. 2 shows an example of CT-subsequence matching.

1
2
3
4
5
6
7
1
2
3
4
5
6
7
S
5
8
2
6
4
7
4
Sb
1
0
0
1
0
1
0
3
2
CT(S)
CT(Sb)
1
5
1
3
2
4
7
5
6
4
7
6

**Fig. 1** This figure shows examples of Cartesian-trees CT(_S_) for a string \(S=\langle 5,8,2,6,4,7,4\rangle\), CT(_S<sub>b</sub>_) for a binary string \(S_b=\langle 1,0,0,1,0,1,0\rangle\). Each node in CT(_S_) and CT(_S<sub>b</sub>_) are labeled by the corresponding position in _S_. Since min\_id(_S<sub>b</sub>_) is the least index _i_ such that _S<sub>b</sub>_\[_i_\] is the smallest element in _S<sub>b</sub>_, CT(_S<sub>b</sub>_) is the tree rooted at _i_=2.

