instance from \[27\] illustrated in Fig. 2. Let \(\alpha_{a_0}=\alpha_{a_1}=\alpha_{b_2}=0\), \(\alpha_{b_1}=1\), and \(\alpha_{a_2}=-1\). It is easy to check that \((x,\alpha)\) satisfies (2)-(4). Thus **_x_** is popular and \(\alpha\) is a witness of **_x_**’s popularity.

_Remark._ When **_x_** is integral, the three constraints (2)-(4) are the same as the three constraints in Theorem 5 that characterized popular matchings in terms of witnesses.

## 2.2 Dominant Matchings

Recall the definition of a dominant matching: this is a popular matching that is more popular than all strictly larger matchings in _G_. Consider the instance in Fig. 3 on six vertices _a_<sub>0</sub>_,a_<sub>1</sub>_,a_<sub>2</sub>_,b_<sub>0</sub>_,b_<sub>1</sub>_,b_<sub>2</sub>. The preferences of vertices are indicated in the figure. This instance has 2 max-size popular matchings: _D_={(_a_<sub>1</sub>_,b_<sub>2</sub>),(_a_<sub>2</sub>_,b_<sub>1</sub>)} and _S_={(_a_<sub>1</sub>_,b_<sub>1</sub>),(_a_<sub>2</sub>_,b_<sub>2</sub>)}. The matching _S_ is not dominant since it does not defeat the larger matching _N_={(_a_<sub>0</sub>_,b_<sub>1</sub>),(_a_<sub>1</sub>_,b_<sub>0</sub>),(_a_<sub>2</sub>_,b_<sub>2</sub>)} while the matching _D_ defeats _N_ and is dominant.

For any matching _M_, let _G<sub>M</sub>_ be the graph obtained from _G_ by removing edges labeled (-,-). Observe that in the example discussed above, there is no _D_-augmenting path in _G<sub>D</sub>_ while there is an _S_-augmenting path _a_<sub>0</sub>-_b_<sub>1</sub>-_a_<sub>1</sub>-_b_<sub>0</sub> in _G<sub>S</sub>_. In fact, the absence of such augmenting paths is what characterizes dominant matchings in the set of popular matchings.

**Theorem 6 (\[11\]).** _A popular matching M is dominant iff G<sub>M</sub> has no M-augmenting path._

Any maximum-size popular (hence any dominant) matching matches the same subset of vertices and in fact, a vertex left unmatched in a dominant matching is left unmatched in every popular matching in _G_ \[24\]. Call a vertex _v popular_ if it is matched in any max-size popular matching, else call _v unpopular_. Similarly, call a vertex _v stable_ if it is matched in some (equivalently, every \[17\]) stable matching in _G_, else call _v unstable_. It is known that every popular matching in _G_ matches all stable vertices \[25\].

The LP-based characterization of dominant matchings given below follows from their combinatorial characterization in \[11\].

**Theorem 7.** _A popular matching M in_ \(G=(A\cup B,E)\) _is dominant if and only if M admits a witness_ \(\alpha\) _such that_ \(\alpha_v\in\{\pm 1\}\) _for every popular vertex v._

We will call a witness \(\alpha\) such that \(\alpha_v\in\{\pm 1\}\) for all popular vertices _v_ a _dominant_ witness. For the dominant matching _D_ in the above example, the vector \(\alpha\) defined as \(\alpha_{a_1}=\alpha_{b_1}=1\), \(\alpha_{a_2}=\alpha_{b_2}=-1\), and \(\alpha_{a_0}=\alpha_{b_0}=0\) is a dominant witness (observe that _a_<sub>0</sub>_,b_<sub>0</sub> are unpopular vertices). The characterization of dominant matchings in terms of such witnesses will be useful to us in Section 3. This characterization will lead to a new compact extended formulation of the dominant matching polytope in Section 7 as a face of the extension E_<sub>G</sub>_ of the popular fractional matching polytope.

ao
1
1
bo
3
3
a1
1
1
b1
2
2
1
1
a2
b2
2
2

**Fig.3.** The numbers on edges denote vertex preferences. So _a_<sub>1</sub>_,b_<sub>1</sub> are each other’s top choice neighbors and their second choices are _b_<sub>2</sub>_,a_<sub>2</sub>, respectively, and their last choices are _b_<sub>0</sub>_,a_<sub>0</sub> respectively, and so on.

