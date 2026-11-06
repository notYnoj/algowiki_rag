## 4.2 Stack Space Reduction

The previous two algorithms utilized an explicit call stack of _O_(l_n_) words to coordinate the processing of subproblems. However, using the static nature of merge boundaries, they can be derived on the fly with little extra information packed in _O_(1) words by the technique from \[5, Appendix A\] (originally used to rebuild subtrees in an array-based scapegoat tree like structure). In this optimization, we utilize this technique to traverse the merging tree (in Definition 1) to coordinate merge operations of the algorithm, maintaining the following information:

• The index of the current node _v_ (according to a 1-indexed binary tree), used to determine if the current node is a left or right child according to the parity of the value.<tbc>

• The subarray boundaries of the current node in _l,r_.<tbc>

• A bitmasked stack D containing the differences in sizes between the children of all ancestor nodes of _v_. One bit is sufficient per entry because Fact 2 implies the difference in size between siblings is either 0 (when parent size is even) or 1 (when parent size is odd). This information is used to deduce the range of sibling nodes, and then parent nodes for backtracking.

**Algorithm 3** Node Class

class Node<br>
procedure Node(n)<br>
  \(v\leftarrow 1,\ell\leftarrow 0,r\leftarrow n,\mathcal{D}\leftarrow 0\triangleright\) Initialize State Variables<br>
   while \(r-\ell>1\) do MoveLeft() \(\triangleright\) Begin Postorder Traversal at Leftmost Leaf<br>
procedure MoveLeft()<br>
  \(\mathcal{D}\leftarrow(\mathcal{D}\checkmark 1)+((r-\ell)\&1)\triangleright\) Push Children Size Difference<br>
  \(v\leftarrow v\checkmark 1\triangleright\) Update Node Index<br>
  \(r\leftarrow\lfloor(\ell+r)/2\rfloor\triangleright\) Update Subarray Boundaries<br>
procedure MoveRight()<br>
  \(\mathcal{D}\leftarrow(\mathcal{D}\checkmark 1)+((r-\ell)\&1)\triangleright\) Push Children Size Difference<br>
  \(v\leftarrow(v\checkmark 1)+1\triangleright\) Update Node Index<br>
  \(\ell\leftarrow\lfloor(\ell+r)/2\rfloor\triangleright\) Update Subarray Boundaries<br>
procedure MovePar()<br>
  \(d\leftarrow\mathcal{D}\&1\triangleright\) Difference in Size from Sibling Node<br>
  \(\mathcal{D}\leftarrow\mathcal{D}\gg 1\triangleright\) Pop from Stack<br>
   if v&1 then \(\ell\leftarrow\ell-(r-\ell-d)\triangleright\) Right Child, Sibling to Left Smaller by d<br>
   else \(r\leftarrow r+(r-\ell+d)\triangleright\) Left Child, Sibling to Right Larger by d<br>
  \(v\leftarrow v\gg 1\triangleright\) Update Node Index<br>
procedure NextPostOrder() \(\triangleright\) Standard Iterative Postorder Traversal Manager<br>
   if v&1 then \(\triangleright\) Right Child: Both Subtrees Completed, Process Parent<br>
MovePar()<br>
   else \(\triangleright\) Left Child: Proceed to Right Sibling’s Subtree<br>
   MovePar() \(\triangleright\) Backtrack<br>
   MoveRight() \(\triangleright\) Move to Right Subtree<br>
   while \(r-\ell>1\) do MoveLeft() \(\triangleright\) Begin at Leftmost Node of Subtree

The MoveLeft and MoveRight methods are trivially correct as they simply follow the static index partitioning logic of the base algorithm. MovePar peeks \(d\leftarrow\mathcal{D}\&1\) to compute the sibling’s size and expand the active interval boundary accordingly. The correctness of restoring parent intervals from D can be shown using the symmetric inversion scheme in \[5, Appendix A\].

