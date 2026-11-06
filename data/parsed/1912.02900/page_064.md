is positive if and only if \(v\in V(P)\backslash\{v_k\}\). Therefore, using Claim 4.1, we get that \(\mathsf{WB}_T(X)\le\sum_{v\in P}\mathsf{cost}(v)\le O(k)\).

## B Binary Search Trees and Equivalence with the Geometric tion

We start by formally defining the BST model. An _access sequence X_={_x_<sub>1</sub>_,...,x<sub>m</sub>_} is a sequence of keys from the universe {1_,...,n_}. We consider algorithms that maintain a Binary Search Tree (BST) _T_ over the set {1_,...,n_} of keys, and support only _access_ operations. After each access the algorithm can reconfigure the tree _T_, as follows. (The definitions below are adapted from \[DHI<sup>+</sup>09\].)

**Definition B.1** _Given two BST’s T_<sub>1</sub> _and T_<sub>2</sub>_, a subtree_ \(\tau\) _of T_<sub>1</sub> _containing the root of T_<sub>1</sub>_, and a tree_ \(\tau'\) _with_ \(V(\tau)=V(\tau')\)_, we say that T_<sub>2</sub> _is a_ reconfiguration of _T_<sub>1</sub> via the operation \(\tau\rightarrow\tau'\)_, if T_<sub>2</sub> _is identical to T_<sub>1</sub> _except that_ \(\tau\) _is replaced by_ \(\tau'\)_. The_ cost _of the reconfiguration is_ \(|V(\tau)|\).

**Definition B.2** _Given an access sequence X_=(_x_<sub>1</sub>_,x_<sub>2</sub>_,...,x<sub>m</sub>), an_ execution sequence _of a BST algorithm on X is_ \(E=(T_0,\tau_1\rightarrow\tau'_1,\dots,\tau_m\rightarrow\tau'_m)\)_, where T_<sub>0</sub> _is the initial tree, and for each_ \(1\le i\le m\), \(\tau_i\rightarrow\tau_{i+1}\) _is a valid reconfiguration operation to be executed at step i, such that_ \(x_i\in\tau_i\)_. The cost of execution E is_ \(\sum_{i=1}^m|V(\tau_i)|\).

As stated in \[DHI<sup>+</sup>09\], the cost of an algorithm’s execution in this model is identical to within a constant-factor to other standard models. This includes, for example, the model that we informally defined in the introduction, where, after each access, the tree is modified by a series of rotations, and the cost consists of the number of such rotations and the distance of the accessed key from the tree’s root.

The BST problem can now be defined as follows:

**Problem B.3 (The BST problem)** _Given an access sequence X, compute an execution sequence for X that has minimum cost. In the online version, the t-th element of the sequence X is revealed at time t, and we need to output a valid reconfiguration operation_ \(\tau_t\rightarrow\tau'_t\) _with_ \(x_t\in\tau_t\) _before the_ (_t_+1)_-th element is revealed._

Observe that any access sequence _X_ uniquely corresponds to a set _P_ of points in the plane that is a semi-permutation: if we denote _X_=(_x_<sub>1</sub>_,x_<sub>2</sub>_,...,x<sub>m</sub>_), then for each \(1\le i\le m\), we add the point (_x<sub>i</sub>,i_) to _P_. For convenience, we do not distinguish between the input sequence _X_ and the corresponding set _P_ of points.

**Theorem B.4 (Implied by Lemmas 2.1, 2.2 and 2.3 from \[DHI<sup>+</sup>09\])** _There is an (online) algorithm for BST, that, for any access sequence X computes an execution sequence of cost at most O_(|_X_|+_c(X_))_, if and only if there is an (online) algorithm for the_ Min-Sat _problem, that, given any input X, computes a solution Y of cost_ \(|Y|\le c(X)\)_. The running time of the two algorithms are the same up to a constant factor._

We then obtain the following corollary.

