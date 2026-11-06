**Algorithm 7** Compute Suffix Values (Forward-Only)

Input: DP DAG G, interval I=\[i,j\], frontier \(F_I^\mathrm{mid}\), sink \(s\in I\) with s\>m(I)<br>
Output: Dictionary g mapping \(v\in F_I^\mathrm{mid}\) to optimal value from v to s with internal vertices in I under the local DP induced by boundary {v}<br>
\(g\leftarrow\emptyset\triangleright\) Output dictionary<br>
\(\triangleright\) For each candidate midpoint vertex<br>
for each \(v\in F_I^\mathrm{mid}\) (in canonical order) \(\leftarrow\)<br>
to \(\triangleright\) doRun forward DP over (v,s] with boundary at v<br>
\(\text{\textit{frontier}}\leftarrow\emptyset\)<br>
\(\text{\textit{valueAtS}}\leftarrow\text{bottom element for}\oplus\)<br>
for \(w\leftarrow v+1\) to \(s\leftarrow\)<br>
to do\(x_w\leftarrow\) bottom element for \(\oplus\)<br>
\(\triangleright\) Compute via recurrence, starting from v and reached vertices in (v,w)<br>
for each \((u,w)\in E\leftarrow\)<br>
if to then u=v do<br>
   \(\triangleright\) Boundary-to-first step uses multiplicative identity at v<br>
   \(\text{\textit{candidate}}\leftarrow\mathbf{1}_\otimes\otimes w_{u,w}\triangleright\) Often just w<sub>u,w</sub><br>
   \(x_w\leftarrow x_w\oplus\text{\textit{candidate}}\)<br>
   else if \(u\in\text{\textit{frontier}}\) then<br>
   \(\text{\textit{candidate}}\leftarrow\text{\textit{frontier}}[u]\otimes w_{u,w}\)<br>
   \(x_w\leftarrow x_w\oplus\text{\textit{candidate}}\)<br>
   end if<br>
   end for<br>
   \(\text{\textit{frontier}}[w]\leftarrow x_w\)<br>
   if w\<s then \(\triangleright\) Cleanup: remove vertices with no successors in (w,s]<br>
   for each \(u\in\text{\textit{frontier}}\leftarrow\)<br>
   to dohasFuture \(\leftarrow\exists z\in(w,s]:(u,z)\in E\)<br>
   if \(\neg\text{\textit{hasFuture}}\) then<br>
remove<br>
_u_<br>
from<br>
_frontier_<br>
   end if<br>
   end for<br>
   end if<br>
   if w=s then<br>
\(\text{\textit{valueAtS}}\leftarrow x_w\)<br>
   end if<br>
   end for<br>
   \(g[v]\leftarrow\text{\textit{valueAtS}}\)<br>
end for<br>
return g<br>
Space: \(O(\omega)\) words (reused)<br>
Time: \(O(|F_I^\mathrm{mid}|\cdot|I|\cdot\Delta_\mathrm{max})=O(\omega\cdot|I|\cdot\Delta_\mathrm{max})\)

