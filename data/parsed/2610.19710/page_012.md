If _v∼_par w in \(G'\) under the original assignment \(\phi_0\), then all nodes keep the same potential, so _v∼_par w still holds under \(\phi_1\).

Otherwise, \(v\unknown_\mathrm{par}w\) under \(\phi_0\), so \(d_{G^\prime}(v,w)\equiv\phi_0(v)-\phi_0(w)+1(\mathrm{mod}2)\). After parity fixing, in the assignment \(\phi_1\) before clearing the edit area, we have

\(d_{G^\prime}(v,w)\equiv\phi_0(v)-\phi_0(w)+1\equiv\phi_1(v)-\phi_1(w),\)

since the potential of either _v_ or _w_ is increased by an odd number. Thus, before clearing the edit area, _v∼_par _w_.

In both cases, we get _v∼_par _w_, so

\(x\sim_\mathrm{par}v\sim_\mathrm{par}w\sim_\mathrm{par}y.\)

By transitivity (Lemma 6 using bipartiteness of \(G'\)), we get _x∼_par _y_. This also holds after clearing the edit area if both _x_ and _y_ remain assigned, since the clearing does not change distances and potentials of assigned nodes.

2. Now, we prove that \(x\unknown y\) holds in \(G'\) under \(\phi_2\). Let _x_ and _y_ be assigned in \(\phi_2\) and connected to _e_ in \(G'\). We distinguish the cases whether a shortest path between _x_ and _y_ in \(G'\) passes through _e_ or not.

**a.** Let a shortest path between _x_ and _y_ in \(G'\) pass through _e_=(_v,w_). Without loss of generality, let this path be of the form (_x,...,v,w,...,y_). Since \(\phi_2(x)\neq\perp\), we must have \(d_{G^\prime}(x,w)\ge D\) (if we instead had \(d_{G^\prime}(x,w)<D\) then also \(d_{G^\prime}(x,v)<D-1\) and _x_ would have been cleared in \(\phi_2\)). Similarly, \(d_{G^\prime}(y,v)\ge D\), since \(\phi_2(y)\neq\perp\). Thus, the length of the shortest path must be at least 2_D_-1. By construction, _D_ is chosen such that

\(2D=\mathrm{max}_{v\in V}\phi_1(v)+1\ge\mathrm{max}_{v\in V}\phi_2(v)+1\ge\phi_2(x)+1.\)

Then, using that \(\phi_2(y)\ge\phi_0(y)\ge 0\),

\(d_{G^\prime}(x,y)\ge 2D-1\ge\phi_2(x)\ge\phi_2(x)-\phi_2(y).\)

Symmetrically, swapping _x_ and _y_ in the reasoning above also gives \(d_{G^\prime}(x,y)\ge\phi_2(y)-\phi_2(x)\). We conclude that \(x\unknown y\) in \(G'\) under \(\phi_2\).

**b.** Otherwise, no shortest path between _x_ and _y_ in \(G'\) passes through _e_. Then _x_ and _y_ were connected in _G_ and \(d_G(x,y)=d_{G^\prime}(x,y)\). Furthermore, using the assumption that \(x\unknown y\) under \(\phi_0\) in _G_ and using fact 2, we have

\(d_G(x,y)=d_{G^\prime}(x,y)\ge|\phi_0(x)-\phi_0(y)|=|\phi_2(x)-\phi_2(y)|,\)

proving \(x\unknown y\) in \(G'\) under \(\phi_2\) as required.

Lemma 8 proved that parity-consistency and potential-separation hold for assigned nodes after fixing the parity and clearing the edit area around the inserted edge. In the next step, the algorithm completes the boundaries with the procedure ExpandBorders, which calls BuildAround until potential 0 is reached. We prove that these procedures maintain the invariants on assigned nodes.

\(\blacktriangleright\) **Lemma 9.** _If all connected pairs x,y of assigned nodes satisfy_ \(x\unknown y\) _and for all outer nodes v we have_ \(\phi(v)\le k\)_, then also in the assignment of potentials resulting from BuildAround(k_) _all connected pairs of assigned nodes satisfy_ \(x\unknown y\).

