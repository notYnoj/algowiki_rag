Now run the algorithm A on _A_. Whenever it makes an I/O, do as follows: If this is the first time the block is being accessed and it is not part of the input or output (a write operation to an untouched block), create a new live block node in _G_ and add a directed edge from the current live memory node to the new block node (see Figure 1e). Label the new node by the next unused integer label. Otherwise, let _v_ be the live node in _G_ corresponding to the last time the disk block was accessed. We add a directed edge from _v_ to the live memory node, mark _v_ as dead, create a new live block node \(v'\) and add a directed edge from the live memory node to \(v'\). We give the new node the same label as _v_ (Figure 1b and Figure 1c). Finally, once for every _m/b_ I/Os, we mark the memory node as dead, create a new live memory node and add an directed edge from the old memory node to the new live memory node (Figure 1d).

To better understand the definition of _G_, observe that all the nodes with the same label represent the different versions of a disk block that existed throughout the execution of the algorithm. Moreover, there is always exactly one live node with any fixed label, representing the current version of the disk block. Also observe that at the end of the execution, there must be a live disk block node in _G_ representing each of the output blocks in _C_, and these have the same labels as the original nodes representing the empty disk blocks of _C_ before the execution of A.

## Fixing the Randomness of A.

Consider the execution of A on an input _A_ representing a uniform random permutation \(\pi\) as well as independent and uniform random bit strings \(d_1,\dots,d_n\in\{0,1\}^w\). Since A makes an expected _t_ I/Os, it follows by Markov’s inequality that A makes more than 6_t_ I/Os with probability less than 1/6. If we simply abort in such cases, we obtain an algorithm with worst case _O(t_) I/Os and error probability at most 1/3+1/6=1/2. Now fix the random choices of A to obtain a deterministic algorithm A<sup>∗</sup> with error probability 1/2 over the random choice of \(\pi\) and _d_<sub>1</sub>_,...,d<sub>n</sub>_. A<sup>∗</sup> makes _t_<sup>∗</sup>=6_t_ I/Os in the worst case. Observe that for A<sup>∗</sup>, we get a fixed I/O graph _G(A_) for every input array _A_ since A<sup>∗</sup> is deterministic.

## Finding a Popular I/O-Graph.

We now find an I/O-graph _G_ which is the result of running A<sup>∗</sup> on a large number of different inputs. For notational convenience, let _t_ denote the worst case number of I/Os made by A<sup>∗</sup> (instead of using _t_<sup>∗</sup> or 6_t_). Observe that the total number of different I/O-graphs one can obtain as the result of running A<sup>∗</sup> is small:

**Lemma 8** _There are no more than_

\((t+n(w+lgn)/b+nw/b+1)^{t+1}\)

_I/O graphs that may result from the execution of_ A<sup>∗</sup>.

## Proof.

There are at most _t_+1 choices for the number of I/Os performed by A<sup>∗</sup> on an input (0 through _t_). Moreover, for each I/O performed, either one of at most _t+n(w_+lg_n)/b+nw/b_ live disk blocks is read, or a new untouched disk block is created, resulting in at most _t+n(w_+lg_n)/b+nw/b_+1 different possible changes to _G_ for each I/O. Thus the total number of possible I/O-graphs is at most \((t+1)(t+n(w+lgn)/b+nw/b+1)^t\le(t+n(w+lgn)/b+nw/b+1)^{t+1}\).

This means that we can find an I/O-graph, which correspond to the execution of A<sup>∗</sup> on many different inputs, and moreover, we can even assume that A<sup>∗</sup> is correct on many such inputs:

**Lemma 9** _There exists a set_ \(\Gamma\) _containing at least_ (_n!_2<sup>_nw_</sup>)/(2(_t+n(w_+lg_n)/b+nw/b_+1)<sup>_t_+1</sup>) _different input arrays A, such that_ A<sup>∗</sup> _is correct on all inputs_ \(A\in\Gamma\) _and the I/O-graph is the same for all_ \(A\in\Gamma\).

