**Algorithm 3** FeasibleOccurrences2(_k,x<sub>k</sub>,_Q)

1: \(Q'\leftarrow\emptyset\)

2: **for all** \(y\epsilon Q\) **do**

3: **if** \(d_H(x_k,y)\le 2d-k\) **then**

4: \(Q'\leftarrow Q'\cup\{y\}\)

5: **end if**

6: **end for**

7: **return** \(Q'\)

**Algorithm 4** IsMotif\((x,q',\mathcal{T})\)

1: matched \(\leftarrow 0\)

2: **for all** \(Q\epsilon T\) **do**

3: found \(\leftarrow\) **false**

4: **for all** \(y\epsilon Q\) **do**

5: **if** \(d_H(x,y)\le d\) **then**

6: found \(\leftarrow\) **true**

7: break the inner loop

8: **end if**

9: **end for**

10: **if** found = **true then**

11: matched \(\leftarrow\) matched + 1

12: **if** matched \(\ge q'\) **then**

13: **return true**

14: **end if**

15: **end if**

16: **end for**

17: **return false**

## 3.2.2 qPMS7

Algorithm qPMS7 was proposed by \[1\] which was based on qPMSPrune \[9\]. Some speedup techniques were introduced to improve the runtime of Algorithm qPMSPrune. qPMS7 also searches for motifs by traversing trees. The primary difference from qPMSPrune is that it utilizes \(r\epsilon\mathcal{S}_2\) as well as \(x_0\epsilon\mathcal{S}_1\) to traverse a tree. The algorithm is based on the following observations.

**Observation 3.2** Let _M_ be any (_l,d,q_)-motif of the input strings _s_<sub>1</sub>_,...,s<sub>n</sub>_. Then there exist \(1\le i\neq j\le n\) and _l_-mer \(x\epsilon s_i^l\) and _l_-mer \(y\epsilon s_j^l\) such that _M_ is in \(\mathcal{B}(x,d)\cup\mathcal{B}(y,d)\) and _M_ is a (_l,d,q_-2)-motif of the input strings excluding _s<sub>i</sub>_ and _s<sub>j</sub>_.

Using an argument similar to the one in \[9\], we infer that it is enough to consider every pair of input strings _s<sub>i</sub>_ and _s<sub>j</sub>_ with \(1\le i,j\le(n-q+2)\). As a result, the above observation gets strengthened as follows.

**Observation 3.3** Let _M_ be any (_l,d,q_)-motif of the input strings _s_<sub>1</sub>_,...,s<sub>n</sub>_. Then there exist<tbc>

