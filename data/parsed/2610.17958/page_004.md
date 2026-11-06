\(|V_X\cap V_Y|=k_{X,Y}\). It is called _complete_ if every node of _V<sub>X</sub>_ is adjacent to every node of _V<sub>Y</sub>_. A complete bipartite graph is called a _biclique_.

**2.4 Support measures.** A _support measure f_ on _G_ is a function that maps an \((\ell,d)\)-motif pair {_X,Y_} to a nonnegative real number _f(G,{X,Y_}). Different types of support functions have been considered in the literature \[1,15,25\]. We restrict our attention to _f<sub>E</sub>_ and \(f_{\chi^2}\), which we define below. The former is simple and illustrative and will serve to make our theoretical analysis lucid. The second works well in practice \[1\] and we use it in our experimental evaluation (we also show that our theoretical results extend to it).

**2.5 The** \(f_{\chi^2}\) **support measure.** The \(\chi^2\)-based support measure of a graph _G_ with respect to an \((\ell,d)\)- motif pair {_X,Y_}, denoted by \(f_{\chi^2}\), is defined as<tbc>

\(f_{\chi^2}(G,\{X,Y\}):=\left\{\begin{array}{ c c }
\frac{(|E_{X,Y}|-\overline{E_{X,Y}})^2}{\overline{E_{X,Y}}} & \text{if}|E_{X,Y}|>\overline{E_{X,Y}}, \\
0 & \text{otherwise},
\end{array}\right.\)

<tbc>where <o>_E<sub>X,Y</sub>_</o> is the expected number of edges between _V<sub>X</sub>_ and _V<sub>Y</sub>_ under a uniform random-graph model. Concretely,<tbc>

\(\overline{E_{X,Y}}:=\text{ed}(G)\cdot E_{k_X,k_Y,k_{X,Y}}^\mathrm{max},\)

<tbc>where \(\text{ed}(G):=|E|/\genfrac(){pt}{2}{|V|}{2}\) is the _edge density_ of _G_, and

\(E_{k_X,k_Y,k_{X,Y}}^\mathrm{max}:=k_Xk_Y-\genfrac(){pt}{2}{k_{X,Y}}{2}-k_{X,Y}\)

is the maximum possible number of edges in the subgraph selected by any (_k<sub>X</sub>,k<sub>Y</sub>,k<sub>X,Y</sub>_)-motif pair. The parameters _k<sub>X</sub>_, _k<sub>Y</sub>_, and _k<sub>X,Y</sub>_ are as defined above; |_V_| and |_E_| are trivially obtained from the input. Intuitively, this measure captures how much above the average density a subgraph selected by a motif pair is, taking into account its size.

**3 An exact algorithm for CMM.** To simplify our presentation, we focus on the _f<sub>E</sub>_ support measure for now, but the same algorithmic ideas also apply to the \(f_{\chi^2}\) support measure. Recall that _f<sub>E</sub>(G,{X,Y_}) counts the edges \(\{u,v\}\in E\) such that _X_ matches a substring of _u_ and _Y_ matches a substring of _v_, or vice versa.

Theorem 3.1. _There is an algorithm for CMM with f<sub>E</sub> running in time_ O(_N_<sup>2</sup>)_, where_ \(N:=\sum_{v\in V}|v|\)_. The space used is_ O(_N)._

_Proof._ The algorithm (see Algorithm 3.1) iterates over all motif pairs {_X,Y_}, such that _X_ and _Y_ are substrings of at least one of the labels, and then counts the corresponding number of edges. That is, it computes<tbc>

<tbc>the value _f<sub>E</sub>(G,{X,Y_}) explicitly. Therefore, taking the maximum will clearly produce the desired output.

The more interesting part is how to implement some of the operations efficiently enough. The short version is that the suffix array (SA) will give us all the necessary tools. First, observe that we can construct the SA of the concatenation of the node strings (with some separation character) in O(_N_) time \[12\] after sorting all characters occurring in all strings \(v\in V\) in O(_N_log_N_) time. The SA (together with the LCP array) gives us a constant- size unique name for each length-\(\ell\) substring of any label that can be computed (after preprocessing) in constant time given a location in a node string. Call this the _rank_ of a substring. Note that the ranks are the same for all occurrences of the same substring. In addition, these are integers bounded by _N_. One may think of this as a perfect hash function that we can use to (1) compare substrings in constant time, and (2) implement the dictionary _C_ defined in Line 1 using O(_N_) space. Using (1) and (2), we implement the loop in Line 3 so that it runs in O(_N_) time. In particular, after a single linear pass over the node strings, we use these names to build a simple inverse index to access the nodes that contain a given rank, as required in Line 4. As we access the nodes for each label exactly once and this inverse index has total size O(_N_), that is also the total time to access the nodes. Similarly, observe that in a linear pass, we can build a list of the unique ranks that occur in each node, making the loop in Line 6 take O(_N_) time in total for each _X_. The operations in the innermost loop require constant time. In particular, the operation \(\unknown\) can be any total order on the length-\(\ell\) substrings. To get a constant-time comparator, we choose the rank order.

Thus, we are finally left to argue why the loop in Line 5 does not blow up the running time. Observe that each edge {_u,v_} is only considered for a motif pair {_X,Y_} if _X_ occurs in _u_ and _Y_ occurs in _v_. (Each edge is visited exactly once in Line 5, oriented so that \(u\in V_X\); the second loop adds the _Y_ ’s that occur only in _u_.) This can happen at most \((|u|-\ell+1)(|v|-\ell+1)\) times. Then

\(\sum_{\{u,v\}\in E}(|u|-\ell+1)(|v|-\ell+1)\le\sum_{(u,v)\in V\times V}|u||v|=\left(\sum_{u\in V}|u|\right)\left(\sum_{v\in V}|v|\right)=\mathcal{O}(N^2),\)

yields the desired bound. The space used is O(_N_) as SA and _C_ are implemented in O(_N_) space. \(\sqcap\sqcup\)

_Remark_ 3.2 (Sparse graphs). It is easy to see that the running time of Algorithm 3.1 can also be bounded by O(_N_log_N_+|_E_|max<sub>_v_∈_V_</sub>|_v_|<sup>2</sup>). Thus, we expect the algorithm to perform better on sparse graphs where the<tbc>

