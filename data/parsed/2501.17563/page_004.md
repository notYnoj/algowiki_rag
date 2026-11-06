2. Constraints:<tbc>

(a) (Bounds<sup>3</sup>) \(\forall i,j\in U:\forall k\in(i\unknown\rightarrow j):0\le X_{ij},X_{ji},Z_{kij}\).<tbc>

(b) (Ancestry) \(\forall i,j\in U:X_{ij}+X_{ji}+\sum_{k\in(i\unknown\rightarrow j)}Z_{kij}\ge 1\).<tbc>

(c) (Loosely LCA) \(\forall Z_{kij}:(1)Z_{kij}\le X_{ki};(2)Z_{kij}\le X_{kj}\).<tbc>

(d) (Depth) \(\forall i\in U:D_i\ge\sum_{(i\neq)j\in U}X_{ji}\).<tbc>

3. Objective function: minimize \(f\cdot D=\sum_{i\in U}f_i\cdot D_i\).

Observe that we relaxed the ancestry and depth constraints to be inequalities, rather than equalities, even though STTs satisfy them with equalities.

**Remark 1.3.** _X_ and _Z_ seem to serve slightly different roles. A canonized way to look at them is by adding variables of the form _Z<sub>iij</sub>_ to represent _i_ being the LCA of _i_ and _j_. In this case _X<sub>ij</sub>=Z<sub>iij</sub>_, and the ancestry inequality becomes \(\forall i,j:\sum_{k\in[i\unknown\rightarrow j]}Z_{kij}\ge 1\). If we wish, we can also define _Z<sub>iii</sub>_ and have an ancestry inequality for _i=j_, which would imply \(Z_{iii}\ge 1\) (every node is its own ancestor) and redefine \(D_i\ge\sum_{j\in U}Z_{jji}\) so that the STT depth and the LP depth are the same. All of this being said, we stick to the separated presentation of the _X_ and _Z_ variables, particularly because _Z_ is a little more artificial (see Section 5.2).

## 1.2 Conjectures and Known Results

In this subsection we summarize important facts regarding the LP, all were proven in \[9\].

**Definition 1.4** (STT Induced Point)**.** Let _T_ be an STT. We denote by (_X<sup>T</sup>,Z<sup>T</sup>,D<sup>T</sup>_) the LP variables it induces: _X<sub>ij</sub>_=1 if _i_ is ancestor of _j_, _Z<sub>kij</sub>_=1 if _k=LCA(i,j_) in _T_. The rest of the _X,Z_ variables are 0, and \(\forall i\in U:D_i=\sum_{j\in U\backslash\{i\}}X_{ji}\).

**Property 1** (Trees are Feasible)**.** Let _T_ be an STT. Then (_X<sup>T</sup>,Z<sup>T</sup>,D<sup>T</sup>_) is a feasible solution. Moreover, the ancestry and depth inequalities are tight (equalities).

**Remark 1.5** (Depth Discrepancy)**.** Let _T_ be an STT. Observe that \(\forall v\in U:depth(v)=D_v^T+1\). This means that we can relate the cost of the STT to the value of the LP on the point it induces: \(cost(T,f)=\sum_{v\in U}f_v\cdot depth(v)=\sum_vf_v+f\cdot D\). If _f_ is a vector of weights and not frequencies, first normalize it. Throughout the text, we usually deal with depths of the LP (the _D_ variables), and it is fine since we know how to relate them to the actual STT depths and its cost.

**Property 2** (Integer Domination)**.** Let \((X',Z',D')\) be an _integer_ feasible solution. Then there exists an STT _T_, which can be computed efficiently, such that \(\forall i\in U:D'_i^T\le D'_i\). Alternatively phrased: the Integer-LP has an optimum that corresponds to an STT.

**Property 3** (2-Approximation)**.** Let \((X',Z',D')\) be _any_ feasible solution. Then there exist an STT _T_, which can be computed efficiently, such that \(\forall i\in U:D_i^T\le 2\cdot D'_i\).

Both Property 2 and Property 3 are proven constructively in \[9\]. The STT that achieves these guarantees is computed by the following rounding scheme. Note that this scheme not only rounds all the coordinates to be integer, it also takes integer solutions and "rounds" them to STTs.

<sup>3</sup>Technically we can omit the non-negativity constraints on _Z_, since _Z_ is not part of the objective and can only "help" the ancestry-constraints when it is non-negative. Alternatively, we can keep \(Z\ge 0\) and have the non-negativity of _X_ implied by the loosely-LCA constrains. We cannot omit both sets, since then the LP becomes unbounded.

