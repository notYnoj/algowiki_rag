**Lemma 3.9** (\[Gup25\])**.** _For each_ \(\alpha\unknown\mathrm{i}\unknown\mathrm{loglog}n-1\)_, the degree of each edge on the_ sa<sub>i</sub> _and_ tb<sub>i</sub> _paths is at most_ \(\tilde{\mathrm{O}}(2^\mathrm{i})\) _with a high probability._

Unlike \[Gup25\], we use FMM crucially in our algorithm. We now state the relevant results in this area.

### 3.1 Fast Matrix Multiplication (FMM)

**Definition 3.10** (Distance product or min-plus product)**.** _Let_ A _be a matrix of size_ \(n\times n^r\) _and_ B _be a matrix of size_ \(n^r\times n\)_. The distance product or min-plus product of_ A _and_ B _is defined as_

\((A\star B)_{\mathrm{i}j}:=\mathrm{min}_{1\unknown\ell\unknown n^r}\{A_{\mathrm{i}\ell}+B_{\ell j}\}\)

_where_ \(1\unknown\mathrm{i},\mathrm{j}\unknown n\).

The distance product can be computed quickly using fast rectangular matrix multiplication. In our paper, we are satisfied even with an approximate distance product. A matrix C is a \((1+\varepsilon)\) approximation of A ⋆B if, for each i,j,

\((A\star B)_{\mathrm{i}j}\unknown C_{\mathrm{i}j}\unknown(1+\varepsilon)(A\star B)_{\mathrm{i}j}\)

where \(\varepsilon>0\). We use the following result implied in \[Zwi02\], which computes a \((1+\varepsilon)\) approximation of the distance product efficiently. Recently, \[DFK<sup>+</sup>24\] used this result to get better algorithms for additive as well as multiplicative APSP.

**Lemma 3.11** (Implied by \[Zwi02\])**.** _Let_ W _be a positive integer and let_ \(\varepsilon>0\) _be a parameter. Consider matrices_ A _of size_ \(n\times n^r\) _and_ B _of size_ \(n^r\times n\) _where each entry of_ A _and_ B _lies in_ \(\{0,1,\dots,W\}\cup\{\infty\}\)_. Then there exists an algorithm that computes a_ \((1+\varepsilon)\) _approximation of the min-plus product_ A ⋆B _in time_

\(\tilde{\mathrm{O}}\left(\frac{n^{\omega(r)}}{\varepsilon}\mathrm{log}W\right).\)

_Here_ \(\omega(r)\) _is a function that depends on_ r.

In our setting, the maximum finite distance between any two vertices is bounded by O(n). Thus, we can set W=O(n), and the logW factor is absorbed by the \(\tilde{\mathrm{O}}(\cdot)\) notation. Thus, we reduce approximate distance products to rectangular matrix multiplication. In our algorithm, the parameter r is small. Specifically, in our dense case, the inner dimension of the matrix multiplication is n<sup>0.125</sup>, which corresponds to r=0.125. Results in \[Cop82, Wil14\] show that when \(r\unknown 0.17227\) we have \(\omega(r)=2\). Therefore, our algorithm runs in \(\tilde{\mathrm{O}}(n^2)\) time even though it uses FMM.

## 4 Constant additive approximation of st path

In the overview, we designed an algorithm that finds a constant additive approximation of the st path. However, the algorithm relied crucially on Theorem 2.6. We now present a lemma that justifies this assumption.

**Lemma 4.1.** _Fix_ \(\alpha=\mathrm{loglog}n-4\) _in Theorem 3.6. There is a randomised algorithm_ ENSUREBALLPROXIMITY _that ensures that upon termination, for every pair of vertices_ \(s,\mathrm{t}\in V\)_, either_ \(\mathrm{est}(s,\mathrm{t})\unknown 2|\mathrm{st}|\)_, or both of the following inequalities hold:_

1. \(|\mathrm{spivot}_\alpha(s)|>\left\lfloor\frac{|\mathrm{st}|}{2}\right\rfloor-c'\)_, and_<tbc>

_2._ \(|\mathrm{tpivot}_\alpha(\mathrm{t})|>\left\lfloor\frac{|\mathrm{st}|}{2}\right\rfloor-c'\)

_where_ \(c'\) _is a constant. Moreover, the running time of_ ENSUREBALLPROXIMITY _is_ \(\tilde{\mathrm{O}}(n^2)\).

