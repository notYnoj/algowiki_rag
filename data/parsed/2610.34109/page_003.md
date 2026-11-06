<tbc>_edges_ (which govern search speed). Under query _q=(x<sub>q</sub>,c<sub>q</sub>,k_), skipping out-of-disk vertices restricts traversal to the _active projection G_\[A(_c<sub>q</sub>_)\]=\((\mathcal{A}(c_q),\{(u,v)\in E:u,v\in\mathcal{A}(c_q)\})\). When vectors and locations are independent, each global edge lands in _c<sub>q</sub>_ with probability \(\sigma(c_q)\), leaving only \(B\sigma(c_q)\) active edges per vertex in expectation (0.032 edges at \(\sigma=10^{-3}\), _B=_32) and disconnecting _G_\[A(_c<sub>q</sub>_)\].

_Example 2.1._ In Figure 1, disk _c=(g,r_) admits A(_c_)={_s,v_<sub>1</sub>_,v_<sub>2</sub>_,v_<sub>3</sub>_,v_<sub>4</sub>_,t_} (green) and excludes {_h_<sub>1</sub>_,...,h_<sub>7</sub>} (grey). In card (a), storing two vector neighbors leaves row(_s_)=\[_h_<sub>1</sub>_,v_<sub>1</sub>\] with only \(s\rightarrow v_1\) and row(_v_<sub>1</sub>)=\[_h_<sub>5</sub>_,h_<sub>2</sub>\] with no active exits, which traps traversal at _v_<sub>1</sub>. In card (b), wider sorted rows (row(_s_)=\[_h_<sub>1</sub>_,v_<sub>1</sub>_,h_<sub>5</sub>_,v_<sub>2</sub>_,..._\] and row(_v_<sub>1</sub>)=\[_h_<sub>5</sub>_,h_<sub>2</sub>_,v_<sub>2</sub>_,s,..._\]) recover the first \(\ell=2\) active entries (\[_v_<sub>1</sub>_,v_<sub>2</sub>\] at _s_ and \[_v_<sub>2</sub>_,s_\] at _v_<sub>1</sub>), restoring the path \(s\rightarrow v_2\rightarrow v_3\rightarrow v_4\rightarrow t\). To ensure that active entries exist when \(\sigma(c)\) is small, each row must combine global vector neighbors with nearby geographic neighbors in one vector-sorted list.

**Why 1D Range and Per-Condition Indexes Fail.** Range-filtered graphs \[12, 23, 43, 47, 48\] sort all objects into one global sequence \(a_1\le\cdots\le a_n\) so that every query interval is contiguous. Two geometric properties rule out this strategy for 2D disks (proof of Theorem 2.2 in Appendix A.3):

Theorem 2.2 (Disk Range Complexity). _The family_ \(\mathcal{A}(\mathcal{D})=\{\mathcal{A}(c):c=(g,r),g\in\mathbb{S}^2,r\ge 0\}\) _of distinct disk active sets satisfies_ \(|\mathcal{A}(\mathcal{D})|\le\sum_{i=0}^4\genfrac(){pt}{2}{n}{i}=O(n^4)\)_, and reaches_ \(|\mathcal{A}(\mathcal{D})|=\Omega(n^2)\) _on worst-case n-object collections._

Proposition 2.3 (Absence of a Universal Contiguous Order). _Place three objects V_={1,2,3} _at the vertices of a small equilateral spherical triangle on_ S<sup>2</sup>_. A disk centered at the midpoint of any pair_ {_i,j_} _with radius_ \(\Delta(s_i,s_j)/2\) _admits only_ {_i,j}; because the first and last elements in any permutation of V are non-contiguous, no linear order makes_ A(_c_) _contiguous for all disks c._

## 3 Ranked Active-Graph Recovery Theory

Because 2D disks induce \(\Omega(n^2)\) active sets and admit no contiguous order, we serve all disks from a _single_ static graph _G=(V,E_) of bounded degree _B_ (complete proofs appear in Appendix A).

### 3.1 Active-Order Invariance and Recovery Graph

**Active-Order Invariance.** Our first observation is that _filtering a vector-sorted neighbor row preserves the relative vector-distance order of the surviving entries._ Suppose vertex _u_ stores its outgoing neighbors in a row row(_u_)=(_v_<sub>1</sub>_,...,v<sub>B</sub>_) ordered strictly by distance _d(x<sub>u</sub>,x<sub>v</sub>_) (with ties broken by ID _v_, denoted \(v\prec_uw\)). Under disk _c=(g,r_), masking out-of-disk entries leaves the active subsequence \(C_u(c)=\mathrm{row}(u)\cap\mathcal{A}(c)=(v_i\in\mathrm{row}(u):v_i\in\mathcal{A}(c))\), which remains strictly sorted under \(\prec_u\). Let \(\mathrm{rank}_{u,c}(v)\in\{1,\dots,|C_u(c)|\}\) denote the 1-based ordinal rank of \(v\in C_u(c)\) within _C<sub>u</sub>(c_).

_Example 3.1._ Suppose row(_u_)=\[_a,b,c,d,e,f_\] is sorted by \(d(x_u,\cdot)\). Under disk _c<sub>q</sub>_, if {_a,c,d,e_} are active and {_b,f_} are inactive (Figure 4), filtering leaves _C<sub>u</sub>(c<sub>q</sub>_)=\[_a,c,d,e_\] with active ranks 1,2,3,4. For budget \(\ell=3\), a left-to-right scan skips _b_ and stops at the third active entry _d_ without reading _e_ or _f_, recovering \[_a,c,d_\].<tbc>

<tbc>_Definition 3.2 (Complete Active Projection and Recovery Graph)._ Given vector-sorted rows \(\{\mathrm{row}(u)\}_{u\in V}\), disk _c_, and integer _recovery budget_ \(\ell\ge 1\), the _recovery graph_ \(\mathcal{H}_\ell(c)=(\mathcal{A}(c),\{(u,v):u\in\mathcal{A}(c),v\in C_u(c),\mathrm{rank}_{u,c}(v)\le\ell\})\) retains the first \(\ell\) active row entries at each \(u\in\mathcal{A}(c)\), and \(\mathcal{H}_\infty(c)=G[\mathcal{A}(c)]\) is the _complete active projection._

Theorem 3.3 (Subgraph Monotonicity and Cut-Rank Threshold). _For any graph G=(V,E_) _of row width B, disk c, and budget_ \(\ell\ge 1\):_(a)_ \(\mathcal{H}_\ell(c)\) _is a spanning subgraph of_ \(\mathcal{H}_\infty(c)\) _with out-degree at most_ \(\mathrm{min}\{\ell,B\}\)_; (b)_ \(\mathcal{H}_\ell(c)\subseteq\mathcal{H}_{\ell^\prime}(c)\) _for_ \(\ell\le\ell'\) _and_ \(\mathcal{H}_B(c)=\mathcal{H}_\infty(c)\)_; and (c) for_ \(|\mathcal{A}(c)|\ge 2\), \(\mathcal{H}_\ell(c)\) _is strongly connected if and only if_ \(\ell\ge\ell_\mathrm{SC}(c)\)_, where the_ cut rank _is_

\(\ell_\mathrm{SC}(c)=\mathrm{max}_{\varnothing\neq S\subseteq\mathcal{A}(c)}\mathrm{min}_{u\in S,v\in C_u(c)\backslash S}\mathrm{rank}_{u,c}(v)\) (1)

_(with inner minimum_ \(\infty\) _if no edge of_ \(\mathcal{H}_\infty(c)\) _leaves S). In_ (1)_, any subset_ \(S\subseteq\mathcal{A}(c)\) _represents a potential isolated component: the inner minimum is the earliest active rank at which some vertex_ \(u\in S\) _has an edge leaving S, and the outer maximum is the worst-case cut across_ A(_c_) _(proof in Appendix A.1)._

### 3.2 Coordinate Fibers and Route Decomposition

**Coordinate Fibers and Closure.** Real geotagged datasets differ widely in coordinate multiplicity. In POI catalogs (Overture-1M), almost all records have distinct coordinates (_M≈n_); in social- media archives (Yfcc-Clip), 64.6% of coordinates are duplicates and up to 5,726 photos share a single landmark location \[1\]. To model the entire range \(1\le M\le n\), we group all objects at each distinct coordinate \(z\in\mathcal{S}\) into a _coordinate fiber_ \(F(z)=\{v\in V:s_v=z\}\).

(a) Same coordinate - same filter result
C = (g, r)
F(z3)
F(zo)
F(z1)
h1
h2
S
ao
b1
a1
F(z2)
F(z4)
b2
t
h3
h4
inside: all kept
outside: all rejected
(b) Contract fibers, then lift the route
Z0
Z1
Z2
F(zo)
F(z1)
F(z2)
S
ao
b1
a1
b2
t
(i)
(ii)
(i)
(ii)
(i)
(i)
inside a fiber
(ii) bridge edge
Capsule = all objects at one geographic coordinate.

**Figure 2: Two-scale route decomposition (Lemma 3.4, Theorem 3.5).** _(a)_ Disk _c=(g,r_) **admits fibers** _F(z_<sub>0</sub>)_,F(z_<sub>1</sub>)_,F(z_<sub>2</sub>) **in full while rejecting** _F(z_<sub>3</sub>)_,F(z_<sub>4</sub>) **in full.** _(b)_ Contracting active fibers **yields quotient route** \(z_0\rightarrow z_1\rightarrow z_2\)**, which lifts to object route** \(s\rightarrow a_0\rightarrow b_1\rightarrow a_1\rightarrow b_2\rightarrow t\) **alternating intra-fiber paths (green, (i)) and inter-coordinate bridges (orange, (ii); Example 3.6).**

