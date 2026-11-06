<tbc>Therefore the proof can be now boiled down to answer whether Algorithm 1 can possibly return to _c_ after applying any dropping strategy. This is summarized in the following lemma as the final step of proof.

**Lemma 5** _In the generalized mechanism, Algorithm 1 can never return to college c with strictly better_ \(\mu(c)\) _if it applied any dropping strategies._

_Proof_ Assuming that Algorithm 1 returns to _c_ with strictly better \(\mu(c)\) after finite steps of iterations. By retrieving the running process of Algorithm 1, we would be able to reconstruct a complete chain<sup>21</sup> of rejection and acceptance as follows (Denote _c=c_<sub>1</sub>=_cn_):

\(c_1-s_1-c_2-s_2-\cdots-c_{n-1}-s_{n-1}-cn\)

The above chain reflects the latest iteration before Algorithm 1 returns with _flag=true_. It starts from _c_<sub>1</sub> (i.e., _c_) rejecting _s_<sub>1</sub>, then _s_<sub>1</sub> applied to _c_<sub>2</sub> following its own preference _p_<sub>_s_<sub>1</sub></sub>; after comparing _s_<sub>1</sub> and _s_<sub>2</sub>, _c_<sub>2</sub> decided to accept _s_<sub>1</sub> and reject _s_<sub>2</sub>; then _s_<sub>2</sub> started its new application and so on. Finally, _s_<sub>_n_-1</sub> was rejected by _c_<sub>_n_-1</sub> and applied to _cn_ (i.e., _c_), which satisfies the stopping condition of Algorithm 1 with _flag=true_.

By inspecting the behavior of _c_<sub>2</sub>, we know that _s_<sub>2</sub> applied to it earlier than _s_<sub>1</sub> (which implies _s_<sub>2</sub> obtained higher bonus score than _s_<sub>1</sub> in _c_<sub>2</sub>) but is still less favored by _c_<sub>2</sub>. The only explanation for this phenomenon is that _s_<sub>1</sub> achieved strictly better exam score than _s_<sub>2</sub>, i.e., _f_<sub>_s_<sub>1</sub></sub>_\>f_<sub>_s_<sub>2</sub></sub>. This rule also applies to other colleges in this chain. In the end, since we suppose _c_ achieves better matching through the dropping strategy, _s_<sub>_n_-1</sub> is regarded better than _s_<sub>1</sub> for _c_, which implies that _f_<sub>_s_<sub>_n_-1</sub></sub>_\>f_<sub>_s_<sub>1</sub></sub>. In summary, we have:

\(f_{s_1}>f_{s_2}\)<br> \(f_{s_2}>f_{s_3}\)<br> \(\cdots\)<br> \(f_{s_{n-2}}>f_{s_{n-1}}\)<br> \(f_{s_{n-1}}>f_{s_1}\)

By adding the left side and right side of those inequations, we derive 0_\>_0, an apparent contradiction!

Thus our initial assumption cannot be true and colleges may not manipulate their preference successfully. \(\sqcap\sqcup\)

## References

<sup>21</sup> To be exact, it may be called a rejection "cycle" since the starting point of the chain coincides with its ending point.

