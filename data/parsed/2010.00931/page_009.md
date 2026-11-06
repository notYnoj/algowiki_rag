**Observation 3.** _If_ ch(_A_) _is a path in S, then A is a Steiner-closed set._

We next define Steiner-closed STTs.

**Definition 4** (Steiner-closed STT \[BCI<sup>+</sup>20\])**.** An STT _T_ on _S_ is Steiner-closed, if for all \(x\in V(S)\), the set of nodes in the search path of _x_ is a Steiner-closed set.

One can obtain a canonical Steiner-closed STT from the underlying search space itself.

**Observation 4.** _Let S be an unrooted tree, and let S<sup>r</sup> be the rooted tree obtained by picking an arbitrary root_ \(r\in V(S)\) _in S. Then S<sup>r</sup> is a Steiner-closed STT on S._

Steiner-closed STTs are useful in particular due to the following observation.

**Lemma 1** (\[BCI<sup>+</sup>20, Lemma 4.2\])**.** _Given an STTT on S, we can find, in polynomial time, a Steiner-closed STT_ \(T'\) _of S so that_ \(\mathtt{depth}_{T^\prime}(x)\le 2\cdot\mathtt{depth}_T(x)\)_, for all_ \(x\in V(S)\).

Note that Lemma 1 is stated by Bose et al. for maximum depth, but it is explicitly observed in their proof that during the transformation from _T_ to \(T'\) the depth of _every node_ at most doubles. An algorithm with running time O(_n_<sup>2</sup>) is implicit in the proof of Bose et al., with standard data structuring. We omit the proof of this statement, as we show a more general result in §3. More precisely, in §3 we define the class of _k-cut_ STTs, and in §4.2 we show that the 2-cut and Steiner-closed properties are equivalent.

## Static and dynamic STT model.

We now discuss the cost model of STTs, as a straightforward extension of the BST cost model (see e.g. \[Wil89, DHIP07\]). Let _T_ be an STT on _S_. The cost of searching \(x\in V(S)\) in _T_ is `depth`_<sub>T</sub>(x_). The cost of serving a sequence of searches \(X=(x_1,\dots,x_m)\in V(S)^m\) in _T_ is \(\mathtt{cost}_T(X)=\sum_{i=1}^m\mathtt{depth}_T(x_i)\).

If re-arrangements of the tree _T_ are allowed, the model is as follows. An algorithm A starts with an initial search tree _T_<sub>0</sub> on _S_, and _T<sub>i</sub>_ denotes the state of the tree after the _i_-th search. At the start of the _i_-th search, a _pointer_ is at the root of _T_<sub>_i_-1</sub> and A can perform an arbitrary number of steps of (1) rotating the edge between the node _x_ at the pointer and its parent, and (2) moving the pointer from the current node _x_ to its parent or to one of its children. When serving the search _x<sub>i</sub>_, the pointer must visit, at least once, the node _x<sub>i</sub>_.

a
C
b
f
d
j
e
i
g
kO
ho

Figure 3.: A tree _S_ with subset _A_ of nodes shaded and convex hull ch(_A_) shown with dotted line. Observe that _A_ is not Steiner-closed, but \(A\cup\{d\}\) is Steiner-closed.

