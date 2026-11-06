For an unsplittable cycle _C_ in a weighted plane graph _G_, let C_<sub>u</sub>(C_) be the set of all unsplittable shortest cycles of _G<sub>C</sub>_ distinct from _C_ that are maximal with respect to \(\le\); see Figure 13b. In other words,

(i) for every distinct \(C_1,C_2\in\mathscr{C}_u(C)\), neither \(C_1\le C_2\) nor \(C_2\le C_1\), and<tbc>

(ii) for any \(C_1\in\mathscr{C}_u(C)\), there is no unsplittable shortest cycle _C_<sub>2</sub> in _G<sub>C</sub>_ other than _C_ such that \(C_1\le C_2\).

As is shown in \[4, Lemma 5.6\], the family C_<sub>u</sub>(C_) is unique, laminar, and every shortest cycle in _G<sub>C</sub>_ distinct from _C_ is either in C_<sub>u</sub>(C_) or embedded inside some cycle of C_<sub>u</sub>(C_).

We are ready to describe the construction of _laminar shortest cycles tree (LSCT)_. Let _G_ be a _clean_ plane weighted graph. As is shown in \[4\], one can find in polynomial time an embedding of _G_ such that the outer face of _G_ is a shortest cycle _C_ of _G_. We do not insist that _G_ is connected, but we will assume that all the vertices and edges of _G_ are drawn inside the region bounded by one of its fixed shortest cycle.

**Definition 5.4** (\[4\])**.** Let _G_ be a clean weighted plane graph embedded in such a way that its outer face is a shortest cycle _C<sub>r</sub>_. The _laminar shortest cycles tree_ (LSCT) of _G_, denoted by T(_G_), is a tree rooted at _C<sub>r</sub>_ whose nodes are (not necessarily all) shortest cycles of _G_, constructed recursively as follows. Initialize _V_(T(_G_))={_C<sub>r</sub>_}, \(E(\mathcal{T}(G))=\emptyset\), C={_C<sub>r</sub>_}, and process each \(C\in\mathcal{C}\) as follows, repeating until \(\mathcal{C}=\emptyset\) (see Figure 4):

Po
P1
S
C
t
Pq-1
Pq

C
C1
C2
C3

(a) Splittable cycle \(C=P_0\cup P_q\) with family P_<sub>s</sub>(C_)={_P_<sub>0</sub>_,P_<sub>1</sub>_,...,P<sub>q</sub>_}. Consecutive pairs \(P_i\cup P_{i+1}\), \(i\in[q-1]\) form C_<sub>s</sub>(C_).

(b) Unsplittable cycle _C_ with family \(\mathscr{C}_u(C)=\{\widehat{C}_1,\widehat{C}_2,\widehat{C}_3\}\). Elements are pairwise incomparable and maximal inside _G<sub>C</sub>_.

Figure 13: Illustration of the families P_<sub>s</sub>(C_) and C_<sub>s</sub>(C_) for a splittable cycle (_left_), and C_<sub>u</sub>(C_) for an unsplittable cycle (_right_).

