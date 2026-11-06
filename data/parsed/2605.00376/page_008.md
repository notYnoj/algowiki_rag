**Algorithm 2** Algorithm to correct two symbol errors

**Input:**<br>
Positive integers _m_ and _k_, with \(m\ge 4\); and a received vector **v**=\[**v**<sub>1</sub>_,...,_**v**_<sub>n</sub>_\], where _n=m+k_.

**Output:**<br>
The corrected codeword _c_, or a declaration that more than two symbol errors have occurred, or that decoding has failed.

(1) Compute **s**=\[**s**<sub>1</sub>**s**<sub>2</sub>_..._**s**_<sub>m</sub>_\] according to Equation (4.2).<tbc>

(2) If there exists \(j\in\{1,\dots,m\}\) such that \(\mathbf{s}_j\neq\mathbf{0}\) and **s**_<sub>i</sub>_=**0** for all \(i\neq j\), then set **e**<sub>_k+j_</sub>=**s**_<sub>j</sub>_ and conclude that the error occurred at position _k+j_. Otherwise, proceed to the next step.<tbc>

(3) If there exist \(j_1,j_2\in\{1,\dots,m\}\) with \(j_1\neq j_2\) such that \(\mathbf{s}_{j_1}\neq\mathbf{0}\), \(\mathbf{s}_{j_2}\neq\mathbf{0}\), and **s**_<sub>i</sub>_=**0** for all \(i\neq j_1,j_2\), then set **e**<sub>_k+j_<sub>1</sub></sub>=**s**<sub>_j_<sub>1</sub></sub> and **e**<sub>_k+j_<sub>2</sub></sub>=**s**<sub>_j_<sub>2</sub></sub>, and conclude that two symbol errors occurred at positions _k+j_<sub>1</sub> and _k+j_<sub>2</sub>. Otherwise, set _l_<sub>1</sub>=0.

4. Set _l_<sub>1</sub>=_l_<sub>1</sub>+1. If _l_<sub>1</sub>_\>k_, then terminate the algorithm and declare that more than two symbol errors have occurred (decoding failure). Otherwise, proceed to the next step.<tbc>

5. Compute the vectors of Equation (4.3).<tbc>

6. If \(\mathbf{y}_1=\mathbf{y}_2=\cdots=\mathbf{y}_m=\mathbf{0}\), then there is a symbol error at position _l_<sub>1</sub>, with magnitude given by<tbc>

\(\mathbf{e}_{l_1}^T=A_{il_1}^{-1}\mathbf{s}_i^T,\) \(\text{(4.5)}\)

for any _i_=1_,...,m_. Otherwise, proceed to the next step.<tbc>

7. If (**y**_<sub>i</sub>,_**y**<sub>_i_+1</sub>)=(**0**,**0**) for some _i_=1_,...,m_-1 or (**y**_<sub>m</sub>,_**y**<sub>1</sub>)=(**0**,**0**), but not all **y**_<sub>i</sub>_ are zero, then one symbol error occurs at position _l_<sub>1</sub> and a second symbol error occurs in the parity symbols, given by<tbc>

\(\mathbf{e}_{l_1}^T=A_{il_1}^{-1}\mathbf{s}_i^T\) \(\text{(4.6)}\)

and<tbc>

\(\mathbf{e}_{k+j}=\mathbf{s}_j-A_{jl_1}\mathbf{e}_{l_1},\) \(\text{(4.7)}\)

for any \(i\neq j\), where _j_ denotes the index corresponding to the nonzero syndrome component associated with the parity error. Otherwise, proceed to the next step.<tbc>

8. For each \(l_2\in\{l_1+1,\dots,k\}\), check whether<tbc>

\(\mathbf{y}_i^T=C^{r_{i-2}}\mathbf{y}_{i-1}^T,\) \(\text{(4.8)}\)

for all _i_=3,4_,...,m_ with<tbc>

\(r_{i-2}=\sigma(i,l_2)-\sigma(i-1,l_2)+Z(\sigma(i,l_1)-\sigma(i,l_2)-\sigma(i-1,l_1)+\sigma(i-1,l_2))-Z(\sigma(i-1,l_1)-\sigma(i-1,l_2)-\sigma(i-2,l_1)+\sigma(i-2,l_2)).\text{(4.9)}\)

If this condition holds, then two symbol errors are declared at positions _l_<sub>1</sub> and _l_<sub>2</sub>. Otherwise, return to Step 4.<tbc>

9. To determine the magnitudes of the errors, solve the linear system.<tbc>

\(\left\{\begin{array}{ c }
A_{il_1}\mathbf{e}_{l_1}^T+A_{il_2}\mathbf{e}_{l_2}^T=\mathbf{s}_i^T \\
A_{jl_1}\mathbf{e}_{l_1}^T+A_{jl_2}\mathbf{e}_{l_2}^T=\mathbf{s}_j^T,
\end{array}\right.\) \(\text{(4.10)}\)

for any _i,j_=1,2_,...,m_ with \(i\neq j\).<tbc>

10. Correct the received vector **v** by setting **c**=**v**-**e**.

The following theorem demonstrates that Algorithm 2 indeed corrects up to two symbol errors of length _b_.

