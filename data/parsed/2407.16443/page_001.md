# Bounds and Algorithms for Alphabetic s and Binary Search Trees

R. Bruno, R. De Prisco, A. De Santis, and U. Vaccaro _Senior Member, IEEE_

**_Abstract_--Alphabetic codes and binary search trees are combinatorial structures that abstract search procedures in ordered sets endowed with probability distributions. In this paper, we design new linear-time algorithms to construct alphabetic codes, and we show that the obtained codes are not too far from being optimal. Moreover, we exploit our results on alphabetic codes to provide new bounds on the average cost of optimal binary search trees. Our results improve on the best-known bounds on the average cost of optimal binary search trees present in the literature.**

**--Key words: Alphabetic codes, searching, variable-length codes, binary search trees, data structures.**

### I. INTRODUCTION

The Theory of Variable-Length s and Search Theory are strongly intertwined. In fact, _any_ search procedure that identifies objects in a given space, by sequentially executing appropriate tests naturally defines a variable-length encoding of elements in the space. To wit, one can encode each possible test outcome with a different symbol of a finite alphabet, and the concatenation of the (encoded) test outcomes, leading to the identification of an object _x_, gives a _bona fide_ encoding of _x_, for any _x_ in the search space.

More specifically, binary alphabetic codes and binary search trees are basic combinatorial structures that naturally arise in Search Theory [2], [3], [15]. In fact, alphabetic codes are _equivalent_ to search procedures (in ordered sets) that operate through comparison queries with binary results, while binary search trees correspond to search procedures that use comparison queries whose outcome is ternary.

Alphabetical codes have been extensively studied in the Information Theory community (see, e.g., [9], [11], [12], [13], [14], [25], [28], [29] and references therein quoted). Equally, binary search trees have been studied in the Computer Science community, because of the important application scenarios where they appear (see, e.g., [18], [21], [22], [26] and references therein quoted). The two survey papers [1], [24] contain many more references.

It is well known that optimal binary alphabetic codes (i.e., with minimum average length) can be constructed in time _O(m_log_m_) [13], where _m_ is the number of codewords, and that optimal binary search trees (again, with minimum possible average path length) can be constructed in time _O(n_<sup>2</sup>) [18], where _n_ is the number of nodes in the tree. Most of the research activity that followed [13] and [18] has concentrated<tbc>

<tbc>on the following issues: constructing close-to-optimal binary alphabetic codes (equivalently, close-to-optimal binary search trees) via _linear-time_ algorithms, and providing explicit upper bounds on the cost (average path length) of the constructed objects. In this paper, we provide novel upper bounds on the cost of optimal binary alphabetic codes and optimal binary search trees. Our bounds improve on the best bounds known in the literature. Our new results are obtained by accurately analyzing novel linear-time construction algorithms.

### II. PRELIMINARIES

Let _S_={_s_<sub>1</sub>_,...,s<sub>m</sub>_} be a set of symbols, ordered according to a given total order relation \(\prec\), that is, for which it holds that \(s_1\prec\cdots\prec s_m\). A binary alphabetical code is an order-preserving mapping \(w:\{s_1,\dots,s_m\}\mapsto\{0,1\}^+\), where the order relation on the set of all binary strings {0,1}<sup>+</sup> is the standard alphabetical order. We denote by _C_ the set of codewords \(C=\{w(s):s\in S\}\), and by \(\phi=(\phi_1,\dots,\phi_m)\) the probability distribution on the symbols in _S_, that is, \(\phi_i\) is the probability of the _i<sup>th</sup>_ symbol _s<sub>i</sub>_. For each \(s_i\in S\) we denote by _w(s<sub>i</sub>_) the codeword associated to _s<sub>i</sub>_, and by \(\ell(w(s_i))\), or simply by \(\ell_i\), the length of _w(s<sub>i</sub>_).

Given an alphabetic code _C_, an order-preserving mapping \(w:s\in\{s_1,\dots,s_m\}\mapsto w(s)\in\{0,1\}^+\), and a probability distribution \(\phi=(\phi_1,\dots,\phi_m)\) on _S_, we denote the average code length of the code _C_ by

\(\mathbb{E}[C]=\sum_{i=1}^m\phi_i\ell_i.\)

In the following sections, we will occasionally see an alphabetic code as a binary tree _T_ where each edge is labeled either by bit 0 or 1, and each leaf of the tree corresponds to a different symbol \(s\in S\). Sometimes, it will be convenient to identify an arbitrary leaf _s<sub>i</sub>_ of the tree _T_ with the probability \(\phi_i\) of the symbol \(s_i\in S\) that is associated to the leaf. The codeword _w(s_) for the symbol \(s\in S\) is equal to the concatenation of all the 0’s and 1’s in the path from the root of _T_ to the leaf associated with _s_. The order-preserving property of alphabetic codes implies that the leaves of _T_, read from the leftmost leaf to the rightmost one, appear in the order \(s_1\prec\cdots\prec s_m\). As said before, alphabetic codes, in their binary tree representation, naturally correspond to a search procedure that makes use of comparison queries with binary outcomes.

Binary search trees represent, in a sense, a generalization of binary trees associated to alphabetic codes, since the former can take into account both successful and unsuccessful searches. More precisely, any comparison-based search algorithm on an ordered list of elements \(x_1\prec\cdots\prec x_n\) can

The authors are with the Dipartimento di Informatica, Università di Salerno, Fisciano (SA), Italy (email: {`rbruno, robdep, ads, uvaccaro`}@unisa.it). This work was partially supported by project SERICS (PE00000014) under the NRRP MUR program funded by the EU- NGEU.

