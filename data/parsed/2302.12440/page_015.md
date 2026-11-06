**Algorithm 3**

procedure NoisySort(A=(x<sub>1</sub>,...,x<sub>n</sub>),p)<br>
   \(S\leftarrow\{-\infty,\infty\}\).<br>
   for \(a\in A\) do<br>
   Add a to S with probability \(\frac{1}{logn}\). \(\triangleright\)Fully independent random bits.<br>
   Sort S using SafeSimpleSort. \(\triangleright\)Fully independent random bits.<br>
   for \(a\in A\backslash S\) do<br>
   Use SafeBinarySearch with \(\delta=\frac{1}{logn}\) to search the predecessor of a in S. \(\triangleright\)We use n<sup>2/3</sup> pairwise independent hash families to feed the first n<sup>2/3</sup> random bits of each SafeBinarySearch call, and errs if some call needs more than n<sup>2/3</sup> random bits.<br>
   Denote the returned answer as \(\hat{l}_a\).<br>
   \(X\leftarrow\emptyset\).<br>
   \(\mathcal{A}\leftarrow S\backslash\{-\infty,\infty\}\).<br>
   for \(l\in S\backslash\{\infty\}\) do<br>
   \(r\leftarrow\) next element in S.<br>
   \(B_l\leftarrow\{a\in A\backslash S:\hat{l}_a=l\}\).<br>
   if |B<sub>l</sub>|\>6log<sup>2</sup>n then<br>
\(X\leftarrow X\cup B_l\)<br>
   else<br>
   Sort B<sub>l</sub> using SafeWeakSort with error probability \(\frac{1}{nlogn}\). \(\triangleright\)We use n<sup>2/3</sup> pairwise independent hash families to feed the first n<sup>2/3</sup> random bits of each SafeWeakSort call, and errs if some call needs more than n<sup>2/3</sup> random bits.<br>
   while |B<sub>l</sub>|\>0 do<br>
   \(x\leftarrow\) first element in B<sub>l</sub>.<br>
   if SafeLessThan(x, l, \(\frac{1}{nlogn}\)) then<br>
\(B\leftarrow B\backslash\{x\}\)<br>
.<br>
   \(X\leftarrow X\cup\{x\}\).<br>
   else<br>
   break<br>
   while |B<sub>l</sub>|\>0 do<br>
   \(x\leftarrow\) last element in B<sub>l</sub>.<br>
   if SafeLessThan(r, x, \(\frac{1}{nlogn}\)) then<br>
\(B_l\leftarrow B_l\backslash\{x\}\)<br>
.<br>
   \(X\leftarrow X\cup\{x\}\).<br>
   else<br>
   break<br>
   Add B<sub>l</sub> to A between l and r.<br>
   for \(x\in X\) do<br>
   Insert x to A using SafeBinarySearch with \(\delta=\frac{1}{nlogn}\). \(\triangleright\)We use n<sup>2/3</sup> pairwise independent hash families to feed the first n<sup>2/3</sup> random bits of each SafeBinarySearch call, and errs if some call needs more than n<sup>2/3</sup> random bits.<br>
   return A.

