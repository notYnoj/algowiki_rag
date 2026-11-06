• _D_<sub>core</sub> holds universe \[_m_\]. For every \(a\in A\) with nonempty core(_I<sub>a</sub>_), it holds the interval core(_I<sub>a</sub>_) with label _a_. _D_<sub>core</sub> is implemented via Lemma 22.<tbc>

• _D_<sub>fringe</sub> holds universe \[_m_\]. For every \(a\in A\) and every fringe interval \(I'\in\mathsf{fringe}(I_a)\) within an _i_th block, it holds the interval \[_i,i_\] with label _a_.<sup>1</sup> _D_<sub>fringe</sub> is also implemented via Lemma 22.<tbc>

• For each block \(i\in[m]\), the data structure _D<sub>i</sub>_ carries universe \[\(\ell\)\]. For every \(a\in A\) and every fringe interval \(I'\in\mathsf{fringe}(I_a)\) within the _i_th block, it holds the interval \(\mathsf{rel}_i(I')\) labeled _a_. Each _D<sub>i</sub>_ is implemented via the assumed linear-time data structure for small universes.

Moreover, for each \(a\in A\), we introduce a bit active_<sub>a</sub>_, initially set, representing whether the label _a_ is still active.

Given a query interval \(J\subseteq[N]\), we perform the following queries to auxiliary data structures and gather all the returned labels.

• Query _D_<sub>core</sub> with inter(_J_).<tbc>

• Query _D_<sub>fringe</sub> with core(_J_) as long as core(_J_) is nonempty.<tbc>

• For each \(J'\in\mathsf{fringe}(J)\), let \(J'\) be contained within the _j_th block. Then query _D<sub>j</sub>_ with \(\mathsf{rel}_j(J')\).

For each returned label _a_, if _a_ is still active, we deactivate _a_ (i.e., unset active_<sub>a</sub>_) and add _a_ to the result label set. This concludes the description of the data structure; we now argue its correctness and efficiency.

## Correctness.

Let _I<sub>a</sub>_ be an input interval labeled _a_ and _J_ be a query interval. First, suppose _a_ is reported by the query. Then, _a_ was still active before the query. If _D_<sub>core</sub> reported _a_, then \(\mathsf{core}(I_a)\cap\mathsf{inter}(J)\neq\emptyset\), which easily implies \(I_a\cap J\neq\emptyset\). Next, if _D_<sub>fringe</sub> reported _a_, then a fringe subinterval \(I'\in\mathsf{fringe}(I_a)\) resides in a block belonging to core(_J_); hence \(I'\cap J\neq\emptyset\) and so \(I_a\cap J\neq\emptyset\). Finally, if _a_ is returned by _D<sub>i</sub>_, then there exist \(I'\in\mathsf{fringe}(I_a)\) and \(J'\in\mathsf{fringe}(J)\), both within the _i_th block, so that \(I'\cap J'\neq\emptyset\); hence trivially \(I_a\cap J\neq\emptyset\).

Conversely, suppose \(I_a\cap J\neq\emptyset\) and _a_ is active. Let _x_ be any element of the intersection and suppose _x_ is within the _i_th block. First, if \(i\in\mathsf{core}(I_a)\), then _D_<sub>core</sub> definitely reports _a_ since _J_ intersects the _i_th block. Otherwise, \(x\in I'\) for some \(I'\in\mathsf{fringe}(I_a)\). If \(i\in\mathsf{core}(J)\), then _D_<sub>fringe</sub> reports _a_ as the data structure carries the interval \[_i,i_\] labeled _a_. In the opposite case, \(x\in J'\) for some \(J'\in\mathsf{fringe}(J)\) and so \(I'\cap J'\neq\emptyset\). Therefore, _D<sub>i</sub>_ returns _a_. We conclude that an active label _a_ is output if and only if \(I_a\cap J\neq\emptyset\), which implies the correctness of our implementation.

## Time.

Suppose _q_ queries are processed by our data structure. Both _D_<sub>core</sub> and _D_<sub>fringe</sub> maintain a universe of size _m_, hold at most O(|_A_|) labels, and accept at most _q_ queries. Thus both of these auxiliary data structures initialize and process the queries in total time O(_m_log_m_+|_A_|+_q_)=O(_N_+|_A_|+_q_). Then, the data structures _D<sub>i</sub>_ have total universe size \(m\ell=\mathcal{O}(N)\), carry at most O(|_A_|) labels in total, and accept O(_q_) queries in total. By our assumption, they all process all the queries in total time O(_N_+|_A_|+_q_). Therefore, the time complexity of our constructed data structure is also linear.

<sup>1</sup>Technically, this may cause two intervals to be assigned to the same label _a_. Formally, in this case, we create two labels _a_<sub>1</sub>_,a_<sub>2</sub> and assign them to the two intervals. Then, whenever _a<sub>i</sub>_ is reported by _D_<sub>fringe</sub>, we translate the label _a<sub>i</sub>_ to _a_ on the fly.

