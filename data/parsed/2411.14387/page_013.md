### 3.1.2 Stating the classification

Consider some left-to-right<sup>8</sup> preferred child alternation that _X_ produces in T . That is, take some value \(b\in S_1\cup\cdots\cup S_l\) and some times \(t_x<t_y\in[m]\) such that

_x_:=_X<sub>tx</sub>_ is in the left subtree of _b_ in T , _y_:=_X<sub>ty</sub>_ is in the right subtree of _b_ in T , and none of the accesses _X_<sub>_tx_+1</sub>_,...,X_<sub>_ty_-1</sub> made in the interim were to values that are strict descendents of _b_. Let _a_ be the lowest ancestor of _b_ such that _a\<b_ and _c_ be the lowest ancestor of _b_ such that _b\<c_.<sup>9</sup> This means that the left and right subtrees of _b_ correspond to the keys in intervals (_a,b_) and (_b,c_). We have \(x,y\prec_\mathcal{T}b\), \(x\in(a,b)\), and \(y\in(b,c)\).

\(\triangleright\) Claim 23. One of the following must hold (from most "local" to most "global"): **1.** All of _b,x,y_ are in the same range _S<sub>jb</sub>_, so _x_ and _y_ are in the left and right subtrees of _b_ in T_<sub>jb</sub>_, and this corresponds to an alternation in T_<sub>jb</sub>_. **2.** _b_ is either the highest ancestor of _x_ such that \(b\in S_{jx}\) and _x\<b_, or the highest ancestor of _y_ such that \(b\in S_{jy}\) and _b\<y_. **3.** \(S_{jb}\prec_\mathcal{T}b\), and either _j<sub>x</sub>_ is the closest (in key value) ancestor of _j<sub>b</sub>_ in \(\widetilde{\mathcal{T}}\) such that _j<sub>x</sub>\<j<sub>b</sub>_, or _j<sub>y</sub>_ is the closest (in key value) ancestor of _j<sub>b</sub>_ in \(\widetilde{\mathcal{T}}\) such that _j<sub>b</sub>\<j<sub>y</sub>_. **4.** All of _b,x,y_ are in different ranges (i.e. _j<sub>x</sub>\<j<sub>b</sub>\<j<sub>y</sub>_), _j<sub>x</sub>_ is in _j<sub>b</sub>_’s left subtree in \(\widetilde{\mathcal{T}}\), and _j<sub>y</sub>_ is in _j<sub>b</sub>_’s right subtree in \(\widetilde{\mathcal{T}}\), so this corresponds to an alternation in \(\widetilde{\mathcal{T}}\).

### 3.1.3 Proving the classification

**Proof of Claim 23.** Let us prove that every alternation is of one of these four types. First, suppose that _j<sub>x</sub>=j<sub>b</sub>=j<sub>y</sub>_. Then by construction of T_<sub>jb</sub>_, _x_ and _y_ are still descendents of _b_ in T_<sub>jb</sub>_, and since T_<sub>jb</sub>_ is a binary search tree, _x_ must be in _b_’s left subtree and _y_ must be in _b_’s right subtree. So this is type 1.

<sup>8</sup> The case where the alternation occurs from right to left is analogous. <sup>9</sup> If either _a_ or _c_ doesn’t exist, let \(a:=-\infty\) or \(c:=+\infty\) by convention.

type 1 type 2 type 3 type 4 a
a a
a c
C c
C b
b b
b X
y X
y X
y X
y Sjb Sjb Sja Sjb Sja Sjb Sjc charge to Tjb charge to tx charge to jb charge to T

**Figure 5** A preferred child alternation in T : _b_’s preferred child changes from the left side (due to an access to _x_) to the right side (due to an access to _y_). There are four qualitatively different ways in which the alternation can happen depending on which ranges _S_<sub>1</sub>_,...,S<sub>l</sub>_ the keys _a,b,c,x,y_ belong.

