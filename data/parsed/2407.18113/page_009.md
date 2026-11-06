### Large alphabets.

In the third version we slightly change the data structure used to store the transformation _T_. This data structure uses maps instead of vectors and is more costly for small alphabets, but the cost is now linear in max(_k,_2_h_) instead of _k_ which means that for fixed _h_ we can compute a lower bound for very large values of _k_. The results obtained with this program are given in  4, and the source code is in the file `EditDistance\_ rally\_large\_alphabets.cpp` from the GIT repository.

## 3 Longest common subsequence

The technique that we use to compute bounds on \(\gamma_k\) is the same as in \[14\], and is moreover almost identical to what we did in the previous section. For the sake of completeness, we provide the definitions and the corresponding statement, but we do not repeat the proofs.

For any strings _u,v_, LCS(_u,v_) is the size of the longest common subsequence of _u_ and _v_. Remember, that given two strings \(u,v\in\mathcal{A}^*\), and letters \(a,b\in\mathcal{A}\), we have

\(\text{LCS}(au,bv)=\left\{\begin{array}{ c c }
1+\text{LCS}(u,v) & \text{if}a=b \\
\text{max}(\text{LCS}(u,bv),\text{LCS}(au,v)) & \text{otherwise}
\end{array}\right.\) (11)

and for all _u_, \(\text{LCS}(u,\varepsilon)=\text{LCS}(\varepsilon,u)=0\), where \(\varepsilon\) is the empty string. For any strings \(u,v,u',v'\), we have

\(\text{LCS}(uv,u'v')\ge\text{LCS}(u,u')+\text{LCS}(v,v').\) (12)

For the rest of this section, the _X<sub>i</sub>_ and _Y<sub>i</sub>_ are independent uniform random variables from A={1_,...,k_}. For all _k_, the quantity \(\gamma_k\) is defined as

\(\gamma_k=lim_{n\rightarrow\infty}\frac{\mathbb{E}\left[\text{LCS}(X_1\dots X_n,Y_1\dots Y_n)\right]}{n}.\)

Linearity of expectation and equation (12) imply that the sequence is subadditive which by Feketes’s lemma implies that \(\alpha_k\) is well-defined.

For any \(n\in\mathbb{N}\) and, \(s,t\in\mathcal{A}^*\), we let

\(W_n(s,t)=\mathbb{E}\left[min_{i+j=ni,j\ge 0}\text{LCS}(sX_1X_2\dots X_i,tY_1Y_2\dots Y_j)\right].\)

The following Lemma can be proven by following the same proof as for Lemma 4.

\begin{tabular}{cccccc}
k & Upper bound & _h_ used & Memory consumption & Computation time & Iterations \\
3 & 0.47276 & 9 & 20Gb & 17m & 100 iterations \\
4 & 0.56578 & 8 & 58Gb & 1h06 & 100 iterations \\
5 & 0.6325 & 7 & 28Gb & 32m & 100 iterations \\
\end{tabular}

3: Our results for the small alphabets using the second version of the code.

