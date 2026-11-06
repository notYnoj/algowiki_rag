The main building block of the oracle is a procedure that takes vector \(u\in\mathbb{R}^d\) and either outputs a directed matching _M_ on nodes _V_ or terminates the oracle. It works as follows \((c',\Delta,\sigma,\mu\) are positive constants that will be specified later):

**1** call `DirectionalFlowCut`(_u_) to obtain _A,B_, heights _h<sub>x</sub>_, value _F_, routing _f_, demand<br>
graph _D_ with weights _d<sub>xy</sub>_, and element cut (_X,Y,U_)

**2** if \(F\le c'n\mu\) then return (_X,Y,U_) and terminate the oracle; by Lemma 12(a), this cut is<br>
\(c'\)-balanced and has cost at most \(2c'n\mu\)

**3** if \(\sum_{x\in A,y\in B}d_{xy}\|x-y\|^2\ge 2\alpha\), then set \(\lambda_e=\sum_{p:e\in p}f_p\) for each \(e\in E\), return \(\lambda\) and<br>
_N_=-L(_D_), and terminate the oracle

**4** let \(M_\mathtt{all}=\{(x,y)\in A\times B:d_{xy}>0,h_y-h_x\ge\sigma\}\) and<br>
\(M_\mathtt{short}=\{(x,y)\in M_\mathtt{all}:\|x-y\|^2\le\Delta\}\)

**5** pick maximal matching \(M\subseteq M_\mathtt{short}\) and return _M_

**Lemma 22.** _Suppose that parameters_ \(\tau,\gamma\) _in eq._ (6) _satisfy_ \(\tau\le 2\), \(\gamma\le\frac{\alpha}{(32/c+2\tau)c'n\mu}\)_. If the algorithm terminates at line 3, then the returned variables_ \(\lambda_{ij}\) _and matrix N are valid output of the reduced oracle. Matrix N has at most O(m_) _non-zero entries, and its spectral norm is at most_ \(2\mu\).

_Proof._ Lemma 12(b) gives the capacity bounds on \(\lambda\), the identity \(N=\sum_pf_pT_p-\mathcal{L}(G^\lambda)=-\mathcal{L}(D)\), and \(\|N\|\le 2\mu\). It remains to show that \(N\bullet X\le-\alpha\). By Assumption 1, \(\|x\|^2\le 4/c\) for each \(x\in S\), and hence \(\|x-y\|^2\le 16/c\) for each \(x,y\in S\). Since \((v_1,\dots,v_n)\approx_{\gamma,\tau}(\tilde{v}_1,\dots,\tilde{v}_n)\), we get \(\|x-y\|^2-\|v_x-v_y\|^2\le\gamma(\|x-y\|^2+\tau)\le\frac{\alpha}{(32/c+2\tau)c'n\mu}(16/c+\tau)=\frac{\alpha}{2c'n\mu}\). We can thus write

\(-N\bullet X=\sum_{x\in A,y\in B}d_{xy}\|v_x-v_y\|^2\ge\sum_{x\in A,y\in B}d_{xy}(\|x-y\|^2-\frac{\alpha}{2c'n\mu})\)<br>
\(\ge\sum_{x\in A,y\in B}d_{xy}\|x-y\|^2-\frac{\alpha}{2c'n\mu}\sum_{x\in A}\sum_{y\in B}d_{xy}\ge 2\alpha-\frac{\alpha}{2c'n\mu}\cdot|A|\cdot\mu=\alpha\)

We will assume that if `Matching`(_u_) terminates at line 2 or 3 then it returns an empty matching. Thus, we always have \(\mathtt{Matching}(u)\subseteq V\times V\) and \(|\mathtt{Matching}(u)|\le|V|\).

**Lemma 23.** _Suppose that_ \(\mu\ge\frac{6\alpha}{c'n\Delta}\)_. There exist positive constants_ \(c',\sigma,\delta\) _for which either (i)_ \(\mathbb{E}_u|\mathtt{Matching}(u)|\ge\delta n\)_, or (ii) Algorithm 4 for u_∼N(0_,I<sub>d</sub>_) _terminates at line 2 or 3 with probability at least_ \(\Theta(1)\).

_Proof._ Choose \(c',\sigma,\zeta\) as in Lemma 13. If the probability of termination at line 2 or 3 is at least \(\zeta/2\), then (ii) holds. Otherwise, with probability at least \(\zeta/2\), the projection gap is at least \(\sigma\) and the algorithm reaches line 5. On this event, let \(A'\subseteq A\) and \(B'\subseteq B\) be the endpoints of the matching _M_. The total demand is at least \(c'n\mu\), and each vertex is incident to demand at most \(\mu\) by Lemma 12(b). Thus, if \(|M|<c'n/3\), then<tbc>

\(\sum_{x\in A-A^\prime,y\in B-B^\prime} d_{xy}\ge c'n\mu-\mu(|A'|+|B'|)>\frac{c'n\mu}{3}.\)

<tbc>Every positive-demand pair in this sum has projection gap at least \(\sigma\) and, by maximality of _M_, squared distance greater than \(\Delta\). Consequently,<tbc>

\(\sum_{x\in A,y\in B}d_{xy}\|x-y\|^2>\frac{c'n\mu\Delta}{3}\ge 2\alpha,\)

**Algorithm 4:** `Matching`(_u_).

