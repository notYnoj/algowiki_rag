_Proof._ We point out that we only consider the case where _b_ is on a hole \(h'\neq h\). However, the case where _b_ on _h_ is simpler and can be straight-forwardly deduced from the description of the harder case by minor adaptions. Assume for contradiction that a vertex \(v_k(h)\in(v_i(h),v_j(h))\) is not in _S<sub>b,h</sub>_, i.e. does not benefit from _e<sup>t</sup>_. Then \(d_{P^t}(b,u^t)+\omega^t+d_{P^t}(v^t,v_k(h))\le d_{P^{t-1}}(b,v_k(h))\).

Let _T<sub>v<sup>t</sup></sub>_ be the shortest path tree rooted at _v<sup>t</sup>_ on _P_. By definition of \(r_{v^t,h^\prime,h}\) and by the assumption \(r_{v^t,h^\prime,h}\notin(v_i(h),v_j(h))\), every path from _b_ to _v<sub>k</sub>(h_) has to cross either the path _T<sub>v<sup>t</sup></sub>_\[_v<sub>i</sub>(h_)\] or the path _T<sub>v<sup>t</sup></sub>_\[_v<sub>j</sub>(h_)\]; see Figure 1(b). In particular, any shortest path from _b_ to _v<sub>k</sub>(h_) that does not contain the edge _e<sup>t</sup>_ has to cross one of these paths. By uniqueness of shortest paths, this is a contradiction.

To see that _S<sub>b,h</sub>_ consists of _O_(1) intervals, it remains to observe that since \[_v<sub>i</sub>(h),v<sub>j</sub>(h_)\] might be a wrapped interval, we might have to split it into two regular intervals before adding it to data structure D_<sub>b,h</sub>_.

## Finding _S<sub>b,h</sub>_ Efficiently.

Finally, we have to show how to compute _S<sub>b,h</sub>_ efficiently, i.e. in \(\tilde{O}(1)\) time. Similar to Lemma 5.6, we only describe how to find _S<sub>b,h</sub>_ for _b_ on a hole \(h'\neq h\). We now describe two essential sub-procedures to find _S<sub>b,h</sub>_ efficiently:

First, we need to compute the vertex \(r_{v^t,h^\prime,h}\) used in Lemma 5.6 in time \(\tilde{O}(\sqrt{|P|})\) for each piece _P_ with \(h,h'\in h(P)\). We give the proof in Appendix B.1.

**Lemma 5.7.** _Given a piece P, distinct holes_ \(h,h'\in h(P)\) _and a vertex v in P. We can find the vertex_ \(r_{v,h,h^\prime}\) _in time_ \(\tilde{O}(\sqrt{|P|})\).

While \(\tilde{O}(\sqrt{|P|})\) seems excessive, we only need to do such a computation for each affected piece _P_ and every ordered pair of holes in _h(P_) once, so we can find all necessary vertices \(r_{v^t,h^\prime,h}\) necessary in total time \(\tilde{O}(\sqrt{|P|})\).

Secondly, we require the following tool.

**Lemma 5.8.** _Given any two vertices v<sub>i</sub>(h),v<sub>j</sub>(h_) _on h, such that_ \(v_i(h),v_j(h)\unknown\in S_{b,h}\)_, there is an algorithm that in_ \(\tilde{O}(1)\) _time detects whether the edge e<sup>t</sup> is contained in the region of the plane to the right of the directed cycle consisting of the shortest path_ \(\pi_{b,v_i(h)}\) _from b to v<sub>i</sub>(h), the path in h from v<sub>i</sub>(h_) _to v<sub>j</sub>(h_) _on h, and the reverse of the shortest path_ \(\pi_{b,v_j(h)}\) _from b to v<sub>j</sub>(h_) _(see Figure 1(b))._

Before we prove Lemma 5.8, let us show how we use these two sub-procedures to compute _S<sub>b,h</sub>_ efficiently. Here, we can employ a simple binary search strategy. Let \(r_{v^t,h^\prime,h}=v_k(h)\) in the cyclic ordering. Take two vertices \(v_i(h),v_j(h)\in Q(h)\) where _v<sub>i</sub>(h_) is the vertex preceding \(r_{v^t,h^\prime,h}\) in the cyclic ordering and \(v_j(h)=v_{i-\lfloor\frac{s_h-(k-i)}{2}\rfloor}(h)\). Recall that we can test membership of _v<sub>i</sub>(h),v<sub>j</sub>(h_) in _S<sub>b,h</sub>_ in constant time, then

• if both are in _S<sub>b,h</sub>_: we know that \([v_j(h),v_i(h)]\subseteq S_{b,h}\) and we continue the search in the interval _Q(h_)\\\[_v<sub>j</sub>(h),v<sub>i</sub>(h_)\] by setting new \(v_j(h)=v_{j-\lfloor\frac{s_h-(k-j)}{2}\rfloor}(h)\).<tbc>

• if neither of them are in _S<sub>b,h</sub>_: use Lemma 5.8 to decide whether _e<sup>t</sup>_ is in the region described in the Lemma. If so, we can conclude that \(S_{b,h}\subseteq(v_j(h),v_i(h))\) and thus repeat the same process on (_v<sub>j</sub>(h),v<sub>i</sub>(h_)) by setting new \(v_j(h)=v_{i-\lfloor\frac{i-j}{2}\rfloor}(h)\) and new _v<sub>i</sub>(h_)=_v_<sub>_i_-1</sub>(_h_); otherwise, we know that \(S_{b,h}\cap(v_i(h),v_j(h))=\emptyset\) and thus continue the search on _Q(h_)\\(_v<sub>j</sub>(h),v<sub>i</sub>(h_)). Here we set the new _v<sub>i</sub>(h_) to be the vertex following \(r_{v,h^\prime,h}\) in the cyclic ordering and \(v_j(h)=v_{j-\lfloor\frac{s_h-(k-j)}{2}\rfloor}(h)\).<tbc>

