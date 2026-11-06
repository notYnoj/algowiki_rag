<tbc>**Algorithm 6** qPMS7-Tree(_k,x_<sub>0</sub>_,r,x<sub>k</sub>,p<sub>k</sub>,_T)

1: \(\mathcal{T}'\leftarrow\emptyset\)

2: **for all** \(Q\epsilon\mathcal{M}\) **do**

3: \(Q'\leftarrow\text{FeasibleOccurrences3}(x_0,r,x_k,p_k,Q)\)

4: **if** \(Q'\neq\emptyset\) **then**

5: \(\mathcal{T}\leftarrow\mathcal{T}'\cup\{Q'\}\)

6: **end if**

7: **end for**

8: **if** \(|\mathcal{T}'|<q-2\) **then**

9: **return**

10: **end if**

11: **if** \(d_H(x_k,x_0)\le d\) and \(d_H(x_k,r)\le d\) and IsMotif\((x_k,q-2,\mathcal{T}')\)=**true** then

12: \(\mathcal{M}\leftarrow\mathcal{M}\cup\{x_k\}\)

13: **end if**

14: **if** _k=d_ **then**

15: **return**

16: **end if**

17: **for** _p_<sub>_k_+1</sub>=_p<sub>k</sub>_+1 **to** _l_ **do**

18: **for all** \(\alpha\epsilon\Sigma\backslash\{x_k[p_{k+1}]\}\) **do**

19: \(z|_{I_+(p_{k+1}-1)}\leftarrow x_k|_{I_+(p_{k+1}-1)}\)

20: \(z[p_{k+1}]\leftarrow\alpha\)

21: \(x_{k+1}|_{I_+(p_{k+1})}\leftarrow z\)

22: **if** _d<sub>H</sub>(z,x_<sub>0</sub>|<sub>_I_<sub>+</sub>(_p_<sub>_k_+1</sub>)</sub>)_\>d<sub>H</sub>(z,r_|<sub>_I_<sub>+</sub>(_p_<sub>_k_+1</sub>)</sub>) **then**

23: \(x_{k+1}|_{I_-(p_{k+1})}\leftarrow x_k|_{I_-(p_{(k+1))}}\)

24: **else**

25: \(x_{k+1}|_{I_-(p_{k+1})}\leftarrow r|_{I_-(p_{(k+1))}}\)

26: **end if**

27: qPMS7-Tree(_k_+1_,x_<sub>0</sub>_,r,x_<sub>_k_+1</sub>_,p_<sub>_k_+1</sub>,T \('\))

28: **end for**

29: **end for**

**Algorithm 7** FeasibleOccurrences3(_x_<sub>0</sub>_,r,x<sub>k</sub>,p<sub>k</sub>,_Q)

1: \(Q'\leftarrow\emptyset\)

2: \(d_x\leftarrow d-d_H(x_k|_{I_+(p_k)},x_0|_{I_+(p_k)})\)

3: \(d_r\leftarrow d-d_H(x_k|_{I_+(p_k)},r|_{I_+(p_k)})\)

4: **for all** \(y\epsilon Q\) **do**

5: \(d_y\leftarrow d-d_H(x_k|_{I_+(p_k)},y|_{I_+(p_k)})\)

6: **if** \(B(x_0|_{I_-(p_k)},d_x)\cap B(r|_{I_-(p_k)},d_r)\cap B(y|_{I_-(p_k)},d_y)\neq\emptyset\) **then**

7: \(Q'\leftarrow Q'\cup\{y\}\)

8: **end if**

9: **end for**

10: **return** \(Q'\)

