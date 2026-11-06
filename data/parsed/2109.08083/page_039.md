<tbc>by \(V_{O/E}^{X\pm Y}(G)\) the set of vertices in \(V(G)\cap V^{X\pm Y}\) that have odd/even parity. We extend this definition naturally also to \(V_{O/E}^{X/Y}(G)\).

For reasons that will become apparent in Chapter 4, we’ll want to be able to pair up vertices of the same parity in _V_<sup>_X+Y_</sup> and _V_<sup>_X-Y_</sup> (to dictate edges but avoid inducing wrap-around edges via these pairings), and as such will want to ensure that the number of vertices of odd parity remaining in _V_<sup>_X+Y_</sup>(_H_<sub>1</sub>) is the same as the number of vertices of odd parity remaining in _V_<sup>_X-Y_</sup>(_H_<sub>1</sub>). (This in turn implies also that the number of vertices of even parity remaining in _V_<sup>_X+Y_</sup>(_H_<sub>1</sub>) is the same as the number of vertices of even parity remaining in _V_<sup>_X-Y_</sup>(_H_<sub>1</sub>), since we reach _H_<sub>1</sub> only by removing disjoint edges from T so that the total size of _V_<sup>_X+Y_</sup>(_H_<sub>1</sub>) is equal to that of _V_<sup>_X-Y_</sup>(_H_<sub>1</sub>).) Thus in the process to reach _H_<sub>1</sub> we must keep track of the parities of vertices remaining in parts _V_<sup>_X+Y_</sup> and _V_<sup>_X-Y_</sup>. Note that this all only applies to the case where _n_ is odd. When _n_ is even, reaching _H_<sub>1</sub> only by removing disjoint edges from T we can be certain that |_V_<sup>_X+Y_</sup>(_H_<sub>1</sub>)|=|_V_<sup>_X-Y_</sup>(_H_<sub>1</sub>)| as every edge removes two vertices of the same parity in parts _X+Y_ and _X-Y_ . Then when it comes to pairing up vertices in _V_<sup>_X+Y_</sup> and _V_<sup>_X-Y_</sup> to dictate edges but avoid wrap-around edges, whilst we know that such a pair with the same parity has pair degree 2, we know that we can therefore _choose_ whether we take the wrap around edge or non-wrap around edge dictated by the pair, depending on what we wish to achieve by this pairing.

Definition 3.27 (_J_-layer intervals). We say that a set _I<sup>J</sup>_ is a _valid J-layer interval_ if \(I^J\subseteq V(\mathcal{T})\cap V^J\) where \(J\in\{X,Y,X+Y,X-Y\}\), with _I<sup>J</sup>_=\[_a,b_\] (i.e. a subinterval of \[-_t_<sub>0</sub>_,t_<sub>0</sub>\]), and \(|I^J|\ge t_0^{1-2\epsilon}.\)3 For \(G\subseteq\mathcal{T}\) , a valid _J_-layer interval _I<sup>J</sup>_ and \(v\notin J\) we let _E<sub>G</sub>(v,I<sup>J</sup>,O/E_) denote the set of edges in _G_ which contain _v_ and a vertex \(u\in V_{O/E}^J(G)\cap I^J\).

We shall keep an eye on these parity related quantities throughout the random greedy edge removal process as well as the initial steps of the iterative matching process. Additionally, for a graph _G_, we let

\(E_{AB}(G)\)

be the set of edges in _G_ such that the _X+Y_ coordinate is of parity type \(A\in\{O,E\}\) and the _X-Y_ coordinate is of parity type \(B\in\{O,E\}\). Then when _n_ is odd \(E_{OE}(G)\cup E_{EO}(G)\) gives the complete set of edges in _G_ which wrap-around. (When _n_ is even we have that \(E_{AB}(G)=\emptyset\) for \(AB\in\{OE,EO\}.\))

The following theorem, proved in Section 5.3, gives the initial quasi-randomness properties which we shall show whp for _H_, the graph obtained from T after removing _A_<sup>∗</sup>, running the random greedy edge removal process and making small parity modifications, and that are required for the iterative matching process described in Chapter 6. Recall \(\alpha_G\) and _p_<sub>gr</sub> as defined in Definition 3.5.

Theorem 3.28. _After removing the absorber A_<sup>∗</sup> _from_ T _, running the random greedy counting process and making some parity modifications, with high probability we obtain a (hyper)graph_ \(H\subseteq\mathcal{T}\) _satisfying the following:_

(_i)_ _every_ T _-valid subset_ \(S\subseteq V(\mathcal{T})\) _satisfies_<tbc>

<tbc>\(|V(H[S])|=(1\pm\alpha_G)|S|p_\mathrm{gr},\)<tbc>

3Recall that \(\epsilon=\frac{10^{-8}}{204800}\) as in Section 3.1.1.

