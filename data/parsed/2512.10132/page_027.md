**Algorithm 5** Compute Middle Frontier

Input: DP DAG G, interval I=\[i,j\], midpoint m<br>
Output: Middle frontier \(F_I^\mathrm{mid}=\{v\in V_I:v\le m\text{and}\exists w>m,(v,w)\in E\}\)<br>
\(F_I^\mathrm{mid}\leftarrow\emptyset\)<br>
\(\triangleright\) Scan vertices up to midpoint<br>
for \(v\leftarrow i\) to \(\mathrm{min}\{m,j\}\leftarrow\)<br>
to dohasCrossingEdge \(\leftarrow\) false<br>
   \(\triangleright\) Check if v has successor beyond midpoint<br>
   for each \((v,w)\in E\leftarrow\)<br>
   if to then w\>m do<br>
   \(hasCrossingEdge\leftarrow\)<br>
true<br>
   break<br>
   end if<br>
   end for<br>
   if hasCrossingEdge then<br>
\(F_I^\mathrm{mid}\leftarrow F_I^\mathrm{mid}\cup\{v\}\)<br>
   end if<br>
end for<br>
return \(F_I^\mathrm{mid}\)<br>
Space: \(O(\omega)\) words<br>
Time: \(O((m-i+1)\cdot\Delta_\mathrm{max})\)

<tbc>_over all O_(log_T_) _levels of the recursion tree and noting that the intervals shrink geometrically, the total time is_

\(T_\mathrm{total}=O\left(\sum_{d=0}^{O(\mathrm{log}T)}\omega\cdot\frac{T}{2^d}\cdot\Delta_\mathrm{max}\right)=O(\omega\cdot T\cdot\Delta_\mathrm{max}\cdot\mathrm{log}T)=T\cdot\mathsf{poly}(\omega,\mathrm{log}T).\)

_In settings where the reversed graph G<sup>R</sup> also has frontier width_ \(O(\omega)\)_, one can replace the per-candidate suffix passes with a single backward DP (as in the classical Hirschberg algorithm), reducing the per-level cost and bringing the total running time closer to_ \(O(T\cdot\Delta_\mathrm{max})\) _while preserving the_ \(O(\omega\mathrm{log}T+\mathsf{polylog}T)\) _space bound._

**Implementation notes.** _Deterministic tie-breaking._ The fixed edge order \(\prec\) can be implemented by:

• Sorting edges lexicographically: \((u_1,v_1)\prec(u_2,v_2)\) if _u_<sub>1</sub>_\<u_<sub>2</sub>, or _u_<sub>1</sub>=_u_<sub>2</sub> and _v_<sub>1</sub>_\<v_<sub>2</sub>, or<tbc>

• Assigning each edge a unique timestamp during graph construction.

In Algorithm 9, iterating over edges in order \(\prec\) ensures that the first maximizing edge is selected.

_Base case threshold._ A practical choice is \(B_\mathrm{base}=\lceil(\mathrm{log}_2T)^2\rceil\). Smaller values increase recursion depth slightly; larger values increase the base-case space usage.

_Frontier management._ The cleanup steps in Algorithms 3, 6, and 7 are essential for maintaining the \(O(\omega)\) space bound. In practice, checking whether a vertex _u_ has successors beyond the current position can be done by:

1. Scanning the adjacency list successors(_u_), or<tbc>

2. Maintaining auxiliary data (e.g., the maximum successor index for each vertex) if preprocessing is permitted.

_Output path format._ The algorithms return paths as lists _P_=\[_v_<sub>0</sub>_,v_<sub>1</sub>_,...,v<sub>k</sub>_\] where \(v_0\in S_\mathrm{src}\), _v<sub>k</sub>=t_, and \((v_{i-1},v_i)\in E\) for all _i_. The output tape writes these vertices in order, contributing _O_(|_P_|) output size but no additional work-tape space.

