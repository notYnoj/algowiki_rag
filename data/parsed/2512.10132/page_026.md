**Algorithm 4** Recursive Traceback

**Input:** DP DAG _G_, interval _I_=\[_i,j_\], boundary set \(B_\mathrm{left}\subseteq\{1,\dots,i-1\}\cup S_\mathrm{src}\), boundary value map \(\beta_\mathrm{left}:B_\mathrm{left}\rightarrow\mathcal{S}\), target \(s\in I\), value val<br>
Output: Path P from B<sub>left</sub> to s with internal vertices in I under the local DP induced by \((B_\mathrm{left},\beta_\mathrm{left})\)<br>
\(\ell\leftarrow j-i+1\triangleright\) Interval length<br>
\(\triangleright\) Base case: interval is small<br>
   if \(\ell\le B_\mathrm{base}\) then<br>
   return \(\mathrm{BaseCase}(G,I,B_\mathrm{left},\beta_\mathrm{left},s)\)<br>
   end if<br>
   \(\triangleright\) Recursive case: divide and conquer<br>
   \(m\leftarrow\lfloor(i+j)/2\rfloor\triangleright\) Midpoint<br>
   if \(s\le m\) then<br>
   return RecursiveTraceback(G, \[_i,m_\], B<sub>left</sub>, \(\beta_\mathrm{left}\), s, val)<br>
   end if<br>
   \(\triangleright\) Otherwise s\>m: perform midpoint search via middle frontier<br>
   \(F_I^\mathrm{mid}\leftarrow\mathrm{ComputeMiddleFrontier}(G,I,m)\)<br>
   \(\triangleright\) Step 1: Compute prefix values f(v) for all \(v\in F_I^\mathrm{mid}\)<br>
   \(f\leftarrow\mathrm{ComputePrefixValues}(G,[i,m],B_\mathrm{left},\beta_\mathrm{left},F_I^\mathrm{mid})\)<br>
   \(\triangleright\) Step 2: Compute suffix values g(v) for all \(v\in F_I^\mathrm{mid}\)<br>
   \(g\leftarrow\mathrm{ComputeSuffixValues}(G,I,F_I^\mathrm{mid},s)\)<br>
   \(\triangleright\) Step 3: Select canonical midpoint<br>
   \(v^\star\leftarrow\mathrm{SelectMidpoint}(F_I^\mathrm{mid},f,g)\)<br>
   \(\triangleright\) Step 4: Recurse on left subinterval<br>
   \(P_\mathrm{left}\leftarrow\mathrm{RecursiveTraceback}(G,[i,m],B_\mathrm{left},\beta_\mathrm{left},v^\star,f[v^\star])\)<br>
   \(\triangleright\) Step 5: Recurse on right subinterval with v<sup>⋆</sup> as fresh boundary source<br>
   \(B_\mathrm{right}\leftarrow\{v^\star\}\)<br>
   \(\beta_\mathrm{right}\leftarrow\emptyset\)<br>
   \(\beta_\mathrm{right}[v^\star]\leftarrow\mathbf{1}_\otimes\triangleright\) Multiplicative identity of the semiring<br>
   \(P_\mathrm{right}\leftarrow\mathrm{RecursiveTraceback}(G,[m+1,j],B_\mathrm{right},\beta_\mathrm{right},s,g[v^\star])\)<br>
   \(\triangleright\) Step 6: Concatenate path segments<br>
   if |P<sub>right</sub>|\>0 and P<sub>right</sub>[0]=v<sup>⋆</sup> then<br>
   \(P\leftarrow P_\mathrm{left}+P_\mathrm{right}[1:]\triangleright\) Remove duplicate v<sup>⋆</sup><br>
   else<br>
   \(P\leftarrow P_\mathrm{left}+P_\mathrm{right}\)<br>
   end if<br>
   return P<br>
   Space: \(O(\omega)\) words per call + O(polylogT) stack<br>
   Time: \(O(\omega\cdot\ell\cdot\Delta_\mathrm{max})\)

