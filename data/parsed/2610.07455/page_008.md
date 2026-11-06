## 2.2 Satisfiability and hard pinning

We now explain why every one-pass algorithm for satisfiability over a core relation _R_ requires \(\Omega_R(\mathsf{NRD}_n(R))\) space, as stated formally in Theorem 5.3. The proof first gives an ideal reduction in which Bob can fix variables to chosen values. We then use CUT to see why unique fixing is sometimes impossible and what weaker property is enough. Finally, we state the general hard-pinning lemma for core relations.

Let _I_={_C_<sub>1</sub>_,...,C<sub>m</sub>_} be a maximum _nonredundant instance_ over a core relation _R_, where _m_=NRD_<sub>n</sub>(R_). Recall from Section 3.3 that every constraint _C<sub>j</sub>_ has a _witness assignment_ \(\alpha_j\) that violates _C<sub>j</sub>_ and satisfies every other constraint in _I_.

In INDEX, Alice receives a string \(b\in\{0,1\}^m\) and inserts _C<sub>i</sub>_ whenever _b<sub>i</sub>_=1. Bob receives an index _j_ and must recover _b<sub>j</sub>_. If Bob could append constraints that _hard-pin_ every variable to the value given by \(\alpha_j\), meaning that the appended constraints force this assignment, then the reduction would be immediate. If _b<sub>j</sub>_=0, the witness \(\alpha_j\) satisfies Alice’s entire instance. If _b<sub>j</sub>_=1, Alice also inserted _C<sub>j</sub>_, which \(\alpha_j\) violates. Thus the final instance would be satisfiable exactly when _b<sub>j</sub>_=0.

The obstacle is that _R_-constraints may not be able to force a unique assignment. The following example shows both the obstacle and the weaker form of pinning that we need.

**Example 2.2** (Hard pinning for CUT)**.** Consider _R_=CUT. Complementing every value preserves every constraint, so any instance satisfied by \(\alpha_j\) is also satisfied by its complement. Bob does not need uniqueness, however. It is enough to append an instance whose satisfying assignments on the original variables are \(\alpha_j\) and its complement.

Bob introduces two dummy variables _z_<sub>0</sub>_,z_<sub>1</sub> and adds the constraint CUT(_z_<sub>0</sub>_,z_<sub>1</sub>). For every original variable _x_, he adds CUT(_x,z_<sub>1</sub>) if \(\alpha_j(x)=0\) and CUT(_x,z_<sub>0</sub>) if \(\alpha_j(x)=1\). Any assignment satisfying these constraints must give _z_<sub>0</sub> and _z_<sub>1</sub> different values. Once those two values are chosen, every original variable is forced. The assignment on the original variables is therefore either \(\alpha_j\) or its complement.

This completes the reduction for CUT. If _b<sub>j</sub>_=0, the assignment \(\alpha_j\) satisfies Alice’s constraints and Bob’s constraints. If _b<sub>j</sub>_=1, Alice inserted _C<sub>j</sub>_, which is violated by \(\alpha_j\). Its complement also violates _C<sub>j</sub>_ because complementing every value preserves whether a CUT-constraint is satisfied. Hence the final instance is satisfiable exactly when _b<sub>j</sub>_=0.

The map that swaps 0 and 1 is an endomorphism of CUT that only permutes its values. Such a bijective endomorphism is called an _automorphism_. Applying an automorphism to every value preserves every constraint, which explains why the unavoidable ambiguity between \(\alpha_j\) and its complement is harmless.

The CUT example shows that Bob does not need to force one assignment uniquely. It is enough to force all original variables according to the same symmetry of the relation. For a core relation, every endomorphism is an automorphism, and this is precisely the property that makes the general construction work.

**Lemma 2.3** (Informal Lemma 4.4)**.** _Let R be a core relation and let_ \(\alpha\) _be an assignment to a set of variables. There is an R-instance whose satisfying assignments on these variables are exactly the assignments_ \(\pi\circ\alpha\)_, where the same automorphism_ \(\pi\) _of R is applied to every variable._

Here is the idea behind the lemma. Introduce one dummy variable _y<sub>a</sub>_ for every value _a_ in the domain. Add constraints among these variables so that, under any satisfying assignment, the map sending _a_ to the value of _y<sub>a</sub>_ preserves _R_ and is therefore an endomorphism. Since _R_ is a core relation, this map must be an automorphism. We then attach every original variable _x_ to these<tbc>

