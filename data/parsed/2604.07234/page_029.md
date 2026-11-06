<tbc>Summing over \(\sigma,\tau\) yields

(4.2) \(\overline{Z}=\sum_{\ell=0}^M\sum_{J\in\genfrac(){pt}{2}{[M]}{\ell}}\sum_{\sigma,\tau\in\Sigma}\unknown\{J\subseteq I(\sigma,\tau)\}.\)

Fix \(\ell\) and \(J=\{j_1<\cdots<j_\ell\}\). If \(J\subseteq I(\sigma,\tau)\) then \(\sigma_{j_r}=\tau_{j_r}\) for each _r_, and these common values form an increasing \(\ell\)-tuple \(K=\{i_1<\cdots<i_\ell\}\subseteq[N]\). Thus<tbc>

\(\unknown\{J\subseteq I(\sigma,\tau)\}=\sum_{K\in\genfrac(){pt}{2}{[N]}{\ell}}\unknown\{\sigma_{j_r}=\tau_{j_r}=i_r\text{for all}r\in[\ell]\}.\)

<tbc>Insert this in (4.2) and exchange sums to obtain

(4.3) \(\overline{Z}=\sum_{\ell=0}^M\sum_{1\le j_1<\cdots<j_\ell\le M}\sum_{1\le i_1<\cdots<i_\ell\le N}\big|\{\sigma\in\Sigma:\sigma_{j_r}=i_r\text{for all}r\in[\ell]\}\big|^2,\)

where the square comes from the independence of \(\sigma\) and \(\tau\) given the constraints.

## 4.1. Counting constrained increasing maps.

Fix \(j_1<\cdots<j_\ell\) and \(i_1<\cdots<i_\ell\). Set the convenient boundary values<tbc>

\(i_0:=0,j_0:=0,i_{\ell+1}:=N+1,j_{\ell+1}:=M+1.\)

<tbc>For each \(k\in[\ell+1]\), consider the interval of _positions_ {_j_<sub>_k_-1</sub>+1_,...,j<sub>k</sub>_-1} of size _j<sub>k</sub>-j_<sub>_k_-1</sub>-1, whose values must lie strictly between _i_<sub>_k_-1</sub> and _i<sub>k</sub>_. There are exactly _i<sub>k</sub>-i_<sub>_k_-1</sub>-1 available integers in {_i_<sub>_k_-1</sub>+1_,...,i<sub>k</sub>_-1}, and choosing which of those occupy the _j<sub>k</sub>-j_<sub>_k_-1</sub>-1 slots uniquely determines \(\sigma\) on that interval by monotonicity. Therefore,

\(\big|\{\sigma\in\Sigma_{N,M}:\sigma_{j_r}=i_r\text{for all}r\in[\ell]\}\big|=\prod_{k=1}^{\ell+1}\genfrac(){pt}{2}{i_k-i_{k-1}-1}{j_k-j_{k-1}-1}.\)

Plugging into (4.3) gives the following explicit form.

**Lemma 4.1** (Gap product formula)**.** _For all_ \(1\le M\le N\),

\(\overline{Z}=\sum_{\ell=0}^M\sum_{1\le j_1<\cdots<j_\ell\le M}\sum_{1\le i_1<\cdots<i_\ell\le N}\prod_{k=1}^{\ell+1}\genfrac(){pt}{2}{i_k-i_{k-1}-1}{j_k-j_{k-1}-1}^2,\)

_with the boundary convention i_<sub>0</sub>=_j_<sub>0</sub>=0 _and_ \(i_{\ell+1}=N+1\), \(j_{\ell+1}=M+1\).

## 4.2. From gaps to compositions.

For each \(k\in[\ell+1]\) define the positive integers<tbc>

\(a_k:=i_k-i_{k-1}\in\mathbb{N}_{>0},b_k:=j_k-j_{k-1}\in\mathbb{N}_{>0}.\)

<tbc>Then \(\sum_{k=1}^{\ell+1}a_k=N+1\) and \(\sum_{k=1}^{\ell+1}b_k=M+1\), and

\(\genfrac(){pt}{2}{i_k-i_{k-1}-1}{j_k-j_{k-1}-1}=\genfrac(){pt}{2}{a_k-1}{b_k-1}.\)

Conversely, any \((a_1,b_1),\dots,(a_{\ell+1},b_{\ell+1})\in(\mathbb{N}_{>0}^2)^{\ell+1}\) with those sum constraints uniquely determines \((i_1,\dots,i_\ell)\) and \((j_1,\dots,j_\ell)\) by partial summation. Thus, Lemma 4.1 can be rewritten as a sum over _block compositions_. We let

\(w(a,b):=\genfrac(){pt}{2}{a-1}{b-1}^2\text{for}a\ge 1,1\le b\le a,w(a,b):=0\text{otherwise},\)

