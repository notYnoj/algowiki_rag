## 4.2 Bounding the depth of the refinement tree

**Definition 10.** _Let v be a node in the refinement tree with the pivots r<sub>v</sub> and b<sub>v</sub>, and let I<sub>r<sub>v</sub>b<sub>v</sub></sub> the list-subinstance of v. Define_ \(R_v=I_{r_vb_v}\cap R\), \(B_v=I_{r_vb_v}\cap B\)_, and P<sub>v</sub> as the_ number of pairs _of v as_ \(P_v=|R_v|\cdot|B_v|\).

**Lemma 11.** _Let v be a non-leaf node of the refinement tree of bichromatic InversionSort and let o,p,q be its children. Then, with probability at least 1/2,_

\(max_{w\in\{o,p,q\}}P_w\le\frac{7}{8}P_v\)

_Proof._ Let \(b\in B\), \(r\in R\) be the inversion and assume w.l.o.g _r<sub>v</sub>\<b\<r\<b<sub>v</sub>_, and call the three children of _v_ as _o,p,q_ with _r<sub>o</sub>=r<sub>v</sub>_, _b<sub>o</sub>=b<sub>p</sub>=b_, _r<sub>p</sub>=r<sub>q</sub>=r_ and _b<sub>q</sub>=b<sub>v</sub>_. See Figure 2. W.l.o.g., assume _b_ is uniformly chosen given _r_, but _r_ has a bias towards making the outer child _q_ smaller, i.e., since _r_ is a max, |P_<sub>q</sub>_| is smaller than if _r_ were uniform. By Lemma 9, we can conclude that with probability at least 3/4, \(max(|B_o|,|B_p|)\le 7/8(|B_o|+|B_p|)\le 7/8|B_v|\), and \(|R_q|\le 3/4|R_v|\) with probability at least 3/4. By a union bound, we have both statements with probability at least 1/2, and in the following we assume they both hold.

From the first statement follows (even if _R<sub>o</sub>=R<sub>v</sub>_ or _R<sub>p</sub>=R<sub>v</sub>_) that \(P_o\le 7/8P_v\) and \(P_p\le 7/8P_v\). From the second statement follows \(P_q\le 3/4P_v\) (even if _B<sub>q</sub>=B<sub>v</sub>_).

With these tools in our hands, we can go back to

**Theorem 5** (Height of the refinement tree)**.** _Let_ T _be the refinement tree of running InversionSort on an instance_ I _with N=n+m elements. With high probability in N, the height of_ T _is O_(log_N)._

_Proof._ Let _x_ be an element of I and consider the root-to-leaf path _P_ of T that consists of the nodes _v_ that contain _x_ in I_<sub>v</sub>_. Let \(Q\subset P\) be the set of nodes where the number of pairs is reduced by a factor 7/8, as in Lemma 11. Then \(|Q|=\Theta(logN)\) and by a Chernoff bound, with probability at least 1-_N_<sup>-2</sup>, |_P_|=_O_(|_Q_|). A union bound over all _x_ gives the statement of the theorem.

## 4.3 pivoting Cost Analysis

Recall that InversionSort always pivots with the newly found inversion, and in doing so, it compares all elements in a bucket _X<sub>i</sub>_ to at most two new pivots. Even though InversionSort does not proceed layer-by-layer (in fact, different vertices of the same layer could have wildly varying times of InversionSort finding inversions in them and refining them into children; see Figure 3), we can still upper bound the total pivoting cost performed on a layer by _O(n+m_). Using Theorem 5, we get that

**Theorem 12** (Pivoting Cost of InversionSort)**.** _Let N=n+m. With probability at least_ 1-1_/N, the pivoting cost of InversionSort on an instance of size N is at most O(N_log_N)._

## 4.4 Inversion Finding Cost Analysis

What remains to be analysed is the cost, in number of comparisons, that is incurred to find the inversions, i.e., pairs of new pivots, as described in Section 2.1

For every stage of InversionSort, the current backbone corresponds to a left-to-right traversal of the current subtree (including the the root) of the refinement tree.

Recalling Definition 8, such an inversion search is performed for each subproblem, we search for an inversion in the list subinstance, and, at least initially or if monochromatic comparisons are<tbc>

