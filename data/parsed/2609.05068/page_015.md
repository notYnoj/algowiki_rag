This result is proved by using the possible loads of arcs (_u<sub>i</sub>,v<sub>j</sub>_), which depend on the commodities they carry, as shown in Lemma 2.9, and the flow conservation at node _v<sub>j</sub>_.

**Proposition 2.2.** _If the DCMCF instance described above has a feasible solution of value_ \(\gamma=1\)_, the 3-Partition instance with weights_ \(\{w_i\}_{i\in I}\) _is of type True._

Lemmas 2.9 and 2.10 showed that if the DCMCF instance is feasible, the arcs (_u<sub>i</sub>,v<sub>j</sub>_) crossed by commodity _k<sub>L</sub>_ allow the construction of triplets of objects (and that each arc carries a load _w<sub>i</sub>_) ; flow conservation and Equation (8) allow us to conclude that the sum of weights of each triplet is \(\frac{W}{m}\) , showing that the 3-Partition instance was feasible. The complete proof is given in Appendix A.11.

**Theorem 2.1.** _DCMCF is strongly NP-hard, even when there are at most_ 3 _commodities, all sharing the same source and destination, and when every path from the source to the destination can potentially be used by each commodity._

_Proof._ This is a direct consequence of Propositions 2.1 and 2.2 and the strong NP-hardness of 3-Partition.

## 3 Relaxation of the delay constraints

Constraints (3) rewritten as (6) are the "difficult" constraints of the DCMCF problem. In fact, the function \(g_p:\{x_p^k,(y_a)_{a\in p}\}\rightarrow\sum_{a\in p}\frac{x_p^k}{c_a-y_a}-x_p^kd^k\) is a non-convex function. One way to get good convex relaxations of DCMCF consists of replacing, for every \(k\in K\) and \(p\in P^k\), constraint \(g_p(\{x_p^k,(y_a)_{a\in p}\})\le 0\) by constraint \(h_p(\{x_p^k,(y_a)_{a\in p}\})\le 0\) where _h<sub>p</sub>_ is convex and satisfies \(h_p\le g_p\). Since _g<sub>p</sub>_ is an additive function with a delay term for each arc of _p_, it is natural to decompose the problem by considering all terms separately. This leads to the study of the function _f_ defined by \(f(x,y)=\frac{x}{1-y}\) for \((x,y)\in[0,1]^2\). Constraints (6) can then be formulated as:

