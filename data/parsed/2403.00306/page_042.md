<tbc>**Algorithm 9** TraverStringRef\_Tree(_k,x_<sub>0</sub>_,r,x<sub>k</sub>,p<sub>k</sub>,_T_,J_)

1: \(\mathcal{T}'\leftarrow\emptyset\)

2: missed \(\leftarrow 0\)

3: **for all** \(Q\epsilon T\) **do**

4: \(Q'\leftarrow\) FeasibleOccurrencesReordered3(_k,x_<sub>0</sub>_,r,x<sub>k</sub>,p<sub>k</sub>,Q,J_)

5: **if** \(Q'\neq\emptyset\) **then**

6: \(\mathcal{T}\leftarrow\mathcal{T}'\cup\{Q'\}\)

7: **else**

8: missed \(\leftarrow\) missed+1

9: **if** missed _\>_|T|-_q_+2 **then**

10: **return**

11: **end if**

12: **end if**

13: **end for**

14: **if** IsMotifFast(\(x_k,q-2,\mathcal{T}'\))=**true** then

15: \(\mathcal{M}\leftarrow\mathcal{M}\cup\{x_k\}\)

16: **end if**

17: **if** _k=d_ **then**

18: **return**

19: **end if**

20: **if** \(|\mathcal{T}'|<q-2\) **then**

21: **return**

22: **end if**

23: Sort the elements of \(\mathcal{T}'\) in the nonincreasing order of \(min_{y\in\mathcal{Q}}d_H(x_k,y)\)(20) {The reference needs to be corrected}

24: **for** _p_<sub>_k_+1</sub>=_p<sub>k</sub>_+1 **to** _l_ **do**

25: **for all** \(\alpha\epsilon\Sigma\backslash\{x_k[J(p_{k+1})]\}\) **do**

26: \(x_{k+1}\leftarrow x_k\)

27: \(x_{k+1}[J(p_{k+1})]\leftarrow\alpha\)

28: \(d_0\leftarrow d+d_H(x_0|_{J_-(p_{k+1})},r|_{J_-(p_{k+1})})\)

29: **if** \(d_H(x_{k+1},r)\le min(d_0,2d-k-1)\) **then**

30: TraverStringRef\_Tree(\(k+1,x_0,r,x_{k+1},p_{k+1},\mathcal{T}',J\))

31: **end if**

32: **end for**

33: **end for**

## 3.2.4 PMS8

The key concepts of increasing efficiency in PMS8 from qPMS7 and qPMSPrune are described below:

