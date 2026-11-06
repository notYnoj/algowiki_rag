**Algorithm 2** Subroutine _FillDiagonally(h,diag,_MaxVldx)

1: \(j\leftarrow 1\)

2: **for** \(s\leftarrow 1\) to _n_<sub>1</sub>-_diag_ **do**

3: \(i\leftarrow s+diag\)

4: \(L(i,s,h)\leftarrow\infty\triangleright\) Initialize.

5: **while** \(j\le n_2\) **do**

6: \(x\leftarrow\text{lcsuf}(T_1[1..i],T_2[1..j])\)

7: **if** j=L(i-1_,s,h_) or x\>0 and \(j\ge x+L(i-x,s-x,h-1)\) **then**

8: \(L(i,s,h)\leftarrow j\triangleright\) By Lemma 4.

9: **break**

10: **end if**

11: \(j\leftarrow j+1\)

12: **end while**

13: **if** \(L(i,s,h)=\infty\) **then**

14: \(\text{MaxVldx}[h]\leftarrow s-1\)

15: **return**

16: **end if**

17: \(j\leftarrow j+1\)

18: **end for**

19: **return**

at most \(n_1-\ell_h\) diagonal lines where \(\ell_h\) is the largest _s_ such that \(L(i,s,h)<\infty\) for some _i_, which is equivalent to the final value of MaxVldx\[_h_\]. Also, for each diagonal line in _L<sub>h</sub>_, at most \(\ell_h+1\) cells are accessed while processing the line. Further, such cells can be computed in _O(n_<sub>1</sub>-_diag+n_<sub>2</sub>)=_O(n_<sub>2</sub>) time by _FillDiagonally_ since the value of the positive integer _j_ is incremented by 1 at the end of the inner while-loop and _j_ is upper-bounded by _n_<sub>2</sub>. Hence the computation time to fill the table _L<sub>h</sub>_ is \(O(n_2(n_1-\ell_h+1))\) and the size of _L<sub>h</sub>_ is \(O(\ell_h(n_1-\ell_h+1))\). Thus, the total time complexity can be written as \(O(\sum_{h=1}^fn_2(n_1-\ell_h+1))\). From the definition of SegLCS, \(\ell_1\ge\ell/f\) holds since \(\ell=\text{slcs}(T_1,T_2,f)\) and \(\ell_1\) is the length of the longest common factor of _T_<sub>1</sub> and _T_<sub>2</sub>. Similarly, \(\ell_h\ge h\ell/f\) holds for \(1\le h\le f\). Thus, the total time complexity is \(O(fn_2(n_1-\ell+1))\) since \(\sum_{h=1}^fn_2(n_1-\ell_h+1)\le\sum_{h=1}^fn_2(n_1-h\ell/f+1)=fn_2(n_1-\ell/2+1)-n_2\ell/2\).

Finally, the total size of tables we actually use is \(O(max_h\{\ell_h(n_1-\ell_h+1)\})\) since our algorithm can compute each table _L<sub>h</sub>_ only using the values in at most two tables _L<sub>h</sub>_ and _L_<sub>_h_-1</sub>. Again, since \(\ell_h\ge h\ell/f\ge\ell/f\) holds for each \(1\le h\le f\), the total space complexity is \(O(\ell(n_1-\ell/f+1))\). We note that, although we depict table _L<sub>h</sub>_ as a two-dimensional table in our examples, we can easily implement each table as one-dimensional array of size \(O(\ell_h(n_1-\ell_h+1))\) representing the diagonal lines.

To summarize, we obtain Theorem 5.

## 6 Conclusions and discussions

In this paper, we have studied two basic problems concerning _f_-segmental subsequences: the pattern matching problem and the LCS problem. Concerning the former, we have presented a quadratic- time algorithm for general \(f\ge 1\) and a linear-time algorithm for \(f\le 2\). We also argued that the quadratic time complexity is unavoidable under the strong exponential-time hypothesis. The latter problem has already been studied in the literature The _f_-segmental LCS problem and its variants<tbc>

