<tbc>**Algorithm 1** SP-LSD-Sort(A)

1: \(n\leftarrow A.length\)

2: **if** \(n\le 1\) **then**

3: **return**

4: **end if**

5: \(max\text{\_}val\leftarrow Maximum(A)\)

6: **if** _max\text{\_}val\<_0 **then**

7: **return**

8: **end if**

9: \(R\leftarrow\lfloor log_n(max\text{\_}val)\rfloor+1\)

10: **if** \(R\le 1\) **then**

11: Counting-Sort-by-Digit(A, A.begin, A.end, 1, n)

12: **return**

13: **end if**

14: Counting-Sort-by-Digit(A, A.begin, A.end, 1, n)

15: \(first\text{\_}active\leftarrow A.begin\)

16: **for** \(r\leftarrow 2\) **to** _R_-1 **do**

17: \(div\leftarrow n^{r-1}\)

18: \(partition\text{\_}point\leftarrow Stable\text{-Partition}(A,first\text{\_}active,A.end,\text{where}\lfloor x/div\rfloor=0)\)

19: Counting-Sort-by-Digit(A, partition\_point, A.end, div, n)

20: \(first\text{\_}active\leftarrow partition\text{\_}point\)

21: **if** _first\_active=A.end_ **then**

22: **return**

23: **end if**

24: **end for**

25: \(div\leftarrow n^{R-1}\)

26: Counting-Sort-by-Digit(A, first\_active, A.end, div, n)

