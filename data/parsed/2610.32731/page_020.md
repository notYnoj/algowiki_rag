<tbc>in _Q_ may thus be much too large. The solution lies in the following definition: If _v_ is a node in a DAG _G_, then the _exclusive out-degree_ \(\mathrm{deg}_+^\mathrm{E}(G,v)\) of _v_ is the number of out-neighbors of _v_ with no other in-neighbors.

We will use \(\mathrm{deg}_+^\mathrm{E}(G',v)\) as the weight of each node _v_ in _Q_, where \(G'\) is the original graph _G_<sub>0</sub> without the previously deleted nodes (thus \(G'\) is precisely _G_ without the edges created by Heapify). Observe that the weight then may need to change, which is why we now need the `increase-weight` operation of WSHs.

Algorithm 2 shows pseudocode for our new algorithm WSHPoseSelect. Our algorithm assumes that the given DAG _G_ has a single source. If this is not the case, we can add a dummy source and connect it to all present sources, as discussed at the start of section 5. Additional details are explained below.

**Algorithm 2** A WSH-based poset selection algorithm.

procedure WSHPoseSelect(_G,k_)<br>
   \(Q\leftarrow\) new WSH with \(\varepsilon=\frac{1}{6}\)<br>
   \(s\leftarrow\) unique source of G<br>
   \(Q.\text{\texttt{insert}}(\mathrm{root}(G),\mathrm{deg}_+^\mathrm{E}(G,v)+1)\).<br>
   \(S\leftarrow\{s\}\)<br>
   \(G_0\leftarrow\) copy of G<br>
   \(G'\leftarrow\) copy of G<br>
   for each \(i\in[k-1]\) do<br>
   \(x\leftarrow Q.\text{\texttt{find-min}}()\)<br>
   while Q contains an in-neighbor p of x in G<sub>0</sub> do<br>
   \(x\leftarrow p\)<br>
   \((x,C)\leftarrow Q.\text{\texttt{delete}}(x)\)<br>
   if x is uncorrupted then<br>
Add<br>
_x_<br>
to<br>
_C_<br>
   for each \(v\in C\) do<br>
   if v is still corrupted in Q then<br>
   Delete<br>
_v_<br>
from<br>
_G_<br>
and<br>
\(G'\)<br>
   \(K,U\leftarrow\) marked/unmarked newly created sources in G.<br>
   if |U|\>0 then<br>
   Mark each \(u\in U\)<br>
   \(r'=\) Heapify(G,U)<br>
   Add \(r'\) to K<br>
   for each \(v\in K\) do<br>
   \(Q.\text{\texttt{insert}}(v,\mathrm{deg}_+^\mathrm{E}(G',v)+1)\)<br>
   Add v to S.<br>
   Update weights of each \(u\in Q\) to \(\mathrm{deg}_+^\mathrm{E}(G',u)+1\) if necessary.<br>
   return Select(S,k)

