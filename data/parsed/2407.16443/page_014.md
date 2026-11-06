Putting it all together we obtain that

\(\text{\texttt{sum}}(L,i)=\text{\texttt{trunc}}(\alpha_i,\text{\texttt{sum}}(L,i-1))+2^{-\alpha_i}\)<br>
\(=\text{\texttt{sum}}(L,i-1)+2^{-\alpha_i}\)<br>
\(=\text{\texttt{sum}}(L,i-1)+2^{-\left(-log_2\phi_{\lfloor\frac{i}{2}\rfloor}+1\right)}\)<br>
\(=\text{\texttt{sum}}(L,i-1)+\frac{\phi_{\lfloor\frac{i}{2}\rfloor}}{2},\)

where the second equality holds because the \(\alpha_i\) are non-decreasing, and therefore the binary representation of `sum`(_L,i_-1) contains bits equal to 1 only in the positions less than or equal to \(\alpha_i\).

Since we add up each \(\phi_i\) exactly once without any truncation, \(\text{\texttt{sum}}(L,2m+1)=\sum_{i=1}^m\phi_i=1\) and by Theorem 1 there does not exist any alphabetic code for the lengths _L_.

**Case 2**: In this case, there is at least one \(\ell_i=x_i\) that does not satisfy the condition of Case 1. Let us suppose that `sum`(_L,_2_m_+1)_\<_1 and show that this leads to a contradiction.

Consider the sub-case in which we increase by 1 _x<sub>i</sub>_, with \(1<i<2m+1\). Let \(L'=\langle\ell_1,\dots,\ell_{i-1},\ell_i+1,\ell_{i+1},\dots,\ell_{2m+1}\rangle\) be the list of lengths after increasing such _x<sub>i</sub>_ by 1. Let us show that \(\text{\texttt{sum}}(L',2m+1)\) can only decrease with respect to `sum`(_L,_2_m_+1). Since _x<sub>i</sub>_ can only affect \(\alpha_i\) and \(\alpha_{i+1}\), we have four cases:

• \(\alpha_i\) increases by 1 and \(\alpha_{i+1}\) does not change:<tbc>

\(\text{\texttt{sum}}(L',i)=\text{\texttt{trunc}}(\alpha_i+1,\text{\texttt{sum}}(L,i-1))+2^{-(\alpha_i+1)}\)<br>
\(\le\text{\texttt{trunc}}(\alpha_i,\text{\texttt{sum}}(L,i-1))+2^{-(\alpha_i+1)}\)<br>
\(+2^{-(\alpha_i+1)}\)<br>
\(=\text{\texttt{trunc}}(\alpha_i,\text{\texttt{sum}}(L,i-1))+2^{-\alpha_i}\)<br>
\(=\text{\texttt{sum}}(L,i).\)

• \(\alpha_i\) does not change and \(\alpha_{i+1}\) increases by 1:<tbc>

\(\text{\texttt{sum}}(L',i+1)=\text{\texttt{trunc}}(\alpha_{i+1}+1,\text{\texttt{sum}}(L,i))\)<br>
\(+2^{-(\alpha_{i+1}+1)}\)<br>
\(\le\text{\texttt{trunc}}(\alpha_{i+1},\text{\texttt{sum}}(L,i))\)<br>
\(+2^{-(\alpha_{i+1}+1)}+2^{-(\alpha_{i+1}+1)}\)<br>
\(=\text{\texttt{trunc}}(\alpha_{i+1},\text{\texttt{sum}}(L,i))+2^{-\alpha_{i+1}}\)<br>
\(=\text{\texttt{sum}}(L,i+1).\)

• Both \(\alpha_i\) and \(\alpha_{i+1}\) increase by 1: then \(\alpha_i=\alpha_{i+1}\) and<tbc>

\(\text{\texttt{sum}}(L',i+1)=\text{\texttt{trunc}}(\alpha_{i+1}+1,\text{\texttt{sum}}(L',i))\)<br>
\(+2^{-(\alpha_{i+1}+1)}\)<br>
\(=\text{\texttt{trunc}}(\alpha_{i+1}+1,\)<br>
\(\text{\texttt{trunc}}(\alpha_i+1,\text{\texttt{sum}}(L,i-1))\)<br>
\(+2^{-(\alpha_{i+1})})\)<br>
\(+2^{-(\alpha_{i+1}+1)}\)<br>
\(=\text{\texttt{trunc}}(\alpha_i+1,\text{\texttt{sum}}(L,i-1))\)<br>
\(+2^{-(\alpha_i+1)}+2^{-(\alpha_{i+1}+1)}\)<br>
\(\text{(since}\alpha_i=\alpha_{i+1})\)<br>
\(=\text{\texttt{trunc}}(\alpha_i+1,\text{\texttt{sum}}(L,i-1))\)<br>
\(+2^{-(\alpha_i+1)}+2^{-(\alpha_i+1)}\)

\(=\text{\texttt{trunc}}(\alpha_i+1,\text{\texttt{sum}}(L,i-1))+2^{-\alpha_i}\)<br>
\(\le\text{\texttt{trunc}}(\alpha_i,\text{\texttt{sum}}(L,i-1))\)<br>
\(+2^{-\alpha_i}+2^{-(\alpha_i+1)}\)<br>
\(<\text{\texttt{trunc}}(\alpha_i,\text{\texttt{sum}}(L,i-1))\)<br>
\(+2^{-\alpha_i}+2^{-\alpha_{i+1}}\)<br>
\(=\text{\texttt{trunc}}(\alpha_{i+1},\)<br>
\(\text{\texttt{trunc}}(\alpha_i,\text{\texttt{sum}}(L,i-1))+2^{-\alpha_i})\)<br>
\(+2^{-\alpha_{i+1}}\)<br>
\(=\text{\texttt{trunc}}(\alpha_{i+1},\text{\texttt{sum}}(L,i))+2^{-\alpha_{i+1}}\)<br>
\(=\text{\texttt{sum}}(L,i+1).\)

• Both \(\alpha_i\) and \(\alpha_{i+1}\) do not change: the final sum remains the same.

Therefore, we have that \(\text{\texttt{sum}}(L',2m+1)\le\text{\texttt{sum}}(L,2m+1)\).

Consider now the sub-cases in which we increase by 1 _x_<sub>1</sub> or _x_<sub>2_m_+1</sub>. In such sub-cases, only \(\alpha_2\) and \(\alpha_{2m+1}\) can be affected. Let us consider the case when _x_<sub>1</sub> is increased and let \(L'=\langle\ell_1+1,\dots,\ell_{2m+1}\rangle\) be the list of lengths after increasing _x_<sub>1</sub>. We have two possibilities:

• \(\alpha_2\) increases by 1:<tbc>

\(\text{\texttt{sum}}(L',2)=\text{\texttt{trunc}}(\alpha_2+1,\text{\texttt{sum}}(L,1))+2^{-\alpha_2-1}\)<br>
\(=\text{\texttt{trunc}}(\alpha_2,\text{\texttt{sum}}(L,1))+2^{-\alpha_2-1}\)<br>
\(<\text{\texttt{trunc}}(\alpha_2,\text{\texttt{sum}}(L,1))+2^{-\alpha_2}\)<br>
\(=\text{\texttt{sum}}(L,2)\)

• \(\alpha_2\) does not change: then \(\text{\texttt{sum}}(L',2)=\text{\texttt{sum}}(L,2)\).

A similar reasoning holds for _x_<sub>2_m_+1</sub> too. By denoting with \(L'=\langle\ell_1,\dots,\ell_{2m+1}+1\rangle\) the list of lengths after increasing _x_<sub>2_m_+1</sub>, we have two possibilities:

• \(\alpha_{2m+1}\) increases by 1:<tbc>

\(\text{\texttt{sum}}(L',2m+1)=\text{\texttt{trunc}}(\alpha_{2m+1}+1,\text{\texttt{sum}}(L,2m))\)<br>
\(+2^{-(\alpha_{2m+1}+1)}\)<br>
\(\le\text{\texttt{trunc}}(\alpha_{2m+1},\text{\texttt{sum}}(L,2m))\)<br>
\(+2^{-(\alpha_{2m+1}+1)}+2^{-(\alpha_{2m+1}+1)}\)<br>
\(=\text{\texttt{trunc}}(\alpha_{2m+1},\text{\texttt{sum}}(L,2m))\)<br>
\(+2^{-\alpha_{2m+1}}\)<br>
\(=\text{\texttt{sum}}(L,2m+1)\)

• \(\alpha_{2m+1}\) does not change: then \(\text{\texttt{sum}}(L',2m+1)=\text{\texttt{sum}}(L,2m+1)\).

Therefore, in such cases too, we have that \(\text{\texttt{sum}}(L',2m+1)\le\text{\texttt{sum}}(L,2m+1)\).

However, the above conclusions readily lead to a contradiction since, if we repeat the process iteratively for each _x<sub>i</sub>_, we obtain that when \(x_i=\ell_{i+1}\) for each \(i\in\{1,3,\dots,2m-1\}\), and \(x_{2m+1}=\ell_{2m}\), it holds that \(\text{\texttt{sum}}(L',2m+1)<1\) and by Theorem 1 there exists an alphabetic codes with lengths \(L'\). But, for such lengths \(L'\), we are in Case 1 and we know that this is not possible. Thus, even for values of _x<sub>i</sub>_ arbitrarily chosen, we have that \(\text{\texttt{sum}}(L,2m+1)\ge 1\) and by Theorem 1 there does not exist any alphabetic code for the list of length _L_.

