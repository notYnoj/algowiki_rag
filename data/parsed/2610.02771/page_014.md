**Algorithm 1** MEDIANEST: 1-Bit Anchor Estimation

**Require:** Uniformly discretized grid **x**=(_x_<sub>1</sub>_,...,x<sub>n</sub>_) with step size \(\Delta x\), tolerance \(\varepsilon'\in(0,1/4)\), failure probability \(\gamma\in(0,1/2)\).

1: Initialize uniform prior: \(w_1(i)=\frac{1}{n-1}\) for all \(i\in\{1,\dots,n-1\}\).

2: Set sample budget \(M=M(n,\varepsilon',\gamma)\), and subsampling rate \(r=\Theta(1/logn)\).

3: Initialize queried sequence list \(L=\emptyset\).

4: **for** _t_=1_,...,M_ **do**

5: Compute the median index of the current posterior:

\(j_t=min\left\{j\in\{1,\dots,n-1\}:\sum_{i=1}^jw_t(i)\ge\frac{1}{2}\right\}.\)

6: Append _j<sub>t</sub>_ to _L_.

7: Query the threshold _x<sub>j<sub>t</sub></sub>_ and observe 1-bit feedback \(Y_t=\mathbf{1}\{X\le x_{j_t}\}\).

8: Compute the unnormalized posterior _v<sub>t</sub>_ by scaling weights based on _Y<sub>t</sub>_:

\(v_t(i)=\left\{\begin{array}{ c c }
w_t(i)\big(1+2\varepsilon'(2Y_t-1)\big) & \text{if}i\le j_t \\
w_t(i)\big(1-2\varepsilon'(2Y_t-1)\big) & \text{if}i>j_t
\end{array}\right.\forall i\in\{1,\dots,n-1\}.\)

9: Normalize the posterior:

\(w_{t+1}(i)=\frac{v_t(i)}{\sum_{k=1}^{n-1}v_t(k)}\forall i\in\{1,\dots,n-1\}.\)

10: **end for**

11: Extract candidate set \(\mathcal{C}=\left\{L_{\lceil k\cdot rM\rceil}:k=1,2,\dots,\lfloor 1/r\rfloor\right\}\) from the history _L_.

12: Set verification budget \(N=\Theta\left(\frac{1}{(\varepsilon')^2}log\frac{|\mathcal{C}|}{\gamma}\right)\).

13: **for** each candidate index \(c\in\mathcal{C}\) **do**

14: Draw _N_ fresh samples _X_<sup>(1)</sup>_,...,X_<sup>(_N_)</sup> to compute the empirical estimate:

\(\widehat{p}_c=\frac{1}{N}\sum_{s=1}^N\mathbf{1}\{X^{(s)}\le x_c\}.\)

15: **if** \(\left|\widehat{p}_c-\frac{1}{2}\right|\le\frac{3\varepsilon'}{4}\) **then**

16: **return** \(\widehat{c}=\frac{x_c+x_{c+1}}{2}\triangleright\) Return the midpoint of the verified interval

17: **end if**

18: **end for**

## A.3 The MEDIANEST algorithm

The MEDIANEST algorithm is shown in Algorithm 1, which adapts BAYESIANSCREENINGSEARCH to our threshold grid. Because the iteration bound in \[9\] includes explicit constant factors that complicate the expression, we omit the exact loop count in Algorithm 1 to focus on the asymptotic scaling laws.

## A.4 Parameter selection and estimate validity

### Choosing the Tolerance (\(\varepsilon'\)).

Because the sample complexity \(M(n,\varepsilon',\gamma)\) scales aggressively as \(O(1/(\varepsilon')^2)\), we cannot afford to let \(\varepsilon'\) shrink to 0 alongside the main BAI target accuracy \(\varepsilon\). Instead, we fix \(\varepsilon'\) as a moderate constant by setting \(\varepsilon'=0.05\). This choice avoids an exploding sample cost while maintaining a strictly bounded localization window.

### Choosing the Grid Density (_n_).

Discretize the bounded domain \([-\lambda,\lambda]\) using a uniform step size \(\Delta x=\kappa\cdot\sigma\) for a small constant \(\kappa>0\). This results in a grid of size \(n=\Theta(\lambda/\sigma)\). Crucially, because _n_ appears inside a logarithm in the sample complexity \(M(n,\varepsilon',\gamma)\), this domain discretization contributes only an additive logarithmic term to the sample budget. The following lemma transforms the probability guarantees of MEDIANEST into rigorous bounds of the distance to the true mean.

