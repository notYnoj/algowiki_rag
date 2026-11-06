**Algorithm 1** Finding Pivots

function FindPivots(B,S)<br>
• **requirement:** for every incomplete vertex v with d(v)\<B, the shortest path to v visits some complete<br>
vertex in S<br>
• **returns:** sets P,W satisfying the conditions in Lemma 3.2<br>
\(W\leftarrow S\)<br>
\(W_0\leftarrow S\)<br>
   for \(i\leftarrow 1\) to k do \(\triangleright\) Relax for k steps<br>
\(W_i\leftarrow\emptyset\)<br>
   for all edges (u,v) with \(u\in W_{i-1}\) do<br>
   if \(\widehat{d}[u]+w_{uv}\le\widehat{d}[v]\) then<br>
\(\widehat{d}[v]\leftarrow\widehat{d}[u]+w_{uv}\)<br>
   if \(\widehat{d}[u]+w_{uv}<B\) then<br>
\(W_i\leftarrow W_i\cup\{v\}\)<br>
\(W\leftarrow W\cup W_i\)<br>
   if |W|\>k|S| then<br>
\(P\leftarrow S\)<br>
   return P,W<br>
\(F\leftarrow\{(u,v)\in E:u,v\in W,\widehat{d}[v]=\widehat{d}[u]+w_{uv}\}\triangleright F\)<br>
is<br>
directed<br>
forest<br>
under<br>
Assumption<br>
2.1<br>
\(P\leftarrow\{u\in S:u\text{is<br>
a<br>
root<br>
of<br>
a<br>
tree<br>
with<br>
\(\ge k\)<br>
vertices<br>
in<br>
_F_<br>
}<br>
   return P,W

_Proof._ Note that all vertices visited by Algorithm 1 are in \(\widetilde{U}\), and those in W are not guaranteed to be complete after the procedure. Also note that every vertex in \(\widetilde{U}\) must visit some vertex in S which was complete before Algorithm 1, since any incomplete vertex v at that time with d(v)\<B must visit some complete vertex in S.

If the algorithm returns due to |W|\>k|S|, we still have |W|=O(k|S|) since the out-degrees of vertices are constant. For every incomplete vertex v such that d(v)\<B, we know that the shortest path to v visits some complete vertex \(u\in S\). Since P=S, we must also have \(u\in P\) and conditions in the lemma are thus satisfied.

If \(|W|\le k|S|\), P is derived from F. For any vertex \(x\in\widetilde{U}\), consider the first vertex \(y\in S\) on the shortest path to x which was complete before Algorithm 1, then y must be a root of a tree in F. If there are no more than k-1 edges from y to x on the path, x is complete and added to W after k relaxations. Otherwise, the tree rooted at y contains at least k vertices, therefore y is added to P. Additionally, \(|P|\le|W|/k\le|\widetilde{U}|/k\) since each vertex in P covers a unique subtree of size at least k in F.

To evaluate the time complexity, note that the size of W is \(O(min\{k|S|,|\widetilde{U}|\})\), so each iteration takes \(O(min\{k|S|,|\widetilde{U}|\})\) time. Computing P after the for-loop runs in O(|W|) time for final W. Therefore, FindPivots finishes in \(O(min\{k^2|S|,k|\widetilde{U}|\})\) time.

We also use the following data structure to help adaptively partition a problem into sub-problems, specified in Lemma 3.3:

**Lemma 3.3.** _Given at most N key/value pairs to be inserted, an integer parameter M, and an upper bound B on all the values involved, there exists a data structure that supports the following operations:_

**Insert** _Insert a key/value pair in amortized O_(max{1,log(_N/M_)}) _time. If the key already exists, update its value._

