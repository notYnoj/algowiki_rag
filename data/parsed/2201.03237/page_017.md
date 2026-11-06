**Algorithm 2** NeighborSelection(_s,E,m,mp,r_)

**Require:** node _s_ selecting neighbors, neighbor candidate set _E_, maximum of neighbor size _m_, threshold of min\_prob _mp_, radius r

**Ensure:** selected neighbor set V

1: \(V\leftarrow\phi\)

2: sort _E_ in the ascending order of distance to s

3: **for all** node _e_ in _E_ **do**

4: **if** _V.size_()==_m_ **then** break

5: exclude \(\leftarrow\) false

6: **for all** node _v_ in _V_ **do**

7: **if** \(\delta(v,e)<\delta(s,e)\) **then**

8: \(m\text{\_}prob\leftarrow\) calculate the min\_prob with edge \(\overrightarrow{sv}\)

9: **if** \(m\text{\_}prob\ge mp\) **then**

10: exclude \(\leftarrow\) true

11: break

12: **if** not exclude **then** _V.add(e_)

13: return _V_

**Algorithm 3** TBSG\_Construction(_CT,KG,m,mp,r,n_)

**Require:** Cover Tree _CT_, KNNG _KG_, maximum of neighbor size _m_, threshold of min\_prob _mp_, radius _r_, dataset cardinality _n_

**Ensure:** TBSG _G_ with enter point _ep_

1: \(ep\leftarrow\) root of CT

2: \(G\leftarrow\)Graph with _n_ nodes and no edges

3: BG \(\leftarrow\) add reversed edges to KG

4: **for all** node _s_ in _G_ **do**

5: \(E\leftarrow\) neighbors of _s_ in _BG_

6: _E.add_(s.children()) in _CT_

7: \(V\leftarrow\) NeighborSelection(_s,E,m,mp,r_)

8: set the neighbors of _s_ in _G_ as _V_

9: return G

