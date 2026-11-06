<tbc>they get their most preferred choices. We conclude that \(y=b_j\in W_2\) for some \(\ell<j\le n\), so her partner is the same as in _M_. Thus _x=a<sub>i</sub>_ for some \(1\le i\le n\), and _a<sub>i</sub>_ must be a man in _A_ who prefers _b<sub>j</sub>_ to his partner in _M_. But then _a<sub>i</sub>b<sub>j</sub>_ would block _M_, a contradiction.

For the other direction, suppose that we can set the preferences of the women in _W_<sub>1</sub> such that there is a stable matching \(M'\) not containing \(uw'\). Since \(uw'\) does not block, we have \(uw\in M'\). This implies that \(u'w'\) must be in \(M'\), too. So the agents corresponding to the original ones are matched among each other. Also, \(M'\) has to be a perfect matching, since a man not covered by \(M'\) would block with _w_. Let _M_ be the perfect matching obtained by restricting \(M'\) to \(H-\{u,u',w,w'\}\). If _M_ is not weakly stable in the original instance, then there exists a blocking edge between a woman _b<sub>j</sub>_ where \(j>\ell\) and a man _a<sub>i</sub>_, but then _a<sub>i</sub>b<sub>j</sub>_ would block \(M'\) too, a contradiction.

The forced edge case 1-forced-sm-strat can be proved in a similar way, the only difference being that we set \(\mu\) to contain the single forced edge _uw_.

**Remark 23.** Note that if the graph is a complete bipartite graph and no woman’s preference list is fixed, then k-forced-sm-strat and k-forbidden-sm-strat become easily solvable: we just have to find a perfect matching satisfying the edge restrictions if one exists, which is an assignment problem.

**Remark 24.** Theorem 22 also implies NP-hardness of the stable allocation problem with forced or forbidden edges, where only one side has preferences.

Our results have an interesting consequence for the stable marriage problem with ties and the incomplete preference lists problem with forced and forbidden edges.

**Corollary 25.** 1-forced-smti _and_ 1-forbidden-smti _are NP-complete even if each man’s preference list is strict and each woman’s preference list is just a single tie. The same holds if each man’s preference list is strict, each woman’s preference list is either strict or a single tie, and all preferences are complete._

Now we turn to the complexity of sr-strat.

**Theorem 26.** sr-strat _is NP-complete even for complete graphs._

_Proof._ The problem is clearly in NP. To show NP-hardness, we reduce from x3c, see the definition in Section 2.

Let _I_ be an instance of the x3c. We construct an instance \(I'\) of sr-strat with _G_=(_V,E_) as follows. For each set _C<sub>j</sub>_, we add seven agents \(c_j^1,c_j^2,c_j^3,d_j^1,d_j^2,d_j^3,x_j\) called the _gadget for C<sub>j</sub>_. For each element _a<sub>i</sub>_, we add an agent also denoted by _a<sub>i</sub>_. Finally, we add 2_n_ selector agents _s_<sub>1</sub>_,...s_<sub>2_n_</sub>, see Figure 5.

The preference lists are defined as follows:

a1
a2
1
2
1
2
1
1
2
1
b1
b2

a1
a2
u
u'
1
3
4
2
1
1
2
4
3
1
4
3
2
2
3
4
4
4
2
4
3
2
3
1
4
1
b1
b2
w
w

(a) An instance of com-smti with ties at _b_<sub>1</sub>. Thick edges form a weakly stable matching _M_.

(b) The corresponding 1-forbidden-sm-strat instance. Thick edges form a stable matching \(M'\), independently from the missing preference values.

Figure 4: An illustration of Theorem 22. Higher values correspond to higher preferences.

