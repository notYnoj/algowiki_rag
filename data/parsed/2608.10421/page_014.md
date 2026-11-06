Let _v,l,r,_D be in some valid initial state. We now show that MovePar restores the state from the left child. In the left child \(\ell\) remains identical, however:

\(r_\mathrm{new}=\lfloor(\ell+r)/2\rfloor=\ell+\lfloor(r-\ell)/2\rfloor\)<br>
\(\mathcal{D}_\mathrm{new}=(\mathcal{D}\checkmark 1)+((r-\ell)\&1)\)

Note that \((\ell+r)\&1\) is equivalent to the difference in size between children. If we call MovePar, the node is a left child ((_v_&1)=0), and the procedure executes the else block, resulting in:

\(r_\mathrm{final}=r_\mathrm{new}+(r_\mathrm{new}-\ell+d)\)<br>
\(=\ell+2\lfloor(r-\ell)/2\rfloor+((r-\ell)\&1)\)<br>
\(=\ell+(r-\ell)=r\)<br>
\(\mathcal{D}_\mathrm{final}=\mathcal{D}_\mathrm{new}\gg 1\)<br>
\(=((\mathcal{D}\checkmark 1)+((r-\ell)\&1))\gg 1\)<br>
\(=\mathcal{D}\)

The original state is restored, hence MovePar correctly backtracks from the left child. By symmetry, a parallel derivation shows MovePar also restores the correct state from the right child.

Using the MoveLeft, MoveRight and MovePar move primitives, we conduct an iterative post-order traversal of the tree (via NextPostOrder) to process subproblems in the correct order without an explicit recursion stack. However, we still need to keep track of the return flags indicating the state of nodes (pure/impure). This is done using another bitmasked stack A containing the return flags of previous left children in the traversal and a single-bit variable _b_ containing the return flag of the previous right child.

**Algorithm 4** Directional Mergesort<sup>+2</sup>

function Sort\((A[],\ell,r,a,b)\triangleright\) _Processing Subarray_ \(A[\ell..r)\)_, Children Returned a,b_

2: **if** \(r-\ell<2\) **then return true**

3: \(m\leftarrow\lfloor(\ell+r)/2\rfloor\)

4: **if** \(A[m-1]\le A[m]\) **then return** \(a\wedge b\triangleright\) _Skip Check_

5: **if** _b_ **then** MergeBw\((A,\ell,m,r)\triangleright\) _Directional Merging_

6: **else** MergeFw\((A,\ell,m,r)\)

7: **return false**

8: **procedure** DirectionalMergesort<sup>+2</sup>(_A_\[]_,n_)

9: \(\mathcal{A}\leftarrow 0,b\leftarrow 0,p\leftarrow\text{new Node}(n)\)

10: **while** _p.v\>_0 **do** \(\triangleright\) _Repeat Until the Tree is Exhausted_

11: \(x\leftarrow\text{Sort}(A,p.\ell,p.r,\mathcal{A}\&1,b)\triangleright\) _Process Current Node_

12: **if** \(p.r-p.\ell>1\) **then** \(\mathcal{A}\leftarrow\mathcal{A}\gg 1\triangleright\) _Dequeue the Consumed Left Return Flag_

13: **if** _p.v_&1 **then** \(b\leftarrow x\triangleright\) _Right Child: Assign to Right Return Variable_

14: **else** \(\mathcal{A}\leftarrow(\mathcal{A}\checkmark 1)+x\triangleright\) _Left Child: Append to Left Returns Stack_

15: _p._NextPostOrder() \(\triangleright\) _Move to Next Node_

Because the parent is always visited immediately after its right child in a postorder traversal, the variable _b_ is guaranteed to hold the return value of the current node’s right child (if one exists). Because the bit stack A contains the return flags of left subtrees along the root to _v_ path ordered by increasing depth, the top of the stack contains the deepest left subtree along the path, which is correctly the current node’s left subtree. Note that the dequeue step is not executed for leaf nodes as they have no left subtree, and thus do not consume entries.

