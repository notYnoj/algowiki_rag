<tbc>**Algorithm 2** Counting-Sort-by-Digit(A, start-iter, end-iter, div, base)

1: \(n\leftarrow\mathrm{Distance}(start-iter,end-iter)\)

2: **if** \(n\le 1\) **then**

3: **return**

4: **end if**

5: Let _count_\[0_..base_-1\] be a new array, initialized to 0

6: Let _output_\[1_..n_\] be a new array

7: **for** \(it\leftarrow start-iter\) **to** _end-iter_-1 **do**

8: \(digit\leftarrow\lfloor(*it)/div\rfloor\) (mod _base_)

9: \(count[digit]\leftarrow count[digit]+1\)

10: **end for**

11: **for** \(i\leftarrow 1\) **to** _base_-1 **do**

12: \(count[i]\leftarrow count[i]+count[i-1]\)

13: **end for**

14: **for** \(it\leftarrow end-iter-1\) **downto** _start-iter_ **do**

15: \(digit\leftarrow\lfloor(*it)/div\rfloor\) (mod _base_)

16: \(output[count[digit]]\leftarrow*it\)

17: \(count[digit]\leftarrow count[digit]-1\)

18: **end for**

19: \(i\leftarrow 1\)

20: **for** \(it\leftarrow start-iter\) **to** _end-iter_-1 **do**

21: \(*it\leftarrow output[i]\)

22: \(i\leftarrow i+1\)

23: **end for**

_Round 1 (div=1)_ The first round sorts by the least significant digit (val (mod 5)). The active range is `A\[0,4\]`.

- Digits: `\[4, 1, 0, 4, 3\]`<tbc>

- Result (after sorting): The `first\_active\_idx` remains `0`.

\(\begin{array}{ c c c c }
0 & 1 & 2 & 3 & 4 \\
620 & 1 & 3 & 4 & 124
\end{array}\)

_Round 2 (div=5)_ The active range is `A\[0,4\]`. The partition predicate is \(\lfloor x/5\rfloor=0\). This is TRUE for `1`, `3`, and `4`.

State after Partitioning: `STABLE-PARTITION` moves the sorted elements to the ’sorted’ region, partition is set at index `3`.

\(\begin{array}{ c c c c c }
0 & 1 & 2 & 3 & 4 \\
1 & 3 & 4 & 620 & 124 \\
\multicolumn{3}{c}{\text{Sorted}} & \multicolumn{3}{c}{\text{Active}} & \multicolumn{3}{c}{\text{Active}}
\end{array}\)

Action: `COUNTING-SORT` now runs on the active range `A\[3,4\]`.

- Digits (\(\lfloor\mathrm{val}/5\rfloor\) (mod 5)): `\[4, 4\]`<tbc>

**-** Result: The active range is sorted.

\(\begin{array}{ c c c c }
0 & 1 & 2 & 3 & 4 \\
1 & 3 & 4 & 620 & 124
\end{array}\)

