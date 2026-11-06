**Proof.** Let _A_ be the \(n\times n\) adjacency matrix of **G** and let _C_ be its complement. Let _I_ be the \(n\times n\) identity matrix. Let _X_ be the \(n\times 2n\) matrix obtained by concatenating _A_ and _I_ (with _I_ to the right of _A_). Now let _Y_ be the \(2n\times n\) matrix obtained by concatenating _C_ on top of _I_.

Note that for any given \(i,j\in[n]\), we have that (_XY_)[_i,j_]=0 iff

for every _k_ such that \((i,k)\in E\), we have \((k,j)\in E\) (i.e. if _A[i,k_]=1, then _C[k,j_]=0), and

also \(i\neq j\) (i.e. \(I[i,i]\cdot I[i,j]=0\)).

Note that the standard reduction from OV on two sets to OV on a single set still works here: you can create a single \(2n\times(2n+2)\) matrix, _Z_, by concatenating _X_ on top of the complement of _Y_ and add two new columns, so that every row in _Z_ corresponding to a row of _X_ has 01 in those two columns, and every row in _Z_ corresponding to a column of _Y_ has 10 in those two columns.

Now we give the second direction of the reduction.

**Lemma B.2.** _Given two sets U and V of n Boolean vectors on n coordinates, in_ O(_n_<sup>2</sup>) _time one can create an_ O(_n)-node graph G so that G contains a dominated vertex if and only if there are_ \(u\in U,v\in V\) _s.t._ \(u\cdot v=0\).

**Proof.** Let _C_ be the _n_ coordinates of the two _n_-sets of _n_-length vectors _U_ and _V_ .

Create a graph as follows (refer to Figure 6 for a visualization): Create vertex sets \(X,Y,X',Y',X'',C',C''\) of size _n_ each. \(C'\) and \(C''\) are nodes corresponding to the coordinates _C_. They are connected by a matching: for every \(c\in C\) there is an edge between its copies \(c'\in C'\) and \(c''\in C''\). Both \(C'\) and \(C''\) are cliques.

_X_ is an independent set, _Y_ is a clique, and there is an edge between every node in _X_ and every node in _Y_ . Every node \(x\in X\) has a copy \(x'\in X'\) and an edge to that copy; \(X'\) is a clique. Similarly, every node \(y\in Y\) has a copy \(y'\in Y'\) and an edge to that copy; \(Y'\) is a clique. Every node in \(X'\) has a copy in \(X''\) and an edge to that copy and \(X''\) is a clique.

Every node in \(X'\) has an edge to every node in _Y_ . Each \(x_i\in X\) corresponds to a vector \(u_i\in U\) and every \(y_j\in Y\) corresponds to vector \(v_j\in V\) . Each \(x_i\in X\) has an edge to \(c\in C'\) iff _u<sub>i</sub>_ has a 1 in position _c_. Each \(y_j\in Y\) has an edge to \(c\in C'\) iff _v<sub>j</sub>_ has a 0 in position _c_.

Now, if _u<sub>i</sub>_ and _v<sub>j</sub>_ are orthogonal, then \(x_i\in X\) is a dominated vertex, dominated by \(y_j\in Y:(x_i,y_j)\in E\), and the remaining neighbors of _x<sub>i</sub>_ are in \(X'\cup C'\): _y<sub>j</sub>_ is adjacent to all of \(X'\) and since _u<sub>i</sub>,v<sub>j</sub>_ are orthogonal, _v<sub>j</sub>_ has a 0 for every coordinate _c_ for which _u<sub>i</sub>_ has a 1, so the neighbors of _x<sub>i</sub>_ are also neighbors of _y<sub>j</sub>_. In fact this is an iff.

By construction, if we have any other pair of nodes (_a,b_) not in \(X\times Y\) , neither can dominate the due to the copies and cliques.

We will be explicit here. If _U_ or _V_ contains an all-0 vector, then the OV instance is a yes-instance and we can output a graph of two adjacent vertices, which has a dominated vertex. Hence we may assume that neither _U_ nor _V_ contains an all-0 vector.

\(\blacksquare\) A node \(x\in X\) cannot dominate another \(x_1\in X\) because they each have an edge to a different node in \(X'\).

\(\blacksquare\) A node \(x\in X\) cannot dominate a node in \(X'\cup X''\cup Y'\cup C'\cup C''\) since these sets are cliques and _x_ is missing an edge to some node in each of these cliques.

\(\blacksquare\) A node \(a\in X\cup X'\cup X''\cup C'\cup C''\) cannot dominate any \(y\in Y\) because _y_ has a neighbor in \(Y'\) and _a_ does not. (This also means \(x\in X\) does not dominate any node.)

\(\blacksquare\) A node \(y'\in Y'\) cannot dominate any node in _Y_ because _Y_ is a clique and \(y'\) only has one edge to that clique.

\(\blacksquare\) A node \(y_1\in Y\) cannot dominate another node \(y_2\in Y\) since they have edges to different nodes in \(Y'\). (This also means that the nodes in _Y_ are not dominated by any other nodes in the graph.)

\(\blacksquare\) A node \(x'\in X'\) cannot dominate any node in \(X''\cup Y'\cup C'\cup C''\) since these sets are cliques and \(x'\) is missing an edge to some node in each of these cliques.

