**Algorithm 3** Approximation algorithm for Minimax-AlmostStable-sri

Input: \(I=(A,\succ):\) an sri instance<br>
Output: M: a matching<br>
\(M\leftarrow\text{Irving}(I)\triangleright\) Compute a stable matching or determine that none exists<br>
if M is not None then<br>
   return M<br>
   end if<br>
\(\text{side}(a_i)\leftarrow 0\forall a_i\in A\)<br>
\(\text{cross}(a_i)\leftarrow 0\forall a_i\in A\)<br>
   \(Q\leftarrow\{a_i\in A|d_i>2\cdot\text{cross}(a_i)\}\triangleright\) As d<sub>i</sub>\>0, this yields \(Q\leftarrow A\), but we maintain this for clarity<br>
   while \(Q\neq\varnothing\) do<br>
   \(a_i\leftarrow Q.\text{pop}()\)<br>
   oldside \(\leftarrow\text{side}(a_i)\)<br>
   side\((a_i)\leftarrow 1-\text{oldside}\)<br>
   for a<sub>j</sub> on \(\succ_i\) do<br>
   if side(a<sub>j</sub>) is oldside then<br>
\(\text{cross}(a_j)\leftarrow\text{cross}(a_j)+1\)<br>
   else<br>
\(\text{cross}(a_j)\leftarrow\text{cross}(a_j)-1\)<br>
   end if<br>
   if \(a_j\in Q\) and \(d_j\le 2\cdot\text{cross}(a_j)\) then<br>
_Q._<br>
remove<br>
(<br>
_a<sub>j</sub>_<br>
)<br>
   else if \(a_j\notin Q\) and \(d_j>2\cdot\text{cross}(a_j)\) then<br>
_Q._<br>
add<br>
(<br>
_a<sub>j</sub>_<br>
)<br>
   end if<br>
   end for<br>
   \(\text{cross}(a_i)\leftarrow d_i-\text{cross}(a_i)\triangleright\) We have flipped crossing and non-crossing entries<br>
   end while<br>
   \(I'\leftarrow(A,\succ')\triangleright\) Where initially \(\succ'_i\) is empty for all \(a_i\in A\)<br>
   for \(a_i\in A\) do<br>
   for a<sub>j</sub> on \(\succ_i\) (in decreasing order of preference) do<br>
   if \(\text{side}(a_i)\neq\text{side}(a_j)\) then<br>
\(\succ'_i.\text{append}(a_j)\)<br>
   end if<br>
   end for<br>
   end for<br>
   \(M\leftarrow\text{GaleShapley}(I')\triangleright\) Compute a stable matching of this new bipartite instance<br>
return M

<tbc>algorithm starts with an arbitrary cut (we choose _A_<sub>1</sub>=_A_ and \(A_2=\varnothing\), but any partition is valid) represented by an array "side" (that assigns either a 0 or 1 to every agent), and initialises cross(_a<sub>i</sub>_)=0 for all agents. We then keep track of all agents whose preference list length strictly exceeds twice their crossing number throughout the execution (which is all agents to start with). While this set is non-empty, we remove one such agent from the set and flip its set membership in the cut. Consequently, we make necessary adjustments to the crossing numbers and memberships of its neighbours. Once no such agent remains in the set, we have a desirable cut in which every agent ranks at least half as many agents from the opposite set as they rank in total (in \(\succ\)). Thus, we can consider the smi instance \(I'\) induced by the spanning bipartite subgraph associated with this final cut (_A_<sub>1</sub>_,A_<sub>2</sub>), and compute a stable matching _M_ of \(I'\) using the Gale-Shapley algorithm \[20\]. Then, by construction, _M_ has the property that, for all \(a_i\in A\),<tbc>

