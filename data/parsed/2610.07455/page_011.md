<tbc>_L_ vertices. Add every edge between the two blocks. For every original vertex _x_, add 10_N_ edges from _x_ to distinct vertices in _Z_<sub>1</sub> when _s(x_)=0, and to distinct vertices in _Z_<sub>0</sub> when _s(x_)=1.

We first show that every optimum makes the two blocks monochromatic, meaning that all vertices in each block receive the same value, and gives the blocks opposite values. Choose a most frequent value in each block. If these two values are the same, at least _L_<sup>2</sup>/4 edges between the blocks are uncut. Making the blocks monochromatic with opposite values cuts all block edges and loses at most the 20_N_<sup>2</sup> edges attached to the original vertices. Since _L_<sup>2</sup>/4_\>_20_N_<sup>2</sup>, an optimum must have opposite majority values. Up to complementing the entire cut, assume that the majority value of _Z_<sub>0</sub> is 0 and that of _Z_<sub>1</sub> is 1.

Let _a_ be the number of vertices assigned 1 in _Z_<sub>0</sub>, and let _c_ be the number assigned 0 in _Z_<sub>1</sub>. The number of uncut edges between the blocks is \(a(L-c)+(L-a)c=L(a+c)-2ac\ge L(a+c)/2\). Making both blocks monochromatic according to their majority values gains these edges and loses at most 2_N(a+c_) attached edges. Since _L/_2_\>_2_N_, an optimum must have _a=c_=0. Thus _Z_<sub>0</sub> is entirely 0 and _Z_<sub>1</sub> is entirely 1, up to complementing all values.

Once the blocks are fixed, every original vertex _x_ receives all its 10_N_ attached edges exactly when _x=s(x_). Giving _x_ the other value loses 10_N_ attached edges and can gain at most its _N_ incident edges in _P_. Hence every optimum agrees with _s_ on all original vertices, up to complementing the whole assignment.

Let _H<sub>s</sub>_ denote the block and attached edges. The intended assignment cuts every edge of _H<sub>s</sub>_, and complementation preserves the value of every CUT-instance. Therefore

\(\mathrm{OPT}_\mathrm{max}(P\cup H_s)=|H_s|+\mathrm{val}_P(s).\)

The construction depends only on the public value _N_ and on _s_, so Bob can build it without knowing which edges Alice inserted.

Bob now makes four copies of Alice’s streaming state and appends _H_<sub>_s_<sub>00</sub></sub>, _H_<sub>_s_<sub>10</sub></sub>, _H_<sub>_s_<sub>01</sub></sub>, and _H_<sub>_s_<sub>11</sub></sub> to the respective copies. From each optimum, he subtracts the known size of the appended gadget and obtains one point evaluation of _P_. Their alternating sum reveals _b<sub>pq</sub>_, giving an \(\Omega(N^2)\) lower bound for Exact-CSP(CUT).<sup>3</sup>

For a general core relation of degree _d_, the construction in Lemma 4.6 plays the same role. It replaces the two CUT blocks by one block for every value in the core domain. The constraints among the blocks force their most frequent values to define one common endomorphism, which must be an automorphism because the relation is a core. The attached constraints then force the original variables to follow the desired assignment under this automorphism. As in the CUT example, the blocks are large enough that every deviation loses more attached constraints than it can gain in Alice’s instance.

The formal construction gives exactly the property needed in the communication reduction.

**Lemma 2.9** (Informal Lemma 4.6)**.** _Let R be a core relation, and let P be a simple R-instance on O<sub>R</sub>(N_) _variables with at most N<sup>d</sup> constraints and maximum variable degree at most N_<sup>_d_-1</sup>_. For every assignment s to the variables of P, there is an R-instance H<sub>s</sub>, using O<sub>R</sub>(N_) _additional variables and constructible without knowing the constraints of P, such that_ \(\mathrm{OPT}_\mathrm{max}(P\cup H_s)=|H_s|+\mathrm{val}_P(s)\).

Alice’s instance and each pinning gadget use only _O<sub>R</sub>(N_) variables. Bob can therefore recover the 2_<sup>d</sup>_ point evaluations needed by the signed sum, and the lower bound for INDEX<sub>_N<sup>d</sup>_</sub> gives the \(\Omega_R(n^d)\) space lower bound.

<sup>3</sup>Kol, Paramonov, Saxena, and Yu \[KPSY23\] also prove an ad hoc \(\Omega(n^2)\) lower bound for Max-Cut via a different reduction.

