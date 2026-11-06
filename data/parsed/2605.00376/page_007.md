**Algorithm 1** Algorithm to correct one symbol error

**Input:**

Positive integers _m_ and _k_, with \(m\ge 2\); and a received vector **v**=[**v**<sub>1</sub>_,...,**v**<sub>n</sub>_], where _n=m+k_.

**Output:**

The corrected codeword **c**, or a declaration that more than one symbol error has occurred.

(1) Compute **s**=[**s**<sub>1</sub>**s**<sub>2</sub>_...**s**<sub>m</sub>_] according to Equation (4.2).

(2) If there exists \(j\in\{1,\dots,m\}\) such that \(\mathbf{s}_j\neq\mathbf{0}\) and **s**_<sub>i</sub>_=**0** for all \(i\neq j\), then set **e**<sub>_k+j_</sub>=**s**_<sub>j</sub>_ and conclude that the error occurred at position _k+j_. Otherwise, set _l_<sub>1</sub>=0.

(3) Set _l_<sub>1</sub>=_l_<sub>1</sub>+1. If _l_<sub>1</sub>_\>k_, then terminate the algorithm and declare that more than one symbol error has occurred (decoding failure). Otherwise, proceed to the next step.

(4) Compute the vectors:

\(\mathbf{y}_1^T=\mathbf{s}_1^T+A_{1l_1}A_{ml_1}^{-1}\mathbf{s}_m^T\)<br>
\(\mathbf{y}_2^T=\mathbf{s}_2^T+A_{2l_1}A_{1l_1}^{-1}\mathbf{s}_1^T\)<br>
\(\mathbf{y}_3^T=\mathbf{s}_3^T+A_{3l_1}A_{2l_1}^{-1}\mathbf{s}_2^T.\) (4.3)

\(\vdots\)<br>
\(\mathbf{y}_m^T=\mathbf{s}_m^T+A_{ml_1}A_{(m-1)l_1}^{-1}\mathbf{s}_{m-1}^T\)

(5) If \(\mathbf{y}_1=\mathbf{y}_2=\cdots=\mathbf{y}_m=\mathbf{0}\), then there is a symbol error at position _l_<sub>1</sub>, with magnitude given by

\(\mathbf{e}_{l_1}^T=A_{il_1}^{-1}\mathbf{s}_i^T,\) (4.4)

for any _i_=1_,...,m_. Otherwise, return to Step 3.

(6) Correct the received vector **v** by setting **c**=**v**-**e**.

This code can correct a single symbol error of length _b_=3, since \(\lfloor\frac{m}{2}\rfloor=\lfloor\frac{2}{2}\rfloor=1\). Assume the received vector **v**=[110110011011]. According to Step 1 of the Algorithm 1, we calculate the syndromes using the Equation (4.2):

\(\mathbf{s}_1=[011]\text{and}\mathbf{s}_2=[100].\)

Since the syndromes obtained are all nonzero, errors may have occurred in the information symbols. So, we make _l_<sub>1</sub>=1 and calculate the vectors as in Equation (4.3):

\(\mathbf{y}_1=[000]\text{and}\mathbf{y}_2=[000].\)

As both vectors are zero, the error in position _l_<sub>1</sub>=1 is confirmed. To obtain the magnitude of this error, calculate the Equation (4.4):

\(\mathbf{e}_1^T=A_{11}^{-1}\mathbf{s}_1^T=I_3^{-1}\left[\begin{array}{ c }
0 \\
1 \\
1
\end{array}\right]=\left[\begin{array}{ c c c }
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right]\left[\begin{array}{ c }
0 \\
1 \\
1
\end{array}\right]=\left[\begin{array}{ c }
0 \\
1 \\
1
\end{array}\right].\)

Therefore,

\(\mathbf{c}=[110110011011]-[\mathbf{011}00000000]=[101110011011]\)

is the codeword transmitted.

Now, we present the algorithm for correcting up to two symbol errors, which requires \(m\ge 4\). This algorithm incorporates specific steps of the Algorithm 1.

