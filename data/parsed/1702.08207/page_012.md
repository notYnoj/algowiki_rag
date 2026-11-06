Before presenting formally the considered quasi-polynomial time procedure, we start by outlining an (exponential time) algorithm which verifies if there exists an aligned schedule assignment \(\hat{\Sigma}\) for \(T'\) whose duration is at most \(L\omega\). Notice that since all weights in \(T'\) are integer multiples of \(\frac{1}{cn}\), the optimal aligned schedule assignment will start and complete the execution of all queries at times which are integer multiples of \(\frac{1}{cn}\); thus, we may restrict the considered class of schedules to those having this property. Any possible schedule of length at most \(L\omega\) at a vertex _v_, which may appear in \(\hat{\Sigma}\), will be represented in the form of the pair \((\sigma_v,t_v)\), where:

• \(\sigma_v\) is a Boolean array with \(L\omega cn\) entries, where \(\sigma_v[i]=1\) when time slot \([\frac{i}{cn},\frac{i+1}{cn}]\) is occupied in the schedule at _v_, and \(\sigma_v[i]=0\) otherwise.<tbc>

• \(t_v\in\mathbb{R}\) represents the start time of the query to _v_ in the schedule of _v_ (we put \(t=\perp\) if such a query does not appear in the schedule).

We now state some necessary conditions for a consistent schedule, known from the analysis of the unweighted search problem (cf. e.g. \[16, 30, 33\]). The first observation expresses formally the constraint that the same time slot cannot be used in the schedules of two children of a node _v_, unless it is separated by an (earlier) query to node _v_ itself. All time slots before the starting time _t<sub>v</sub>_ of job (_v,t<sub>v</sub>_) are free if and only if the corresponding time slot is free for all of the children of _v_.

**Observation 4.3.** _Assume that the tuple_ \((\sigma_v,t_v)_{v\in V}\) _corresponds to a consistent schedule. Let_ \(v\in V\) _be an arbitrarily chosen node with set of children_ {_v_<sub>1</sub>_,...,v<sub>l</sub>}. Let the completion time_ \(t_{end}^v\) _of the query to v in the schedule of v be given as:_<tbc>

\(t_{end}^v=\left\{\begin{array}{ c c }
t_v+w'(v), & \text{\textit{if}}t_v\neq\perp, \\
+\infty, & \text{\textit{if}}t_v=\perp.
\end{array}\right.\)

<tbc>_Then, for any time slot_ \([\frac{i}{cn},\frac{i+1}{cn}]\)_, we have:_

\(\sigma_v[i]=\sum_{j=1}^l\sigma_{v_j}[i],\text{\textit{when}}\frac{i+1}{cn}\le t_v,\sigma_v[i]=1\text{\textit{and}}\sum_{j=1}^l\sigma_{v_j}[i]=0,\text{\textit{when}}t_v<\frac{i+1}{cn}\le t_{end}^v,\sigma_v[i]=0,\text{\textit{when}}\frac{i+1}{cn}>t_{end}^v.\right\}\) (4.3)

We remark that the last of the above conditions (4.3) follows from the w.l.o.g. assumption we made when defining sequence assignments that whenever node _v_ appears in the schedule of _v_, it is the last node in the query sequence for _v_.

Moreover, any valid search strategy which locates a target vertex must eventually query at least one of the endpoints of every edge of the tree \(T'\), since otherwise, it will not be able to distinguish targets located at these two endpoints. We thus make the following observation.

**Observation 4.4.** _Assume that the tuple_ \((\sigma_v,t_v)_{v\in V}\) _represents a consistent schedule. Let_ \(v\in V\) _be an arbitrarily chosen node with set of children_ {_v_<sub>1</sub>_,...,v<sub>l</sub>}. Then:_

\(\text{\textit{If}}t_v=\perp\text{\textit{, then}}t_{v_j}\neq\perp\text{\textit{, for all}}1\le j\le l.\) (4.4)

