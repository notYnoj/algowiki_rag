<tbc>In the language of FOL, a motif (say, a triangle) query is an _existential FOL_ statement. We are asking: do there exist vertices _u,v_ and _w_ such that the (_u,v,w_) forms a triangle, maybe satisfying certain temporal constraints? In mathematical language, we would write \(\exists u\exists v\exists w\phi(u,v,w)\), where \(\phi(u,v,w)\) is a Boolean predicate stating that there are edges among _u,v,w_ forming a triangle with the desired constraints. (A temporal motif would enforce some timestamp conditions in \(\phi(u,v,w)\).) The motif counting problem is to count all possible solutions to the FOL statement.

A general FOL statement would involve both existential _and_ universal quantifiers. For example, the FOL statement \(\exists u\exists v\forall w\phi(u,v,w)\) could express the query: do there exist vertices _u,v_ such that for all neighbors _w_ of _v_, (_u,v,w_) form a triangle? With a more complex predicate \(\phi\), we can even express: do there exist _u,v_ such that for all neighbors _w_ where (_u,w_) is an edge, (_w,v_) is an edge that formed within 10 minutes? As we discuss later, we also include _thresholded universal quantifiers_, which represent "for at least a \(\tau\)-fraction of neighbors" (for parameter \(\tau\)).

There are applications for analysis of financial transaction networks. Recent work of Liu et al. [29] on the Venmo transaction network discovered that the temporal triangle in Figure-1 is a likely indication of gambling activities. An FOL query can determine if there are edges (_u,v_) such that most neighbors of _w_ participate in such triangles. As another example, consider the two patterns, denoted "Scatter-Gather" and "Bipartite" in Figure-1. Altman et al. discovered these patterns as signs of money laundering in financial networks [4]. Often the yellow nodes are individuals, and the blue nodes are fake or laundering accounts. The challenge of representing these as motifs is that the number of blue nodes is unknown, so we may not know the size of the motif.

The Scatter-Gather pattern is easily captured as a triadic FOL query: are there vertices _u,v_ such that for (say) most _w_ where (_u,w_) is a transaction, the transaction (_w,v_) occurs within (say) a few days? Observe how we apply a thresholded universal quantifier<tbc>

<tbc>over _w_ to capture the intermediate blue nodes, so we do not need to specify their number. A similar FOL query captures the Bipartite money laundering pattern.

In addition, solutions to these queries can be used to discover edges, which participate in a cohesive group of vertices in _G_. For instance, in a citation network [53] where nodes represent papers and edges (_u,v_) indicate that paper _u_ cites paper _v_, we assign each edge the timestamp of _u_. Next, we run the \(\exists\exists\forall\) query on this dataset for \(\delta=1\) year, list all the edges which satisfy this query, along with their common neighbors. We observe that these vertices correspond to research papers, which were either published in the same journal or are on related topics. For instance, the temporal edge between the paper tiled "Virtual Memory,ACM Computing Surveys (CSUR)"(_u_) and "Measurements of segment size"(_v_) served as a solution to this query. The common neighbours of this edge were papers titled:

(1) "Dynamic storage allocation systems"<tbc>

(2) "Further experimental data on the behavior of programs in a paging environment"<tbc>

(3) "The working set model for program behavior"<tbc>

(4) "A note on storage fragmentation and program segmentation"

Out of these 6 papers, 5 were published in "Communications of ACM", except for the paper titled "Virtual Memory", which was published in "ACM Computing Surveys". Thus, the set \(\{u\}\cup\{v\}\cup\{N(u)\cap N(v)\}\) for any solution _e_=(_u,v,t_) to the \(\exists\exists\forall\) query could potentially form a cohesive set of vertices.

Motivated by these applications, we ask:

_Can we give a formalism for thresholded FOL motif queries on temporal networks, and design efficient algorithms for answering such queries?_

## 1.2 Formal Definition

Let _G_=(_V,E_) be a temporal network. Every edge in _G_ is represented as a triple (_u,v,t_), where _u_ is the head, _v_ is the destination, and _t_ is the edge timestamp. Note that _G_ is a multigraph, since there can be many temporal edges (in both directions) between a pair of vertices. We define our main query below. We use the definitions of temporal motifs from [37-39].

Definition 1.1. _A_ thresholded First Order Logic (FOL) _triadic query is an expression Q_<sub>1</sub>_uQ_<sub>2</sub>_vQ_<sub>3</sub>_w_ \(\phi(u,v,w)\) _where each Q<sub>i</sub> is either_ \(\exists\) _(existential quantifier) or_ \(\forall_\tau\)_, for parameter_ \(\tau\in(0,1)\) _(thresholded universal quantifier)._

_An_ \(\exists u\dots\) _quantifier is satisfied if there exists some u in the universe (vertex set) satisfying the remaining sentence. A_ \(\forall_\tau u\) _quantifier is satisfied if for at least a_ \(\tau\)_-fraction of the universe, the remaining sentence is satisfied. Typically, the universe for a_ \(\forall_\tau\) _quantifier is the neighborhood of a previous vertex._

_The Boolean predicate_ \(\phi(u,v,w)\) _represents a temporal motif on the vertices u,v,w. A_ temporal motif _specifies the direction of edges in u,v,w, the time ordering of edges, and an upper bound on the time interval containing these edges._

To give a concrete example, consider the following query: \(\exists u\exists v\forall_{1/2}w\in N(v)\), (_u,v,w_) form the triangle of Figure-1c within one hour. A solution to this query is pair (_u,v_) of adjacent vertices, which form a triangle (_u,v,w_) with at least half of _v_’s neighbors<tbc>

u
V
u
V
W
(a) Scatter-Gather
(b) Bipartite
W
U
V
(c) Temporal Triangle for gambling

**Figure 1: Different Money-Laundering and Gambling Patterns in Financial Transaction Networks [4, 29]**

