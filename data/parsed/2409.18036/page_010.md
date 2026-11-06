Data: a Bucket-Grouping Structure BG-Str(_X_), PSS query parameters \((\alpha,\beta)\), the current recursion level \(\ell_\mathrm{cur}\)<br>
Result: a PSS result, with parameters \((\alpha,\beta)\), \(T\subseteq X\)<br>
\(N\leftarrow|X|\);<br>
\(j_1\leftarrow\left\lfloor\frac{\lfloor\mathrm{log}_2\frac{W_X(\alpha,\beta)}{N^2}\rfloor-1}{\mathrm{log}_2N}\right\rfloor\), the maximum possible \((\alpha,\beta)\)-insignificant group index;<br>
\(T_1\leftarrow\) QueryInsignificant(BG-Str(_X_), \((\alpha,\beta)\), \(j_1\cdot\mathrm{log}_2N\)) // Algorithm 2;<br>
\(j_2\leftarrow\lfloor\frac{\lceil\mathrm{log}_2W_X(\alpha,\beta)\rceil}{\mathrm{log}_2N}\rfloor\), the minimum possible \((\alpha,\beta)\)-certain group index;<br>
\(T_2\leftarrow\) QueryCertain(BG-Str(_X_), \((\alpha,\beta)\), \(j_2\cdot\mathrm{log}_2N\)) // Algorithm 3;<br>
\(T_3\leftarrow\emptyset\);<br>
for j from j<sub>1</sub>+1 to j<sub>2</sub>-1 do<br>
   \(T'_3\leftarrow\) QueryASignificantGroup(BG-Str(_X_), \((\alpha,\beta)\), j, \(\ell_\mathrm{cur}\)) // Algorithm 4;<br>
   \(T_3\leftarrow T_3\cup T'_3\);<br>
\(T\leftarrow T_1\cup T_2\cup T_3\);<br>
return T;

<tbc>item _x_ with sampling probability \(p_x(\alpha,\beta)\), we first sample _x_ as a _potential item_ with some probability \(p'\ge p_x(\alpha,\beta)\), and then, we accept this item _x_ as a PSS result with probability \(\frac{p_x(\alpha,\beta)}{p'}\) independently. In this way, item _x_ will be sampled with probability \(p_x(\alpha,\beta)\) independently as required in the PSS query.

Next, we claim that that all the mathematical computations involved in Algorithm 1 can be evaluated in _O_(1) time in the Word RAM model. To prove this, it suffices to show the following Claim 4.3. As a result, the largest index _j_<sub>1</sub> of the insignificant groups and the smallest index _j_<sub>2</sub> of the certain groups can be computed in _O_(1) time in the Word RAM model, as \(W_X(\alpha,\beta)\) is a rational number that satisfies the conditions in Claim 4.3.

Claim 4.3. \[<sup>∗</sup>\] _Consider a rational number x\>_0 _with its numerator and denominator being O_(1)_-word integers, then_ \(\lceil\mathrm{log}_2(x)\rceil\) _and_ \(\lfloor\mathrm{log}_2(x)\rfloor\) _can be calculated in O_(1) _time._

<u>_Handling the Insignificant Instance (Algorithm 2)_.</u> By definition, each item _x_ in the buckets in all those \((\alpha,\beta)\)-insignificant groups has probability at most \(\frac{1}{N^2}\) to be sampled. Thus, we first generate a _bounded geometric variate_ \(k\sim\) B-Geo\((\frac{1}{N^2},N+1)\) to simulate the process of flipping a Bernoulli coin \(\mathrm{Ber}(\frac{1}{N^2})\) for each item, one by one, and _k_ is the index of the first item to be sampled. Clearly, if _k\>N_, then nothing will be sampled and thus done. Otherwise, Algorithm 2 first collects all the items in this insignificant instance and stores them in an array _A_. If _k\>|A_|, then it is done. But if \(k\le|A|\), the item _x_ at the _k_<sup>th</sup> index in _A_, i.e., _A_\[_k_\], is a potential item, and it is accepted in the sampling result with probability \(\frac{p_x(\alpha,\beta)}{1/N^2}\) . Thus, this item _x_ is equivalently sampled with probability \(p_x(\alpha,\beta)\). For each of the remaining items _x_, at index starting from _k_+1 in the array _A_, Algorithm 2 flips a Bernoulli coin with probability \(p_x(\alpha,\beta)\) to accept _x_. Therefore, each item _x_ in the array _A_ will be correctly sampled, independently, with probability \(p_x(\alpha,\beta)\).

In terms of query efficiency, recall that the bounded geometric variate \(k\sim\) B-Geo\((\frac{1}{N^2},N+1)\) can be generated in _O_(1) expected time. If _k\>N_, the running time cost is _O_(1). Otherwise, the process<tbc>

**Algorithm 1:** One-Level PSS Query Algorithm: Query(BG-Str(_X_), \((\alpha,\beta)\), \(\ell_\mathrm{cur}\))

