Data: a Bucket-Group Structure BG-Str(_X_), PSS query parameters \((\alpha,\beta)\), the maximum possible bucket index _i_<sub>1</sub> in the \((\alpha,\beta)\)-insignificant groups<br>
Result: a PSS result \(T_1\subseteq X\) within all the \((\alpha,\beta)\)-insignificant groups<br>
initialize \(T_1\leftarrow\emptyset\) and \(N\leftarrow|X|\);<br>
\(k\leftarrow\) B-Geo(1/_N_<sup>2</sup>,_N_+1);<br>
if \(k\le N\) then<br>
   \(A\leftarrow\) the set of all the items in the non-empty buckets (with bucket index \(\le i_1\));<br>
   if |A|\<k then<br>
   return \(\emptyset\);<br>
   \(x\leftarrow A[k]\), the k<sup>th</sup> item in A;<br>
   \(T_1\leftarrow T_1\cup\{x\}\) with probability \(\frac{p_x(\alpha,\beta)}{1/N^2}\) ;<br>
   for \(i\leftarrow\{k+1,\dots,|A|\}\) do<br>
   \(x\leftarrow A[i]\), the i<sup>th</sup> item in A;<br>
   \(T_1\leftarrow T_1\cup\{x\}\) with probability \(p_x(\alpha,\beta)\);<br>
return T<sub>1</sub>;

Data: a Bucket-Group Structure BG-Str(_X_), PSS query parameters \((\alpha,\beta)\), the minimum possible bucket index _i_<sub>2</sub> in the \((\alpha,\beta)\)-certain groups<br>
Result: a PSS result \(T_2\subseteq X\) within all the \((\alpha,\beta)\)-certain groups<br>
initialize \(T_2\leftarrow\emptyset\);<br>
   for each non-empty buckets B<sub>X</sub>(i_) with bucket index \(i\ge i_2\) in BG-Str(_X_) do<br>
\(T_2\leftarrow T_2\cup B_X(i)\)<br>
;<br>
return T<sub>2</sub>;

Data: a Bucket-Group Structure BG-Str(_X_), PSS query parameters \((\alpha,\beta)\), an \((\alpha,\beta)\)-significant group index _j_, the current recursion level \(\ell_\mathrm{cur}\)<br>
Result: a PSS result \(T_3\subseteq X\) within the \((\alpha,\beta)\)-significant group G<sub>X</sub>(_j_)<br>
if G<sub>X</sub>(j_) is empty then<br>
return \(\emptyset\);<br>
// obtain a PSS result T<sub>Y<sub>j</sub></sub> with parameters \((0,W_X(\alpha,\beta))\) on the next-level item set Y<sub>j</sub> of G<sub>X</sub>(j);<br>
if \(\ell_\mathrm{cur}=1\) then<br>
\(T_{Y_j}\leftarrow\) Query(BG-Str(Y<sub>j</sub>), \((0,W_X(\alpha,\beta))\), \(\ell_\mathrm{cur}+1\)) // recursively invoke Algorithm 1;<br>
else<br>
\(T_{Y_j}\leftarrow\) QueryFinalLevel(BG-Str(Y<sub>j</sub>), \((0,W_X(\alpha,\beta))\)) // in Section 4.4;<br>
\(T_3\leftarrow\) ExtractItems(BG-Str(_X_), T<sub>Y<sub>j</sub></sub>, \((0,W_X(\alpha,\beta))\)) // Algorithm 5;<br>
return T<sub>3</sub>;

## D Proofs for Section 4 (Our Optimal DPSS Algorithm)

Claim 4.3. _Consider a rational number x\>_0 _with its numerator and denominator being O_(1)_-word integers, then_ \(\lceil\mathrm{log}_2(x)\rceil\) _and_ \(\lfloor\mathrm{log}_2(x)\rfloor\) _can be calculated in O_(1) _time._

**Algorithm 2:** QueryInsignificant(BG-Str(_X_), \((\alpha,\beta)\), _i_<sub>1</sub>)

**Algorithm 3:** QueryCertain(BG-Str(_X_), \((\alpha,\beta)\), _i_<sub>2</sub>)

**Algorithm 4:** QueryASSignificantGroup(BG-Str(_X_), \((\alpha,\beta)\), _j_, \(\ell_\mathrm{cur}\)

