The first three data structures can be computed simultaneously by considering every transition of \(A'\) at most once; the last two data structures can be computed by considering each state at most once. Thus, all these data structures can be computed in time \(O(m')\).

By Lemma 4.6, we can construct in time _O_(|roots|) a data structure R, storing initially the set of states in roots, and supporting the following operations:

• Push: Insert a state _q_ in R.<tbc>

• Pop: Given \(a\in\Sigma\), retrieve all states \(q\in\mathcal{R}\) such that \(a\notin\mathcal{L}_q\) and remove them from R (or indicate that no such state exists).

The initialisation of R is done by repeatedly pushing the states of roots in it. Further, the time needed by R to process a sequence of \(\ell\) push and pop operations where each state of \(A'\) is pushed at most once in total is \(O(\ell+m)\); this includes the initial push of the states in roots.

Our algorithm is an efficient implementation of the state-set simulation for the automaton \(A'\) on _w_ (see Section 3). That is, for every _i_=0,1,2_,...,|w_|, we compute a state-set _S<sub>i</sub>_ of all states of \(A'\) reachable from _q_<sub>0</sub> by a path labelled with _w_\[1:_i_\]. Moreover, since \(A'=\text{cond}(A_\text{sup})\) and Proposition 4.5 holds, we will have \(Q'=S_0\supseteq S_1\supseteq\dots\supseteq S_{|w|}\).

We implement all the sets _S<sub>i</sub>_ with a single Boolean characteristic array, which allows us to obtain _S<sub>i</sub>_ from _S_<sub>_i_-1</sub> by changing |_S_<sub>_i_-1</sub>\\_S<sub>i</sub>_| many entries from 1 to 0 (due to the fact that \(S_{i-1}\supseteq S_i\)).

We start with \(S_0=Q'\). Recall that the data structure R contains the set of states roots.

Let us first give an intuitive explanation of how _S<sub>i</sub>_ is computed from _S_<sub>_i_-1</sub>. Let _a=w_\[_i_\]. Since \(S_{i-1}\supseteq S_i\), we only have to identify those states that must be deleted from _S_<sub>_i_-1</sub> in order to obtain _S<sub>i</sub>_, which are exactly the states that cannot be reached by an _a_-labelled path from any other state of _S_<sub>_i_-1</sub>. Since \(A'\) has a DAG structure, this can be done as follows.

Every root without a self-loop with _a_ has to be deleted, and every root with a self-loop with _a_ will be in _S<sub>i</sub>_. In particular, we can ignore the outgoing transitions of those roots that will be in _S<sub>i</sub>_ in the rest of the update step, since they necessarily point to states that will also be in _S<sub>i</sub>_. This means that we have to be able to initially get those roots that have no self-loop with _a_, for which we employ the data structure R. Now if we remove some root _q_, then each of its outgoing transitions \((q,x,q')\) with \(x\in\Sigma\cup\{\varepsilon\}\) has to be removed, but we also have to process each such transition as follows. If _x=a_, then \(q'\) will necessarily be in _S<sub>i</sub>_ and we do not have to consider \(q'\) again in this update step (we also mark \(q'\) accordingly). If, on the other hand, \(x\neq a\), then we first check if \(q'\) has a self-loop with _a_, which is also sufficient for \(q'\) being in _S<sub>i</sub>_ (again, we mark it accordingly and do not have to consider it again). If \(q'\) has no self-loop with _a_ and at least one other incoming transition, then we do not know whether it is in _S<sub>i</sub>_ or not, since this might be determined by some other incoming transition from a root. If \(q'\) has no self-loop with _a_, but becomes a root when we delete \((q,x,q')\), then it has to be treated as one of the initial roots (i.e., it will be deleted at some point and its outgoing transitions have to be deleted and processed as described above). In particular, this means that when we delete states and transitions, we have to update the in-degrees of states to be able to identify those states that become roots. Let us now formally define this algorithm.

We initially set \(S_i\leftarrow S_{i-1}\). Then we extract from R all states _q_ such that \(a\notin\mathcal{L}_q\) (i.e, _q_ has no self-loop with _a_) and store them in a queue _G_. While _G_ is not empty, we pop state _q_ from the queue _G_ and remove it from \(A'\) and _S<sub>i</sub>_. Then we remove from \(A'\) each transition \((q,b,q')\) with \(b\in\Sigma\cup\{\varepsilon\}\) in _L_\[_q_\] and proceed as follows:

1. If _b=a_, then<tbc>

• set \(\text{in}[q']\leftarrow\text{in}[q']-1\);<tbc>

• set \(\text{mark}[q']=i\) (this state needs to stay in _S<sub>i</sub>_, and will no longer be analysed in this update step);<tbc>

• if \(\text{in}[q']=0\) then insert \(q'\) into R (i.e., it is now a root of \(A'\) and has to be treated like one in the next update step).<tbc>

