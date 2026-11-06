During each round, each red node \(r\in R\) removes at most one blue node \(b\in B\) from _C(r_). We say that such an edge {_r,b_} is a _lost edge_ because it can no longer occur in the matching. We write \(L_i\subseteq E\) for the set of all edges lost by the end of round _i_. Note that \(L_1=\emptyset\) because only ‘propose’ messages are sent during the first round.

Because _E_ is a finite set and \(L_{i-1}\subseteq L_i\subseteq E\), there exists a \(z\in\{2,3,\dots\}\) such that _L<sub>z</sub>=L_<sub>_z_-1</sub>. Since received ‘reject’ and ‘break’ messages increase the number of lost edges, it follows that no such messages were received during round _z_. In particular, any unmatched \(r\in R\) at the end of round _z_ must have _C_<sub>_z_-1</sub>(_r_) empty (and hence _C<sub>z</sub>(r_) empty), because otherwise it would have received a ‘reject’ or ‘break’ during round _z_. It follows by Lemma 1 that _M<sub>z</sub>_ is a stable matching. Let us denote this stable matching by \(M_\infty\) in what follows.

## 5.2 Weight and potential

Associate with each edge \(e\in E\) a positive integer weight _w(e_) such that the weights respect the preferences of each node; that is, whenever a node _v_ prefers _x_ over _y_, it holds that \(w(\{v,x\})\ge w(\{v,y\})\). This is always possible, e.g., by choosing \(w\equiv 1\). In fact, to prove Theorem 1, taking \(w\equiv 1\) is sufficient, while the proof (and actually the statement) of Theorem 2 deals with an arbitrary _w_.

Associate with each blue node \(b\in B\) the _weight w<sub>i</sub>(b_)=_w_({_b,p<sub>i</sub>(b_)}) if _b_ is matched; otherwise _w<sub>i</sub>(b_)=0. The _total blue weight_, \(w_i(B)=\sum_{b\in B}w_i(b)\), is equal to the total weight of the matching _M<sub>i</sub>_.

Associate with each red node \(r\in R\) a _potential f<sub>i</sub>(r_) as follows. If _r_ is matched or _C<sub>i</sub>(r_) is empty, set _f<sub>i</sub>(r_)=0. Otherwise, set _f<sub>i</sub>(r_)=_w_({_r,b_}) where _b_ is the first element of _C<sub>i</sub>(r_).

Intuitively, the potential _f<sub>i</sub>(r_) is an upper bound for the extra weight that _r_ could have if we ran the algorithm further than _i_ rounds. In a stable matching, _f<sub>i</sub>(r_)=0 for all \(r\in R\), but we do not necessarily achieve this by running the algorithm for a constant number of rounds. However, we can derive an upper bound for the _total potential_ \(f_i(R)=\sum_{r\in R}f_i(r)\) by observing that lost edges are heavier than those along which proposals (will) go.

**Lemma 2.** _For all i_=2,3_,... it holds that_ \(f_i(R)\le w(L_i)-w(L_{i-1})\).

_Proof._ Each \(r\in R\) that has a positive potential at the end of round \(i\ge 2\) has either received a ‘reject’ or ‘break’ during the round _i_; in both cases _r_ has removed a unique blue node _b_ from _C(r_). The weight of the lost edge {_r,b_} is at least the potential _f<sub>i</sub>(r_) because _C(r_) is ordered by decreasing preference. The claim follows by taking the sum over all red nodes and edges lost during round _i_.

