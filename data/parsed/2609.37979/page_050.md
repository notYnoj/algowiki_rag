#### Decision versions.

We view IS as the decision problem on instances (_G,k_) asking whether _G_ has an independent set of size at least _k_, and MaxCut as the decision problem on instances (_H,T_) asking whether _H_ has a cut of size at least _T_.

### Reduction.

Given an instance (_G,k_) of IS, let _G_=(_V,E_) and _m_:=|_E_|. We construct a graph _H=R(G_) as follows (cf. \[Bar23\]): add a distinguished vertex _s<sup>⋆</sup>_ adjacent to every \(v\in V\) ; and for each edge \(e=\{u,v\}\in E\), attach a constant-size gadget by adding two new vertices _e<sub>u</sub>,e<sub>v</sub>_ and the five edges<tbc>

\(\{e_u,e_v\},\{s^\star,e_u\},\{s^\star,e_v\},\{u,e_u\},\{v,e_v\}.\)

<tbc>(No other edges are added; in particular, we do not keep the original edges of _G_ in _H_.) We set the MaxCut threshold to

\(T:=k+4m,\)

and output the instance (_H,T_). Barak proves that _G_ has an independent set of size at least _k_ if and only if _H_ has a cut of size at least _T_, so this is a valid polynomial-time many-one reduction \[Bar23\].

### Isomorphism preservation.

Let \(\varphi:G\rightarrow G'\) be a graph isomorphism and note that it preserves the parameter _k_ and the number of edges _m_. We extend \(\varphi\) to an isomorphism \(\psi:R(G)\rightarrow R(G')\) by mapping \(s^\star\mapsto s^\star\), each original vertex \(u\mapsto\varphi(u)\), and for each edge \(e=\{u,v\}\in E(G)\) mapping the gadget vertices \(e_u\mapsto(\varphi(e))_{\varphi(u)}\) and \(e_v\mapsto(\varphi(e))_{\varphi(v)}\), where \(\varphi(e)=\{\varphi(u),\varphi(v)\}\in E(G')\). Since the gadget adjacencies are defined purely in terms of incidences to _s<sup>⋆</sup>_, _u_, _v_, and the internal gadget edge {_e<sub>u</sub>,e<sub>v</sub>_}, this mapping preserves all edges. Hence \(R(G)\cong R(G')\) and the threshold _T_ is preserved.

Therefore the reduction is isomorphism-preserving, i.e. \(\mathsf{IS}\le_p^\cong\mathsf{MaxCut}\).

## 9.4 The Hardness of 3-SAT

To establish the hardness of 3-SAT, we need a reduction other than the one introduced by Karp in \[Kar72\], as Karp’s reduction is not isomorphism-preserving. Instead, we prove hardness through the following sequence of reductions: \(\mathsf{Coloring}\le_p^\cong 3\)-\(\mathsf{Coloring}\le_p^\cong 3\)-SAT

### 9.4.1 Lovász’s Reduction for Colorability

The following construction goes back to László Lovász (see \[Lov73\]). We give a full description of Lovász’s construction here since the paper is hard to find.<sup>36</sup> See Figure 4 for an example of the construction.

**Definition 9.18** (See \[Lov73\])**.** Given a graph _G_ with vertex set _V(G_) and edge set _E(G_). Further, let \(k\ge 3\) be an integer. We construct a new graph L(_G,k_) with:

• \(V(\mathcal{L}(G,k)):=V\unknown C\unknown W\unknown\{G_g,G_b\}\) with<tbc>

– \(V:=\{v^{(i)}|v\in V(G),i\in[k]\}\)<tbc>

– \(C:=\{c_v^{(i)}|v\in V(G),i\in[k]\}\)<tbc>

**–** \(W:=\{e_u^{(i)},e_v^{(i)},e_g^{(i)}|e=\{u,v\}\in E(G),i\in[k]\}\)<tbc>

• \(E(\mathcal{L}(G,k)):=E_b\unknown E_g\unknown E_C\unknown E_W\) with<tbc>

**–** \(E_b:=\{G_b,G_g\}\cup\{\{v^{(i)},G_b\}|v\in V(G),i\in[k]\}\)<tbc>

<sup>36</sup>We refer the interested reader to the following website for further information: `https://users.encs.concordia. ca/~chvatal/notes/color.html`

