rithms with improved performance guarantees or on refining the analysis of the algorithm presented in this paper.

## A Proof of the DCMCF complexity

### A.1 Proof of Lemma 2.1

_Proof._ The set of all possible paths from _s_ to _t_ is:

\(\{s\rightarrow u_i\rightarrow v_j\rightarrow t\}_{i\in I,j\in J}\cup\{s\rightarrow u_i\rightarrow v_j\rightarrow v_j^1\rightarrow\cdots\rightarrow v_j^N\rightarrow t\}_{i\in I,j\in J}\)<br>
\(\cup\{s\rightarrow v_j\rightarrow v_j^1\rightarrow\cdots\rightarrow v_j^N\rightarrow t\}_{j\in J}\cup\{s\rightarrow u_i\rightarrow t\}_{i\in I}\cup\{s\rightarrow v_j\rightarrow t\}_{j\in J}\cup\{s\rightarrow v_j^N\rightarrow t\}_{j\in J}.\)

We must prove that commodity _k_<sub>2</sub> cannot follow paths from the first three subsets of this union.

For \(i\in I\) and \(j\in J\), the minimum delay of path \(s\rightarrow u_i\rightarrow v_j\rightarrow t\) (obtained if the load of all arcs is zero) is:

\(d_{s\rightarrow u_i\rightarrow v_j\rightarrow t}=\frac{1}{mw_i+(m-1)W+2}+\frac{1}{w_i+2W}+\frac{1}{m+2}.\)

Using the assumption that \(w_i\le\frac{W}{m}\) and \(W=\frac{1}{4n^2}\), we can bound the delay<tbc>

(a) Performance Graph: solving time
45%
S
40%
T
35%
Big- M
Convex
30%
25%
20%
15%
10%
5%
0%
0
500
1000
1500
2000
2500
3000
3500
(b) Performance Graph: gap after 1h
100%
S
90%
T
Big- M
Convex
80%
70%
60%
50%
40%
100
101
102

Figure 7: Performance graphs for the exact resolution of the DCMCF problem on the randomly generated instances. Left: proportion of instances solved in less than a solving time (for instances solved in less than 1h); right: proportion of instances with a gap below a specified value after 1h.

