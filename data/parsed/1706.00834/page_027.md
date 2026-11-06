<tbc>which is the difference between the total gain of the algorithm and the total gain of the single best cutting chosen in hindsight. See Figure 8 as an example.

## The Dynamic Programming Representation.

Finding the optimal cutting can be solved via dynamic programming (Cormen et al., 2009). Each subproblem is simply denoted by _i_ for \(0\le i\le n\), indicating the rod cutting problem given a rod of length _i_. The base subproblem is _i_=0, and the complete subproblem is _i=n_. The dynamic programming for the rod cutting problem uses the following max-sum recurrence:

\(\text{OPT}(i)=\left\{\begin{array}{ c c }
0 & i=0 \\
max_{0\le j\le i}\{OPT(j)+p_{i-j}\} & i>0.
\end{array}\right.\)

This recurrence always recurses on 1 subproblem. Thus the multipaths are regular paths and the problem is essentially the online longest-path problem from the source to the sink. The associated DAG has the subproblems/vertices _V_={0,1_,...,n_}, source _s=n_ and sink T={0}. Also at node _i_, the set \(M_i^{(\text{out})}\) consists of _i_ edges going from the node _i_ to the nodes 0,1_,...,i_-1. Figure 9 illustrates the DAG and paths associated with the cuttings.

Since the above recurrence relation correctly solves the offline optimization problem, every path in the DAG represents a cutting, and every possible cutting can be represented<tbc>

.9
.7
.1
.4
.4
(a)
(b)
(c)
.1
.7
.1
.1
.4
.1
.4
.1
(d)
(e)
(f)
.4
.1
.1
.1
.1
.1
(g)
(h)

P4
T
P3
P3
P2
P2
P2
S
0
1
2
3
4
P1
P1
P1
P1
P1

Figure 8: All cuttings of a rod of length _n_=4 and their profits given (_p_<sub>1</sub>_,p_<sub>2</sub>_,p_<sub>3</sub>_,p_<sub>4</sub>)=(.1,.4,.7,.9).

Figure 9: An example of rod cutting problem with _n_=4. The cutting with two smaller pieces of size 2 is highlighted.

