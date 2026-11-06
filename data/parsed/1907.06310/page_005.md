<tbc>by this search. If _x_ is not `null` then the algorithm repeatedly applies a splay step until _x_ becomes the root. A splay step has one of three forms. If the parent of _x_ is the root then rotate at _x_. (This case is always terminal.) Otherwise, if _x_ is a left child and its parent is a right child, or vice-versa, rotate at _x_ twice. Otherwise, rotate at the parent of _x_, and then rotate at _x_. Sleator and Tarjan assigned the respective names _zig_, _zig-zag_ and _zig-zig_ to these three cases \[61\]. The series of splay steps that bring _x_ to the root are collectively called splaying at _x_, or simply splaying _x_. If _X_=(_x_<sub>1</sub>_,...,x<sub>m</sub>_) is a sequence of requested keys in _T_ then the cost of splaying _X_ starting from _T_ is \(\sum_{i=1}^md_{T_{i-1}}(x_i)\), where _T_<sub>0</sub>=_T_ and _T<sub>i</sub>_ is the result of splaying _x<sub>i</sub>_ in _T_<sub>_i_-1</sub> for \(1\le i\le m\). We will primarily be dealing with the Splay algorithm, so cost(_X,T_), without subscript, will always refer to the cost of splaying the keys of _X_ starting from _T_.

While an individual splay path can involve every node in the tree, the mean cost of a splay operation, averaged over sufficiently many requests, is logarithmic in the tree’s size \[61, Theorem 1\]. This performance is similar to that of balanced binary search trees. What makes Splay remarkable is that it also takes advantage of latent structure in the request sequence. The amortized cost per splay operation is logarithmic in the number of unique keys requested since the previous request for the splayed key \[61, Theorem 4\]. Thus, Splay exploits temporal locality in the access pattern. Splay simultaneously exploits spatial locality. The amortized cost of a splay operation is logarithmic in the difference between successively requested keys’ indices in the starting tree \[18, 19\]. The _dynamic optimality conjecture_ states that Splay is dynamically optimal.

Splay has many generalizations. Subramanian defined a class of algorithms that reshape a tree in small steps. A set of rules, called a "template," determines which step to take based on the arrangement of nodes in the immediate vicinity of the currently selected node. Different templates give rise to different algorithms, and a number of these algorithms have many of the same properties as Splay \[62\]. Georgakopoulos and McClurkin \[29\] and later Chalermsook et al. \[14\] proved further results about related algorithms. Section 6 examines a generalization of template algorithms.

Besides Splay, the main candidate algorithm for optimality is colloquially known as _Greedy_. Lucas and Munro independently conjectured a version of the algorithm that arranges keys on the access path according to their soonest future access times is dynamically optimal \[49, 53\]. Demaine et al. subsequently developed a representation of binary search tree executions as cartesian coordinate point-sets \[22\]. They showed that in this geometric representation, Greedy executes a new request by uniting its execution of the previous requests with the minimum set of points needed to make the new execution satisfy some required properties. Subsequently, many of the interesting behaviors that first drew attention to Splay have been proved for Greedy, including exploitation of temporal locality \[25, 31\] and spatial locality \[39\], as well as some additional properties \[13, 30\].

Two other algorithms serve primarily demonstrative purposes. "Tango" trees require cost proportional to at most lgl|_T_| times the optimum cost in order to execute an instance \[23\], and<tbc>

y
x
rotation at x
X
C
A
y
A
B
rotation at y
B
C

Figure 2: Rotation at node _x_ with parent _y_, and reversing the effect by rotating at _y_. Triangles denote subtrees.

