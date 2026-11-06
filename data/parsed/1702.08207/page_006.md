## 2.3 Query Sequences and Stable Strategies

By a slight abuse of notation, we will call a search strategy _polynomial-time_ if it can be implemented using a dynamic (adaptive) algorithm which computes the next queried vertex in polynomial time.

We give most of our attention herein to search strategies in trees which admit a natural (non-adaptive, polynomial-space) representation called a _query sequence assignment_. Formally, for a rooted tree _T_, the _query sequence assignment S_ is a function \(S:V\rightarrow V^*\), which assigns to each vertex \(v\in V\) an ordered sequence of vertices _S(v_), known as the _query sequence_ of _v_. The query sequence assignment directly induces a strategy A_<sub>S</sub>_, presented as Algorithm 2.1. Intuitively, the strategy processes successive queries from the sequence _S(v_), where _v_ is the root vertex of the current search tree, \(v=r(T\langle U,x\rangle)\), where _U_ is the set of queries performed so far. This processing is performed in such a way that the strategy iteratively takes the first vertex in _S(v_) that belongs to \(T\langle U,x\rangle\) and queries it. As soon as the root of the search tree changes, the procedure starts processing queries from the sequence of the new root, which belong to the remaining search tree. The procedure terminates as soon as \(T\langle U,x\rangle\) has been reduced to a single vertex, which is necessarily the target _x_.

**Algorithm 2.1** Search strategy A_<sub>S</sub>_ for a query sequence assignment _S_

1: \(v\leftarrow r(T)\) // stores current root

2: \(U\leftarrow\emptyset\)

3: **while** |_T\langle U,x\rangle|\>_1 **do**

4: **for** \(u\in S(v)\) **do**

5: **if** \(u\in T\langle U,x\rangle\) **then** // _u_ is the first vertex in _S(v_) that belongs to \(T\langle U,x\rangle\)

6: QueryVertex(_u_)

7: \(U\leftarrow U\cup\{u\}\)

8: **if** \(v\neq r(T\langle U,x\rangle)\) **then** // query reply is ‘down’

9: \(v\leftarrow r(T\langle U,x\rangle)\)

10: **break** // for loop

In what follows, in order to show that our approximation strategies are polynomial-time, we will confine ourselves to presenting a polynomial-time algorithm which outputs an appropriate sequence assignment.

A sequence assignment is called _stable_ if the replacement of line 9 in Algorithm 2.1 by any assignment of the form \(v\leftarrow v''\), where \(v''\) is an arbitrary vertex which is promised to lie on the path from \(r(T\langle U,x\rangle)\) to the target _x_, always results in a strategy which performs a (not necessarily strict) subsequence of the sequence of queries performed by the original strategy A_<sub>S</sub>_. Sequence assignments computed on trees with a bottom-up approach usually have the stability property; we provide a proof of stability for one of our main routines in Section 4.

Without loss of generality, we will also assume that if \(v\in S(v)\), then _v_ is the last element of _S(v_). Indeed, when considering a subtree rooted at _v_, after a query to _v_, if _v_ was not the target, then the root of the considered subtree will change to one of the children of _v_, hence any subsequent elements of _S(v_) may be removed without changing the strategy.

## 2.4 Strategies Based on Consistent Schedules

Intuitively, we may represent search strategies by a schedule consisting of some number of jobs, with each job being associated to querying a node in the tree (cf. e.g. \[17, 26, 27\]). Each job has a fixed processing time, which is set to the weight of a node. Formally, in this work we will refer to the schedule \(\hat{S}\) only in the very precise context of search strategies A_<sub>S</sub>_ based on some query sequence assignment _S_. The _schedule assignment_ \(\hat{S}\) is the following extension of the sequence<tbc>

