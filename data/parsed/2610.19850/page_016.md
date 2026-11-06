**Lemma 10** (\[6\])**.** _Let_ \(\Omega\) _be a PMC of G and S a minimal separator of G contained in_ \(\Omega\)_. The set_ \(\Omega\backslash S\) _is included into one connected component of G_\\_S which is full for S._

One aspect of neighbor separators is crucial to achieve the analysis of both BT-Enum \[6\] and our algorithm PMC-Traversal. It concerns the impact of _triangulating_ these separators \(S\unknown\Omega\), _i.e._ adding all possible edges in \(S\times S\).

**Definition 15** (Active separator \[6\])**.** _Let_ \(\Omega\) _be a PMC of G and_ \(S\subseteq\Omega\) _a minimal separator of G. We say S is active for_ \(\Omega\) _if_ \(\Omega\) _is not a clique after triangulating all neighbor separators_ \(S'\unknown\Omega\) _different from S, i.e._ \(S'\neq S\)_. PMCs which admit at least one active separator are called_ active PMCs.

A surprising point is that the notion of active separator is in some way related to the property of being (or not) a PMC in subgraphs of _G_. We define _a-nice PMCs_, reusing an expression from \[15\].

**Definition 16** (_a_-nice PMC)**.** _Given a graph G and some vertex_ \(a\in V(G)\)_, we say a PMC_ \(\Omega\) _of G is a_-nice _iff_ \(a\notin\Omega\) _and_ \(\Omega\) _is not a PMC of graph G_\\{_a}._

Authors of \[6\] established that if \(\Omega\) is a PMC of _G_ but not of _G_\\{_a_}, then necessarily the singleton {_a_} in _G_ is a one-vertex separator which blocks the reachability between at least two vertices of \(\Omega\). Consequently, the separator \(S=N(C_G(a,\Omega))\) is active: as {_a_} is sufficient to separate some pair \(u,v\in\Omega\) in \(G[\overline{\Omega}\cup\{u,v\}]\), then for any connected component _C_ of \(G\backslash\Omega\) different from \(C_G(a,\Omega)\), we cannot have \(\{u,v\}\subseteq N(C)\). So, triangulating all separators _N(C_) with \(C\neq C_G(a,\Omega)\) will not make \(\Omega\) become a clique, since edge (_u,v_) will miss. This is why _a_-nice PMCs are also active PMCs. This notion of _a_-nice PMCs is described in Figure 3.

Now we can briefly present the algorithm BT-enum proposed in \[6\] to enumerate all the PMCs in output-quadratic time. Lemmas following this paragraph will justify why BT-enum actually finds all PMCs of the input graph. This algorithm uses recursivity, based upon the following key idea: knowing the PMCs of graph \(G'=G\backslash\{a\}\) for some \(a\in V(G)\), we are able to compute the PMCs of a graph _G_. To achieve this transfer, BT-enum performs four successive enumeration steps:

1. The PMCs of _G_ can be PMCs of \(G'\): we consider the list of PMCs returned recursively for \(G'\) and check whether they are PMCs of _G_ in polynomial time (Lemma 7).<tbc>

2. The PMCs of _G_ can be possibly written as \(\Omega'\cup\{a\}\), where \(\Omega'\) is a PMC of \(G'\): we consider the list of PMCs returned recursively for \(G'\) and check whether all \(\Omega'\cup\{a\}\) are PMCs or not.<tbc>

a
b
b
a
Ω
Ω
Ω

(a) A PMC \(\Omega\) (blue vertices) of _G_.

(b) \(\Omega\) is not a PMC in _G_\\{_a_}.

(c) But \(\Omega\) is a PMC in _G_\\{_b_}.

Figure 3: An example of PMC \(\Omega\) which is _a_-nice but not _b_-nice. Indeed, \(\Omega\) does not satisfy the reachability property in _G_\\{_a_}: there is a conflict pair (pink dashed line).

