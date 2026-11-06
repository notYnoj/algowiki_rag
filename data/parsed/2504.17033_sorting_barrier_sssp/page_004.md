### Total order of Paths.

Like in many papers on shortest path algorithms, we make the following assumption for an easier presentation of our algorithm:

**Assumption 2.1.** _All paths we obtain in this algorithm have different lengths._

This assumption is required for two purposes:

1. To ensure that `PRED`\[_v_\] for all vertices \(v\in V\) keep a tree structure throughout the algorithm;<tbc>

2. To provide a relative order of vertices with the same value of \(\widehat{d}[]\).

Next, we show that this assumption does not lose generality since we can provide a total order for all paths we obtain. We treat each path of length _l_ that traverses \(\alpha\) vertices \(v_1=s,v_2,\dots,v_\alpha\) as a tuple \(\langle l,\alpha,v_\alpha,v_{\alpha-1},\dots,v_1\rangle\) (note that the sequence of vertices is reversed in the tuple). We sort paths in the lexicographical order of the tuple in principle. That is, first compare the length _l_. When we have a tie, compare \(\alpha\). If there is still a tie, compare the sequence of vertices from \(v_\alpha\) to _v_<sub>1</sub>. Comparison between the tuples can be done in only _O_(1) time with extra information of `PRED`\[\] and \(\alpha\) stored for each \(\widehat{d}[v]\):

**Relaxing an edge** (_u,v_)**:** If \(u\neq\text{\texttt{PRED}}[v]\), even if there is a tie in _l_ and \(\alpha\), it suffices to compare between _u_ and `PRED`\[_v_\], and if _u_=`PRED`\[_v_\], then \(\widehat{d}[u]\) is updated to currently "shortest" and \(\widehat{d}[v]\) needs to get updated;

**Comparing two different** \(\widehat{d}[u]\) **and** \(\widehat{d}[v]\) **for** \(u\neq v\)**:** Even if there is a tie in _l_ and \(\alpha\), it suffices to compare the endpoints _u_ and _v_ only.

Therefore, in the following sections, we may assume that each path started from _s_ has a unique length.

## 3 The Main Result

### 3.1 The Algorithm

Recall that we work on SSSP from source _s_ in constant-degree graphs with _m=O(n_). Let \(k:=\lfloor log^{1/3}(n)\rfloor\) and \(t:=\lfloor log^{2/3}(n)\rfloor\) be two parameters in our algorithm. Our main idea is based on divide-and-conquer on vertex sets. We hope to partition a vertex set _U_ into 2_<sup>t</sup>_ pieces \(U=U_1\cup U_2\cdots\cup U_{2^t}\) of similar sizes, where vertices in earlier pieces have smaller distances, and then recursively partition each _U<sub>i</sub>_. In this way, the size of the sub-problem shrinks to a single vertex after roughly (log_n)/t_ recursion levels. To construct our structure dynamically, each time we would try to compute the distances to a set of closest vertices (without necessarily recovering a complete ordering between their true distances), and report a boundary indicating how much progress we actually make.

Suppose at some stage of the algorithm, for every _u_ with _d(u)\<b_, _u_ is complete and we have relaxed all the edges from _u_. We want to find the true distances to vertices _v_ with \(d(v)\ge b\). To avoid the \(\Theta(logn)\) time per vertex in a priority queue, consider the "frontier" _S_ containing all current vertices _v_ with \(b\le\widehat{d}[v]<B\) for some bound _B_ (without sorting them). We can see that the shortest path to every incomplete vertex \(v'\) with \(b\le d(v')<B\) must visit some complete vertex in _S_. Thus to compute the true distance to every \(v'\) with \(b\le d(v')<B\), it suffices to find the shortest paths from vertices in _S_ and bounded by _B_. We call this subproblem _bounded multi-source shortest path_ (BMSSP) and design an efficient algorithm to solve it. The following lemma summarizes what our BMSSP algorithm achieves.

**Lemma 3.1** (Bounded Multi-Source Shortest Path)**.** _We are given an integer level_ \(l\in[0,\lceil log(n)/t\rceil]\)_, a set of vertices S of size_ \(\le 2^{lt}\)_, and an upper bound_ \(B>max_{x\in S}\widehat{d}[x]\)_. Suppose that for every incomplete vertex v with d(v)\<B, the shortest path to v visits some complete vertex_ \(u\in S\).

