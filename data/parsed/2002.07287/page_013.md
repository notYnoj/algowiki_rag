Munro and Raman realize tree navigation by supporting the following three operations on the balanced parenthesis representation.

\(\blacktriangleright\) **Lemma 9.** _For any balanced parenthesis representation of length n there is an auxiliary structure on top of the representation that consists of o(n_) _bits and provides, after O(n_) _initialization time, the following operations in constant time:_

\(\blacksquare\) \(\text{\textit{findclose}}(i)(i\in IN)\)_: Returns the position of the closing parenthesis matching the open parenthesis at position i._

\(\blacksquare\) \(\text{\textit{findopen}}(i)(i\in IN)\)_: Returns the position of the open parenthesis matching the closed parenthesis at position i._

\(\blacksquare\) \(\text{\textit{enclose}}(i)(i\in IN)\)_: Returns the position of the closest open parenthesis part of the parenthesis pair enclosing the open parenthesis at position i._

The parenthesis representation is typically stored as a bit sequence _B_ with open parenthesis represented via a 1 and a closed parenthesis via a 0. Via rank-select structure (Lemma 1) on _B_ a bidirectional mapping between each node _u_ of an ordinal tree \(T'\) and the index of _u_’s open parenthesis can be created.

A parenthesis representation can easily be generalized to allow not just one type of matching parenthesis, but instead use parenthesis from a constant sized universe while providing the same operations as described in Lemma 9 and using the same asymptotic space bound. The techniques for this are outlined in a book on compact data structures by Navarro [43, Chapter 7]. Concretely, in a later section we use a parenthesis representation that uses the alphabet {(,),[,]}. In this section we only use the alphabet {(,)}.

To compute a balanced parenthesis representation of a tree _T_, one requires to execute a DFS traversal of _T_. As we want our solutions to be space-efficient, this DFS traversal must be space-efficient as well. One simple solution is to use the space-efficient algorithm for DFS traversal of Banerjee et al. [17, Lemma 2]. Their algorithm works with _O(n+m_) bits and time, which is _O(n_) bits on all sparse graph classes. As described, their algorithm requires the input graph to have so-called _crosspointers_, which is a common extension of the standard adjacency array representation. We show that one can execute a simple linear-time and -bit DFS when only a standard adjacency array representation of the graph is given. The general idea is quite similar to the algorithm of Banerjee et al. [17]. Intuitively, we execute a standard iterator based DFS, that uses neighborhood iterators. One can implement such an iterator space-efficiently using self-delimiting numbers, such that the sum of bits required is _O(n+m_) for graphs with _n_ vertices and _m_ edges. We summarize this in the following lemma.

\(\blacktriangleright\) **Lemma 10.** _Let G be an n-vertex m-edge graph given via an adjacency array representation. There is a DFS that runs on G in O(n+m_) _time and bits._

**Proof.** As described in Section 2, let `adj`[_u_] be the adjacency array of a vertex \(u\in V(G)\). We begin by describing a small auxiliary data structure, which we call _compact iterator_. It is initialized for a vertex \(u\in V(G)\) and allows iteration over all neighbors of _u_ in _G_ in addition to outputting the parent _v_ of _u_ in the DFS tree (or null if the vertex has no parent). The parent _v_ of _u_ is passed as an optional parameter during initialization. The exact operations that the compact iterator provides for a vertex _u_ are as follows:

\(\blacksquare\) `initialize`(_u,v_): Given a vertex _u_ and an (optional) parent _v_ of _u_ in the DFS tree, initialize the compact iterator by setting an iterator variable _i_ to 0, followed by iterating over `adj`[_u_] to find and store the index _j_ so that _v_=`adj`[_u_][_j_].

