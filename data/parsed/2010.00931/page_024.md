nodes. In Line 3 the branching nodes _x_<sub>1</sub>_,...,x<sub>k</sub>_ on the search path are found, indexed from the root towards _x_. Then, in Lines 5-6, from bottom-to-top, each branching node _x<sub>i</sub>_ is splayed up, until it becomes the child of its nearest branching ancestor _x_<sub>_i_-1</sub> (or it becomes the root, in case of _x_<sub>1</sub>). By Lemma 15, splay(_x<sub>i</sub>,x_<sub>_i_-1</sub>) creates no new branching nodes on the search path of _x_, and afterwards, _x<sub>i</sub>_ is no longer a branching node. As such, the search path of _x_ after the first phase contains no branching nodes, and by Lemma 14, the tree remains Steiner-closed. In the second phase (Line 7), node _x_ is splayed all the way to the root on the transformed search path. Again, by Lemma 14, the tree remains Steiner-closed.

**Algorithm 4.** SplayTT search operation

Input: Search tree T on S. Node x to be searched.<br>
procedure search(x)<br>
Follow search path in T from root to x.<br>
Identify branching nodes x<sub>1</sub>,...,x<sub>k</sub> on the search path of x. \(\triangleright\) (phase 1)<br>
Let x<sub>0</sub>=null.<br>
for i=k,...,1 do<br>
splay<br>
(<br>
_x<sub>i</sub>,x_<br>
<sub>_i_-1</sub><br>
)<br>
splay<br>
(<br>
_x,null_<br>
)<br>
\(\triangleright\) (phase 2)

Note that the search path of _x_ after phase 1 is a subset of the initial search path, in particular it contains the previously branching nodes _x_<sub>1</sub>_,...,x<sub>k</sub>_. We illustrate the operation of SplayTT with an example in Figure 7.

As both phases involve a single pass through the search path, the entire process can be implemented in time linear in the length of the search path. The ZIG, ZIG-ZIG, and ZIG-ZAG steps take a constant number of rotations and oracle calls, the splaying in both phases thus clearly takes linear overall time. To find the branching nodes of the search path _P_ (Line 3), we calculate the boundary sizes of the search path nodes as in Section 4.1, and identify the branching nodes using the characterization in Lemma 13. Note that, in the spirit of self-adjusting structures, the algorithm does not need to know the global structure of _S_, and does not require persistent book-keeping between searches.

