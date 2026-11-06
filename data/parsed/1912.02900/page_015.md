_The strong WB-1 bound of X is_ \(\mathsf{WB}(X)=\mathrm{max}_\sigma\mathsf{WB}_\sigma(X)\)_, where the maximum is taken over all permutations_ \(\sigma\) _of the lines in_ L.

It is well known that the WB-1 bound is a lower bound on the optimal solution cost:

**Claim 2.9** _For any semi-permutation X,_ \(\mathsf{WB}(X)\le 2\cdot\mathsf{OPT}(X)\).

The original proof of this fact is due to Wilber \[Wil89\], which was later presented in the geometric view by Demaine et al. \[DHI<sup>+</sup>09\], via the notion of _independent rectangles_. In Appendix C.6, we give a simple self-contained proof of this claim.

Combining Claims 2.6 and 2.9, we obtain the following immediate corollary.

**Corollary 2.10** _For any semi-permutation X,_ \(\mathsf{WB}(X)\le O(r(X)\mathrm{log}c(X))\).

## 3 Geometric Decomposition Theorems

In this section, we develop several technical tools that will allow us to decompose a given instance into a number of sub-instances. We then analyze the optimal solution costs and the Wilber bound values for the resulting subinstances. We start by introducing a _split operation_ of a given instance into subinstances in Section 3.1. In Section 3.2, we present a decomposition property of the optimal solution cost, which will be used in our algorithms. Finally, in Section 3.3, we discuss the decomposition of the strong WB-1 bound, that our negative results rely on.

### 3.1 Split Instances

Consider a semi-permutation _X_ and its partitioning tree _T_. Let \(U\subseteq V(T)\) be a collection of vertices of the tree _T_, such that the strips \(\{S(v)\}_{v\in U}\) partition the bounding box. In other words, every root-to-leaf path in _T_ must contain exactly one vertex of _U_. For instance, _U_ may contain all vertices whose distance from the root of the tree _T_ is the same. We now define splitting an instance _X_ via the set _U_ of vertices of _T_.

**Definition 3.1 (A Split)** _A_ split _of_ (_X,T_) _at U is a collection of instances_ \(\{X^c,\{X_v^s\}_{v\in U}\}\)_, defined as follows._

• _For each vertex_ \(v\in U\)_, instance_ \(X_v^s\) _is called a_ **strip instance**_, and it contains all points of X that lie in the interior of the strip S(v)._<tbc>

• _Instance X<sup>c</sup> is called a_ **compressed instance**_, and it is obtained from X by collapsing, for every vertex_ \(v\in U\)_, all active columns in the strip S(v_) _into a single column._

We also partition the tree _T_ into sub-trees that correspond to the new instances: for every vertex \(v\in U\), we let _T<sub>v</sub>_ be the sub-tree of _T_ rooted at _v_. Observe that _T<sub>v</sub>_ is a partitioning tree for instance \(X_v^s\). The tree _T<sup>c</sup>_ is obtained from _T_ by deleting from it, for all \(v\in U\), all vertices of _V(T<sub>v</sub>_)\\{_v_}. It is easy to verify that _T<sup>c</sup>_ is a valid partitioning tree for instance _X<sup>c</sup>_. The following lemma lists several basic properties of a split. Recall that, given an instance _X_, _r(X_) and _c(X_) denote the number of active rows and active columns in _X_, respectively.

