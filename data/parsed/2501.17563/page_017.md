<tbc>primary directions do not maximize the approximation ratio, we also show a deviation from one of the directions, marked with \(p'\) in the table. It is possible to deviate from a primary direction by not too much while maintaining the same vertex solution of the LP. Thus, by considering some random deviations we were able to find an improved direction. We emphasize that this is likely not the direction that maximizes the approximation ratio as our search was not exhaustive.

## 3 Positive Results

In this section we prove some positive results, including the facts that the LP for topologies with \(n\ge 3\) nodes always has integer vertices that are not induced by STTs, and that the LP for a star graph has only integer vertices, implying optimality of the LP for stars of any size.

### 3.1 Basic Properties

**Lemma 3.1** (Depths Bound)**.** Let (_X,Z,D_) be a feasible solution of the LP. Then for _every_ subset of coordinates \(S\subseteq\{1,\dots,n\}\) it holds that: \(\sum_{i\in S}D_i\ge|S|-1\).

The claim is obvious for points induced by STTs, since the LP-depth of every node except for the root is at least one. For the general case, we argue as follows.

_Proof._ Fix _i_ and _j_ and consider their ancestry constraint: \(1\le X_{ij}+X_{ji}+\sum_{k\in(i\unknown j)}Z_{kij}\le X_{ij}+X_{ji}+\sum_{k\in(i\unknown j)}min\{X_{ki},X_{kj}\}\le X_{ij}+X_{ji}+\frac{1}{2}\sum_{k\in(i\unknown j)}(X_{ki}+X_{kj})\le\frac{1}{2}(X_{ij}+X_{ji}+D_i+D_j)\). Then: \(\genfrac(){pt}{2}{|S|}{2}\le\sum_{\{i,j\}\subset S}\frac{1}{2}(X_{ij}+X_{ji}+D_i+D_j)\). Note that each _D<sub>i</sub>_ appears exactly |_S_|-1 times on the right side, and that we have one more contribution of (at most) _D<sub>i</sub>_ from the variables _X<sub>ji</sub>_. Therefore: \(\genfrac(){pt}{2}{|S|}{2}\le\frac{|S|}{2}\sum_{i\in S}D_i\Rightarrow|S|-1\le\sum_{i\in S}D_i\).

**Corollary 3.2.** The depths-vector of any feasible solution has at most _k_ entries with value at most \(\frac{k}{k+1}\). Particularly, at most one coordinate smaller than \(\frac{1}{2}\), at most two smaller than \(\frac{2}{3}\), etc.

**Remark 3.3.** Corollary 3.2 interprets Lemma 3.1 as an upper-bound on the number of nodes with small depth _d\<_1 (it is not meaningful for \(d\ge 1\)). However, there are no lower-bound guarantees. Unlike STT induced vertices that are guaranteed to have one 0 depth (the root’s), a general vertex could have only "large" coordinates.

It may be interesting to understand whether the minimum depth (coordinate) of a vertex is bounded from above. We emphasize that this question is interesting only with respect to vertices rather than with respect to general feasible solutions, because it is easy to take a combinations of STTs to get a feasible point whose minimum depth is large. As a concrete example of vertices whose minimum depth is 1, there are four such vertices up to automorphisms for the topology _U_<sub>(8,4)</sub> (Figure 6) which are (2,2,4.5,1.5,1,1,2,2), (1.5,2,4.5,1.5,1,1,2.5,2.5), (2.5,2.5,4.5,1.5,1.5,1.5,1.5,1), (1.5,2,5,1.5,1,1,2.5,2.5) and one vertex for the topology _U_<sub>(8,13)</sub> which is (1.5,2,3.5,2,1,1,3.5,1.5).

Lemma 3.1 is agnostic to weights. The following Lemma 3.4 takes weights into account.

**Lemma 3.4** (Depth by weights)**.** Let _i_ be a node whose frequency is _f<sub>i</sub>_ where \(\sum_{u\in U}f_u=1\). Then \(depth(i)\le\frac{1}{f_i}\) in every optimal STT. (Recall that the root’s depth is 1.)

