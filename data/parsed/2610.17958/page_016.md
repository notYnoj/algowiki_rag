## A Materials omitted from Section 3.

### A.1 The \(f_{\chi^2}\) support measure.

While the function _f<sub>E</sub>_ lends itself well to our theoretical analysis, it is not ideal for the biological domain. In particular, in a PPI network, maximizing the _f<sub>E</sub>_ function finds a motif pair {_X,Y_} that potentially explains many interactions (i.e., there are many edges where _X_ appears on one side and _Y_ on the other). To make it more likely we find an actual interaction, we also want the property that there are few _non_-edges where _X_ appears on one side and _Y_ on the other. In other words, we want the presence of _X_ and _Y_ to make an interaction likely. This is not captured by _f<sub>E</sub>_. In graph-theoretic terms, we want to ensure that the subgraph selected by {_X,Y_} is _dense_. Here, this means denser than the average over the whole interaction network. This is exactly what the \(f_{\chi^2}\) support function is designed to capture. Boyen et al. "experimentally establish the superiority of the Chi-square-based support measure over other support measures" \[1\].

Fortunately, the hard part in computing \(f_{\chi^2}\) turns out to be computing _f<sub>E</sub>_. In the following corollary, we show that the additional information needed to derive \(f_{\chi^2}(G,\{X,Y\})\) from _f<sub>E</sub>(G,{X,Y_})=|_E<sub>X,Y</sub>_| is easy to compute, lifting Algorithm 3.1 to support \(f_{\chi^2}\).

Corollary A.1 (to Theorem 3.1). _There is an algorithm for CMM with_ \(f_{\chi^2}\) _running in time_ O(_N_<sup>2</sup>)_, where_ \(N=\sum_{v\in V}|v|\)_. The space used is_ O(_N)._

_Proof._ We sketch how to adapt Algorithm 3.1. Given a graph _G_=(_V,E_), where \(V\subseteq\Sigma^*\), and a positive integer \(\ell\), our goal is to find a pair {_X,Y_} of motifs maximizing \(f_{\chi^2}(G,\{X,Y\})\). Computing this quantity reduces to computing the following parameters: the number _k<sub>X</sub>_ (resp. _k<sub>Y</sub>_) of nodes in which _X_ (resp. _Y_ ) occurs, the number _k<sub>X,Y</sub>_ of nodes in which both _X_ and _Y_ occur, and the number |_E<sub>X,Y</sub>_| of edges in which _X_ occurs in an endpoint and _Y_ occurs in the other.

The number |_E<sub>X,Y</sub>_| of edges can be easily obtained in O(_N_<sup>2</sup>) time using Theorem 3.1. For _k<sub>X</sub>_ (resp. _k<sub>Y</sub>_), iterate over the nodes and, for each distinct length-\(\ell\) substring _X_ of the current node, increment a counter indexed by rank(_X_). By handling duplicates locally at each node, this counting can be done in O(_N_) time. This is a simplification of Algorithm 3.1. Finally, for _k<sub>X,Y</sub>_, construct a graph \(G'\) from _G_ as follows. Let \(V(G')=V\) and \(E(G')=\{\{v,v\}|v\in V\}\). Applying Algorithm 3.1 to \(G'\) yields the desired number _k<sub>X,Y</sub>_ for every pair of length-\(\ell\) substrings {_X,Y_}. (Algorithm 3.1 and its analysis apply to graphs with self-loops). \(\sqcap\sqcup\)

### A.2 Why we cannot do better.

In this section, we use tools from fine-grained complexity to establish<tbc>

<tbc>conditional hardness. SETH \[9\] is a standard assumption about the complexity of deciding the satisfiability of conjunctive normal form formulas. We show that a polynomially faster algorithm for CMM (in _N_) yields a faster algorithm for the following problem, which in turn is known to refute SETH \[2, 27\].

Recall that \(\langle\cdot,\cdot\rangle\) denotes the inner product. The hardness conjecture for the MaxIP problem states that for every constant \(\varepsilon>0\), there exists a constant \(c(\varepsilon)>0\) such that MaxIP with dimension \(m=c(\varepsilon)\mathrm{log}n\) cannot be solved in time \(\mathcal{O}(n^{2-\varepsilon})\). Refuting this conjecture refutes SETH. With these tools, we are ready to prove our conditional hardness result.

Theorem A.2. _There is no algorithm solving CMM with f<sub>E</sub> in time_ \(\mathcal{O}(N^{2-\varepsilon}\mathrm{poly}(|E|,|V|))\)_, for any_ \(\varepsilon>0\)_, unless SETH fails._

_Proof._ We reduce the decision version of MaxIP to the decision version of CMM; since the decision version is no harder than CMM itself, the lower bound carries over. Let _A_={_a_<sub>1</sub>_,...,a<sub>n</sub>_} and _B_={_b_<sub>1</sub>_,...,b<sub>n</sub>_} be sets of _m_-dimensional binary vectors, where _m_ and _n_ are positive integers. Let \(\mathtt{enc}:\mathbb{Z}_{\ge 1}\rightarrow\{0,1\}^+\) denote the usual binary encoding of any positive integer and _a_\[_k_\] (resp. _b_\[_k_\]) the _k_-th coordinate of vector _a_ (resp. _b_). Our goal is to determine whether there are vectors \(a\in A\) and \(b\in B\) such that \(\sum_{i=1}^ma[i]b[i]\ge p\), where _p_ is a non-negative integer.

We construct an instance \(\langle G=(V,E),\ell\rangle\) of CMM with \(V=U\cup W\) as follows. Let _U_={_u_<sub>1</sub>_,...,u<sub>m</sub>_} and _W_={_w_<sub>1</sub>_,...,w<sub>m</sub>_} be sets of strings over the alphabet \(\Sigma=\{0,1\}\cup\{\#_j|1\le j\le m\}\), and \(E=\{\{u_j,w_j\}|1\le j\le m\}\). If some _u<sub>j</sub>_ or _w<sub>j</sub>_ is the empty string, we omit that node together with the<tbc>

u1
001#1 011#1
101#1
W1
u2
010#2 011#2
101#2 111#2
W2
u3
001#3 010#3
110#3 111#3
W3

Maximum Inner Product (MaxIP)
Input: Two sets A, B \(\subseteq\{0,1\}^m\) of n vectors each.
Output: The value maxa A, b B a, b

Figure A.1: The construction in the proof of Theorem A.2 for _n=m_=3, _a_<sub>1</sub>=(1,0,1), _a_<sub>2</sub>=(0,1,1), _a_<sub>3</sub>=(1,1,0), _b_<sub>1</sub>=(1,1,0), _b_<sub>2</sub>=(0,0,1), and _b_<sub>3</sub>=(0,1,1). Here, \(\ell=3\), and `enc`(1)=`01`, `enc`(2)=`10`, `enc`(3)=`11`. The motif pair {`011`,`101`}, which encodes _a_<sub>3</sub> and _b_<sub>1</sub>, occurs in the endpoints of the two highlighted edges, so \(f_E(G,\{\mathtt{011},\mathtt{101}\})=2=\langle a_3,b_1\rangle\).

