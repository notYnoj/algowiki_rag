# Approximation Strategies for Generalized Binary Search in Weighted Trees

**Abstract**

We consider the following generalization of the binary search problem. A search strategy is required to locate an unknown target node _t_ in a given tree _T_. Upon querying a node _v_ of the tree, the strategy receives as a reply an indication of the connected component of _T_\\{_v_} containing the target _t_. The cost of querying each node is given by a known non-negative weight function, and the considered objective is to minimize the total query cost for a worst-case choice of the target.

Designing an optimal strategy for a weighted tree search instance is known to be strongly NP-hard, in contrast to the unweighted variant of the problem which can be solved optimally in linear time. Here, we show that weighted tree search admits a quasi-polynomial time approximation scheme (QPTAS): for any \(0<\varepsilon<1\), there exists a \((1+\varepsilon)\)-approximation strategy with a computation time of \(n^{O(logn/\varepsilon^2)}\). Thus, the problem is not APX-hard, unless \(NP\subseteq DTIME(n^{O(logn)})\). By applying a generic reduction, we obtain as a corollary that the studied problem admits a polynomial-time \(O(\sqrt{logn})\)-approximation. This improves previous \(\hat{O}(logn)\)-approximation approaches, where the \(\hat{O}\)-notation disregards _O_(polyloglog_n_)- factors.

**Key Words:** Approximation Algorithm; Adaptive Algorithm; Graph Search; Binary Search; Vertex Ranking; Trees

### 1 Introduction

In this work we consider a generalization of the fundamental problem of searching for an element in a sorted array. This problem can be seen, using graph-theoretic terms, as a problem of searching for a target node in a path, where each query reveals on which ‘side’ of the queried node the target node lies. The generalization we study is two-fold: a more general structure of a tree is considered and we assume non-uniform query times. Thus, our problem can be stated as follows. Given a node-weighted input tree _T_ (in which the query time of a node is provided as its weight), design a search strategy (sometimes called a decision tree) that locates a hidden _target node x_ by asking _queries_. Each query selects a node _v_ in _T_ and after the time that equals the weight of the selected node, a reply is given: the reply is either ‘yes’ which implies that _v_ is the target node and thus the search terminates, or it is ‘no’ in which case the search strategy receives the edge outgoing from _v_ that belongs to the shortest path between _u_ and _v_. The goal

Dariusz Dereniowski<sup>1</sup>, Adrian Kosowski<sup>2</sup>, Przemysław Uznański<sup>3</sup>, and Mengchuan Zou<sup>2</sup>

<sup>1</sup>Faculty of Electronics, Telecommunications and Informatics, Gdańsk University of Technology, Poland

<sup>2</sup>Inria Paris and IRIF, Université Paris Diderot, France

<sup>3</sup>Department of Computer Science, ETH Zürich, Switzerland

