Let Y_<sub>G</sub>_ be the polytope described by (27)-(32). We will show that the projection of Y_<sub>G</sub>_ onto the space of the **_x_** variables is the dominant matching polytope D_<sub>G</sub>_. Thus X_<sub>G</sub>_ is the same as D_<sub>G</sub>_.

We proved in Section 7.1 that constraints (19)-(24) define an extension R_<sub>G</sub>_ of D_<sub>G</sub>_ (see Theorem 15). Claim 8 settles the upper bound given in Theorem 4.

**Claim 8** Y_<sub>G</sub> is obtained from_ R_<sub>G</sub> by projecting out coordinates x_<sub>(_u,u_)</sub> _for_ \(u\in A\cup B\).

_Proof._ Consider any point \((\mathbf{x},\unknown)\in\mathcal{R}_G\).

1. Constraint (19) and constraint (27) are the same.<tbc>

2. Constraints (22) and (24) imply that \(\sum_{e\in\delta(u)}x_e=1\) for all \(u\in(A\cup B)\backslash U\) and _x_<sub>(_u,u_)</sub>=1 for all \(u\in U\). Thus the right side of constraint (21) is exactly the same as _c<sub>x</sub>(u,u_) for all vertices _u_. Thus constraints (28)-(30) hold.<tbc>

3. Constraints (31) and (32) are implied by constraints (23) and (24).

Thus if \(\mathcal{R}'_G\) is the projection of R_<sub>G</sub>_ obtained by projecting out coordinates _x_<sub>(_u,u_)</sub> - i.e., corresponding to self-loops - then \(\mathcal{R}'_G\subseteq\mathcal{Y}_G\).

Conversely, consider any point \((\mathbf{x},\unknown)\in\mathcal{Y}_G\). Constraints (29) and (30) imply that \(\alpha_u\ge c_x(u,u)=-1=-\sum_{e\in\delta(u)}x_e\) for \(u\in(A\cup B)\backslash U\). We also have \(\alpha_u\ge c_x(u,u)=0=-\sum_{e\in\delta(u)}x_e\) for \(u\in U\) (the second equality holds because every edge _e_ incident to \(u\in U\) is in _E_\\_E<sub>D</sub>_ and constraint (31) tells us that _x<sub>e</sub>_=0). Thus constraints (19)-(21) hold.

Let us augment **_x_** with coordinates _x_<sub>(_u,u_)</sub> for all vertices _u_ defined as _x_<sub>(_u,u_)</sub>=1 for all \(u\in U\) and _x_<sub>(_u,u_)</sub>=0 for all \(u\in(A\cup B)\backslash U\).

- Since \(\sum_{e\in\delta(u)}x_e=1\) for \(u\in(A\cup B)\backslash U\) and \(\sum_{e\in\delta(u)}x_e=0\) for \(u\in U\), constraint (22) is satisfied.<tbc>

**-** Constraint (23) clearly holds.<tbc>

**-** Moreover, constraint (31) along with the above values of _x_<sub>(_u,u_)</sub> for all _u_ implies constraint (24).

Thus the augmented \((\mathbf{x},\unknown)\in\mathcal{R}_G\), in other words, the original \((\mathbf{x},\unknown)\in\mathcal{R}'_G\) (the projection of R_<sub>G</sub>_ defined above). That is, \(\mathcal{Y}_G\subseteq\mathcal{R}'_G\). Hence, \(\mathcal{Y}_G=\mathcal{R}'_G\). \(\square\)

## 7.3 A Lower Bound on the Number of Facets of the Dominant Matching Polytope

We will now prove the second part of Theorem 4, i.e., the dominant matching polytope D_<sub>G</sub>_ has \(\Omega(c^m)\) facets, for some constant _c\>_1. For any \(k\ge 2\), we will construct an instance _G_ on _n_=8_k_+2 vertices and \(m=\Theta(k)\) edges and a family N of 2_<sup>k</sup>_ max-size popular matchings that are _not_ dominant. Because of the results from Section 7.2, for every matching \(N\in\mathcal{N}\), there has to be some constraint in (25) or (26) that is violated by _N_. For any distinct \(N,N'\in\mathcal{N}\), we will show that among the constraints in (25)-(26), the ones violated by _N_ and those violated by \(N'\) have no overlap. This will lead to the lower bound.

Fig. 13 shows the instance _G_ that will be used here. The preferences of \(a'_i,b'_i,c'_i,d'_i\) for \(1\le i\le k\) will be totally analogous to the preferences of the corresponding _a<sub>i</sub>,b<sub>i</sub>,c<sub>i</sub>,d<sub>i</sub>_, with \(x'\) replacing _x_ and vice-versa for every _x_ in \(\cup_i\{a_i,b_i,c_i,d_i\}\).

We describe below the preference lists of _a<sub>i</sub>,b<sub>i</sub>,c<sub>i</sub>,d<sub>i</sub>_ for all _i_ other than _a_<sub>1</sub> and _b<sub>k</sub>_.

\(a_i:b_i\succ d_i\succ b_{i-1}\succ b'_{i-1}c_i:b_i\succ d_i\)<br>
\(b_i:a_{i+1}\succ a'_{i+1}\succ a_i\succ c_id_i:a_i\succ c_i.\)

Note that _b<sub>i</sub>_ prefers both neighbors \(a_{i+1},a'_{i+1}\) that are outside its own gadget \(\langle a_i,b_i,c_i,d_i\rangle\) to neighbors _a<sub>i</sub>,c<sub>i</sub>_ in its own gadget while _a<sub>i</sub>_ prefers both neighbors _b<sub>i</sub>,d<sub>i</sub>_ in its own gadget to neighbors \(b_{i-1},b'_{i-1}\) that are outside its own gadget. The preference lists of _a_<sub>1</sub> and _b<sub>k</sub>_ are given below.

\(a_1:b_1\succ d_1\succ sb_k:a_k\succ c_k\succ t.\)

