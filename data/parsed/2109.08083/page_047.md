## 4.1. FINDING AN INTEGRAL DECOMPOSITION FOR _L_<sup>∗</sup> 41

<tbc>\(O\left(p_Ln^{2.6\times 10^{-5}}\right)\) edges to \(\Phi\)): (0,-1,-1,1) and (0,1,1,-1) with negative sign, and (-1,0,-1,-1) and (1,0,1,1) with positive sign (see Figure 1). In this way, no weight is added to \(V^{X+Y}\cup V^{X-Y}\) and, at worst, rather than cancelling weight in _V<sup>Y</sup>_, we add at most _t<sub>X</sub>_ to the support in \(V^Y\cap[-1,1]\) and have no support anywhere else in T .

Suppose that the total size of the support on _V<sup>Y</sup>_ is now \(t'_Y\). By the nature of the edges added, it still follows that \(v_1^Y,v_{-1}^Y=\pm t'_Y/4\), and \(v_0^X=\mp t'_Y/2\). However, we know that, since \(\mathbf{v}\in\mathcal{L}_1^Y(\mathcal{T})\), by Proposition 3.16, \(\sum_{i\in V^Y\cap[-1,1]}i^2v_i=0\mathrm{mod}n\), and thus that \(\sum_{i\in V^Y\cap[-1,1]}i^2v_i=0\). That is, \((-1)^2t'_Y/4+(0)^2t'_Y/2+(1)^2t'_Y/4=0\). It follows that \(t'_Y=0\), completing the proof. □

Lemma 4.1 tells us that we have an integral decomposition \(\Phi\) for _L_<sup>∗</sup> with an upper bound on \(|\Phi|\). More specifically it tells us that we can describe _L_<sup>∗</sup> as the difference of the shadows of two (multi)-sets of edges, \(\Phi^+\) and \(\Phi^-\), each of size \(O\left(p_Ln^{2.6\times 10^{-5}}\right)\). We now wish to modify \(\Phi\) so that \(\Phi\in\{-1,0,1\}^{E(\mathcal{T})},\partial\Phi-L^*=\mathbf{0}\) (i.e. this property is not affected), but \(\Phi^+\) and \(\Phi^-\) are both matchings. We shall use zero-sum configurations to achieve this. By adding a zero-sum configuration to \(\Phi\), we are adding four edges with positive weight, and four edges with negative weight, in total changing the support at any vertex by -1+1=0, therefore not affecting \(\partial\Phi-L^*\).

Lemma 4.5. _Let_ \(\Phi\) _be an integral decomposition for L_<sup>∗</sup> _such that_ \(\Phi\) _consists of_ \(O\left(p_Ln^{2.6\times 10^{-5}}\right)\) _edges and all edges are contained in the interval_ \(I'_{n^{10-5}}\)_. Then we can modify this to a decomposition_ \(\Phi'\) _which is the difference of two matchings, M_<sup>+</sup> _and M_<sup>-</sup> _using only_ \(O\left(p_Ln^{2.6\times 10^{-5}}\right)\) _additional edges, such that_ \(\Phi'\subseteq\mathcal{T}[I'_{n^{2.61\times 10^{-5}}}]\).

Proof. We plan to use zero-sum configurations as follows: suppose a vertex _v_ is covered by more than one positive edge or more than one negative edge. Then either \(\Phi\) contains the same number of positive and negative edges covering _v_, or \(\Phi\) contains one more positive edge covering _v_ than the number of negative edges,

VX
-1
0
1
VY
-1
0
1
VX+Y
-1
1
VX-Y
-1
1

Figure 1. Edges added to push support onto _V<sup>Y</sup>_. Green edges are added with weight +1 and red edges are added with weight

-1.

