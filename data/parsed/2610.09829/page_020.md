<tbc>proof. We remark that our problem is not directly amenable to a dynamic programming over this structure alone: the recurrence relies on a second, auxiliary dynamic programming over a graph of shortest cycles, layered on top of the tree recursion. We will begin by recalling the notion of _laminar shortest cycles tree_ for a given plane graph and some useful results regarding them from \[4\].

## 5.1 Laminar Shortest Cycles Tree

We start by recalling the terminology and basic properties of _laminar shortest cycles tree_ from \[4\]; we slightly rephrase some of them for convenience. We begin by recalling how two shortest cycles may interact in a planar graph.

**Proposition 5.1** (Lemma 5.1 \[4\])**.** _Consider a weighted planar graph G and two shortest cycles_ \(C,C'\) _in G, where_ \(|V(C)\cap V(C')|\ge 2\)_. Then exactly one of the following holds (see Figure 10): i)_ \(C\cap C'\) _is a subpath of C (resp._ \(C'\)_), or ii)_ \(E(C)\cap E(C')=\emptyset\) _and_ \(V(C)\cap V(C')\) _has exactly two vertices, say s,t, where s and t are at distance exactly g(G)/_2 _in G (and also in C and_ \(C'\)_)._

Recall a plane graph is a planar graph whose embedding is fixed. Consider a plane graph _G_ and two distinct cycles \(C,C'\) in _G_. Also, each edge _e_ of _G_ is drawn as a curve in the plane, and each cycle defines a closed Jordan curve, where Int(_C_) is the open bounded region enclosed by the Jordan curve of _C_ (i.e., the region not containing the outer face of _G_).

**Definition 5.1** (Crossing cycles)**.** Let _G_ be a plane graph and let \(C,C'\) be two distinct cycles in _G_. The cycles _C_ and \(C'\) _cross_ if both of the following conditions hold (see Figure 11):

(i) there is \(e\in E(C)\) such that every interior point of the curve of _e_ lies in \(\mathrm{Int}(C')\), and<tbc>

Properties of the LSCT Item 4 and propo- sition 5.2
Cycle inter- section lemma Proposition 5.1
Non-tree cycles & paths bounded Lemma 5.1
2 4k leaves: trivial case Lemma 5.3
Testing P-validity Lemma 5.4
Computing IIP(a,h) Lemma 5.5
Main theorem Theorem 1.2

Figure 9: Dependency structure of the proof of Theorem 1.2. The top row, together with Proposition 5.1, is imported from \[4\]. Lemma 5.5 is itself established in Section 5.3 via a further dynamic program (see the companion figure).

