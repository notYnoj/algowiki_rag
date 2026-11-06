<tbc>a minimum _pu_-cut (_S<sub>p,u</sub>,S<sub>u,p</sub>_). Each node _u_ is then reassigned to a set \(S_{u^\prime,p}\) containing _u_, where nodes reassigned to the same \(S_{u^\prime,p}\) are grouped together. This partition satisfies that its biggest part is of expected size at most \(\frac{3}{4}n\), while preserving property (\*) below. This allows the algorithm to continue recursively with an _O_(log_n_) bound on the recursion-tree depth.

(\*) For every pair \(s'\in S_{i,p},t'\in S_{j,p}\) for \(i\neq j\), at least one of (_S<sub>i,p</sub>,S<sub>p,i</sub>_) or (_S<sub>j,p</sub>,S<sub>p,j</sub>_) corresponds in _G_ to a \((1+\varepsilon)\)-approximate minimum \(s't'\)-cut.

Crucially, property (\*) ensures that the Max-Flow values between node pairs of different sets are determined at the current recursion step, i.e. one of the minimum cuts computed from _p_ captures the (approximated) value of Max-Flow(_u,v_), while handling the remaining pairs is postponed to a later stage.

## Barriers in adapting \[AKT20a\]

While symmetry holds in our case of undirected graphs with unit node-capacities, the same intuition is not directly applicable due to two main issues.

First, the triangle inequality 1.1 does not generally hold. This is illustrated by the example of nodes _p,u,v_ satisfying \(v\in C_{p,u}\) or \(u\in C_{p,v}\), where _C<sub>p,v</sub>_ is the separator in a minimum vertex _pv_-cut. This makes the presence of nodes in separators of many pairs an issue, as their own Max-Flow to other nodes might remain undetermined for most pivot choices _p_ and through multiple recursion depths, resulting in no cuts for them.

Second, and even if the first issue is resolved, the pivot _p_ itself could be present in optimal vertex _uv_-separators. This means that even when the minimum _pu_-cut separates a pair _v,u_, it might do so in a sub-optimal way that must not include the pivot _p_ in _C<sub>u,v</sub>_, and we would not have any indication for it. Moreover, there might not be any pivot choice that is absent from all separators, making the situation worse. To address these issues, we first provide an overview of a Monte Carlo version of our algorithm, to be followed by the necessary changes to achieve a Las Vegas algorithm.

## Overcoming barriers in \[AKT20a\]: A Monte Carlo algorithm

Despite the issues mentioned, the underlying intuition is applicable in our setting, and the shared symmetry property turns out to be enough to recover an \(\tilde{O}(m^2)\) running time. Our algorithm uses a similar framework as in \[AKT20a\], which involves a node partition inspired by minimum cuts from a random pivot and recursion. However, we introduce reinforcements in the form of additional Max-Flow queries to address the issues described. The main challenge is to ensure that the total number of additional queries does not exceed \(\tilde{O}(m)\), thus maintaining the total time complexity of \(\hat{O}(m^2)\) using the almost linear time algorithm for Max-Flow \[CKL<sup>+</sup>22, vdBCP<sup>+</sup>23\], as required.

To address the first issue, we implement the following changes. When a uniformly random node \(p\in V'\) is selected, in addition to the Max-Flow calls to all nodes \(u\in V'\backslash\{p\}\), we also directly query the Max-Flow between every node _q_ in the separator _C<sub>p,u</sub>_, and _u_. Recall that in our setting, it holds that \(|C_{p,u}|\le d_G(u)\) where _d<sub>G</sub>(u_) is the degree of node _u_ in the input graph _G_, and therefore the total number of additional queries for \(V'\) is at most the sum of node degrees in \(V'\). Since the node sets \(V'\) in any depth of the recursion are disjoint, the total number of extra queries is \(\tilde{O}(m)\).

To address the second issue, it is important to note that node pairs with a large separator, that is where both nodes have high degrees, are the most problematic in this context. Therefore, we would like to adopt a similar high degree/low degree approach to the one taken previously in \[AKT20b, HLSW23\]; solving Max-Flow between all pairs of high degree nodes, and letting the "main" algorithm handle the remaining pairs.

However, there are a few challenges involved in doing so. First, simply querying all pairwise nodes of high degree is not sufficient for our needs. This is because our requirement is exceptionally<tbc>

