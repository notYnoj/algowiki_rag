and the right half \(a_{\lfloor(l^\prime+r^\prime)/2\rfloor+1}\dots a_{r^\prime}\) to the right subtree. Rearranging, the left subtree receives \(\lfloor(r'-l')/2\rfloor+1\) active representatives and the right subtree \(\lceil(r'-l')/2\rceil\) active representatives. From the property \(0\le\lfloor(r'-l')/2\rfloor+1-\lceil(r'-l')/2\rceil\le 1\) for all positive integers \(l\le r\), for any node _n<sub>k</sub>_ in the rebuilt subtree \(0\le\mathrm{size}(n_{2k})-\mathrm{size}(n_{2k+1})\le 1\), spreading active representatives as evenly as possible, which guarantees the invariant (A.1) is upheld in the rebuilt subtree. To calculate the suitable range for all leaf nodes, we are unable to use the recursive method in \[3\] as it requires a recursion stack of _O_(lg_z_) words. Instead, we utilize a more complex method that requires a stack _K_ of only _O_(lg_z_) bits.

Start by initializing \(l'=1\), \(r'=z\) and \(j'=j\) to denote the current node in the traversal is the scapegoat node _n<sub>j</sub>_ which should have all the collected active representatives _a_<sub>1</sub>_...a<sub>z</sub>_ under it. _K_ is initially empty. We now describe three move primitives to move the current node \(n_{j^\prime}\) to the left child, right child, and parent node whilst updating the variables \(l'\) and \(r'\) correctly. We assume that \(j'\), \(l'\), \(r'\) and _K_ are stored in some scope such that they are accessible in the procedures.

The procedure to move to the left child pushes \(\lfloor(r'-l')/2\rfloor+1-\lceil(r'-l')/2\rceil\) into _K_, then sets \(r':=\lfloor(l'+r')/2\rfloor\) and \(j':=2j'\).

The procedure to move to the right child pushes \(\lfloor(r'-l')/2\rfloor+1-\lceil(r'-l')/2\rceil\) into _K_, then sets \(l':=\lfloor(l'+r')/2\rfloor+1\) and \(j':=2j'+1\).

The procedure to move to the parent first reads the top of _K_ and stores it in a variable _d_, and pops the top of _K_. Then, if \(n'_j\) is a left child, which is the case when \(j'\) is even, set \(r':=r'+(r'-l'+1-d)\). Otherwise, \(n'_j\) is a right child and set \(l':=l'-(r'-l'+1+d)\). Lastly, set \(j':=\lfloor j'/2\rfloor\) regardless of which side \(n'_j\) is on.

In the stack, we store the difference in sizes of the two child nodes for every ancestor of the current node \(n_{j^\prime}\) up to the scapegoat node _n<sub>j</sub>_. As \(0\le\lfloor(r'-l')/2\rfloor+1-\lceil(r'-l')/2\rceil\le 1\), this value is either 0 or 1, which can be represented using one bit. Since the height of the subtree rooted at _n<sub>j</sub>_ is \(\mathrm{lg}s'_\#-\lfloor\mathrm{lg}j\rfloor\le\mathrm{lg}m\), the entire stack fits in a single word of at least lg_m_ bits.

Trivially, the procedures to move to the left child and right child give us the correct values \(l'\) and \(r'\) as they simply follow the definitions of \(l'\) and \(r'\). Using the stored difference in sizes and the property that the left child is always larger as \(\lfloor(r'-l')/2\rfloor+1\ge\lceil(r'-l')/2\rceil\), we can determine the range of active representatives distributed to the sibling node from the current node, and as the parent node contains the union of its children, this also allows us to determine the range of active representatives distributed to the parent node.

We now show that moving to the parent correctly reverses moving to a child. We start by assuming the variables \(j'=j'_i\), \(l'=l'_i\) and \(r'=r'_i\) are in some arbitrary valid state. After we move to the left child, \(j'=2j'_i\), \(l'=l'_i\), \(r'=l'_i+\lfloor(r'_i-l'_i)/2\rfloor\), and we have \(\lfloor(r'_i-l'_i)/2\rfloor+1-\lceil(r'_i-l'_i)/2\rceil\) at the top of the stack. Then, if we move back to the parent, \(j'=\lfloor 2j'_i/2\rfloor=j'_i\), \(l'=l'_i\), and

\(r'=l'_i+\lfloor(r'_i-l'_i)/2\rfloor\)<br> \(+(l'_i+\lfloor(r'_i-l'_i)/2\rfloor-l'_i+1-(\lfloor(r'_i-l'_i)/2\rfloor+1-\lceil(r'_i-l'_i)/2\rceil))\)

Cancelling out complementary terms

\(r'=l'_i+\lfloor(r'_i-l'_i)/2\rfloor+\lceil(r'_i-l'_i)/2\rceil\)

Using \(\lfloor(r'_i-l'_i)/2\rfloor+\lceil(r'_i-l'_i)/2\rceil=r'_i-l'_i\) for all \(r'_i-l'_i\in\mathbb{Z}\), we obtain

\(r'=r'_i\)

