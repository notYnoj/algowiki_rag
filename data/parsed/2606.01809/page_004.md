<tbc>_setting, such that each update is processed in_ \(\tilde{O}(\sqrt{r})\) _worst-case update time, and the weight of each edge_ (_x,y_) _with_ \(x,y\in\partial H\) _can be returned in query time O_(log_n). Moreover the data structure is deterministic and has a preprocessing time_ \(\tilde{O}(n)\).

_If the graph is incremental, then our data structure also works in the online setting._

It is not hard to see from the discussion above how this result can be combined with Theorem 1.3 to derive Theorem 2.1 as a corollary. Thus, the following sections are concerned with proving Theorem 2.3.

Our result can be applied to obtain an improvement to the following variant of dynamic max flow/min st-cut:

**Corollary 2.4.** _Given an n-vertex undirected planar flow network G with edge capacities, a source s, and a sink t, there is a deterministic data structure that can maintain the value of a max flow from s to t (equivalently, the value of a min st-cut) under either an offline sequence of edge weight changes or an online sequence of edge weight decreases. Each update and each query for the current max flow value can be handled in_ \(\tilde{O}(\sqrt{n})\) _worst-case time._

The previous best update/query time bound was \(\tilde{O}(n^{2/3})\) by Italiano et al.\[20\]. Corollary 2.4 follows easily by replacing the trivial dynamic DDG algorithm in \[20\] with our data structure; the proof can be found in Appendix E.

### Conceptual Contribution.

We believe that our techniques and conceptual ideas give first indications towards designing such algorithms in the online setting:

• Our main conceptual change is a shift in perspective to view DDGs as a data structure and allow for small (but non-constant) query times. This is in stark contrast to previous literature where the DDGs where mostly seen as complete graphs that where explicitly constructed.<tbc>

• Further, our online incremental DDG data structure can be used to reduce the online dynamic APSP problem to the online decremental DDG setting. More precisely, if one can give an online algorithm A that maintains a DDG on a graph subject to edge weight increases with worst-case update time \(\tilde{O}(n^{1-\epsilon})\) for any \(\epsilon>0\), query time \(\tilde{O}(1)\), and preprocessing \(\tilde{O}(n)\), then there exists an online algorithm B for the dynamic APSP problem with worst-case update/query time \(n^{2/3-\Omega(\epsilon)}\). A precise statement and proof can be found in Section D.

## 3 Related Work

### Dynamic Shortest Paths in Planar Graphs.

As stated in the introduction, the only two dynamic data structures for APSP in planar graphs are currently \[16, 25\]. Both achieve update time \(\tilde{O}(n^\delta)\) and query time \(\tilde{O}(n^{1-\delta/2})\) for \(\delta\in[0,1]\). In particular, for \(\delta=\frac{2}{3}\), they achieve update and query time \(\tilde{O}(n^{2/3})\). We note that various improvements followed that improved the above algorithms by logarithmic or doubly-logarithmic terms or generalized the result \[29, 21, 18\].

A lower bound for the exact problem, given in \[1\], stipulates that \(\tilde{\Omega}(n^\delta)\) update time and \(\tilde{\Omega}(n^{1-\delta})\) query time is necessary if one believes in the APSP conjecture.

For undirected planar graphs in the setting where one allows for a \((1+\epsilon)\)-approximation on the distance queries, Abraham, Chechik and Gavoille \[2\] presented a data structure that achieves<tbc>

