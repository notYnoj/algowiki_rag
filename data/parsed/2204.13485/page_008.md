that _v<sub>t</sub>v_<sub>1</sub> blocks _M_<sup>∗</sup>, a contradiction again. That is, at least one of the vertices _v_<sub>1</sub>_,...,v<sub>p</sub>_ is deleted or out-dominated.

We conclude that the number of in-dominators in each odd cycle _C_ is at most the sum of the numbers of out-dominated and deleted vertices in _C_ minus one. If _C_ is an even cycle, then the number of in-dominators is at most the sum of the numbers of out-dominated and deleted vertices. Finally, a singleton in \(\pi\) cannot be an in-dominator. It follows from the definitions that the number of in-dominators and the number of out-dominated vertices are the same. By combining these observations, we get that |_S_<sup>∗</sup>| is at least the number of odd cycles in \(\pi\).

The theorem follows by Claims 5 and 6.

We now show that the subset version of the problem is hard.

**Theorem 7.** vertex-subset-del-sr _is NP-complete._

_Proof._ The problem is clearly in NP. To show hardness, we reduce from com-smti, see the definition in Section 2.

Consider an instance (_G_=(_A,B;E),\>_) of com-smti, where _A_={_a_<sub>1</sub>_,...,a<sub>n</sub>_}, _B_={_b_<sub>1</sub>_,...,b<sub>n</sub>_}, and ties are restricted to a subset \(b_1,\dots,b_\ell\), each of which have two neighbors. We create an instance of vertex-subset-del-sr as follows, see Figure 1b for an example. For each \(a_i\in A\), we add three agents \(a'_i\), _x<sub>i</sub>_ and \(x'_i\). For each \(i\in[\ell]\), we add three agents \(b'_i\), \(b''_i\) and _y<sub>i</sub>_. Finally, for \(i=\ell+1,\dots,n\), we add an agent \(b'_i\). Let \(T:=\{b'_i|i\in[n]\}\cup\{b''_i|i\in[\ell]\}\cup\{y_i|i\in[\ell]\}\).

The preference lists of the vertices \(a'_i\) for \(i\in[n]\) and \(b'_i\) for \(i=\ell+1,\dots,n\) are inherited from the original instance. We further extend the preferences as follows:

• we add \(x_i>x'_i\) to the end of each \(a'_i\)’s preference lists,<tbc>

• _x<sub>i</sub>_ has preference \(x'_i>a'_i\) and \(x'_i\) has preference \(a'_i>x_i\),<tbc>

• _y<sub>i</sub>_ has preference \(b''_i>b'_i\),<tbc>

• if \(i\in[\ell]\) and _b<sub>i</sub>_’s two neighbors were _a<sub>j</sub>_ and _a<sub>k</sub>_ with _j\<k_, then \(b'_i\)’s preference is \(y_i>b''_i>a'_j\) and \(b''_i\)’s preference is \(b'_i>y_i>a'_k\).

Let \((G',>',T)\) denote the obtained instance of vertex-subset-del-sr. We claim that there exists a perfect weakly stable matching in (_G,\>_) if and only if there exists a removable set \(S\subseteq T\) in \((G',>',T)\). First suppose there is a perfect weakly stable matching _M_. We create a matching \(M'\) in \(G'\) by adding \(a'_ib'_j\) or \(a'_ib''_j\) for each \(a_ib_j\in M\) and \(x_ix'_i\) for \(i\in[n]\). Then, for every \(i\in[\ell]\), we delete _y<sub>i</sub>_ and the unmatched copy of _b<sub>i</sub>_. Suppose there is a blocking edge to \(M'\). It cannot contain _x<sub>i</sub>_ or \(x'_i\), since each \(a'_i\) is with a better partner. On the other hand, if there is a blocking edge of type \(a'_ib'_j\), then \(j>\ell\), since \(b'_j\) is matched with the best remaining partner if \(j\le\ell\). But by the definition of \(>'\), this means that _a<sub>i</sub>b<sub>j</sub>_ is blocking _M_, a contradiction.

For the other direction, suppose there is a set \(S\subseteq T\) such that there is a stable matching \(M'\) in \(G'-S\). Each _a<sub>i</sub>_ must be matched to some \(b'_j\) or \(b''_j\), since otherwise there would be no stable matching because of the cycle \(\{a'_i,x_i,x'_i\}\). Also, for any \(j\in[\ell]\), at most one of \(b'_j\) and \(b''_j\) can be matched to some \(a'_i\), since otherwise \(b'_jb''_j\) would be a blocking edge. Therefore, \(M'\) induces a perfect matching _M_ in the original instance. If there is an edge blocking _M_, then the copy of the same edge is blocking \(M'\), contradiction.

**Remark 8.** vertex-subset-del-sr is NP-complete even in the special case when _G_ is complete. In the reduction above, we can add the remaining edges to the end of the agents’ preference lists, such that they are strictly worse than any original edge.

