**Algorithm 4** Sparse Selection

function SelectSparse(_X,k_)<br>
   \(Y\leftarrow\emptyset\)<br>
   \(L\leftarrow[0]*n\)<br>
   loop cn<sup>2/3</sup>logn times<br>
   Generate a subset S of X of size n<sup>1/3</sup><br>
   \(S\leftarrow\text{Sort}(S)\)<br>
   \(T\leftarrow S[k/n^{2/3}-n^{1/6}:k/n^{2/3}+n^{1/6}]\)<br>
   for \(x_i\in S[:k/n^{2/3}-n^{1/6}]\) do<br>
   \(L[i]\leftarrow L[i]+1\)<br>
   end for<br>
   \(Y\leftarrow Y\cup T\)<br>
   end loop<br>
   \(Z\leftarrow\emptyset\)<br>
   for i=0..n-1 do<br>
   if \(x_i\unknown\in Y\) and \(L[i]>\frac{c}{2}logn\) then<br>
   \(Z\leftarrow Z\cup\{x_i\}\)<br>
   end if<br>
   end for<br>
   \(\Gamma\leftarrow X\backslash(Y\cup Z)\)<br>
   if \(k\le|Z|\) then<br>
**return**<br>
GetMax<br>
(<br>
_Z_<br>
)<br>
   else if \(k\le|Z|+|Y|\) then<br>
\(Y\leftarrow 100\)<br>
-<br>
Sort<br>
(<br>
_Y_<br>
)<br>
   return Y[k-|<br>
_Z_<br>
|<br>
-<br>
1<br>
]<br>
   else<br>
**return**<br>
GetMin<br>
(<br>
\(\Gamma\)<br>
)<br>
   end if<br>
end function

**Lemma 6.2.** _If_ \(|L_x|\le\frac{1}{10}n^{2/3}\)_, for r\>_0 _and x<sub>i</sub>\>x<sub>L</sub> there exists c large enough that_ \(Pr\big[L[i]>\frac{c}{2}logn\big]<\frac{1}{n^r}\).

_Proof._ Consider the iterations in which _x<sub>i</sub>_ is chosen. By a union bound,<tbc>

\(Pr[L_x\cap S\neq\emptyset|x_i\in S]\le|L_x|\frac{n^{1/3}-1}{n-1}\le\frac{1}{10}n^{2/3}\frac{n^{1/3}-1}{n-1}\le\frac{2}{10}\)

<tbc>for _n_ sufficiently large. Conditioning on _x<sub>i</sub>_ being \(\in S\), the number of elements of _S_ that are \(\le x_k\) (call this _V_ ) follows a Hypergeometric(_n,k,n_<sup>1/3</sup>)<sup>†</sup> distribution. By a tail bound:

\(Pr\big[V\le k/n^{2/3}-n^{1/6}|x_i\in S\big]=Pr\big[V\le(k/n-n^{-1/6})n^{1/3}\big]\)<br>
\(\le e^{-2(n^{-1/6})^2n^{1/3}}\)<br>
\(=e^{-2}.\)

factor to 5. <sup>†</sup>If there are multiple items with value _x<sub>k</sub>_, the second argument can be larger than _k_, but that can only make the bounds better.

