<tbc>within the component, if one exists, and, otherwise, include a maximum-cardinality matching that leaves exactly one agent unmatched - which agent to exclude depends on the occurrences of deviator agents in the cycle.

**Algorithm 2** Exact algorithm for sri problems with lists of length at most 2

Input: I : an sri instance<br>
Input: D : deviator agents<br>
Output: M : a matching<br>
\(M\leftarrow\varnothing\triangleright\) Initialise an empty solution<br>
for each path P=(a<sub>r<sub>1</sub></sub>a<sub>r<sub>2</sub></sub>a<sub>r<sub>3</sub></sub>...a<sub>r<sub>k</sub></sub>) of I involving k agents do<br>
   \(M\leftarrow M\cup\mathsf{GaleShapley}(I|_{A(P)})\)<br>
end for<br>
for each cycle C=(a<sub>r<sub>1</sub></sub>a<sub>r<sub>2</sub></sub>a<sub>r<sub>3</sub></sub>...a<sub>r<sub>k</sub></sub>) of I involving an even number of k agents do<br>
   \(M\leftarrow M\cup\mathsf{GaleShapley}(I|_{A(C)})\)<br>
end for<br>
for each cycle C=(a<sub>r<sub>1</sub></sub>a<sub>r<sub>2</sub></sub>a<sub>r<sub>3</sub></sub>...a<sub>r<sub>k</sub></sub>) of I involving an odd number of k agents do<br>
   \(M_t\leftarrow\mathsf{Irving}(I|_{A(C)})\triangleright\) Find a stable matching, if one exists<br>
   if M<sub>t</sub> exists then<br>
   \(M\leftarrow M\cup M_t\)<br>
   else<br>
   if there exist a<sub>r<sub>u</sub></sub>,a<sub>r<sub>v</sub></sub> in A(C)\\D such that a<sub>r<sub>v</sub></sub> is a<sub>r<sub>u</sub></sub>’s first choice then<br>
   \(M\leftarrow M\cup\{\{a_{r_{v+2x-1}},a_{r_{v+2x}}\}|1\le x\le\lfloor\frac{k}{2}\rfloor\}\triangleright\) Leave a<sub>r<sub>v</sub></sub> unmatched<br>
   else if there exist \(a_{r_u}\in A(C)\backslash D\), \(a_{r_v}\in A(C)\cap D\) such that a<sub>r<sub>v</sub></sub> is a<sub>r<sub>u</sub></sub>’s first choice then<br>
   \(M\leftarrow M\cup\{\{a_{r_{v+2x-1}},a_{r_{v+2x}}\}|1\le x\le\lfloor\frac{k}{2}\rfloor\}\triangleright\) Leave a<sub>r<sub>v</sub></sub> unmatched<br>
   else<br>
   \(M\leftarrow M\cup\{\{a_{r_1},a_{r_2}\},\{a_{r_3},a_{r_4}\},\dots,\{a_{r_{k-2}},a_{r_{k-1}}\}\}\triangleright\) Leave a<sub>r<sub>k</sub></sub> unmatched<br>
   end if<br>
   end if<br>
end for<br>
return M

**Theorem 6.1.** _Let_ \(I=(A,\succ)\) _be an_ sri _instance with n agents and let_ \(D\subseteq A\) _be a set of deviators. If all preference lists of I are of length at most 2, then Algorithm 2 computes an optimal solution to_ Deviator-sri _and_ Deviator-BA-sri _in O(n_) _time._

_Proof._ Let _M_ be the matching returned by Algorithm 2. First, notice that distinct connected components have - by definition - independent preference systems, so no two agents from distinct connected components can form a blocking pair together. Hence, any blocking pairs and any blocking agents admitted by _M_ must stem from our treatment of cycles _C_ involving an odd number of agents, because all other components are bipartite and must admit stable matchings, which we include in _M_.

Now, let _C_=(_a_<sub>_r_<sub>1</sub></sub>_a_<sub>_r_<sub>2</sub></sub>_a_<sub>_r_<sub>3</sub></sub>_...a<sub>r<sub>k</sub></sub>_) be a cycle involving an odd number of agents _k_. If _C_ admits a stable matching, then we find it using Irving’s algorithm \[34\]. Otherwise, _C_ must be an ordered cycle such that either \(a_{r_{i+1}}\succ_{r_i}a_{r_{i-1}}\) or \(a_{r_{i-1}}\succ_{r_i}a_{r_{i+1}}\) for all \(1\le i\le k\) (addition and subtraction taken modulo _k_) \[44\]. Without loss of generality, suppose that the former case holds, i.e., that every agent prefers their successor over their predecessor (as indicated by the increasing index within _C_). Then, when we include one of the maximum-cardinality matchings of _C_, i.e., a matching that leaves exactly one _a<sub>r<sub>j</sub></sub>_ agent unmatched, the minimum number of (two) blocking agents (one blocking pair) is created. Hence, to minimise the number of blocking _D_ agents contained in _C_ (or to minimise the number of blocking pairs involving agents in _D_), we shall include a maximum-cardinality matching that leaves an agent \(a_{r_j}\notin D\) unmatched (_a<sub>r<sub>v</sub></sub>_<tbc>

