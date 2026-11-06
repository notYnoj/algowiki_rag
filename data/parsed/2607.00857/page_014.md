extracted. First, we prove that every pair \((u',v')\) with \(d(u',v')<d(u,v)\) is already extracted. Suppose there is another pair \((u',v')\) still in _Q_ with \(d(u',v')<d(u,v)\le D[u,v]\le D[u',v']\). By (ii), there is a marked subpath of a shortest \((u',v')\)-path still in _Q_. Let (_a,b_) be a minimal such subpath. Since all subpaths of (_a,b_) are either extracted or unmarked but with no marked subpath in _Q_, all subpaths of (_a,b_) must be correct. If there is one such path still in _Q_, it must be shorter and hence extracted before \((u',v')\) and (_u,v_). If none are in _Q_, by (iii), _D[a,b_] is correct. But then

\(D[a,b]=d(a,b)<d(u',v')<d(u,v)\le D[u,v],\)

and (_a,b_) should have been extracted before (_u,v_), a contradiction.

For (i), suppose we extract (_u,v_) with _D[u,v]\>d(u,v_) for the sake of contradiction. Notice that every subpath of a shortest (_u,v_)-path has weight at most _d(u,v_) and must hence be already extracted and, by (i), also correctly computed. By (ii), there must be a marked subpath (_x,y_) of (_u,v_) in _Q_. But then again, by (i) and (iii), _D[x,y_]=_d(x,y_) and it should be extracted before (_u,v_).

Next, we show that (ii) is still satisfied. The only way it can no longer be satisfied is if the extracted (_u,v_) was marked and now there is some unmarked (_x,y_) that does not have the correct distance and no marked subpath. Then, there is a shortest path via \(x\rightarrow u\rightarrow v\rightarrow y\). Notice that _D[x,u_] must also be correct, because otherwise (_x,u_) is marked or there is another marked subpath of (_x,u_) and hence (_x,y_). Similarly, _D[v,y_] must be correct. Since _D[x,v_] is relaxed with _D[x,u_]+_D[u,v_] now, it must also be correct, as well as _D[u,y_]. This means that _D[x,u_] and _D[u,y_] are both correct and unmarked, so they were always correct and unmarked. But then, by assumption that _D[x,y]\>d(x,y_), we know that (_x,y_) must be in _U_ by Lemma 4 and hence be marked, a contradiction.

Furthermore, (iii) clearly still holds by definition of the algorithm. After the execution is complete, _D_ holds all correct distances by (i) and the algorithm is correct.

## 5 Handling negative edge weights

Our main algorithm crucially relies on nonnegativity of edge weights. In this section, we describe how to preprocess the graph to ensure that this condition holds. Assume there is no cycle of negative total weight, since shortest paths are not well-defined otherwise. We employ a standard trick in the area of shortest paths (see, e.g., [22]), originally due to Johnson [27]. Let graph _G_=(_V,E,w_) be an edge-weighted graph and let \(\phi:V\rightarrow\mathbb{R}\) be a _potential function_. For any edge \((u,v)\in E\), define the \(\phi\)-_adjusted_ edge weights \(w_\phi(u,v):=w(u,v)+\phi(u)-\phi(v)\).

We state a few observations about this definition. First, in the \(\phi\)-adjusted graph \(G_\phi=(V,E,w_\phi)\), the shortest path lengths stay the same up to the potential of the endpoints, i.e., \(d_G(u,v)=d_G_\phi(u,v)-\phi(u)+\phi(v)\). In fact, for fixed \(u,v\in V\) , the length of any (_u,v_)-path gets preserved (when switching between _G_ and \(G_\phi\)) up to the same offset \(\phi(u)-\phi(v)\). Johnson’s trick states that we can always compute a potential \(\phi\) such that \(w_\phi\) is non-negative.

\(\blacktriangleright\) **Observation 6** (Johnson’s trick [27])**.** _By choosing_ \(\phi(v)=min_{u\in V}d(u,v)\)_, all_ \(\phi\)_-adjusted weights_ \(w_\phi\) _are non-negative._

Note that to compute a potential \(\phi\) as in Observation 6, we can simply add one vertex _s_ to _V_ with weights _w(s,v_)=0 for all \(v\in V\) and run any single-source shortest path algorithm that works for negative weights.

By computing such a potential \(\phi\) in the beginning, running our algorithms in Sections 2-4 on the \(\phi\)-adjusted graph, and removing the offset in the end, we can hence guarantee non- negative edge weights. Note that we do not change the certificate. It remains to argue that

