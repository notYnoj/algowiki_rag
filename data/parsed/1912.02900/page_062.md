For each point \(p\in X\), for each vertex \(v\in V(T)\) of the partitioning tree _T_, such that \(p\in S(v)\), we add the projection points proj(_p,v_) to the solution, depending on whether there exists an index \(i\in\{0,1,\dots,D\}\) and a tree \(T'\in\mathcal{T}_i\), such that _v_ lies in the middle layer \(U_{T^\prime}\) of \(T'\), and whether _p_ is the first or last point of its \(T'\)-box. Notice that in the online setting, when the point _p_ arrives, we need to be able to immediately decide which copies of _p_ to add to the solution. Since the trees in the families T<sub>0</sub>,T<sub>1</sub>_,...,_T_<sub>D</sub>_ are known in advance, and we discover, for every vertex \(v\in V(T)\) whether \(p\in S(v)\) immediately when _p_ arrives, the only missing information, for every relevant tree \(T'\), is whether vertex _p_ is the first or the last vertex in its \(T'\)-box. In fact it is easy to check whether it is the first vertex in its \(T'\)-box, but we will not discover whether it is the last vertex in its \(T'\)-box until the next iteration, at which point it is too late to add points to the solution that lie in the row of _p_.

In order to avoid this difficulty, we slightly modify the instance and the solution.

## 7.2 Online-friendly solutions

In this section we slightly modify both the input set of points and the solutions produced by our algorithm, in order to adapt them to the online setting.

### Modifying the Instance.

Let _X_={_p_<sub>1</sub>_,...,p<sub>m</sub>_} be the input set of points, where for all \(1\le i\le m\), the _y_-coordinate of _p<sub>i</sub>_ is _i_. We produce a new instance \(X'=\{p'_i,p''_i|1\le i\le m\}\), as follows: for all \(1\le i\le m\), we let \(p'_i\) and \(p''_i\) be points whose _y_-coordinates are (2_i_-1) and 2_i_, respectively, and whose _x_-coordinate is the same as that of _p<sub>i</sub>_. We refer to \(p'_i\) and to \(p''_i\) as _copies of p<sub>i</sub>_.

Clearly, \(|X'|=2|X|\), and it is easy to verify that \(\mathsf{OPT}(X')\le 2\mathsf{OPT}(X)\). Indeed, if we let _Y_ be a solution for _X_, we can construct a solution \(Y'\) for \(X'\), by creating, for every point \(q\in Y\) , two copies \(q'\) and \(q''\), that are added to rows with _y_-coordinates 2_q.y_-1 and 2_q.y_ respectively.

For convenience, we denote \(\mathcal{T}=\bigcup_{i=0}^D\mathcal{T}_i\). Notice that, for every tree \(T'\in\mathcal{T}\) , for every point _p<sub>i</sub>_ of the original input _X_, copy \(p'_i\) of _p<sub>i</sub>_ may never serve as the last point of a \(T'\)-box, and copy \(p''_i\) of _p<sub>i</sub>_ may never serve as the first point of a \(T'\)-box.

### Modifying the Solution.

Let _Y_ be the solution that our _O_(loglog_n_)-approximation algorithm produces for the new instance \(X'\). For convenience, for all \(1\le i\le 2m\), we denote by _R<sub>i</sub>_ the row with _y_-coordinate _i_. Notice that all points of _Y_ lying on a row _R_<sub>2_i_-1</sub> are projections of the point \(p'_i\). Since this point may only serve as the first point of a \(T'\)-box for every tree \(T'\in\mathcal{T}\) , when point \(p'_i\) arrives online, we can immediately compute all projections of \(p'_i\) that need to be added to the solution. All points of _Y_ lying on row _R_<sub>2_i_</sub> are projections of the point \(p''_i\). This point may only serve as the last point of a \(T'\)-box in a tree \(T'\in\mathcal{T}\) . But we cannot know whether \(p''_i\) is the last point in its \(T'\)-box until we see the next input point. Motivated by these observations, we now modify the solution _Y_ as follows.

We perform _m_ iterations. In iteration _i_, we consider the row _R_<sub>2_i_</sub>. If no point of _Y_ lies on row _R_<sub>2_i_</sub>, then we continue to the next iteration. Otherwise, we move every point of _Y_ that lies on row _R_<sub>2_i_</sub> to row _R_<sub>2_i_+1</sub> (that is, one row up). Additionally, we add another copy \(p'''_i\) of point _p<sub>i</sub>_ to row _R_<sub>2_i_</sub>, while preserving its _x_-coordinate.

In order to show that the resulting solution is a feasible solution to instance \(X'\), it is sufficient to show that the solution remains feasible after every iteration. Let _Y<sub>i</sub>_ be the solution _Y_ obtained<tbc>

