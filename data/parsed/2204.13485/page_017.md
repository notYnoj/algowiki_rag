The forced edge case 1-forced-sm-strat can be proved in a similar way, the only difference being that _u_ is dismissed from the construction and we set \(\mu\) to contain the single forced edge \(u'w\).

**Remark 21.** Kobayashi et al. \[20\] showed hardness of the problem whether there exist preferences for the women such that the man-optimal stable matching contains a given matching _M_. Our results imply that if the graph is not complete, then the problem remains hard even if the matching consists of a single edge. To see this, observe that in our construction this problem also reduces to deciding whether there are preferences for women such that the man-optimal stable matching matches a given set of women. Indeed, the additional man \(u'\) proposes to all of them before proposing to his forced pair _w_, so they all have to reject him, which is only possible if each of them get a partner that can be set to be the best on the preference list of the given woman. Since each stable matching covers the same set of agents, this is equivalent to deciding whether there is a stable matching that matches all the original women.

In the proof of Theorem 20, the reduction was based on a non-complete bipartite graph, e.g., it contained a pendant edge _uw_. We show that the problems remain NP-complete even in complete bipartite graphs. However, in this case the preference lists of some women might be fixed.

**Theorem 22.** 1-forced-sm-strat _and_ 1-forbidden-sm-strat _are NP-complete even if the graph is a complete bipartite graph._

_Proof._ We start with the proof for 1-forbidden-sm-strat; the problem is clearly in NP. To show NP-hardness, we reduce from com-smti, see the definition in Section 2.

Consider an instance _I_=(_G_=(_A,B;E),\>_) of com-smti, where _A_={_a_<sub>1</sub>_,...,a<sub>n</sub>_}, _B_={_b_<sub>1</sub>_,...,b<sub>n</sub>_}, and ties are restricted to a subset \(b_1,\dots,b_\ell\), each of which have two neighbors. We construct a 1-forbidden-sm-strat instance \(I'\) as follows. We extend the original bipartite graph by adding two men _u_ and \(u'\) to _A_ and two women _w_ and \(w'\) to _B_. That is, \(U=A\cup\{u,u'\}\) and \(W=B\cup\{w,w'\}\). Finally, _H_ is a complete graph, that is, \(F=\{xy|x\in U,y\in W\}\), see Figure 4 for an example.

Let \(W_1=\{b_i|i\in[\ell]\}\) and \(W_2=\{b_i|\ell<i\le n\}\). The fixed preferences are the following. Each _a<sub>i</sub>_ has the same preferences as in _I_ as the top of its preference list, followed by _w_, and then by the remaining women in any order. Each \(b_i\in W_2\) has the same preferences as in _I_ as the top of her preference list, followed by the remaining men in any order. The other fixed preference lists are the following:

• _w_: _u_ is the least preferred, otherwise arbitrary,<tbc>

• \(w'\): _u_, followed by \(u'\), then the rest in arbitrary order,<tbc>

• _u_: _w_, followed by \(w'\), then the rest in arbitrary order,<tbc>

• \(u'\): \(w'\), then the rest in arbitrary order.

Finally, let \(\tau\) consists of the single forbidden edge \(uw'\).

We claim that there is a perfect weakly stable matching _M_ in _G_ if and only if the preferences of the remaining women in _H_ can be set in a way such that there is a stable matching \(M'\) avoiding \(uw'\). First suppose there is a perfect weakly stable matching _M_ in _I_. Let \(M'\) be the matching obtained from _M_ by adding _wu_ and \(w'u'\). We set the preferences of the women in _W_<sub>1</sub> such that the best man for them is their partner in _M_. We claim that \(M'\) is stable. Suppose indirectly that there is a blocking edge _xy_. Then _y_ cannot be _w_ since each man _a<sub>i</sub>_ is with an original (and hence better) partner, and _u_ is with a better partner, too. Furthermore, _y_ cannot be \(w'\) either, since her only better partner _u_ is with his best choice. Similarly, _y_ cannot be from _W_<sub>2</sub>, since<tbc>

