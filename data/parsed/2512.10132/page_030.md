**Algorithm 8** Select Canonical Midpoint

Input: Frontier \(F_I^\mathrm{mid}\), prefix values f, suffix values g<br>
Output: Canonical vertex \(v^\star\in F_I^\mathrm{mid}\) maximizing \(f(v)\otimes g(v)\)<br>
   \(bestValue\leftarrow\) bottom element for \(\oplus\)<br>
   \(v^\star\leftarrow\mathrm{NULL}\)<br>
   \(\triangleright\) Iterate in canonical order for deterministic tie-breaking<br>
   for each \(v\in F_I^\mathrm{mid}\) (in increasing order) \(\leftarrow\)<br>
   to \(\mathrm{do}\text{\textit{combined Value}}\leftarrow f[v]\otimes g[v]\)<br>
   \(\text{\textit{combined Value}}\succ\text{\textit{bestValue then}}\)<br>
   \(bestValue\leftarrow\text{\textit{combined Value}}\)<br>
   \(v^\star\leftarrow v\)<br>
   end if<br>
   \(\triangleright\) Ties broken by iteration order (first occurrence wins)<br>
   end for<br>
   assert \(v^\star\neq\mathrm{NULL}\triangleright\) At least one vertex must maximize<br>
   return v<sup>⋆</sup><br>
   Space: O(1) words Time: \(O(|F_I^\mathrm{mid}|)=O(\omega)\)

**Example: Grid alignment.** For an \(m\times n\) grid DP with \(m\le n\) (e.g., global sequence alignment), the grid is topologically ordered column-by-column (or row-by-row), with T=(m+1)(n+1) and \(\omega=m+1\).

• _Global forward DP_ (Algorithm 3) sweeps through all (m+1)(n+1) cells in O(mn_) time using a single column buffer of size m+1.<tbc>

• _Recursive traceback_ (Algorithm 4) splits \(I=\left[1,(m+1)(n+1)\right]\) at the midpoint, corresponding roughly to column \(\lfloor n/2\rfloor\). The middle frontier \(F_I^\mathrm{mid}\) consists of all cells \((i,\lfloor n/2\rfloor)\) for \(0\le i\le m\).<tbc>

• _Prefix computation_ (Algorithm 6) performs one forward DP pass over columns \(0,\dots,\lfloor n/2\rfloor\) with boundary at the left edge.<tbc>

• _Suffix computation_ (Algorithm 7) runs a forward DP for each frontier cell \((i,\lfloor n/2\rfloor)\) over columns \(\lfloor n/2\rfloor+1,\dots,n\) with that cell as boundary.<tbc>

• _Midpoint selection_ (Algorithm 8) chooses the row i<sup>⋆</sup> maximizing the combined value.<tbc>

• _Recursion_ splits into subproblems on the left and right halves of the grid, each with half the column range.

The recursion depth is O(logn), and each level reuses the same O(m) workspace, giving total space O(m+logn) words as in Corollary 1.

