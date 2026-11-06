**Algorithm 1** SearchKnn(_G,q,ep,l,k_)

**Require:** Graph _G_,query point _q_, enter point _ep_, result pool size _l_, nearest neighbor size _k_

**Ensure:** _k_ nearest neighbors to _q_

1: result pool \(C\leftarrow\phi\)

2: _C.add(ep_)

3: **while** _true_ **do**

4: **if** nodes in _C_ are all visited **then**

5: break

6: \(c\leftarrow\)the first unvisited node in _C_

7: mark _c_ as visited

8: **for all** neighbor _e_ of _c_ in _G_ **do**

9: _C.add(e_)

10: sort _C_ in the ascending order of the distance to _q_

11: **if** _C.size_()_\>l_ **then**

12: _C.resize(l_)

13: return the first _k_ nodes in C

