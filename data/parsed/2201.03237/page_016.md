neighbors. The value of _K_ ranges from hundreds to thousands. The TBSG combines the both and adopts our edge selection strategy to select neighbors to approximate a (_r,p_)-MSNET.

## 2.4.1. Cover Tree

Cover Tree, proposed by Beygelzimer et al.[28], is a data structure used for exact nearest neighbor search. It recursively divides a spherical space into several smaller spherical spaces, each with a vector as the center, and the radius of the sphere decreases exponentially with the depth of the tree. Izbicki et al.[27] simplified the Cover Tree structure to make the number of nodes in the tree exactly equal to size of dataset, which is also the Cover Tree used in this paper.

We present a two-dimensional Cover Tree example in Figure 6. To construct a Cover Tree, first we select a node _e<sub>root</sub>_ as the root node, and then we insert other nodes into the Cover Tree. To insert a new node, we start from _e<sub>root</sub>_ and search for the node _e<sub>child</sub>_ that is closest to the inserted node among the children of _e<sub>root</sub>_. If the inserted node is in the sphere space of the node _e<sub>child</sub>_, then insert into the subtree of _e<sub>child</sub>_ recursively. Otherwise, add a new subtree of _e<sub>root</sub>_ with the inserted node as root.

B
E
D
K
U
M
A
I
G
H
J

Figure 6: A toy example of Cover Tree in two dimensional space.

