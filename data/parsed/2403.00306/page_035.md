inputs. Algorithm qPMSPrune uses the d-neighborhood concept to build the tree structure. The key points of the algorithm is described as follows.

**Key Steps of qPMSPruneI**

Most of the motif search algorithms combine a sample driven approach with a pattern driven approach. Here in the sample driven part the _d_-neighborhood (B(_x_<sub>0</sub>_,d_)) of a given input string _x_<sub>0</sub> is generated as a tree. Every _l_-mer in the neighborhood is a candidate motif.

The qPMSPrune algorithm is based on the following observation.

**Observation 3.1** _Let M be any (l, d, q)-motif of the input strings s_<sub>1</sub>_,...,s<sub>n</sub>. Then there exists an i (with_ \(1\le i\le n-q+1\)_) and a l-mer_ \(x\epsilon s_i^l\) _such that M is in_ \(\mathcal{B}(\unknown,\unknown)\) _and M is a (l, d, q_-1)_-motif of the input strings excluding si._

Based on the above observation, for any _l_-mer _x_, it represents B(_x,d_) as a tree _T<sub>d</sub>(x_). It generates the _d_-neighborhood of every _l_-mer _x_ in _s_<sub>1</sub> by generating the tree _T<sub>d</sub>(x_). The height of _T<sub>d</sub>(x_) is _d_. The root of this tree will have _x_. If a node _t_ is parent of a node \(t'\) then the hamming distance between the strings is \(dH(t,t')=1\). As a result, if a node is at level _h_, then its hamming distance from the root is _h_.

For example, the tree _T_<sub>2</sub>(1010) with alphabet \(\Sigma=\{0,1\}\) is illustrated in Figure fig. 3.1.

The trees are generated and explored in depth first manner. In pattern driven part, each node is checked whether it is a valid motif or not. While traversing a node _t_ in the tree _T<sub>d</sub>(x_) in a depth- first manner, the hamming distance between the input strings are calculated incrementally. If \(q'\) is the number of input strings _s<sub>j</sub>_ such that \(dH(t,s_j)\le d\). If \(q'\ge q-1\), output _t_ as a motif.

1010
0010
1110
1000
1011
0110
0000
0011
1100
1111
1001

Figure 3.1: \(T_2(1010)\) with alphabet \(\Sigma=\{0,1\}\)

