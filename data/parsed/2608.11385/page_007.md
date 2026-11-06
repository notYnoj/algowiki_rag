Since \(\Delta\le n-1\), we have _L=O(n_), and hence _N_=|_V(G_)|=_O(n_<sup>2</sup>) and |_E(G_)|=_O(n_<sup>3</sup>). Thus G(_H_), and all oracle queries generated from it, can be constructed in polynomial time.

The following lemma shows that every maximum cut of _G_ encodes a maximum cut of _H_, and that each maximum cut of _H_ has exactly two lifts to _G_.

**Lemma 2.1** (Gadget rigidity)**.** _Every maximum cut of G places each A<sub>v</sub> and B<sub>v</sub> monochromatically on opposite sides, places r and s on opposite sides, and induces a maximum cut of H through the orientation of the sets A<sub>v</sub>. Conversely, every maximum cut of H and either orientation of_ (_r,s_) _determine a maximum cut of G. Consequently,_

\(\mathrm{MC}(G)=nL^2+2nL+1+L\mathrm{MC}(H),\) (12)

\(|\#\mathrm{MC}(G)|=2|\#\mathrm{MC}(H)|.\) (13)

_Moreover every maximum cut contains exactly_ |_W|/_2=_nL vertices of W on each side._

_Proof._ Each vertex of a variable _K<sub>L,L</sub>_ has at most \(\Delta+2\) external neighbors. Consider one variable gadget with parts _A<sub>v</sub>_ and _B<sub>v</sub>_. Its two proper orientations assign +1 to all of _A<sub>v</sub>_ and -1 to all of _B<sub>v</sub>_, or the reverse. Choose the orientation at minimum Hamming distance from the current labeling, allowing either choice in a tie. Relative to this choice, let _a_ vertices of _A<sub>v</sub>_ and _b_ vertices of _B<sub>v</sub>_ be misplaced, and set _q=a+b_. The Hamming distances from the current labeling of \(A_v\cup B_v\) to the two proper bipartite orientations sum to 2_L_. Therefore the nearer orientation has Hamming distance \(q\le L\). The number of cut edges internal to the gadget is<tbc>

\((L-a)(L-b)+ab=L^2-Lq+2ab.\)

<tbc>Thus correcting the orientation of the gadget gains at least

\(Lq-2ab\ge Lq-\frac{q^2}{2}\ge\frac{Lq}{2}\)

internal cut edges, where we used \(2ab\le q^2/2\) and \(q\le L\). Each moved vertex has at most \(\Delta+2\) external neighbors, so this correction loses at most \((\Delta+2)q\) external cut edges. This bound counts incidences between moved vertices and external edges; an external edge incident to two moved vertices may therefore be counted twice, but this is harmless for an upper bound. Since \(L>2(\Delta+2)\), the net change is strictly positive whenever _q\>_0. Consequently every maximum cut orients each _K<sub>L,L</sub>_ gadget properly. Thus each gadget contributes _L_<sup>2</sup> cut edges and exactly _L_ vertices to each side.

If the anchors lie on the same side, flipping one anchor leaves the total number of cut anchor-_W_ edges unchanged, because _W_ is balanced, and additionally cuts {_r,s_}. Hence the anchors are opposite. With opposite anchors, every \(w\in W\) contributes exactly one cut anchor edge. The only orientation-dependent edges are the synchronous edges: the _L_ edges representing \(\{u,v\}\in E(H)\) are cut exactly when the orientations of _A<sub>u</sub>_ and _A<sub>v</sub>_ differ. The gadget and anchor edges contribute the fixed amount _nL_<sup>2</sup>+2_nL_+1, while the synchronous edges contribute _L_ times the encoded cut value in _H_. Maximizing the cut of _G_ therefore maximizes this encoded cut, giving (12). Finally, each labeled maximum cut of _H_ determines every gadget spin, and the two anchor orientations give exactly two lifts, proving (13).

Our graph construction is simpler and more symmetric than the gadget used in Ref. \[5\]. The latter employs asymmetric complete-bipartite vertex gadgets, a separate large complete-bipartite frame, and an additional controller vertex in order to isolate the maximal Laurent exponent. By contrast, our reduction uses only balanced (_K<sub>L,L</sub>_) variable gadgets and two universal anchors (r,s).<tbc>

