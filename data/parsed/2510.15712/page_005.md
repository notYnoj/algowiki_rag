It is not possible to reuse the general reduction from 3-SAT to show hardness of approximation. Consider the clauses \(A=\neg y\), _C=x_, \(C'=\neg x\) and \(D=x\vee y\) with the weights _w(A_)=8 , \(w(C)=w(C')=2\) and _w(D_)=1. The assignment \(x,y\mapsto 0,0\) has a weight of _w(C_)+_w(D_)=3, whereas flipping the value of x leads to an assignment of weight \(w'(C)=2\). Thus, this is an improving move, but not if it should improve by an \(\alpha\ge 2\) and similar examples exist for larger \(\alpha\). These problems don’t occur with lexicographic weights, and using a reduction from LocalLexMax-4-SAT, we can give a very short proof.

\(\blacktriangleright\) **Proposition 6** (Skopalik and Vöcking [21])**.** _For any computable_ \(\alpha>1\) _and any congestion game G, finding an_ \(\alpha\)_-equilibrium is PLS-complete._

**Proof.** We reduce from LocalLexMax-4-SAT. Let \(F=C_0\wedge C_1\wedge\cdots\wedge C_{m-1}\) be a weighted 4- CNF formula with _w(C<sub>j</sub>_)=2_<sup>j</sup>_. For an assignment \(\alpha\), define \(C(\alpha):=(C_{m-1}(\alpha),\dots,C_0(\alpha))\in\{0,1\}^m\). The total weight of satisfied clauses is thus simply \(C(\alpha)\), interpreted as a binary number. Thus, \(\mathrm{Value}(\alpha)\le\mathrm{Value}(\beta)\) if and only if \(C(\alpha)\unknown_\mathrm{lex}C(\beta)\), i.e., only the first differing bit matters. This means we can change the clause weights from 2_<sup>j</sup>_ to _c<sup>j</sup>_ for any \(c\ge 2\) and all the answers to \(\mathrm{Value}(\alpha)\le^?\mathrm{Value}(\beta)\) will stay the same. We choose \(c=\alpha+1\).

A solution to LocalLexMax-4-SAT is an assignment that locally maximizes the weight of satisfied clauses. In the following proof it might be better to think about _minimizing_ the weight of _unsatisfied_ clauses (which is of course the same).

We will now define the congestion game. The resources are the clauses _C_<sub>0</sub>_,...,C_<sub>_m_-1</sub>. The players are the variables {_x_<sub>1</sub>_,...,x<sub>n</sub>_}. Player _x<sub>i</sub>_ has two strategies:

\(\mathrm{true}_i:=\{C\in F|\neg x\in C\}\)<br> \(\mathrm{false}_i:=\{C\in F|x\in C\}.\)

Note that strategy profiles in the game are in a 1-to-1 correspondence with the Boolean assignments to the variables of _F_. A player (i.e., variable _x_) uses the resources (i.e., clauses) that are _not_ satisfied by the current assignment and contain the variable _x_. The delay _d<sub>C</sub>_ of clause/resource _C<sub>j</sub>_ is defined to be 0 if strictly fewer than _k_ players use it (where \(k\le 4\) is the size of _C<sub>j</sub>_), and \(w(C_j)=(1+\alpha)^j\) if _k_ players do (note that _C<sub>j</sub>_ can never be used by more than _k_ players). The more valuable clauses thus cause a higher delay for the player then less valuable clauses. Apart from the value \(1+\alpha\), this is roughly as in [7].

We must now show that a pure \(\alpha\)-Nash equilibrium corresponds to a local minimum of LocalLexMax-4-SAT. Contrapositively, we show that a variable flip that improves the weight of satisfied clauses corresponds to a player who will change their strategy. Consider an improving flip of variable _x<sub>i</sub>_ (from False to True, without loss of generality). There is an index _j_ such that _C<sub>j</sub>_ used to be unsatisfied before the flip and is now satisfied, and the clauses _C_<sub>_j_+1</sub>_,...,C<sub>m</sub>_ do not change their status. The delay for player _x<sub>i</sub>_ before the flip is therefore at least

\((1+\alpha)^j.\) (2.1)

Since the flip does not change the status of _C_<sub>_j_+1</sub>_,...,C<sub>m</sub>_, the unsatisfied among them contain neither _x_ nor \(\bar{x}\) and thus do not contribute to the delay for player _x_. Thus, their delay after the flip is at most

\(\sum_{l\le j-1}(1+\alpha)^l=\frac{(1+\alpha)^j-1}{\alpha}.\) (2.2)

Thus, changing the strategy reduces the delay of player _x<sub>i</sub>_ at least by a factor of \(\alpha\), so this is not an \(\alpha\)-Nash equilibrium. \(\blacktriangleleft\)

