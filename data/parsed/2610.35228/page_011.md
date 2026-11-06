(c) \(|U_i|\ge 2^{-(t+1)-\sum_{k=0}^{i-1}c_k}N\).<tbc>

<tbc>These invariants imply two further facts. First,<tbc>

\(\sum_{k=0}^{i-1}log(1+2^{j_k})=log(\tau_i/\tau_0)\le t+1.\) (13)

<tbc>The first step follows from invariant (b), and the second step uses \(\tau_i\le 1\) and \(\tau_0=2^{-(t+1)}\). Each summand is at least log(3/2)_\>_1/2, so _i\<_2(_t_+1), or equivalently \(i\le 2t+1\). Second,<tbc>

\(\sum_{k=0}^{i-1}c_k\le K\sum_{k=0}^{i-1}log(1+2^{j_k})\le K(t+1).\) (14)

<tbc>The first step applies Lemma 4.2 with \(\ell+1\) in place of \(\ell\), and the second step follows from Eq. (13). Consequently,

\(|U_i|\ge 2^{-(K+1)(t+1)}N.\) (15)

This follows by substituting Eq. (14) into invariant (c). In particular, _U<sub>i</sub>_ is nonempty, since the hypothesis implies \(N\ge 2^{(K+1)(t+1)}\).

_Base case._ Let \(S_0:=\emptyset\). Then \(\mu(S_0)=1\), \(\mu_{S_0}=\mu\), and \(\tau_0\le 1\). Moreover,

\(2^{-t}N\le\sum_{u\in V}\mu(u)\le|U_0|+\tau_0N.\)

The first step follows from the assumed objective bound. The second step uses Lemma 3.2-(a) on _U_<sub>0</sub> and the bound \(\mu(u)<\tau_0\) outside _U_<sub>0</sub>. Hence \(|U_0|\ge 2^{-(t+1)}N\), establishing invariant (c) for _i_=0.

_Inductive Step._ Suppose that the invariants hold at index _i_ and that \(d(U_i)>\delta\). The bound \(i\le 2t+1\) gives \(i\le r-2\), so Lemma 3.3 shows that \(\nu:=\mu_{S_i}\) is a level-(_r-i_) pseudo-distribution with \(r-i\ge 2\). The set _U<sub>i</sub>_ is nonempty by Eq. (15), and every \(u\in U_i\) satisfies \(\nu(u)\ge\tau_i\). Invariant (b) gives \(\tau_i\in[\tau_0,1]\), and therefore \(J:=\lceil log(1/\tau_i)\rceil\le t+1\).

Apply Lemma 4.1 to \(\nu,U_i,\tau_i,\delta,\ell\). It gives an integer _j<sub>i</sub>_ with \(-1\le j_i\le J-1\le t\) and a vertex \(v_i\in U_i\) such that<tbc>

\(W:=\{u\in U_i:\nu(u,v_i)\ge(1+2^{j_i})\nu(u)\nu(v_i)\}\)

<tbc>satisfies

\(|W|\ge\frac{3\delta}{8}2^{-(j_i+1)(\ell+1)}|U_i|=2^{-h-log(8/3)-(j_i+1)(\ell+1)}|U_i|=2^{1-c_i}|U_i|.\)

The first step follows from Eq. (12). The second step uses \(\delta=2^{-h}\), and the third step uses the definitions of \(\Lambda\) and _c<sub>i</sub>_.

Set \(S_{i+1}:=S_i\cup\{v_i\}\) and \(\tau_{i+1}:=(1+2^{j_i})\tau_i\). Since \(v_i\in U_i\subseteq V\backslash S_i\), we have |_S_<sub>_i_+1</sub>|=_i_+1. Since \(\nu(v_i)\ge\tau_i>0\), Lemma 3.3 gives \(\mu(S_{i+1})>0\). Thus invariant (a) holds at the next index.

For \(u\in W\backslash\{v_i\}\), we have \(u\notin S_{i+1}\) and<tbc>

\(\mu_{S_{i+1}}(u)=\frac{\nu(u,v_i)}{\nu(v_i)}\ge(1+2^{j_i})\nu(u)\ge(1+2^{j_i})\tau_i=\tau_{i+1}.\)

<tbc>The first step follows from the conditioning identity in Lemma 3.3. The second step uses \(u\in W\) , the third step uses \(u\in U_i\), and the fourth step follows from the definition of \(\tau_{i+1}\). Thus \(W\backslash\{v_i\}\subseteq U_{i+1}\).

