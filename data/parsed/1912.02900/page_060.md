instance {(}_q_) corresponds to some sub-tree of the partitioning tree _T_, that we denote by _T<sub>q</sub>_. For all \(i\ge 0\), let \(\Lambda'_i\) be the set of all vertices of the tree _R_ that lie at distance exactly _i_ from the root of _R_. We say that the vertices of \(\Lambda'_i\) belong to the _i_th layer of _R_. Notice that, if vertex _q_ lies in the _i_th layer of _R_, then the height of the corresponding tree _T<sub>q</sub>_ is bounded by \(H\cdot(2/3)^i\) (the constant 2/3 is somewhat arbitrary and is used because, when a tree \(T'\) is split in its middle layer, each of the resulting subtrees has height at most \(\lfloor\text{height}(T')/2\rfloor+1\le 2H/3\)). Recall that the recursion terminates once we obtain instances whose corresponding partitioning trees have height 1. It is then easy to verify that the height of the recursion tree _R_ is bounded by _O_(loglog_n_).

Consider now some layer \(\Lambda_i\) of the recursion tree _R_. We let T_<sub>i</sub>_ be the collection of all sub-trees of the partitioning tree _T_ corresponding to the vertices of \(\Lambda_i\), so \(\mathcal{T}_i=\{T_q|q\in\Lambda_i\}\). Recall that all trees in T_<sub>i</sub>_ have height at most \(H\cdot(2/3)^i\).

Notice that T<sub>0</sub>={_T_}. Let _U_={_v_<sub>1</sub>_,...,v<sub>k</sub>_} be the middle layer of _T_. Then T<sub>1</sub>={_T_<sub>_v_<sub>1</sub></sub>_,...,T<sub>v<sub>k</sub></sub>,T<sub>r</sub>_}. Set T<sub>2</sub> is similarly obtained by subdividing every tree in T<sub>1</sub>, and so on. (See Figure 10 for an illustration. ) The construction of the tree sets T_<sub>i</sub>_ can be described using the following process:

• Start from T<sub>0</sub>={_T_}.<tbc>

• For _i_=1_,...,D_, if some tree in T<sub>_i_-1</sub> has height greater than 1, then construct the set T_<sub>i</sub>_ of trees as follows: For every tree \(T'\in\mathcal{T}_i\) whose height is greater than 1, split \(T'\) at the middle layer \(U_{T^\prime}\subseteq V(T')\). For every vertex \(v\in U_{t^\prime}\), we then obtain a sub-tree of \(T'\) rooted at _v_, that is added to T_<sub>i</sub>_ - this tree corresponds to a strip instance. Additionally, we obtain a sub-tree of \(T'\) rooted at the root of \(T'\), whose leaves are the vertices of \(U_{t^\prime}\), that we also add to T_<sub>i</sub>_ - this tree corresponds to the compressed instance.

The following observation is immediate.

**Observation 7.1** _For each_ \(1\le i\le D\), \(\bigcup_{T^\prime\in\mathcal{T}_i}V(T')=V(T)\)_, and for each pair_ \(T',T''\in\mathcal{T}_i\) _of trees, either_ \(V(T')\cap V(T'')=\emptyset\) _or the root of one of these trees is a leaf of the other tree._

To
T1
T2

Figure 10: An illustration of the families T_<sub>i</sub>_. Notice that T<sub>1</sub> contains 5 trees, each having height 2.

