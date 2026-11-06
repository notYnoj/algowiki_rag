<tbc>the augmented graph). See Figure 2c. It is not difficult to see that this is also the case after removing the artificial edges.

**Claim 3.** _The u-to-v path P in T is a_ 3/4_-balanced path separator for the input graph (without artificial edges)._

_Proof._ First, in the augmented graph with artificial edges we are exactly in Case 1: we find a balanced node, which translates to a 3/4-balanced separator with respect to vertex-weights, as we proved in Case 1. This separator defines a cycle also in the original input graph (with possibly one additional edge). The set of vertices inside and outside this cycle are exactly the same in the augmented and original graph (and they have the same weight), and they are not affected by the artificial edges. Hence, the same separator is also a 3/4-balanced separator in the original input graph.

Finally, _P_ and _e_ (if added to _G_) constitute a fundamental cycle _C(T,e_) in \(G\cup\{e\}\), and obviously _e_ does not violate planarity as it was embedded inside a face. This concludes the proof of Lemma 5.

The above concludes the correctness of Algorithm 1 which we summarize in the following Theorem 2. In Section 5 we show how to implement it distributively thus proving Theorem 1.

**Theorem 2.** _Let G be a bi-connected embedded planar graph, T a spanning tree of G, and_ \(w\left(\cdot\right)\) _a_ 1/12_- proper weight assignment to G’s vertices. Then, Algorithm 1 deterministically finds a_ 3/4_-balanced path separator P of G, where P is a path in T. Moreover, there exists an edge_ \(e\notin T\) _(maybe even_ \(e\notin G\)_), such that,_ \(S=P\cup\{e\}\) _is a_ 3/4_-balanced fundamental cycle separator of G (after adding e in case_ \(e\notin G\)_, in which case, e does not violate planarity)._

## 5 A Distributed Implementation

In this section we present the distributed implementation of Algorithm 1. We first define some notions and briefly overview a set of existing tools in distributed algorithms.

### 5.1 Distributed Tools

The main computational task our algorithm performs is computing _aggregations_. This is by now a simple and standard building block in CONGEST algorithms. The advantage of an algorithm that works only with aggregations is that, it can be easily extended to be applied on multiple subgraphs of _G_ simultaneously, which is useful for applications. We elaborate on this more in Section 5.2.

**Definition 8** (Aggregate operator)**.** Given a set of _b_-bit strings {_x_<sub>1</sub>_,...,x<sub>m</sub>_}, an aggregate operator \(\oplus\) over all _x<sub>i</sub>_ is denoted \(\oplus_ix_i\), and is defined as the result of repeatedly replacing any two strings _x<sub>i</sub>_, _x<sub>j</sub>_ with the _b_-bit string \(x_i\oplus x_j\), until a single string remains. We use simple commutative operators like _AND, OR, SUM._

**Low-congestion shortcuts and aggregations.** _Low-congestion shortcuts_ is a well known tool, first introduced in [7], and is used to communicate in multiple subgraphs of the input graph simultaneously, in particular, it allows us to solve the classic _part-wise aggregation (PA)_ problem efficiently.

**Definition 9** (Part-wise aggregation (PA))**.** Let \(\{G_i\}_{i=1}^k\) be a partition of _G_ into vertex-disjoint con nected subgraphs, such that each \(v\in G_i\) has an \(\tilde{O}(1)\)-bit string _x<sub>v</sub>_. The part-wise aggregation problem asks that each vertex of _G<sub>i</sub>_ knows the aggregate value \(\oplus_{v\in G_i}x_v\).

Since _G<sub>i</sub>s_ are given as an input, they might be of arbitrarily large diameter. This is the challenge that low-congestion shortcuts resolve.

**Definition 10** (Low-congestion shortcuts [7])**.** Let \(\{G_i\}_{i=1}^k\) be a partition of _G_ into vertex-disjoint connected subgraphs, a (_c,d_)-shortcut, is a set of subgraphs \(\{H_i\}_{i=1}^k\) of _G_ such that the diameter of each \(G_i\cup H_i\) is at most _d_ and each edge of _G_ participates in at most _c_ subgraphs _H<sub>i</sub>_.

