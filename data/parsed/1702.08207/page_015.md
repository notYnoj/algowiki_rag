**Algorithm 4.1** Dynamic programming routine BuildStrategy for a tree \(T'\). \(L,c\in\mathbb{N}\) are global parameters. Subroutines MergeSchedules and InsertVertex are provided further on.

procedure BuildStrategy(vertex v, box size \(\omega\in\mathbb{R}\))<br>
   \(l\leftarrow\) number of children of v in \(T'\) // Denote by v<sub>1</sub>,...,v<sub>l</sub> the children of v.<br>
   for i=1..l do<br>
   \(\hat{\mathcal{S}}[v_i]\leftarrow\) BuildStrategy(v<sub>i</sub>, \(\omega\));<br>
   \(s\leftarrow 0^L\)<br>
   \(s.max\text{\_}child\text{\_}load\leftarrow 0^L\)<br>
   \(s.must\text{\_}contain\text{\_}v\leftarrow false\)<br>
   \(\hat{\mathcal{S}}_0\leftarrow\{s\}\) // \(\hat{\mathcal{S}}_0\) contains the schedule with no queries.<br>
   // Inductively, \(\hat{\mathcal{S}}_i^*\) is based on merging schedules at v<sub>1</sub>,...,v<sub>i</sub>.<br>
   for i=1..l do<br>
   \(\hat{\mathcal{S}}_i^*\leftarrow\emptyset\)<br>
   for each schedule \(s\in\hat{\mathcal{S}}_{i-1}^*\) do<br>
   for each schedule \(s_{add}\in\hat{\mathcal{S}}[v_i]\) do<br>
   \(\hat{\mathcal{S}}_i^*\leftarrow\hat{\mathcal{S}}_i^*\cup\) MergeSchedules(s, \(s_{add}\), \(\omega\));<br>
   \(\hat{\mathcal{S}}[v]\leftarrow\emptyset\)<br>
   for each \(s\in\hat{\mathcal{S}}_l^*\) do<br>
   if \(w'(v)>c\omega\) then // v is heavy<br>
   for p=0..L-1 do<br>
//<br>
attempt<br>
to<br>
insert<br>
(<br>
into<br>
_s_<br>
)<br>
query<br>
to<br>
_v_<br>
starting<br>
from<br>
time-box<br>
_p_<br>
   \(\hat{\mathcal{S}}[v]\leftarrow\hat{\mathcal{S}}[v]\cup\) InsertVertex\((s,v,\omega,p\cdot\omega)\)<br>
   else //v is light<br>
   for real \(t=0..L\cdot\omega\) step \(\frac{1}{cn}\) do<br>
   //<br>
attempt<br>
to<br>
insert<br>
(<br>
into<br>
_s_<br>
)<br>
query<br>
to<br>
_v_<br>
at<br>
slot<br>
from<br>
time<br>
_t_<br>
   \(\hat{\mathcal{S}}[v]\leftarrow\hat{\mathcal{S}}[v]\cup\) InsertVertex\((s,v,\omega,t)\)<br>
   if s.must\_contain\_v=false then<br>
   \(\hat{\mathcal{S}}[v]\leftarrow\hat{\mathcal{S}}[v]\cup\) InsertVertex\((s,v,\omega,\perp)\)<br>
   return \(\hat{\mathcal{S}}[v]\)

Eventually, the set of schedules \(\hat{\mathcal{S}}_l^*\), obtained after merging the schedules of all children of v, contains an element s satisfying (4.7). Next, we test all possible values of \(t_v\in\mathbb{R}\cup\{\perp\}\), which are feasible for an aligned schedule. These values depend on whether vertex v is heavy or light, for which t<sub>v</sub> should represent the starting time of a box or slot, respectively. Using procedure InsertVertex, we then set the load of each box following (4.5):

\(s_v[p]\leftarrow\left\{\begin{array}{ c c }
a_p+\sum_{j=1}^ls_{v_j}[p], & \text{when}t_{end}^v\ge(p+1)\omega, \\
a_p, & \text{when}p\omega<t_{end}^v<(p+1)\omega, \\
0, & \text{when}t_{end}^v\le p\omega,
\end{array}\right.\) (4.8)

where a<sub>p</sub> is defined as in (4.3). In the pseudocode of function InsertVertex, for compactness we replace the second and third condition by equivalently setting \(s_v[p]\leftarrow a_p\) when the first condition does not hold. We additionally constrain in procedures MergeSchedules and InsertVertex the possibility of the condition \(t_v=\perp\) occurring by enforcing the constraints of (4.4) (corresponding of the setting of parameter s.must\_contain\_v to false). Condition (4.6) is enforced through procedures MergeSchedules and InsertVertex using the auxiliary array s.max\_child\_load\[p\], \(0\le p\le L-1\), defined so that s.max\_child\_load\[p\] \(\leftarrow\) max\(_{1\le j\le l}s_{v_j}[p]\).

Since \(\hat{\mathcal{S}}[v_i]\), for all \(1\le i\le l\), contains all minimal schedules satisfying (4.4), (4.5), and (4.6), the same holds for \(\hat{\mathcal{S}}[v]\), which was constructed by enforcing only the required constraints. We remark that we obtain only the set of minimal (and not all) schedules due to the slight<tbc>

