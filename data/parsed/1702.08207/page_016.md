**Algorithm 4.2** Subroutines MergeSchedules and InsertVertex of procedure BuildStrategy from Algorithm 4.1.

procedure MergeSchedules(schedule s<sub>orig</sub>, schedule s<sub>add</sub>, box size \(\omega\in\mathbb{R}\))<br>
   \(s\leftarrow s_{orig}\) // copy schedule and its properties to answer<br>
   for p=0..L-1 do // for each time-box add load of s<sub>1</sub> and s<sub>2</sub><br>
   \(s[p]\leftarrow s_{orig}[p]+s_{add}[p]\)<br>
   if s\[p\]\>1 then<br>
   \(s[p]\leftarrow+\infty\)<br>
   \(s.max\text{\_}child\text{\_}load[p]\leftarrow max\{s.max\text{\_}child\text{\_}load[p],s_{add}[p]\}\)<br>
   if \(s_{add}.t_v=\perp\) then<br>
\(s.must\text{\_}contain\text{\_}v\leftarrow true\)<br>
   return s<br>
procedure InsertVertex(schedule s<sub>orig</sub>, vertex v, box size \(\omega\in\mathbb{R}\), time \(t\in\mathbb{R}\cup\{\perp\}\))<br>
   \(s\leftarrow 0^L\) // initialize empty schedule for answer<br>
   if \(t\neq\perp\) then<br>
   \(I\leftarrow[t,t+w'(v)]\) // time interval into which query to v is being inserted<br>
   \(s.t_v\leftarrow t\)<br>
   \(t_{end}^v\leftarrow t+w'(v)\)<br>
   else<br>
   \(I\leftarrow\emptyset\)<br>
   \(s.t_v\leftarrow\perp\)<br>
   \(t_{end}^v\leftarrow+\infty\)<br>
   for p=0..L-1 do // for each time-box<br>
   \(a_p\leftarrow\frac{1}{\omega}|I\cap[p\cdot\omega,(p+1)\cdot\omega]|\) // contribution of query to v to load of box p<br>
   if s.max\_child\_load\[p\]+a<sub>p</sub>\>1 then<br>
   return \(\emptyset\)<br>
   if \(t_{end}^v\ge(p+1)\omega\) then<br>
   \(s[p]\leftarrow s_{orig}[p]+a_p\) // add load from children in box p<br>
   if s\[p\]\>1 then //insertion failed<br>
   return \(\emptyset\)<br>
   else<br>
   \(s[p]\leftarrow a_p\)<br>
   return {s}

difference between (4.8) and (4.5) in the second condition: instead of requiring \(s_v[p]\ge a_p\), we put \(s_v[p]\leftarrow a_p\), thus setting the p-th coordinate of the schedule at its minimum possible value.

It follows directly from Lemma 4.6 that, for any value \(\omega^*\), tree T may only admit an aligned schedule assignment of duration at most \(\omega^*L\) if a call to procedure BuildStrategy\((r(T),\omega^*)\) returns a non-empty set. Taking into account Lemmas 4.1 and 4.2, we directly obtain the following lower bound on the length of the shortest aligned schedule in tree \(T'\).

**Lemma 4.7.** _If_ BuildStrategy\((r(T),\omega^*)=\emptyset\)_, then:_

\(\omega^*L<\left(1+\frac{3}{c}\right)\mathsf{OPT}(T')\le\left(1+\frac{3}{c}\right)\left(1+\frac{2}{c}\right)\mathsf{OPT}(T)\le\left(1+\frac{11}{c}\right)\mathsf{OPT}(T).\)

Finally, we bound the running time of procedure BuildStrategy.

