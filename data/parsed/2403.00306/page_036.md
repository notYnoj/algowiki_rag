<tbc>Moreover the algorithm prunes the branch if _q"\<q_-1 where _q"_ is the number of input strings _s<sub>j</sub>_ such that \(d_H(t,s_j)\le 2d-d_H(t,x)\).

The time and space complexities of algorithm qPMSPrune are given by _O_((_n-q_+1)_nm_<sup>2</sup>_n_<sub>B</sub>(_l,d_)) and _O(nm_<sup>2</sup>) respectively. The pseudocode of qPMSPrune is shown in algorithm algorithm 1.

**Algorithm 1** qPMSPrune

1: \(M\leftarrow\emptyset\)

2: **for** _i_=1 **to** _n-q_+1 **do**

3: **for** _j_=1 **to** _m-l_+1 **do**

4: \(T\leftarrow\{S_h|1\le h\le N,h\neq i\}\)

5: qPMSPruneI\_Tree(0,\(s_{ij}^l,0,T\))

6: **end for**

7: **end for**

8: Output _M_

**Algorithm 2** qPMSPrune\_Tree(_k,x<sub>k</sub>,p<sub>k</sub>,_T)

1: \(T'\leftarrow\emptyset\)

2: **for all** \(Q\epsilon T\) **do**

3: \(Q'\leftarrow\) FeasibleOccurrences2(_k,x<sub>k</sub>,Q_)

4: **if** \(Q'\neq\emptyset\) **then**

5: \(T\leftarrow T'\cup\{Q'\}\)

6: **end if**

7: **end for**

8: **if** \(|T'|<q-1\) **then**

9: **return**

10: **end if**

11: **if** IsMotif(\(x_k,q-1,T'\)) = **true then**

12: \(M\leftarrow M\cup\{x_k\}\)

13: **end if**

14: **if** _k=d_ **then**

15: **return**

16: **end if**

17: **for** _p_<sub>_k_+1</sub>=_p<sub>k</sub>_+1 **to** _l_ **do**

18: **for all** \(\alpha\epsilon\Sigma\backslash\{x_k[p_{k+1}]\}\) **do**

19: \(x_{k+1}\leftarrow x_k\)

20: \(x_{k+1}[p_{k+1}]\leftarrow\alpha\)

21: qPMSPruneI\_Tree(\(k+1,x_{k+1},p_{k+1},T'\))

22: **end for**

23: **end for**

