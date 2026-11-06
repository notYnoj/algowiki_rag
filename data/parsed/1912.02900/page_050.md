<tbc>_height_ of the tree _T_, denoted by height(_T_), is the largest index _i_ such that \(\Lambda_i\neq\emptyset\). If the height of the tree _T_ is _h_, then we call the set \(\Lambda_{\lceil h/2\rceil}\) of vertices the _middle layer_ of _T_. Notice that, if _T_ is a balanced partitioning tree for input _X_, then its height is at most 2log_c(X_).

Our algorithm takes as input a set _X_ of points that is a semi-permutation, a balanced partition tree _T_ for _X_, and an integral parameter \(\rho>0\).

Intuitively, the algorithm uses the splitting operation to partition the instance _X_ into subinstances that are then solved recursively, until it obtains a collection of instances whose corresponding partitioning trees have height at most \(\rho\). We then either employ dynamic programming, or use a trivial _O_(log_c(X_))-approximation algorithm. The algorithm returns a special feasible solution for the instance. Recall that the height of the tree _T_ is bounded by \(2logc(X)\le 2logn\).

The following two theorems will be used as the recursion basis.

**Theorem 6.6** _There is an algorithm called_ LeafBST-1 _that, given a semi-permutation instance X of_ Min-Sat _in reduced form, and a partitioning tree T for it, produces a feasible T-special solution for X of cost at most_ 2|_X_|+2OPT(_X), in time_ \(|X|^{O(1)}\cdot c(X)^{O(c(X))}\).

**Theorem 6.7** _There is an algorithm called_ LeafBST-2 _that, given a semi-permutation instance X of_ Min-Sat _in reduced form, and a partitioning tree T for it, produces a feasible T-special solution of cost at most_ 2|_X_|height(_T), in time_ poly(|_X_|).

The proofs of both theorems are deferred to the next two subsections, after we complete the proof of Theorem 1.3 using them. We now provide a schematic description of our algorithm. Depending on the guarantees that we would like to achieve, whenever the algorithm calls procedure LeafBST, it will call either procedure LeafBST-1 or procedure LeafBST-2; we specify this later.

\(\text{RecursiveBST}(X,T,\rho)\)

1. Keep removing redundant points from _X_ until _X_ is in reduced form.<tbc>

2. IF _T_ has height at most \(\rho\),<tbc>

3. **return** LeafBST(_X,T_)<tbc>

4. Let _U_ be the set of vertices lying in the middle middle layer of _T_.<tbc>

5. Compute the split \((X^c,\{X_v^s\}_{v\in U})\) of (_X,T_) at _U_.<tbc>

6. Compute the corresponding sub-trees \((T^c,\{T_v^s\}_{v\in U})\) of _T_.<tbc>

7. For each vertex \(v\in U\), call to RecursiveBST with input \((X_v^s,T_v^s,\rho)\), and let _Y<sub>v</sub>_ be the solution returned by it.<tbc>

8. Call RecursiveBST with input \((X^c,T^c,\rho)\), and let \(\hat{Y}\) be the solution returned by it.<tbc>

9. Let _Z_ be a point set containing, for each vertex \(v\in U\), for each point \(p\in X_v^s\), two copies \(p'\) and \(p''\) of _p_ with \(p'.y=p''.y=p.y\), where \(p'\) lies on the left boundary of _S(v_), and \(p''\) lies on the right boundary of _S(v_).<tbc>

10. **return** \(Y^*=Z\cup\hat{Y}\cup(\bigcup_{v\in U}Y_v)\)

