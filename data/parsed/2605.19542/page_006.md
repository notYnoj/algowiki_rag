<tbc>_Proof._ Note that

\(\gamma_n=\sum_{j=1}^tw(c_j)c_j^n=\sum_{j=1}^tc_j^n\sum_{a\in A,b\in Ba+b=c_j}w_1(a)w_2(b)(a-b)\)<br>
\(=\sum_{a\in A,b\in B}w_1(a)w_2(b)(a-b)(a+b)^n.\)

Since<tbc>

\((a+b)^n=\sum_{i=0}^nC_n^ia^ib^{n-i},\)

<tbc>we have

\(\gamma_n=\sum_{a\in A,b\in B}w_1(a)w_2(b)(a-b)\sum_{i=0}^nC_n^ia^ib^{n-i}\)<br>
\(=\sum_{a\in A,b\in B}w_1(a)w_2(b)\sum_{i=0}^nC_n^ia^{i+1}b^{n-i}\)<br>
\(-\sum_{a\in A,b\in B}w_1(a)w_2(b)\sum_{i=0}^nC_n^ia^ib^{n+1-i}.\)

We observe that

\(\sum_{a\in A,b\in B}w_1(a)w_2(b)\sum_{i=0}^nC_n^ia^{i+1}b^{n-i}\)<br>
\(=\sum_{i=0}^nC_n^i\big(\sum_{a\in A}w_1(a)a^{i+1}\big)\big(\sum_{b\in B}w_2(b)b^{n-i}\big)\)<br>
\(=\sum_{i=0}^nC_n^i\alpha_{i+1}\beta_{n-i}.\)

Similarly, we also have

\(\sum_{a\in A,b\in B}w_1(a)w_2(b)\sum_{i=0}^nC_n^ia^ib^{n+1-i}\)<br>
\(=\sum_{i=0}^nC_n^i\big(\sum_{a\in A}w_1(a)a^i\big)\big(\sum_{b\in B}w_2(b)b^{n+1-i}\big)\)<br>
\(=\sum_{i=0}^nC_n^i\alpha_i\beta_{n+1-i}.\)

