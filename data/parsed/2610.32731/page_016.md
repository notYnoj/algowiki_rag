**Algorithm 1** A WSH-based tree selection algorithm.

procedure WSHTreeSelect(T,k,L)<br>
   \(Q\leftarrow\) new WSH with \(\varepsilon=\frac{1}{6}\)<br>
   \(Q.\text{\texttt{insert}}(\text{root}(T),\text{deg}(T,\text{root}(T))+1)\).<br>
   \(S\leftarrow\{r\}\)<br>
   \(T_0\leftarrow\) copy of T<br>
   for each \(i\in[k-1]\) do<br>
   \(x\leftarrow Q.\text{\texttt{find-min}}()\)<br>
   while parent\((T_0,v)\in Q\) do<br>
   \(x\leftarrow\text{parent}(T_0,v)\)<br>
   \(C\leftarrow Q.\text{\texttt{delete}}(x)\)<br>
   if x is uncorrupted then<br>
Add<br>
_x_<br>
to<br>
_C_<br>
   for each \(v\in C\) do<br>
   \(K\leftarrow\) marked children of v in T<br>
   \(U\leftarrow\) unmarked children of v in T<br>
   if |U|\>0 then<br>
   Mark each \(u\in U\)<br>
   \(r'=\text{Heapify}(T,U)\)<br>
   \(\text{Add}r'\) to K<br>
   for each \(v\in K\) do<br>
   \(Q.\text{\texttt{insert}}(v,\text{deg}(T_0,v)+1)\)<br>
   Add v to S.<br>
   return Select(S,k)

