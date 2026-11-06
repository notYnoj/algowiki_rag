At a very high level, the idea is for all the dense vertices on the left to distribute its load to the right vertices, such that each right vertex receives no more than _d/_(2log<sup>2</sup>_m_) real super-elements. After the load distribution step, we empty all real super-elements from the dense chunks; and now all vertices on the left and right are sparse chunks. We now compress each left and right chunk to 1/log<sup>2</sup>_m_ of its original size without losing any real super-elements. This would compress the array by a \(\Theta(1/log^2m)\) factor.

**Offline phase.** The load distribution step consists of an offline phase and an online phase. The offline phase looks at only the real/filler indicator of each super-element, and does not look at the payloads. The goal of the offline phase is to output a matching _M_ between the left vertices _L_ and the right vertices _R_, such that each dense chunk on the left has _d/_2 neighbors in the matching _M_, and each right vertex has no more than _d/_2log<sup>2</sup>_m_ neighbors in _M_. If such a matching can be found, then during the online phase, each dense chunk can route up to _d/_2 super-elements each along a distinct edge in the matching _M_ to a right vertex.

To find the matching, we use the ProposeAcceptFinalize algorithm first proposed by Pippenger \[Pip96\]. For convenience, a left vertex is called a _factory_ and a right vertex is called a _facility_.

Initially, each factory corresponding to a dense chunk is _unsatisfied_ and each factory corresponding to a sparse chunk is _satisfied_. Each productive factory \(u\in L\) has at most _d/_2 real super-elements. Now, repeat the following for \(\text{iter}:=logn'/loglogn'\) times and output the resulting matching _M_ at the end:

(a) _Propose_: Each unsatisfied factory sends a proposal (i.e., the bit 1) to each one of its neighbors. Each satisfied factory sends 0 to each one of its neighbors.<tbc>

(b) _Accept_: If a facility \(v\in R\) received no more than _d/_(2log<sup>2</sup>_m_) proposals, it sends an acceptance message to each one of its _d_ neighbors; otherwise, it sends a reject message along each of its _d_ edges.<tbc>

(c) _Finalize_: Each currently unsatisfied factory \(u\in L\) checks if it received at least \(\frac{d}{2}\) acceptance messages. If so, for each edge over which an acceptance message is received, mark it as part of the matching _M_. At this moment, this factory becomes satisfied.

In our subsequent formal sections, we will use the Expander Mixing Lemma (see Lemma A.1 of Appendix A) to prove that in each iteration of the above ProposeAcceptFinalize algorithm, at most 32/log<sup>4</sup>_m_ fraction of the unsatisfied factories remain unsatisfied at the end of the iteration (Lemma 13.4). Therefore, one can show that after \(logn'/loglogn'\) iterations, all factories become satisfied. Note that each iteration takes _O_(log_d_)=_O_(loglog_n_) depth (this is needed for tallying how many proposals or acceptance messages a vertex has received), and therefore the total depth is only _O_(log_n_). One crucial observation is that the number of edges in the bipartite group is within a constant factor of the number of super-elements, which is _O(n/_log_n_). In this way, over all log_n/_loglog_n_ iterations of the offline phase, the number of generalized boolean gates is upper bounded by _O(n_).

Finally, like in prior work \[ALM90,Pip96\], it is not hard to show that each facility on the right will be matched with at most _d/_(2log<sup>2</sup>_m_) factories.

**Online routing phase.** Each dense chunk wants to route each of its up to _d/_2 real super-elements along a distinct edge in the matching _M_ to the right. The challenge is that we need to accomplish this using a linear number of gates, i.e., each chunk is allowed to consume \(O(d\cdot w)\) gates (ignoring polylog<sup>∗</sup> terms). In comparison, in prior works \[ALS21,Pip96\], this was a non-issue because their chunks were constant in size.

