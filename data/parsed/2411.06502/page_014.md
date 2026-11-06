**Forest Edit Distance (FED)**<br>
**Input:** Two forests **F** and \(\mathbf{F}'\) and \(\mathrm{sin}(\mathrm{sub}(v),\mathrm{sub}(v'))\) for all \((v,v')\in\mathbf{F}\times\mathbf{F}'\).<br>
**Output:** The following values:<br>
\(\mathrm{sin}(\mathbf{F}[x..y\text{\textbf{)}},\mathbf{F}')\) for all \(x,y\in[1..(2|\mathbf{F}|+1)]\),<br>
\(\mathrm{sin}(\mathbf{F}[x..(2|\mathbf{F}|+1)\text{\textbf{)}},\mathbf{F}'[1..y'\text{\textbf{)}})\) for all \(x\in[1..(2|\mathbf{F}|+1)]\), \(y'\in[1..(2|\mathbf{F}'|+1)]\),<br>
\(\mathrm{sin}(\mathbf{F},\mathbf{F}'[x'..y'\text{\textbf{)}})\) for all \(x',y'\in[1..(2|\mathbf{F}'|+1)]\), and<br>
\(\mathrm{sin}(\mathbf{F}[1..y\text{\textbf{)}},\mathbf{F}'[x'..(2|\mathbf{F}|+1)\text{\textbf{)}})\) for all \(y\in[1..(2|\mathbf{F}|+1)]\), \(x'\in[1..(2|\mathbf{F}'|+1)]\).

In Section 4, we demonstrate that FED can indeed be reduced to APSP, and we prove:

**Main Theorem 4.** _Suppose there exists an algorithm computing the min-plus product of two_ \(m\times m\) _matrices in time_ T<sub>_MUL_</sub>(_m). Then, there is an algorithm for FED running in time_ \(\mathcal{O}(\mathsf{T}_{MUL}(n)+n^{2+o(1)})\)_, where_ \(n=\mathrm{max}(|\mathbf{F}|,|\mathbf{F}'|)\).

To address FED, we adopt a divide-et-impera approach. Our recursive scheme presented in Main Theorem 4 builds upon Mao’s decomposition scheme for forests introduced in \[Mao22\].

## 2.4 Unweighted Tree Edit Distance

We now discuss our algorithm for Unweighted Tree Edit Distance. Consider two forests \(\mathbf{F},\mathbf{F}'\) with \(n,n'\) nodes respectively. We can make two simple observations with respect to the matrices involved in max-plus products in our reduction:

The similarity matrices are row-monotone and column-monotone.<br>
The entries of the similarity matrices are bounded by \(\mathcal{O}(\mathrm{min}(n,n'))\).

Note that the first observation holds even in the weighted setting. For example, in Equation (1), for a fixed \(x,\mathrm{sin}((x,b'),(r,y'))\) must be non-decreasing in \(y'\). In the unweighted setting, the second observation additionally holds, since the value of any alignment is at most twice the number of nodes. In particular, in computing FED (Main Theorem 4) and SED (Main Theorem 3), we can instead use Bounded Monotone Min-Plus Matrix Multiplication.

Recall that the min-plus (or max-plus) product of an \(n\times n\) arbitrary integer matrix and an \(n\times n\) bounded monotone matrix can be computed in time \(\tilde{\mathcal{O}}(n^{(3+\omega)/2})\) \[CDXZ22\], with subsequent generalizations to arbitrary rectangular matrices \[Dür23, SY24\].

Directly applying the observation, we have that SED between two forests of size \(m,m'\) can be computed in time \(\tilde{\mathcal{O}}(\mathrm{max}(m,m')^{(3+\omega)/2})\) \[CDXZ22\] which may be improved to \(\tilde{\mathcal{O}}(\sqrt{\mathrm{min}(m,m')}\cdot\mathrm{max}(m,m')^{(2+\omega)/2})\) by our bound on entries \[Dür23\].

Let us see the result we can obtain via Lemma 2.1.

Recall that Lemma 2.1 states that given an \(\mathcal{O}(f(m)g(m'))\) algorithm for SED, there is an \(\tilde{\mathcal{O}}(f(n)g(n'))\) algorithm for TED on two forests of size \(n,n'\). Suppose \(f(x)=\mathcal{O}(x^a),g(x)=\mathcal{O}(x^b)\). Setting \(m'=1\), we have \(m^{(2+\omega)/2}=\mathcal{O}(m^am^{^\prime b})=\mathcal{O}(m^a)\), so that \(a\ge(2+\omega)/2\). Similarly, we obtain \(b\ge(2+\omega)/2\), so that we only obtain a TED algorithm running in time \(\mathcal{O}(n^{2+\omega})\) for two forests of size _n_. Even if \(\omega=2\), the running time O(_n_<sup>4</sup>) is prohibitively expensive.

In general, a running time \(\tilde{\mathcal{O}}(\mathrm{min}(m,m')^c\mathrm{max}(m,m')^d)\) can be upper bounded by \(\tilde{\mathcal{O}}(m^{\mathrm{max}(c,d)}m^{^\prime d})\). Hence, in order to keep the total exponents of the two formulations the same, we hope to obtain a running time with \(c\ge d\) without increasing _c+d_, i.e., we hope for an algorithm for SED with running time \(\tilde{\mathcal{O}}(\mathrm{min}(m,m')^c\mathrm{max}(m,m')^d)\) for \(c\ge d\) and \(c+d=(3+\omega)/2\). This is achieved by the following theorem:

