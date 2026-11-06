## 4 APA Matrix Multiplication is Stable

In this section, we show that alternative basis APA matrix multiplication is stable by proving a (weak) forward error bound for a floating-point implementation of the approximate-to-exact procedure represented by Algorithm 4. In line three of this algorithm, **AltBasis-Recursive-APA**\(_{\langle\phi,\psi,\nu\rangle}\) is a recursive implementation of an alternative basis APA matrix multiplication routine (i.e, Algorithm 2), indexed by the corresponding symbolic basis transformations \(\phi\), \(\psi\), and \(\nu\). Following the previous section, this algorithm is based on an alternative basis \(\langle m_0,k_0,n_0;t\rangle\) scheme defined by parameterized encoding matrices \(U_\phi(\varepsilon)\), \(V_\psi(\varepsilon)\) and \(W_\nu(\varepsilon)\).

**Algorithm 4** Approximate-to-Exact Alternative Basis APA Matrix Multiplication

**Input:** \(A\in\mathbb{C}^{m\times k}\), \(B\in\mathbb{C}^{k\times n}\) and parameters \(\varepsilon_1,\dots,\varepsilon_p\in\mathbb{C}\), where _p=dL_+1.

**Output:** _C=AB_.

1: \([\alpha_1,\dots,\alpha_p]=\text{\textbf{Vandermonde-Solve}}(\varepsilon_1,\dots,\varepsilon_p)\)

2: **for** _j_=1:_p_ **do**

3: \(C_j=\text{\textbf{AltBasis-Recursive-APA}}_{\langle\phi,\psi,\nu\rangle}(A,B,\varepsilon_j)\)

4: **end for**

5: \(C=\alpha_1C_1+\alpha_2C_2+\cdots+\alpha_pC_p\)

6: **return** _C_

As discussed in the introduction, Algorithm 4 obtains the exact product of _A_ and _B_ by evaluating **AltBasis-Recursive-APA**\(_{\langle\phi,\psi,\nu\rangle} p=dL+1\) times with different values of \(\varepsilon\) and taking a linear combination of the output (after applying the corresponding basis transformation \(\nu_\varepsilon\)). The coefficients in this linear combination solve the Vandermonde system (1.5) with _p_ replacing _d_ and are computed in line 1 of Algorithm 4 by the routine **Vandermonde-Solve**. Note that each \(\alpha_j\) can be expressed in terms of \(\varepsilon_1,\dots,\varepsilon_p\) as follows:

\(\alpha_j=(-1)^{p-1}\prod_{k\neq j}\frac{\varepsilon_k}{\varepsilon_j-\varepsilon_k}=\prod_{k\neq j}\frac{\varepsilon_k}{\varepsilon_k-\varepsilon_j}.\) (4.1)

We also have the special case \(\alpha_j=1/p\) for all _j_ when the \(\varepsilon_i\) are the _p_-th roots of unity.

To obtain a forward error bound for a floating-point implementation of Algorithm 4 we extend work of Schwartz et al. \[53\] to the APA setting. The results of \[53\] are the most recent in a long line of research on the stability of fast matrix multiplication, which traces its roots back to work of Brent \[12\] and Bini and Lotti \[11\]. The normwise stability bounds derived by these authors for specific algorithms - i.e., the same notion of weak forward stability established for APA algorithms in this paper (see Theorem 4.6) - was eventually shown to apply to the broad class of fast (exact) matrix multiplication routines by Demmel et al. \[21\]. The contribution of Schwartz et al. in \[53\], itself a generalization of \[2\], was to extend this framework to include alternative basis matrix multiplication \[32\], and hence their bounds are a natural fit for our setting in light of the previous section. To the best of our knowledge, the results presented here are the first stability bounds derived for APA matrix multiplication.

**Remark 4.1.** The bounds presented in this section are stated in terms of the maximum-entry norm - i.e., \(\|A\|=max_{ij}|A(i,j)|\). This matches most of the results in the literature on the stability of fast matrix multiplication. Dumas, Pernet, and Sedoglavic \[25\], however, recently derived new bounds in terms of arbitrary norms, which are tighter than what can be obtained by simply applying norm equivalence. They demonstrate the efficacy of their bounds by using them to obtain algorithms that are more stable in practice (including with respect to the maximum entry norm). Since our goal in this section is to demonstrate stability for Algorithm 4, we leave an APA extension of these results to future work. Similarly, we do not consider scaling techniques (e.g., \[26\]), even though this is a well-documented way to further improve the stability of fast exact matrix multiplication (see the discussion in \[23\]).

### 4.1 Preliminaries

We begin by summarizing the building blocks of our analysis. Throughout, we adopt a standard model for floating-point arithmetic \[31, 48\], in which each binary floating-point operation \(\circ\in\{+,-,\times,\div\}\) satisfies

\(fl(x\circ y)=(x\circ y)(1+\delta)\text{for some}|\delta|\le\text{\textbf{u}},\) (4.2)

