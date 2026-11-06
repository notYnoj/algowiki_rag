**Algorithm 6** Compute Prefix Values

Input: DP DAG G, interval [i,m], boundary set B<sub>left</sub>, boundary value map \(\beta_\mathrm{left}\), target set \(F_I^\mathrm{mid}\)<br>
Output: Dictionary f mapping \(v\in F_I^\mathrm{mid}\) to optimal value from B<sub>left</sub> to v with internal vertices in [i,m]<br>
under the local DP induced by \((B_\mathrm{left},\beta_\mathrm{left})\)<br>
   \(\triangleright\) Initialize frontier with boundary values<br>
   \(frontier\leftarrow\emptyset\)<br>
   for each \(u\in B_\mathrm{left}\leftarrow\)<br>
   to do\(frontier[u]\leftarrow\beta_\mathrm{left}[u]\)<br>
   end for<br>
   \(f\leftarrow\emptyset\triangleright\) Output dictionary<br>
   \(\triangleright\) Forward DP from i to m<br>
   for \(v\leftarrow i\) to \(m\leftarrow\)<br>
   if to then \(v\in B_\mathrm{left}\) do<br>
   \(x_v\leftarrow frontier[v]\triangleright\) Already initialized for this subproblem<br>
   else<br>
   \(\triangleright\) Compute via recurrence restricted to boundary and previously reached vertices<br>
   \(x_v\leftarrow\) bottom element for \(\oplus\)<br>
   for each \((u,v)\in E\) with \(u\in frontier\leftarrow\)<br>
   to do\(x_v\leftarrow x_v\oplus(frontier[u]\otimes w_{u,v})\)<br>
   end for<br>
   \(frontier[v]\leftarrow x_v\)<br>
   end if<br>
   \(\triangleright\) Record value if v is in middle frontier<br>
   if \(v\in F_I^\mathrm{mid}\) then<br>
\(f[v]\leftarrow frontier[v]\)<br>
   end if<br>
   \(\triangleright\) Cleanup: remove vertices with no successors in (v,m]<br>
   if v\<m then<br>
   for each \(u\in frontier\leftarrow\)<br>
   to dohasFuture \(\leftarrow\exists w\in(v,m]:(u,w)\in E\)<br>
   if \(\neg hasFuture\) then<br>
remove<br>
_u_<br>
from<br>
_frontier_<br>
   end if<br>
   end for<br>
   end if<br>
end for<br>
end for

