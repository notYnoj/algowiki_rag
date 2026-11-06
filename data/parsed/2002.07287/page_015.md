the _n_-node tree _T_ that there exists a function color : V(T) → {0,1}<sup>+</sup> that outputs for each node \(u\in V(T)\) a binary string color(u) that represents the color of _u_. After the construction of \(T'\) we want to maintain the color information, but as \(T'\) is only isomorphic to _T_ this is not directly possible. Roughly speaking, \(T'\) is a re-labeling of _T_, and we thus need to account for this. Note that \(T'\) is labeled using a DFS on _T_, meaning each node of \(T'\) is labeled in pre-order. During the traversal, when visiting a node _u_ of _T_ for the first time, we simply write the binary string color(u) into a bit vector _C_, and in a secondary bit vector _R_ mark the first position in _C_ of the newly written binary string color(u) into _C_. Once \(T'\) is constructed in this fashion, _C_ is a concatenation of all binary strings color(u) for \(u\in V(T)\) sorted via pre-order traversal. Using a rank-select structure on _R_ then allows to evaluate the colors for \(T'\), i.e., we store the colors in _C_ via static space allocation. We summarize this in the following corollary.

\(\blacktriangleright\) **Corollary 12.** _Given a rooted n-node colored tree T and a color function_ color : V(T) → {0,1}<sup>+</sup> _that can be evaluated in time O_(|color(u)|) _for each_ \(u\in V(T)\) _there is an algorithm that computes a data structure representing an ordinal colored tree_ \(T'\) _in O(n+b) time using O(n+b) bits such that T and_ \(T'\) _are isomorphic, with_ \(b=\sum_{u\in V(T)}|\text{color(u)}|\)_. The data structure allows tree navigation on_ \(T'\) _in constant time in addition to access to the_ color _function for each_ \(u'\in V(T')\).

## 5 Tree Isomorphism

We start this section by giving an introduction to graph and tree isomorphism.

\(\blacktriangleright\) **Definition 13.** _(graph isomorphism) Two given graphs G_=(_VG,EG_) _and H_=(_VH,EH_) _are isomorphic exactly if there exists a bijective mapping_ \(f:VG\rightarrow VH\) _such that vertices_ \(u,v\in VG\) _are adjacent in G if and only if_ \(f(u),f(v)\in VH\) _are adjacent in H. Then f is called an_ isomorphic mapping.

Buss [44] shows an equivalent definition for rooted trees.

9
1
11
12
4
7
1
2
7
8
9
14
10
3
13
5
14
2
6
8
3
4
5
6
10
11
12
13
(a) A rooted tree T.
(b) An ordinal tree T' isomorphic to T.
1
2
3
4
5
6
7
8
9
10
11
12
13
14

**Figure 3** Given a rooted tree _T_ (shown in (a)) with the root _u_=9 a balanced parenthesis representation bpr<sub>u</sub>_ (below of (a) and of (b)) of an ordinal tree \(T'\) that is isomorphic to _T_ (shown in (b)) can be computed by a single DFS run on _T_ in preorder. The parenthesis pairs of each node of \(T'\) are connected by a line and the index of each open parenthesis represents the label of that node in \(T'\).

