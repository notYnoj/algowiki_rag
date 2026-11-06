**Algorithm 3** Exact algorithm for Max-sri problems with lists of length at most 2

Input: I : an sri instance<br>
Input: D : deviator agents<br>
Output: M : a matching<br>
\(M\leftarrow\varnothing\triangleright\) Initialise an empty solution<br>
for each path P=(a<sub>r<sub>1</sub></sub>a<sub>r<sub>2</sub></sub>a<sub>r<sub>3</sub></sub>...a<sub>r<sub>k</sub></sub>) of I involving an even number of k agents do<br>
   \(M\leftarrow M\cup\{\{a_{r_1},a_{r_2}\},\{a_{r_3},a_{r_4}\},\dots,\{a_{r_{k-1}},a_{r_k}\}\}\triangleright\) Add the only max-card matching<br>
end for<br>
for each path P=(a<sub>r<sub>1</sub></sub>a<sub>r<sub>2</sub></sub>a<sub>r<sub>3</sub></sub>...a<sub>r<sub>k</sub></sub>) of I involving an odd number of k agents do<br>
   \(M_t\leftarrow\{\{a_{r_1+2x-1},a_{r_1+2x}\}|1\le x\le\lfloor\frac{k}{2}\rfloor\}\triangleright\) Leave a<sub>r<sub>1</sub></sub> unmatched<br>
for each \(3\le s\le k\) in steps of 2 do<br>
   \(M'_t\leftarrow\{\{a_{r_{s+2x-1}},a_{r_{s+2x}}\}|1\le x\le\lfloor\frac{k}{2}\rfloor\}\triangleright\) Leave a<sub>r<sub>s</sub></sub> unmatched<br>
   if \(|\bigcup_{a_i\in D}bp_i(M'_t)|<|\bigcup_{a_i\in D}bp_i(M_t)|\) then \(\triangleright\) Replace with \(|ba(M'_t)\cap D|<|ba(M_t)\cap D|\) to minimise the number of blocking D agents instead<br>
   \(M_t\leftarrow M'_t\)<br>
   end if<br>
   end for<br>
   \(M\leftarrow M\cup M_t\)<br>
end for<br>
for each cycle C=(a<sub>r<sub>1</sub></sub>a<sub>r<sub>2</sub></sub>a<sub>r<sub>3</sub></sub>...a<sub>r<sub>k</sub></sub>) of I involving an even number of k agents do<br>
   \(M_1\leftarrow\{\{a_{r_1},a_{r_2}\},\{a_{r_3},a_{r_4}\},\dots,\{a_{r_{k-1}},a_{r_k}\}\}\)<br>
   \(M_2\leftarrow\{\{a_{r_1},a_{r_k}\},\{a_{r_2},a_{r_3}\},\dots,\{a_{r_{k-2}},a_{r_{k-1}}\}\}\)<br>
   if \(|\bigcup_{a_i\in D}bp_i(M_1)|\le|\bigcup_{a_i\in D}bp_i(M_2)|\) then \(\triangleright\) Replace with \(|ba(M_1)\cap D|\le|ba(M_2)\cap D|\) to minimise the number of blocking D agents instead<br>
   \(M\leftarrow M\cup M_1\)<br>
   else<br>
   \(M\leftarrow M\cup M_2\)<br>
   end if<br>
end for<br>
for each cycle C=(a<sub>r<sub>1</sub></sub>a<sub>r<sub>2</sub></sub>a<sub>r<sub>3</sub></sub>...a<sub>r<sub>k</sub></sub>) of I involving an odd number of k agents do<br>
   \(M_t\leftarrow\{\{a_{r_2},a_{r_3}\},\{a_{r_4},a_{r_5}\},\dots,\{a_{r_{k-1}},a_{r_k}\}\}\)<br>
   for each \(2\le s\le k\) do<br>
   \(M'_t\leftarrow\{\{a_{r_{s+x+1}},a_{r_{s+x+2}}\}|0\le x\le k-2\) in steps of 2}<br>
   if \(|\bigcup_{a_i\in D}bp_i(M'_t)|<|\bigcup_{a_i\in D}bp_i(M_t)|\) then \(\triangleright\) Replace with \(|ba(M'_t)\cap D|<|ba(M_t)\cap D|\) to minimise the number of blocking D agents instead<br>
   \(M_t\leftarrow M'_t\)<br>
   end if<br>
   end for<br>
   \(M\leftarrow M\cup M_t\)<br>
end for<br>
return M

<tbc>_D_ agents), so the correctness of this approach is easy to see. Notice, furthermore, that each such cycle with an odd number of agents _k_ admits _k_ different maximum-cardinality matchings, which are precisely maximum-cardinality matchings of the even-length paths resulting from the deletion of any one agent. We enumerate all such matchings and include the one that minimises the number of blocking pairs involving _D_ agents (or the number of blocking _D_ agents), so the correctness of this approach is easy to see too. Thus, the resulting matching we return is a maximum-cardinality matching of _I_ and minimises the total number of blocking pairs involving _D_ agents (or the total number of blocking _D_ agents).

Regarding time complexity, note that each component is dealt with exactly once. Before<tbc>

