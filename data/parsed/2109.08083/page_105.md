<tbc>Proof. By definition, for a vertex \(v\in V(G[I_{t_{i+1}}])\), _G<sup>o</sup>_ includes an edge \(e\in G\) containing _v_ if and only if \(e\cap(I_{t_i}\backslash I_{t_{i+1}})\neq\emptyset\). All edges \(e\in G\) containing _v_ which are not in _G<sup>o</sup>_ must therefore satisfy \(e\subseteq I_{t_{i+1}}\). Since _v_ is also in _I_<sub>_t<sub>i</sub>_+1</sub> it follows that \(e\in G[I_{t_{i+1}}]\). The first result follows. The second result is clear, noting that since \((G,\omega)\) is _i_-permissible we have that \(d_{\omega,G}(v)\le 1\) and \(d_{\omega^o}(v)<1\), since \(\omega(E_G(v,I_{t_{i+1}}))>0\). □

We note two more facts about \((G,\omega)\) given that \((G,\omega)\) is _i_-permissible for some _i_. The first is a trivial consequence of the definition, but we note it explicitly since we shall use the consequence several times in subsequent sections.

Proposition 6.26. _Suppose that_ \((G,\omega)\) _is i-permissible for some i. Then for every open or closed_ (_i_-1)_-reachable tuple_ (_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>) _which is an i-permissible tuple, we have that_<tbc>

\(\frac{c_1|S_1|}{t_ilog^{l_3+2}(n)}\le\omega(E_G(v,S_1,S_2,S_3))\le\frac{c_3|S_1|log^{l_1}(n)}{t_i},\)

<tbc>_and for every open or closed i-permissible tuple_ (_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>) _satisfying_ \(\bigcup\{e\backslash\{v\}:e\in E_\mathcal{T}(v,S_1,S_2,S_3)\}\subseteq K_{j+1}\)_, we have that_

\(\omega(E_G(v,S_1,S_2,S_3))=w_{1^*}(E_{H_{1^*}}(v,S_1,S_2,S_3)).\)

Proof. This follows by the bounds in (P3) and (P5). □

Corollary 6.27. _Suppose that_ \((G,\omega)\) _is i-permissible for some i. Let_ \(v\in I_{t_{i+1}}\)_. Then_

\(1-d_{w^o}(v)\ge\omega(E_G(v,I_{t_{i+1}}))\ge\frac{c_1}{log^{l_3+2}(n)}.\)

Proof. By Proposition 6.25 we have that

\(\omega(E_G(v,I_{t_{i+1}}))+d_{\omega^o}(v)=d_{\omega,G}(v)\le 1.\)

So \(1-d_{\omega^o}(v)\ge\omega(E_G(v,I_{t_{i+1}}))\ge\frac{c_1}{log^{l_3+2}(n)}\) by Proposition 6.26, since \(|I_{t_{i+1}}|\ge t_i\). □

**6.3.3.** _i_**-permissibility and the iterative matching process.** In this section we’ll introduce an algorithm that takes us through the iterative matching process, and in particular, describes how to obtain (_H_<sub>_i_+1</sub>_,w_<sub>_i_+1</sub>) from (_H<sub>i</sub>,w<sub>i</sub>_) for each \(i\in[c_h-1]\). Our strategy relies on using Theorem 6.2, and we’ll show that, for every _i_, given an _i_-permissible pair \((G,\omega)\) we can use Theorem 6.2 on \((G^o,\omega^o)\) to obtain a matching _M<sup>o</sup>_ and have control over various properties in the graph _G_\[_V(G_)\\_V(M<sup>o</sup>_)\]. To do this we introduce the following definition. Recalling _p<sub>S</sub>_ as defined in Section 6.3.1.1, we say that a function \(f:V(G^o)\rightarrow\mathbb{R}_{\ge 0}\) is _vertex allowable for_ \((G,\omega,\Delta,\eta)\) if _p<sub>S</sub>_ satisfies (6.1) (with _r_=4 and _L_=16), and we say that a function \(f_v:E(G^o)\rightarrow\mathbb{R}_{\ge 0}\) is _v-edge allowable for_ \((G,\omega,\Delta,\eta)\) if the functions _q_<sup>(1)</sup>_,q_<sup>(2)</sup>_,q_<sup>(3)</sup> from Proposition 6.17 all satisfy (6.1) with respect to parameters \((G,\omega,\Delta,\eta)\). We also say that \(f:E(G^o)\rightarrow\mathbb{R}_{\ge 0}\) is _edge allowable_ if we can define _f<sub>v</sub>_ such that _f<sub>v</sub>(e_)=_f(e_) if \(e\unknown v\) and _f(e_)=0 otherwise for each \(v\in V(G^o)\) and _f<sub>v</sub>_ is _v-edge allowable for_ \((G,\omega,\Delta,\eta)\). With these definitions in mind we have the following key theorem.

Theorem 6.28. _Given that_ \((G,\omega)\) _is i-permissible and_ T\[_I<sub>t<sub>i</sub></sub>_\] _has depth j, we may obtain a matching M<sup>o</sup> such that in the subgraph_ \(G':=G[V(G)\backslash V(M^o)]\) _the following all hold:_

