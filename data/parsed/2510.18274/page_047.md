For the inductive step, suppose the claim holds for all vertices _v_ with \(d(v)\le d-1\). Consider a vertex _u_ with _d(u_)=_d_. Let \(u'\) be the predecessor of _u_ on the shortest path from _s_ to _u_ in _H_, meaning \(d(u')=d-1\), and \((u',u)\) is an edge in _H_. By the induction hypothesis, \(u'\) has a unique label, denoted as \(l\in\{s,t\}\). We now consider the possible orientations of the edge(s) between _u_ and \(u'\) in _H<sub>F</sub>_:

1. Either \((u,u',2)\) or \((u',u,2)\) belongs to _H<sub>F</sub>_. In this case, \(u\in V(E_2)\), which contradicts the assumption that \(u\notin V(E_2)\).<tbc>

2. Both \((u,u',1)\) and \((u',u,1)\) belong to _H<sub>F</sub>_. Since \(u\notin V(C)\), neither \((u,u',1)\) nor \((u',u,1)\) is an _s-t_ edge. Therefore, _u_ and \(u'\) must have the same label. As \(u'\) can only take the label _l_, _u_ must also be labeled _l_.

This completes the induction proof. As a result, given a labeling of \(V(E_2)\cup V(C)\) from Steps 1 and 2, there can be at most one possible labeling of the remaining vertices in _V_ . See Figure 4 for an illustration.

Combining the three steps, for a fixed _C_, there are at most _n<sup>f</sup>_ possible labels that are consistent<tbc>

't'
't'
's'
's'
's'
s
t

't'
't'
's'
's'
's'
't'
't'
s
t
't'
's'
's'
's'
's'
's'

Figure 3: Continuing from Step 1, the shaded vertices are already given a fixed label. Shown above one of the 4 possible consistent labeling to a segment of length _l_=4 on the blue flow. The remaining 3 possibilities are as follows: ‘s’ \(\leftarrow\) ‘s’ \(\leftarrow\) ‘s’; ‘s’ \(\leftarrow\) ‘t’ \(\leftarrow\) ‘t’; ‘t’ \(\leftarrow\) ‘t’ \(\leftarrow\) ‘t’.

Figure 4: Continuing from Step 2, the shaded vertices are already given a fixed label. Shown above is the only possible label to the remaining (unshaded) vertices

