<tbc>The scheduler reads the input and broadcasts it to all workers. Then each worker requests a sub problem from the scheduler, solves it and repeats. The scheduler loops until all jobs have been requested and all workers have been notified that no more jobs are available. At the end, all processors send their motifs to the scheduler which outputs them. The process is illustrated in figure 2.

### 2.4 Pruning conditions

In this section we present pruning conditions applied for filtering _l_-mers in the sample driven part and for pruning enumeration trees in the pattern driven part.

Two _l_-mers _a_ and _b_ have a common neighbor _M_ such that \(Hd(a,M)\le d_a\) and \(Hd(b,M)\le d_b\) if and only if \(Hd(a,b)\le d_a+d_b\). For 3 _l_-mers, no trivial necessary and sufficient conditions have been known up to now. In \[6\] sufficient conditions for 3 _l_-mers are obtained from a preprocessed table. However, as _l_ increases the memory requirement of the table becomes a bottleneck. We will give simple necessary and sufficient conditions for 3 _l_-mers to have a common neighbor. These conditions are also necessary for more than 3 _l_-mers.

Let _T_ be a set of _l_-mers and _M_ be an _l_-mer. If \(\sum_{u\in T}Hd(M,u)>|T|d\) then, by the pigeonhole principle, one _l_-mer must have a distance from _M_ greater than _d_. Therefore, _M_ cannot be a common neighbor of the _l_-mers in _T_. If we have a lower bound on \(\sum_{u\in T}Hd(M,u)\) for any _M_, then we can use it as a pruning condition. If the lower bound is greater than |_T|d_ then there is no common neighbor for _T_. One such lower bound is the _consensus total distance_.

**Definition 1.** _Let T be a set of l-mers, where k_=|_T|. For every i, the set T_<sub>1</sub>\[_i_\]_,T_<sub>2</sub>\[_i_\]_,...,T<sub>k</sub>_\[_i_\] _is called the i-th column of T. Let m<sub>i</sub> be the maximum frequency of any character in column i. Then_ \(Cd(T)=\sum_{i=1..l}k-m_i\) _is called the consensus total distance of T._

