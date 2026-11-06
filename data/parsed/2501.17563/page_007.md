<tbc>weighted depth of 10, and depths: \[1,0,3,2,1\]. Indeed: in this case, we are dealing with a binary search tree (BST). Note that _w_<sub>3</sub>=0, so we put it at the bottom, and we need to find the best BST over weights _w_<sub>1,2,4,5</sub>=\[3,2,2,3\]. Thanks to symmetry, there are only three candidate options (other options are worse), see the dashed box in Figure 2: (a) The root has weight 2, with two children of weight 3: then the weighted depth is \([3,2,2,3]\cdot[1,0,2,1]=10\). (b) The root and its child have a weight of 3: then the weighted depth is \([3,2,2,3]\cdot[0,2,3,1]=13\). (c) The root has weight 3, its child has weight 2 and it is not its neighbor in the topology: then the weighted depth is \([3,2,2,3]\cdot[0,2,1,2]=12\).

Finally, the case analysis. We show that the best weighted depth of an STT is 30 (there are multiple STTs that attain it). This will conclude the proof, since we already determined that the weighted depth of _P_ is 29.5. See also Figure 2.

1. Consider an STT rooted at 3: it divides the next search on _U_ to three separate 2-node components (its legs). While there is a total of 8 such STTs, there is a single dominating STT such that we root each subtree by the heavier node, which is a leaf in _U_. Overall, the weighted depth of this best tree is \(w\cdot[1,2,0,2,1,2,1]=3+4+0+4+3+6+10=30\).<tbc>

2. Consider an STT rooted at a mid-node: Then its adjacent leaf is a direct child of the root, and the other subtree is a BST on a path of 5 nodes. Because all the legs are such that the mid- node is heavier than its corresponding leaf, and because the leg of (6,7) is strictly heaviest, the best such STT must be rooted at 6. The remaining subtree is therefore a BST over the path of nodes 1 to 5. We found earlier the best BST over this path. Therefore, adding +1 to the depth of each node in this BST due to it being a subtree, we get that the weighted depth of the best tree rooted in a mid-node is \(w\cdot[2,1,4,3,2,0,1]=6+2+0+6+6+0+10=30\).<tbc>

10
3
2
0
2
3
3
0
1
10
3
10
3
0
3
2
3
2
3
10
2
3
2
0
2
3
b
3
10
2
3
2
3
3
3
3
2
0
2
3
10
3
2
0
2
3
C
10
10
3
2
3
3
2
0
2
3
3
2
0
2
3
2
0
3
b
C
3
2
3
3
3
3
2
2
2
2
2
2
3
0
0
0

Figure 2: Visualization of the case analysis in proving Theorem 2.2. The blue nodes emphasize the heaviest leg, weights are written within the nodes, and the shapes emphasize the type of each node in the topology: center (triangle), mid-node (square), leaf (circle). A dashed ellipse indicates that the STT for this component is undetermined, yet. The numbers and letters within the arrows correspond to the cases of the proof. Green arrows lead to an STT that minimizes the LP among STTs, gray arrows lead to sub-optimal solutions.

