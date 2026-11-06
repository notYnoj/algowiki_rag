<tbc>tree. To take the advantage of this procedure the position of the strings reordered so that the positions where the letters are different come earlier. For this an _l_-dimensional vector is computed for each pair at the root node of the search tree.

The pseudo-code of the algorithm TraverStringRef is given in Algorithm \[algorithm 8\].

**Algorithm 8** TraverStringRef

1: \(\mathcal{M}\leftarrow\emptyset\)

2: **for** \(i_1\leftarrow 1\) **to** _n-q_+1 **do**

3: **for** \(j_1\leftarrow 1\) **to** _m-l_+1 **do**

4: \(T\leftarrow\{S_h|i_1+1\le h\le n\}\)

5: Sort the elements of T in the nonincreasing order

6: **while** \(|\mathcal{T}|\ge q-2\) **do**

7: \(\mathcal{R}\leftarrow\) first element of T

8: \(\mathcal{T}\leftarrow\mathcal{T}\backslash\mathcal{R}\)

9: **for all** \(r\in\mathcal{R}\) **do**

10: Initialize the vector _J_

11: **if** \(d_H(s_{i_1j_1}^l,r)\le 2d\) **then**

12: TraverStringRef.Tree(0,\(s_{i_1j_1}^l,r,s_{i_1j_1}^l,0,\mathcal{T},J\))

13: **end if**

14: **end for**

15: **end while**

16: **end for**

17: **end for**

18: Output M

