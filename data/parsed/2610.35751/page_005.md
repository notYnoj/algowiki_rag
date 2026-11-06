<tbc>the in-neighbor that triggers the insertion of _r_ into the candidate queue during the expansion of _v_. After the search, we count the frequency distribution of all retrieved nodes across different cosine values \(cos(\phi)\), as shown in Figure 5. From Figure 5, we make the following key observation:

<u>_Pareto-Angle Locality_</u>. Retrieved nodes exhibit strong locality in the Pareto angle space, where high-frequency Pareto angle regions form contiguous intervals. For instance, when \(\alpha=0.1\), nodes with higher retrieval frequency are mainly distributed in the range of \(cos(\phi)\in[0.2,0.4]\).

**Intuition.** Based on the observation, it is unnecessary for each neighbor to be compared against all other neighbors when computing its active range. Instead, comparisons should be restricted to neighbors with small differences in Pareto angle values. This is because such neighbors are more likely to be jointly retrieved under a given preference parameter \(\alpha\), and hence jointly participate in forming triangles with the target node during graph traversal.

## 4.2 Active Range Computation Based on Pareto Angle Difference

Based on the above intuition, we propose an <u>angle</u>-constrained <u>active</u> <u>range</u> computation algorithm, _ACAR_, which leverages the Pareto angle constraint to avoid unnecessary distance computations. The core idea of ACAR is that, for any two candidate neighbors _e_ and _f_ of a node _v_, if both are retrieved during the search under a given \(\alpha\), the absolute difference between their Pareto angles, i.e., \(|\phi(v,e)-\phi(v,f)|\), should be constrained in a scope.

Specifically, when computing the active ranges of a node’s candidate neighbors, ACAR employs different strategies for candidates in the first Pareto-frontier layer and those in the remaining layers, as shown in Algorithm 2. This is because nodes in the first layer are more likely to lie on the exact Pareto frontier, and thus require more precise active range computation.

<u>_(1) The First Layer_</u>. In DEG, the first traversed node is assigned an active range of \[0,1\] simply because the neighbor set _NS_ is initially empty, which is clearly inaccurate. More importantly, the active range computation for nodes in the remaining layers depends on the active ranges of nodes in the first layer, making the accuracy of the first-layer active ranges crucial. To address this, ACAR employs a bidirectional two-stage scan over the first-layer candidate neighbors to compute more accurate active ranges. Specifically, in the first- stage scan, ACAR traverses the first-layer candidate neighbors in forward order to obtain the most reliable active ranges of the final retained node in _NS_ (line 4). After completing the forward scan, we perform a reverse scan with the same pruning operations (line 5), refining the active ranges of the first-layer neighbors.

<u>_(2) The Remaining Layers_</u>. Since the proportion of candidate neighbors in the first layer is relatively small (only 4.53% on the OI dataset), the majority of the computational cost during the AR computation is incurred by computing the active ranges of candidate neighbors in the remaining layers. When computing the active ranges of each neighbor, DEG compares it with all nodes currently retained in _NS_, which leads to substantial computational overhead. To address this, inspired by the observation in Section 4.1, ACAR leverages a Pareto angle threshold \(\theta_{th}\in[0,\frac{\pi}{2}]\) (see line 10)<tbc>

Input: Candidate set C={PF<sup>1</sup>,...,PF<sup>l</sup>} organized in a two-level order, maximum number of edges R, threshold \(\tau\) to prune edges with small active ranges, and angular threshold \(\theta_{th}\in[0,\frac{\pi}{2}]\)<br>
Output: Neighbor set NS<br>
   \(NS\leftarrow\emptyset\);<br>
  // Retained nodes<br>
   foreach PFi\(\in C\) do<br>
   if i=1 then<br>
//<br>
The<br>
first<br>
layer<br>
layer<br>
   Compute<br>
active<br>
ranges<br>
of<br>
each<br>
node<br>
in<br>
PF<br>
<sup>1</sup><br>
in<br>
forward<br>
order<br>
;<br>
   Compute<br>
active<br>
ranges<br>
of<br>
each<br>
node<br>
in<br>
PF<br>
<sup>1</sup><br>
in<br>
reverse<br>
order<br>;<br>
   else<br>
//<br>
The<br>
remaining<br>
layers<br>
   foreach \(p\in PFi\) do<br>
   \(ar_p^-\leftarrow\emptyset\);<br>
  //<br>
The<br>
pruning<br>
range<br>
   foreach \(w\in NS\) do<br>
   if \(|\phi(v,p)-\phi(v,w)|\le\theta_{th}\) then<br>
   compute<br>
pruning<br>
range<br>
of<br>
_p_<br>
induced<br>
by<br>
\(w,ar_p^{^\prime-}\)<br>
;<br>
   \(ar_p^-\leftarrow ar_p^-\cup ar_p^{^\prime-}\);<br>
   \(ar_p^-\leftarrow[0,1]\backslash ar_p^-\);<br>
  //<br>
The<br>
active<br>
range<br>
   if \(|ar_p|\ge\tau\) then<br>
\(NS\leftarrow NS\cup\{p\}\)<br>
;<br>
   if \(|NS|\ge R\) then<br>
break<br>
;<br>
return<br>
_NS_<br>
;

<tbc>to skip distance computations with a subset of nodes that violate the angular constraint, thereby improving the efficiency of active range computation. It is worth noting that the angular-constraint computation (line 10) derived from Eq. (2) incurs much lower cost than the pruning range computation (line 11). This is because the distance values required for Pareto-angle computation, i.e., \(\delta_x\) and \(\delta_y\), are already maintained during candidate construction and can be accessed directly without additional distance evaluations.

**Example 2:** Figure 6 illustrates how to compute the active ranges of candidate neighbors for node _v_. For the candidate neighbors in the first layer, ACAR traverses them in forward order (e.g., the _x_-dimension), proceeding from node _a_ to node _e_, as shown in Figure 6a<tbc>

<tbc>1.<br>
Through this traversal, ACAR computes the active ranges of node _e_ and inserts it into the neighbor set _NS_. Subsequently, ACAR traverses the remaining candidates of the first layer in reverse order to compute their active ranges, proceeding from node _d_ back to node _a_, as illustrated in Figure 6a<tbc>

<tbc>2. For candidate neighbors in the remaining layers, we take node _f_ as an example, as shown in Figure 6b. At this point, nodes _a_, _b_, _c_, and _e_ remain in the current neighbor set _NS_, while node _d_ has been pruned. ACAR compares node _f_ with all nodes in _NS_ that satisfy the angle constraint. For instance, for node _a_, ACAR computes \(|\phi(v,a)-\phi(v,f)|\). If \(|\phi(v,a)-\phi(v,f)|\le\theta_{th}\), ACAR computes the pruning range induced by _a_, otherwise, the computation is skipped. \(\sqcap\sqcup\)

## 4.3 Discussion

**Applicability.** ACAR is specifically designed for DVQ, where each object is associated with exactly two attribute vectors. Extending<tbc>

**Algorithm 2:** ACAR(_C,R,_\(\tau\),\(\theta_{th}\))

