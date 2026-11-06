Here \(\mathrm{dist}(a,\perp):=\mathrm{max}_{a^\prime\in\mathcal{A},b\in\mathcal{B}}\mathrm{dist}(a',b)\).

An _alignment gadget_ is a mapping from A,B into respective strings GA_<sub>A</sub>_(A),GA_<sub>B</sub>_(B) such that for some parameter _c_GA=_c(n<sub>A</sub>,n<sub>B</sub>_):

\(\mathrm{min}_\mathrm{alignment}\mu\mathrm{cost}(\mu,\mathcal{A},\mathcal{B})\le\mathrm{dist}(\mathrm{GA}_A(\mathcal{A}),\mathrm{GA}_B(\mathcal{B}))+c_\mathsf{GA}\le\mathrm{min}_\mathrm{structuredalignment}\mu\mathrm{cost}(\mu,\mathcal{A},\mathcal{B}).\) (5)

_Lemma_ 19 (Alignment gadgets \[BK15\]).

_Edit distance, LCS (with binary alphabet), and Dynamic Time Warping admit alignment gadgets that can be computed in linear time._

## Completing the proof of BP-SETH-hardness

_Proof of Theorem 17._ Suppose that we have an algorithm that computes dist() for strings of length _N_ with preprocessing time _O(N<sup>t</sup>_) and query time \(O(N^{2-\epsilon})\). Given a BP over _n_=2log<sub>2</sub>(_N_) variables, we construct all its normalized vector gadgets in near-linear time as in Lemma 18.

We partition the A-NVGs into 2<sup>(1-1_/t)n_</sup> subsets A<sub>1</sub>_,..._A<sub>2<sup>(1-1_/t)n_</sup></sub> of size 2_<sup>n/t_</sup> each (and likewise for B). For each subset A_<sub>i</sub>_, we construct its alignment gadget _A<sub>i</sub>_ of size \(\tilde{O}(N^{1/t})\). For B_<sub>j</sub>_, let _B<sub>j</sub>_ be constructed by the alignment gadget for the set repeated twice. If no pair of half-assignments corresponding to \(\mathcal{A}_i\times\mathcal{B}_j\) satisfies the BP, then every pair of NVGs is at distance _c<sub>F</sub>_, and by (5) the distance of _A<sub>i</sub>,B<sub>j</sub>_ will be _d<sub>F</sub>_:=2_<sup>n/t</sup>c<sub>F</sub>-c_GA. If there is a satisfying pair, then the structured alignment that matches the corresponding NVGs will have cost at most

\(d_T:=c_T+(2^{n/t}-1)c_F-c_\mathsf{GA}<d_F.\)

We preprocess all the strings in total time \(\tilde{O}\big(N^{1-1/t}\cdot(N^{1/t})^t\big)=\tilde{O}(N^{2-1/t})\). Finally, we compute the distance between all (_N_<sup>1-1_/t_</sup>)<sup>2</sup> pairs in time \(O\big(N^{2-2/t}\cdot(N^{1/t})^{2-\epsilon}\big)=O\big(N^{2-2\epsilon/t}\big)\). The BP is satisfiable iff at least one of the pairs is at distance at most _d<sub>T</sub>_.

## 7.2 Preprocessing doesn’t help for approximate ED in truly-subquadratic time

_Theorem_ 20 (Hardness of Approximation).

_If there is an_ \(\alpha\)_-approximation algorithm for edit distance that runs in polynomial preprocessing time and truly-subquadratic query time, then there is an_ \((\alpha+o(1))\)_-approximation algorithm that runs in truly-subquadratic time with no preprocessing._

The proof combines the divide-and-conquer steps from our approximate edit distance algorithm (Section 5) with that of \[WW18\] (see also last step in the proof of Theorem 17).

_Proof._ Suppose that there exists an algorithm that computes an \(\alpha\)-approximation of edit distance using _O(n<sup>t</sup>_)-preprocessing and \(O(n^{2-\epsilon})\)-query time. First, we assume wlog that the true edit distance is \(k=\omega(n^{1-1/2t})\), otherwise we can solve the problem in time _O(n_<sup>2-1_/t_</sup>) using the algorithm of \[LMS98\]. In particular, we can henceforth neglect additive errors of _O(n_<sup>1-1/2_t_</sup>).

Using the notation of Section 5.2, we decompose the strings into windows with base width _d_:=_n_<sup>1_/t_</sup>. The _A_-windows have no overlap, and for the _B_-windows we consider \(\mathcal{B}^\tau\) for \(\tau=n^{-1/2t}\). Hence we have \(\tilde{O}(n^{1-1/t})\mathcal{A}\)-windows and \(\tilde{O}(n^{1-1/2t})\mathcal{B}\)-windows, all of length _O(n_<sup>1_/t_</sup>).

We preprocess all the windows in time \(\tilde{O}\big(n^{1-1/2t}\cdot(n^{1/t})^t\big)=\tilde{O}\big(n^{2-1/2t}\big)\).

We then run the \(\alpha\)-approximate edit distance algorithm on pairs of windows. By the argument of \[Ukk85\], it suffices to only compute the distances between pairs of windows whose starting points are within \(\pm k\) far apart. In particular for every A-window, we only need to compute the<tbc>

