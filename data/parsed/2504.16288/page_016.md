2. If \(b\neq a\), then

• set \(\mathsf{in}[q']\leftarrow\mathsf{in}[q']-1\);<tbc>

• if \(\mathsf{loops}[q',a]=1\) then set \(\mathsf{mark}[q']=i\) (meaning that this state needs to stay in _S<sub>i</sub>_, and will no longer be analysed in this update step);<tbc>

• if \(\mathsf{in}[q']=0\) and \(\mathsf{mark}[q']=i\) then insert \(q'\) into R;<tbc>

• if \(\mathsf{in}[q']=0\) and \(\mathsf{mark}[q']\neq i\) then push \(q'\) to _G_ (this state needs to still be removed from _S<sub>i</sub>_, at a later point during the processing of _w_\[_i_\]).

Once the set _S_<sub>|_w_|</sub> is computed, we provide a positive answer to the supersequence matching problem if and only if _S_<sub>|_w_|</sub> contains the final state \(q'_\mathsf{f}\).

In order to prove the correctness of the algorithm, it is sufficient to prove that we really compute the sets _S_<sub>0</sub>_,S_<sub>1</sub>_,...,S_<sub>|_w_|</sub> of the state-set simulation of \(A'\) on _w_.

Since we start with \(S_0=Q'\), this is clearly true for _S_<sub>0</sub> due to the property of Proposition 4.5. Moreover, the following invariant is satisfied: for every \(q\in S_0\), in\[_q_\] stores the number of transitions, other than self-loops, that have _q_ as target and some \(q'\in S_0\) as origin, and R stores exactly those states \(q\in S_0\) with in\[_q_\]=0.

Let us next assume that _S_<sub>_i_-1</sub> has been computed correctly for some \(i\in\{1,2,\dots,|w|\}\), and that the invariant is satisfied, i.e., for every \(q\in S_{i-1}\), in\[_q_\] stores the number of transitions, other than self-loops, that have _q_ as target and some \(q'\in S_{i-1}\) as origin, and R stores exactly those states \(q\in S_{i-1}\) with in\[_q_\]=0. We will now show that _S<sub>i</sub>_ is correctly computed in such a way that the invariant is also satisfied.

Let us call every state \(q\in S_{i-1}\) _good_ if there is some state \(p\in S_{i-1}\) with a _w_\[_i_\]-labelled path from _p_ to _q_ (which can also be a self-loop); and denote states from _S_<sub>_i_-1</sub> as _bad_ if they are not good. This means that _S<sub>i</sub>_ is exactly the set of good states from _S_<sub>_i_-1</sub>. Observe that if a state _q_ is good then all states that can be reached from _q_ are also good. We will show that our algorithm constructs _S<sub>i</sub>_ by deleting exactly the bad states from _S_<sub>_i_-1</sub>.

Assume |_S_<sub>_i_-1</sub>|=_h_ and let us consider an arbitrary topological sorting _q_<sub>1</sub>_\<...\<q<sub>h</sub>_ of the states in _S_<sub>_i_-1</sub>, w.r.t. the transitions between states of _S_<sub>_i_-1</sub> which are not self-loops. We will show, by induction on _j_, with \(1\le j\le h\), that the states removed by our algorithm from _q_<sub>1</sub>_\<...\<q<sub>j</sub>_ are exactly the bad states of {_q_<sub>1</sub>_,...,q<sub>j</sub>_}. For _j_=1, this clearly holds. Indeed, _q_<sub>1</sub> must be a root of _S_<sub>_i_-1</sub>, as it comes first in the topological sorting. It is removed if and only if it has no self-loop labelled with _w_\[_i_\]; but this is equivalent to _q_<sub>1</sub> being a bad state. Assume now that our claim holds for _j_-1, and let us show that it holds for _j_. We want to show that _q<sub>j</sub>_ is removed if and only if _q<sub>j</sub>_ is bad. Assume first that _q<sub>j</sub>_ is removed by our algorithm. If _q<sub>j</sub>_ is a root of _S_<sub>_i_-1</sub>, the same argument as for _q_<sub>1</sub> holds. Assume _q<sub>j</sub>_ is not a root. This means that all its parents were also removed by our algorithm (as a state _q_ is removed only if in\[_q_\]=0). But all the parents of _q<sub>j</sub>_ must come before _q<sub>j</sub>_ in any topological sorting of _S_<sub>_i_-1</sub>. They were removed, so they are bad states, by the induction hypothesis. Moreover, when the parents of _q<sub>j</sub>_ were removed, no _w_\[_i_\]-transition targeting _q<sub>j</sub>_ and no _w_\[_i_\]-self-loop of _q<sub>j</sub>_ were discovered. Thus, _q<sub>j</sub>_ is also bad. For the converse, assume _q<sub>j</sub>_ is a bad state. This means that all its parents (if any) are also bad. But, as before, all the parents of _q<sub>j</sub>_ (if any) must come before _q<sub>j</sub>_ in any topological sorting of _S_<sub>_i_-1</sub>. By the induction hypothesis, as they are bad, they are also removed by our algorithm. During their removal, we explore all transitions connecting them to _q<sub>j</sub>_, and this allows us to check whether there are any _w_\[_i_\]-transitions targeting _q<sub>j</sub>_ or any _w_\[_i_\]-self-loops of _q<sub>j</sub>_. The existence of such a transition would be a contradiction to the fact that _q<sub>j</sub>_ is bad. Thus, we never set \(\mathsf{mark}[q_j]\leftarrow i\), but we decrement in\[_q<sub>j</sub>_\] until it becomes 0. When this happens, _q<sub>j</sub>_ is inserted in _G_, so it will be removed. This concludes the proof of our claim. Hence, we compute _S<sub>i</sub>_ correctly.

With respect to the invariant, we observe that the values in\[_q_\] are correctly updated whenever we remove a transition, and whenever a state becomes a root, but is not removed (i.e., it will be a root in _S<sub>i</sub>_), then this state is explicitly added to R.

This concludes the proof of correctness.

As far as the complexity is concerned, the number of steps of the algorithm is proportional to the sum of |_w_|, the number of removed edges (which is \(O(m')\)), and the total time spent with the<tbc>

