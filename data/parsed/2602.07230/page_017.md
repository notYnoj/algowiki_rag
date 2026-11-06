<tbc>every arc entering a sink carries flow 1_/q_. Thus, each sink receives a total flow of 1, and each shared arc _a<sub>i</sub>_ with \(i\in\{1,\dots,k\}\) carries a total flow of \(q\cdot 1/q=1\).

Consider any unsplittable _b_-transshipments of our instance. Flow from source _s<sup>j</sup>_ can only be routed to sink _t<sup>j</sup>_, and unsplittability requires to route its entire flow value along one arc. This yields a violation of 1-(_k_+1)_/q_, which converges to _d_<sub>max</sub>=1 as \(q\rightarrow\infty\). Thus, even when each sink is connected to arbitrarily many sources, no unsplittable transshipment can avoid a violation of _d_<sub>max</sub>, establishing the tightness of the bound.

## Appendix D Proof of Theorem 7

To prove Theorem 7, we need to specify Step 9 of Algorithm 1 in more detail. Consider the situation where the algorithm finds a singular digraph rooted at the junction vertex _w_, and _w_ has been reached on a forward path along its incoming arc \(a'\). Moreover, let _t_ be a (sub-)sink located at _w_ with \(d_t>y_{a^\prime}\).

By Lemma 1, the singular digraph with the super-source _s_<sup>∗</sup> removed forms an in-tree rooted at _w_. The flow _y_ on this in-tree satisfies the demands of all (sub-)sinks located at its vertices, with the sole exception of the sink _t_, for which only a demand of \(d_t-y_{a^\prime}\) is satisfied within the in-tree, while the remaining demand \(y_{a^\prime}\) is supplied via arc \(a'\).

We proceed iteratively as follows. Starting from a leaf \(s\in S^+\) of the in-tree, we follow its outgoing arc _a_ and continue along the unique path toward the root _w_ until a (sub-)sink \(t'\) is encountered. If \(t'\) is located at the root _w_, we select \(t'=t\) only if no other (sub-)sink is located at _w_. If \(d_{t^\prime}\le y_a\), the entire demand \(d_{t^\prime}\) can be routed along this path. In this case, we move \(t'\) backward along the path to _s_ and further to the super-sink _s_<sup>∗</sup>, reducing the flow on all arcs of the path by \(d_{t^\prime}\). Otherwise, if \(d_{t^\prime}>y_a\), we split \(t'\) into two sub-sinks \(t'_1\) and \(t'_2\) with demands \(d_{t_1^\prime}:=d_{t^\prime}-y_a\) and \(d_{t_2^\prime}:=y_a\), respectively. The sub-sink \(t'_2\) is then moved backward to _s_ and further to the super-sink _s_<sup>∗</sup>, and the flow on all arcs of the path is reduced by _y<sub>a</sub>_. As a consequence, the arc _a_ is deleted and _s_ has no remaining outgoing arcs. We thus delete _s_ from the in-tree.

This process is repeated until all flow on the singular digraph has been eliminated and only the sub-sink _t_<sub>1</sub> remains at the root _w_, after which it is moved backward along the arc \(a'\).

1/q
1 - k/q
S1
t1
1
1/q
1/q
Sq+1
1 - k/q
S2
t2
1
1/q
a1
1
1/q
1/q
1/q
1/q
1 - k/q
Sq-1
1/q
1/q
Sq+k
1
1
ak
1
1/q
1/q
1 - k/q
Sq
t9
1

Figure 4: An instance to show _d_<sub>max</sub> is a tight lower bound for the required capacity violation.

