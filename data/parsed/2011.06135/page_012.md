_Proof._ For the sake of contradiction, suppose that there exists such _F_ and _G_ with \(\gamma>3\). For a string \(S\subset\{0,1\}^d\), denote by _S<sup>d</sup>_ its _d_-th bit and _S<sup>\<d</sup>_ its restriction to the first _d_-1 bits. Let _S,T_ be two strings such that DISJ(_S<sup>\<d</sup>,T<sup>\<d</sup>_)=1. Then, _S<sup>d</sup>_ and _T<sup>d</sup>_ determines the value of DISJ(_S,T_). That is, if _S<sup>d</sup>=T<sup>d</sup>_=1 then DISJ(_S,T_)=0. Otherwise, DISJ(_S,T_)=1. Now consider restrictions \(F':\{0,1\}\rightarrow\mathcal{M}\) and \(G':\{0,1\}\rightarrow\mathcal{M}\) of _F_ and _G_, defined as

\(F'(x)=F(S^{<d},x),\)<br>
\(G'(y)=G(T^{<d},y).\)

By our assumption we have \(D(F'(1),G'(1))>\gamma r\), while we have \(D(F'(0),G'(0))<r\), \(D(F'(1),G'(0))<r\) and \(D(F'(0),G'(1))<r\). But this is a contradiction if \(\gamma>3\), since it must be the case

\(D(F'(1),G'(1))\le D(F'(1),G'(0))+D(F'(0),G'(0))+D(F'(0),G'(1))<3r\)

due to the triangle inequality.

