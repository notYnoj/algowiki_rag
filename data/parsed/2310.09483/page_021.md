_Proof._ This is implicitly proven in the previous lemma, where we prove the position in the original array of _x_<sup>∗</sup> is less than _k_.

**Corollary 6.11.** _If x_<sup>∗</sup> _is the item returned by `Select+`, for any r\>_0 _there exists c sufficiently large that_ \(x^*\ge_{200}x_k\) _with probability_ \(>1-\frac{1}{n^r}\)

_Proof._ Symmetric.

**Theorem 6.12.** \(\text{\textit{Select}}\pm\) _uses O(n_log<sup>6/5</sup>_n_) _comparisons and_ 100 _rounds._

_Proof._ All comparisons are done in `100-Sort`, so the number of comparisons is _O_((_n_<sup>5/6</sup>log_n_)<sup>6/5</sup>)=_O(n_log<sup>6/5</sup>_n_). Since `100-Sort` takes 100 rounds, so does \(\text{\texttt{Select}}\pm\).

## 6.3 Combining

**Algorithm 6** Pivot

function Count(_X,x<sub>i</sub>_)<br>
   \(c\leftarrow 0\)<br>
   for \(x\in X\) do<br>
   if x\<<sub>c</sub>x<sub>i</sub> then<br>
   \(c\leftarrow c+1\)<br>
   end if<br>
   end for<br>
   return c<br>
end function

**Algorithm 7** Selection

function Select(X,k)<br>
   \(x_i\leftarrow\text{SelectSparse}(X,k)\)<br>
   \(c_i\leftarrow\text{\texttt{Count}}(X,x_i)\)<br>
   if c<sub>i</sub>\<k then<br>
   \(x_j\leftarrow\text{Select}-(X,k)\)<br>
   if x<sub>j</sub>\><sub>c</sub>x<sub>i</sub> then return x<sub>j</sub><br>
   else return x<sub>i</sub><br>
   end if<br>
   else<br>
   \(x_j\leftarrow\text{Select}+(X,k)\)<br>
   if x<sub>j</sub>\<<sub>c</sub>x<sub>i</sub> then return x<sub>j</sub><br>
   else return x<sub>i</sub><br>
   end if<br>
end function

**Lemma 6.13.** _For any r\>_0_, we can choose c sufficiently large that_ \(|x_k-x^*|\le max(200,1+min(|x_k-x_i|,|x_k-x_j|))\) _with probability_ \(>1-\frac{1}{n^r}\).

_Proof._ By symmetry, we may assume without loss of generality that _c<sub>i</sub>\<k_. In this case, we return the item with the larger `Count`. Since we return the maximum of _x<sub>i</sub>_ and _x<sub>j</sub>_ (according to the<tbc>

