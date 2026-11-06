**Lemma 2.7.** _Let H_<sub>1</sub>_,H_<sub>2</sub>_,...,H<sub>k</sub> and F be graphs such that there exists an increasing injective homomorphism from F to H_<sub>1</sub>_. Then_ \(R_\text{type}(F,H_2,\dots,H_k)\unknown R_\text{type}(H_1,H_2,\dots,H_k)\) _for each_ \(\text{type}\in\{\text{ord},\text{ref},\text{cyc},\text{dih}\}\).

_Proof._ Let \(n\in\mathbb{N}\) and consider a _k_-edge-coloring of _K<sub>n</sub>_. Let _G_ denote the spanning subgraph of _K<sub>n</sub>_ comprising the edges of color 1. Furthermore, let \(\Gamma\) and \(\Lambda\) denote the permutation groups associated with _H_<sub>1</sub> and _F_, respectively, in the permutational Ramsey numbers _R_type(_H_<sub>1</sub>_,H_<sub>2</sub>_,...,H<sub>k</sub>_) and _R_type(_F,H_<sub>2</sub>_,...,H<sub>k</sub>_). To complete the proof, it suffices to show that if _H_<sub>1</sub> is \(\Gamma\)-embeddable in _G_, then _F_ is \(\Lambda\)-embeddable in _G_.

Let \(\chi\) be an increasing injective homomorphism from _F_ to _H_<sub>1</sub>, and suppose that there exists a homomorphism from _H_<sub>1</sub> to _G_ of the form \(\psi_1\circ\varphi_1\), where \(\varphi_1\in\Gamma\) and \(\psi_1:V(H_1)\rightarrow V(G)\) is an increasing injection. Then \(f:=\psi_1\circ\varphi_1\circ\chi\) is an injective homomorphism from _F_ to _G_. We carry out the proof by showing that _f_ can be written as \(f=\psi_2\circ\varphi_2\) for some \(\varphi_2\in\Lambda\) and increasing injection \(\psi_2:V(F)\rightarrow V(G)\).

If type=ord, then \(\varphi_1\) is the identity permutation, so _f_ is increasing, which directly gives the desired result. On the other hand, if type=ref, then \(\varphi_1\) is either the identity permutation, in which case we are done, or \(\varphi_1\) is the reflection with respect to the natural vertex order. In the latter case, we have \(\varphi_1(x)=|H_1|-1-x\) for each \(x\in V(H_1)\), which implies that _f_ is decreasing. By defining \(\varphi_2\in\Lambda\) via \(\varphi_2(x)=|F|-1-x\) for each \(x\in V(F)\), it follows that \(\psi_2:=f\circ\varphi_2\) is an increasing injection from _V(F_) to _V(G_). Therefore, \(f=\psi_2\circ\varphi_2^{-1}=\psi_2\circ\varphi_2\) is the desired representation of _f_.

Next, suppose that type=cyc. Here, we have \(\varphi_1=g^p\) for \(g=\left(\begin{array}{ c c c c }
0 & 1 & 2 & \cdots & |H_1|-2 & |H_1|-1 \\
1 & 2 & 3 & \cdots & |H_1|-1 & 0
\end{array}\right)\) and some \(p\in\mathbb{N}\). First, we show that for any increasing injection \(h_1:V(F)\rightarrow V(H_1)\), the map \(g\circ h_1\) can be written as \(g\circ h_1=h_2\circ r\) for some \(r\in\Lambda\) and increasing injection \(h_2:V(F)\rightarrow V(H_1)\). If \(h_1(|F|-1)\neq|H_1|-1\), then \(g\circ h_1\) is increasing, so we are done. Otherwise, \((g\circ h_1)(|F|-1)=0\) and \(1\unknown(g\circ h_1)(0)\unknown(g\circ h_1)(1)\unknown\cdots\unknown(g\circ h_1)(|F|-2)\). By letting \(r:=\left(\begin{array}{ c c c c }
0 & 1 & 2 & \cdots & |F|-2 & |F|-1 \\
1 & 2 & 3 & \cdots & |F|-1 & 0
\end{array}\right)\), it follows that \(h_2:=(g\circ h_1)\circ r^{-1}\) is an increasing injection, so \(g\circ h_1=h_2\circ r\) is the desired representation of \(g\circ h_1\). Now, by a simple induction on _p_, we conclude that for any increasing injection \(h_1:V(F)\rightarrow V(H_1)\), the map \(g^p\circ h_1\) can also be written as \(g^p\circ h_1=h_2\circ r\) for some \(r\in\Lambda\) and increasing injection \(h_2:V(F)\rightarrow V(H_1)\). By applying this observation to \(g^p\circ\chi\), we obtain \(f=\psi_1\circ g^p\circ\chi=\psi_1\circ h_2\circ r\), so the original desired representation follows by letting \(\psi_2:=\psi_1\circ h_2\) and \(\varphi_2:=r\).

Finally, suppose that type=dih, and let _g_ be defined as above. In this situation, either \(\varphi_1=g^p\) for some \(p\in\mathbb{N}\), or \(\varphi_1=t\circ g^p\) for \(t=\left(\begin{array}{ c c c c }
0 & 1 & 2 & \cdots & |H_1|-1 \\
|H_1|-1 & |H_1|-2 & |H_1|-3 & \cdots & 0
\end{array}\right)\) and some \(p\in\mathbb{N}\). In the former case, the result is proved in the same manner as in the case type=cyc. In the latter case, we have \(f=\psi_1\circ t\circ g^p\circ\chi\), so by the results from the case type=cyc, we conclude that _f_ can be written as \(f=\psi_1\circ t\circ h_2\circ r\), where _r=z<sup>q</sup>_ for \(z=\left(\begin{array}{ c c c c }
0 & 1 & 2 & \cdots & |F|-2 & |F|-1 \\
1 & 2 & 3 & \cdots & |F|-1 & 0
\end{array}\right)\) and some \(q\in\mathbb{N}\), and \(h_2:V(F)\rightarrow V(H_1)\) is an increasing injection. Now, define \(w\in\Lambda\) via _w(x_)=|_F_|-1-_x_ for each \(x\in V(F)\), and observe that \(\psi_2:=\psi_1\circ t\circ h_2\circ w\) is an increasing injection from _F_ to _G_. Therefore, \(\psi_1\circ t\circ h_2=\psi_2\circ w^{-1}=\psi_2\circ w\), which yields \(f=\psi_2\circ w\circ r\). The desired representation now follows by letting \(\varphi_2:=w\circ r\).

0
1
2
3
4

0
1
2
3
4
5

0
1
2
3

0
1
2
3
4
5
6
7

(a) The alternating path \(P_5^\text{alt}\).

(b) The alternating path \(P_6^\text{alt}\).

Figure 1: The alternating paths of orders five and six. Source: \[4, Figure 1\].

(a) The nested matching \(M_4^\text{nest}\).

(b) The nested matching \(M_8^\text{nest}\).

Figure 2: The nested matchings of orders four and eight. Source: \[4, Figure 3\].

