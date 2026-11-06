<tbc>max-sum recurrence:<tbc>

\(\text{OPT}(i)=\left\{\begin{array}{ c c }
0 & i=0 \\
max\{\text{OPT}(i-1),\text{OPT}(\text{pred}(i))+p_i\} & i>0.
\end{array}\right.\)

<tbc>where

\(\text{pred}(i):=\left\{\begin{array}{ c c }
0 & i=1 \\
max_{\{j<i,I_i\cap I_j=\emptyset\}}j & i>1.
\end{array}\right.\)

This recurrence always recurses on 1 subproblem. Thus the multipaths are regular paths and the problem is essentially the online longest-path problem from the source to the sink. The associated DAG has the subproblems/vertices _V_={0,1_,...,n_}, source _s=n_ and sink T={0}. Also at node _i_, the set \(M_i^{(\text{out})}\) consists of 2 edges going from the node _i_ to the nodes _i_-1 and pred(_i_). Figure 11 illustrates the DAG and paths associated with the scheduling for the example given in Figure 10.

Since the above recurrence relation correctly solves the offline optimization problem, every path in the DAG represents a scheduling, and every possible scheduling can be represented by a path of the DAG. We have |_M_|=|_E_|=_O(n_) multiedges/edges which are the components of our new representation. The gains of the edges going from the node _i_ to the nodes _i_-1 and pred(_i_) are 0 and _p<sub>i</sub>_, respectively. Note that the gain associated with each<tbc>

Interval Index
1
2
3
4
5
6

T
P4
P6
P2
P3
P5
P1
S
0
1
2
3
4
5
6
0
0
0
0
0
0
0
0
0

Figure 10: An example of weighted interval scheduling with _n_=6

Figure 11: The underlying DAG associated with the example illustrated in Figure 10. The scheduling with _I_<sub>1</sub>, _I_<sub>3</sub>, and _I_<sub>5</sub> is highlighted.

