Using \(s_\#\le 2s'_\#\) yields the final bound for size(_n_leaf)

\(size\left(n_\text{leaf}\right)\le 2e+1\) (A.3)

This bound is critical in proving the existence of a scapegoat node, shown shortly. We will first describe the procedure for dynamic rebalancing on a full gap _L<sub>i</sub>_:

Firstly, initialize the procedure. We use the variables: _j_ to denote the current node in the traversal is _n<sub>j</sub>_, _z_ to denote the size of the node _n<sub>j</sub>_, and variables \(z'_1\) and \(z'_2\) to denote the size of the child nodes of _n<sub>j</sub>_, where \(z'_1\) and \(z'_2\) can correspond to any child. We begin at the leaf node _n<sub>j</sub>_ that corresponds to the full gap _L<sub>i</sub>_, so \(j=i+s'_\#-1\) and _z_=8.

Secondly, traverse to the parent of the current node _n<sub>j</sub>_. Set \(z'_1:=z=size\left(n_j\right)\), and \(z'_2:=size\left(n_{j\oplus 1}\right)\). To find \(size\left(n_{j\oplus 1}\right)\), first set \(z'_2:=0\), then use the general formula to find the range \(L_\ell\dots L_r\) covered by \(n_{j\oplus 1}\), and iterate through all gaps in \(L_\ell\dots L_r\), where for each gap a linear scan from \(\ell_2\) counts the number of active representatives in the gap and adds it to \(z'_2\) (similar to during resizes, but without exchanging active representatives). This process requires \(size\left(n_{j\oplus 1}\right)=z'_2\) comparisons. Lastly, set \(j:=\lfloor j/2\rfloor\), moving the current node marker to the parent of the current node, then \(\{z'_1,z'_2\}=\{size\left(n_{2j}\right),size\left(n_{2j+1}\right)\}\), which are correctly the size of the two children of _n<sub>j</sub>_. As _n<sub>j</sub>_ covers the union of the ranges of its children, calculate \(z:=z'_1+z'_2\). This moves the current node to its parent node whilst maintaining the correctness of all variables.

Thirdly, verify if the current node _n<sub>j</sub>_ obeys the requirement

\(|size\left(n_{2j}\right)-size\left(n_{2j+1}\right)|>max\left(1,size\left(n_j\right)/lgs'_\#\right)\) (A.4)

Here we do not need to recompute the sizes of the nodes, as they are already computed and stored in _z_, \(z'_1\) and \(z'_2\). As size(_n_<sub>2_j_</sub>) and size(_n_<sub>2_j_+1</sub>) are interchangeable in (A.4), the lack of differentiation between the left and right children of _n<sub>j</sub>_ in \(z'_1\) and \(z'_2\) does not matter. If the requirements are met, _n<sub>j</sub>_ is the scapegoat node, and we rebuild the subtree rooted at the _n<sub>j</sub>_, distributing active representatives under _n<sub>j</sub>_ as evenly as possible, then terminate. Otherwise, return to step 2 and continue traversing upwards the tree.

Given that _L<sub>i</sub>_ is full, a scapegoat node that obeys these requirements must exist. Condition (A.4) is the negation of the invariant (A.1); a node that violates (A.1) satisfies (A.4). By (A.3), if all ancestors of _L<sub>i</sub>_ obey the invariant (A.1), the size of _L<sub>i</sub>_ is at most 2_e_+1. However, as _L<sub>i</sub>_ is full with 8_\>_2_e_+1 active representatives, we have a contradiction, and thus there must exist an ancestor that disobeys the invariant (A.1) and thus obeys (A.4).

## A.4 Rebuilding

The process for rebuilding the subtree rooted at the scapegoat node _n<sub>j</sub>_ covering the range \(L_\ell\dots L_r\) with _z_=size(_n<sub>j</sub>_) involves the following:

Firstly, by a linear scan of \(L_\ell\dots L_r\) identical to the scan in resizing, exchange all active representatives to a contiguous block _a_<sub>1</sub>_...a<sub>z</sub>_ at the front of _D_. Now the region \(L_\ell\dots L_r\) is composed entirely of buffer representatives.

Secondly, replace the active representatives into \(L_\ell\dots L_r\). For all gaps \(L_k\in L_\ell\dots L_r\) with the corresponding leaf node \(n_{k^\prime}\) (where \(k'=k+s'_\#-1\)) under _n<sub>j</sub>_, determine the active representatives \(a_{l^\prime}\dots a_{r^\prime}\) that should be in _L<sub>k</sub>_, and exchange them into the first \(r'-l'+1\) positions of _L<sub>k</sub>_. We cannot simply distribute them naively in the manner of [2] as the invariant (A.1) is based off weight instead of density which may remain violated even after a naive redistribution, thus we define \(a_{l^\prime}\dots a_{r^\prime}\) for all nodes in the subtree as follows:

The scapegoat node _n<sub>j</sub>_ trivially covers all active representatives _a_<sub>1</sub>_...a<sub>z</sub>_. For a node with current range \(a_{l^\prime}\dots a_{r^\prime}\), distribute the left half \(a_{l^\prime}\dots a_{\lfloor(l^\prime+r^\prime)/2\rfloor}\) to the left subtree

