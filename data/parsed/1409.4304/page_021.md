<tbc>words,

\(b(\{u',v'\})+\alpha_{u^\prime,v^\prime} b(\{u',v'\})+\alpha_{v,v^\prime} b(\{u,v\})+\alpha_{u,v^\prime} b(\{u,v\})\)<br>
\(\ge b(\{u,v'\})+\alpha_{u,v^\prime} b(\{u,v'\}).\)

Then there is an accord ing rule in _D_<sub>2</sub> and the combined existence of \(\{u',v'\}\) and {_u,v_} results in \(\{u,v'\}\) being dominated.

Hence, whenever \(\{u,v'\}\) is an undominated candidate coalition, it represents a perce vived blocking pair for the current matching. Further when it gets inserted, any former matching edges of _u_ and \(v'\) get dominated by weight and dropped, while all other edges remain unaffected. Hence, the new coalition structure represents exactly matching _M_ after resolving \(\{u,v'\}\).

## A.4 Proof of Theorem 2

The proof generalizes a similar result for locally stable matchings [19] and is based on two observations:

1. Note that by design of _T_ and _D_, if some generation rule ({_C_<sub>1</sub>}_,C_<sub>2</sub>) is finally applied, we need to have _w(C_<sub>2</sub>)_\>w(C_<sub>1</sub>) and the creation of _C_<sub>2</sub> causes the deletion of _C_<sub>1</sub>. Thus, within any sequence of improvement steps we can identify a unique predecessor for each coalition \(C\notin\mathcal{C}_g\) whose presence is necessary for creation of _C_. Furthermore, this predecessor has weight strictly smaller than _w(C_). Hence the sequence of predecessors necessary to generate any coalition _C_ is limited by _m_.<tbc>

2. Our second observation is that the only domination rules that are applied in the deletion of an existing coalition are those based on weight domination. Thus, every deletion of a coalition is accompanied by the creation of a worthier coalition. A chain of deletions again is limited in length by _m_.

Now let I be some sequence of improvement steps converting S<sub>0</sub> into S<sup>∗</sup>. If a coalition is created and deleted again but neither used to delete another coalition nor marked as a predecessor to create one, then this coalition provides no contribution for the transformation from S<sub>0</sub> to S<sup>∗</sup>. Thus we can delete all these coalitions from I and receive a sequence I<sub>1</sub> which as well transforms S<sub>0</sub> into S<sup>∗</sup> via improvement steps. Now in I<sub>1</sub> there might be coalitions which get created and deleted again without use as they only deleted or created coalitions we dropped from I<sub>1</sub>. Thus we can repeat this sequence truncation until all remaining coalitions are of use. We claim that this sequence I<sup>∗</sup> has to be of polynomial length.

First assume state S<sub>0</sub> is the empty coalition structure. Then we do not have to delete any unfitting coalitions but simply create the needed ones. As not all of S<sup>∗</sup> might be in _C<sub>g</sub>_ we possibly have to use generation rules of _T_ but by (1) we know that for each desired coalition we need at most _m_ steps. Thus, overall we need at most _m_<sup>2</sup> steps. Now for an arbitrary starting coalition structure we might also have to delete certain coalitions to reach S<sup>∗</sup>. Thus each of coalition of S<sub>0</sub> might generate a chain of coalitions deleting each other throughout the sequence,<tbc>

