<tbc>_w, then_ \(u'\) _is undefined. If_ \(B_2\backslash B_1\neq\varnothing\)_, then at least one of_ \(u'\) _or_ \(w'\) _exists, and all BPs in B_<sub>2</sub>\\_B_<sub>1</sub> _must involve either_ \(u'\) _or_ \(w'\).

_Proof._ Consider any BP (_x,y_) that exists in _B_<sub>2</sub> but not in _B_<sub>1</sub>. Since (_x,y_) forms a BP in _M_<sub>2</sub> and not in _M_<sub>1</sub>, the matchings of _x_ or _y_ must have been changed. The only changes in the matchings from _M_<sub>1</sub> to _M_<sub>2</sub> are attributed to the removal of the BP (_u,w_), affecting the matchings of \(u,w,u'\), and \(w'\).

(i). Consider agents _u_ and _w_. If _u_ was free in _M_<sub>1</sub>, then no new BPs involving _u_ can be introduced in _M_<sub>2</sub> as such BPs would have been identified in _M_<sub>1</sub>. Conversely, if _u_ was full in _M_<sub>1</sub>, any BPs involving _u_ with candidates worse than _w_ in _B_<sub>1</sub> will no longer exist, and no additional BPs including _u_ will be introduced. The same logic applies to _w_.<tbc>

(ii). Consider agents \(u'\) and \(w'\). If \(u'\) and \(w'\) are both undefined, then clearly no new BPs involving them can arise. If either \(u'\) or \(w'\) exists, new BPs might be introduced. Specifically, if \(w'\) was free in _M_<sub>1</sub>, then no new BPs involving \(w'\) are introduced in _M_<sub>2</sub>, except potentially \((w',u')\), as any such BPs would have existed in _M_<sub>1</sub>. This condition holds unless \(u'\), previously full in _M_<sub>1</sub>, becomes free in _M_<sub>2</sub>, and if \(u'\) is a candidate of \(w'\), thus establishing \((w',u')\) as a new BP. If \(w'\) was full in _M_<sub>1</sub>, let _z_ represent the worst partner of \(w'\) in _M_<sub>1</sub>; in _M_<sub>2</sub>, where \(w'\) is free, possible new BPs might arise involving \(w'\) and candidates worse than _z_. The same logic applies to \(u'\).

Therefore, if _B_<sub>2</sub>\\_B_<sub>1</sub> is non-empty, it necessitates that at least one of \(u'\) or \(w'\) exists, and all BPs in _B_<sub>2</sub>\\_B_<sub>1</sub> must involve either \(u'\) or \(w'\).

Given these propositions, verifying the existence of BPs for each agent after refining the tie-breaking strategy is unnecessary. It is sufficient to focus on a specific subset of agents. Consequently, we maintain a set of agents requiring examination, initially set to _Q<sub>a</sub>_. In each iteration, an agent _v_ is randomly selected from this set, and all BPs involving _v_ are removed. Specifically, if BPs involving _v_ are identified, the UBP from _v_’s perspective is removed. Subsequently, any agents who were previously full and disconnected are added to the set. The BP removal process is repeated until the set is empty or the time threshold is reached, as detailed in lines 2-24 of Algorithm 4.

## 4.4 Equity-focused variant of TBLS

To achieve a relatively equitable outcome with a low sex equality cost when solving the MAX-SMTI problem, two modifications are introduced to TBLS:

(i). Use an algorithm designed for the SESM problem, such as PDB, as the base algorithm.<tbc>

(ii). Restrict the choice of tie adjustments based on the current bias of the matching. If the matching favors the _U_ side, adjustments related to agents of _U_ are permitted. Specifically, only adjustments within the set \(\{a\in R_M^b|a[1]\in U\}\) are allowed. Conversely, if the current matching favors the _W_ side, only adjustments related to agents of _W_ are permitted. In cases where no adjustments are available within the constraint, the restriction is temporarily lifted.<tbc>

