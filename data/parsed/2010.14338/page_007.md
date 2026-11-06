the same manner. This avoids unwanted interference among different clause and variable gadgets, respectively. The variable gadgets are placed to the bottom-left of all clause gadgets.

For each positive occurrence of a variable _X<sub>i</sub>_ in a clause _C<sub>j</sub>_, we place a dedicated _connection point_ \(p_{ij}^+\in P_\phi\) as well as suitable _connection demands_ from \(p_{ij}^+\) to a dedicated inner point of _GX<sub>i</sub>_ and to a dedicated inner point of _GC<sub>j</sub>_. Their purpose is to force optimal MinGMConn solutions to create specific M-paths (going first up and then right in a narrow corridor) connecting a variable to the clauses in which it appears positively. We call the area covered by these two demands a _(positive) variable-clause path_. Similarly, there are connection points \(p_{ij}^-\in P_\phi\) with suitable demands for negative appearances of _X<sub>i</sub>_ in _C<sub>j</sub>_, creating a _(negative) variable-clause path_ (going first right and then up in a narrow corridor).

Finally, there is a _starting point_ \(S\in P_\phi\) to the bottom-left of all other points. It has a demand to a _clause point c<sub>j</sub>_ in the top-right of each clause gadget _GC<sub>j</sub>_ (an _SC demand_) and to a _variable point x<sub>i</sub>_ in the bottom-left of each variable gadget _GX<sub>i</sub>_ (an _SX demand_). The inside of clause gadgets simply provides different entrance points for the variable-clause paths, while the inside of variable gadgets forces an optimal solution to choose between using either only positive or only negative variable-clause paths. We will use these choices inside variable gadgets to identify an optimal solution for \((P_\phi,D_\phi)\) with a variable assignment for \(\phi\). Details about clause and variable gadgets are given in Figure 3 and at the end of this section.

### Intuition of the Reduction.

Our construction is such that the non-_SC_ demands (including the ones within gadgets) form a monotone, vertically separable demand set. Thus, for

\(D_\overline{SC}:=\{d\in D_\phi|d\text{is not an}SC\text{demand}\}\text{and}\alpha=\alpha(\phi):=|D_\overline{SC}|,\) (1)

Lemma 6 implies that any solution \(Q_\phi\) for \((P_\phi,D_\phi)\) has size at least \(\alpha\).

1
GC1
X2
GC2
X3
GC3
GX1
X1
GX2
X2
GX3
X3
GX4
X3
S

Figure 2: MinGMConn instance \((P_\phi,D_\phi)\) for \(\phi=(X_1\vee\neg X_2\vee X_3)\wedge(X_1\vee X_2\vee\neg X_4)\wedge(\neg X_1\vee\neg X_2\vee X_4)\). Input points are shown as (red, yellow, or black) disks. For clause and variable gadgets, we show only the clause points _c<sub>j</sub>_ and the variable points _x<sub>i</sub>_; their remaining inner points and demands are illustrated in Figure 3. The small black disks represent the connection points \(p_{ij}^+,p_{ij}^-\). Non-_SC_ demands are shown as shaded, orange rectangles, while _SC_ demands are shown as dashed, red rectangles.

