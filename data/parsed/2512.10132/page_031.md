**Algorithm 9** Base Case: Direct Traceback

**Input:** DP DAG _G_, small interval _I_=\[_i,j_\] with \(|I|\le B_\mathrm{base}\), boundary set _B_<sub>left</sub>, boundary value map \(\beta_\mathrm{left}\), target \(s\in I\)<br>
Output: Path P from B<sub>left</sub> to s with internal vertices in I under the local DP induced by \((B_\mathrm{left},\beta_\mathrm{left})\)<br>
\(\triangleright\) Build local DP table with predecessor pointers<br>
   \(dp\leftarrow\emptyset\triangleright\) Maps \(v\mapsto(x_v,\mathsf{pred}(v))\) in this subproblem<br>
   \(\triangleright\) Initialize boundary values for this subproblem<br>
   for each \(u\in B_\mathrm{left}\leftarrow\)<br>
   to do\(dp[u]\leftarrow(\beta_\mathrm{left}[u],\perp)\triangleright\) No predecessor inside I<br>
   end for<br>
   \(\triangleright\) Forward DP with predecessor tracking on I<br>
   for \(v\leftarrow i\) to \(j\leftarrow\)<br>
   if to then \(v\in B_\mathrm{left}\) do<br>
   continue<br>
   \(\triangleright\) Already initialized<br>
   end if<br>
   \(bestValue\leftarrow\) bottom element for \(\oplus\)<br>
   \(bestPred\leftarrow\perp\triangleright\) Find best predecessor using recurrence and tie-breaking<br>
   for each \((u,v)\in E\) (in order \(\prec\)) \(\leftarrow\)<br>
   if to then \(u\in dp\) do<br>
   \(candidateValue\leftarrow dp[u].value\otimes w_{u,v}\)<br>
   if candidate\(Value\succ bestValue\) then<br>
   \(bestValue\leftarrow candidateValue\)<br>
   \(bestPred\leftarrow u\)<br>
   end if<br>
   \(\triangleright\) First in edge order wins ties<br>
   end if<br>
   end for<br>
   \(dp[v]\leftarrow(bestValue,bestPred)\)<br>
   end for<br>
   \(\triangleright\) Backtrack from s to reconstruct path segment<br>
   \(P\leftarrow\) empty list<br>
   \(current\leftarrow s\)<br>
   while \(current\neq\perp\) and \(current\notin B_\mathrm{left}\) do<br>
   prepend current to P<br>
   \(current\leftarrow dp[current].predecessor\)<br>
   end while<br>
   \(\triangleright\) Add boundary vertex if reached<br>
   if \(current\in B_\mathrm{left}\) then<br>
prepend<br>
_current_<br>
to<br>
_P_<br>
   end if<br>
   return P<br>
   Space: \(O(\omega+B_\mathrm{base})=O(\omega+\mathrm{polylog}T)\) words<br>
   Time: \(O(B_\mathrm{base}\cdot\Delta_\mathrm{max})\)

