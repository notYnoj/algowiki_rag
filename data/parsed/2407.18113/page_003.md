## 2 Average edit distance

For any strings _u,v_, _d<sub>e</sub>(u,v_) is the _edit distance_ (or _Levenshtein distance_) between _u_ and _v_, that is, the minimum number of substitutions, deletions and insertions necessary to transform _u_ to _v_. Given two strings \(u,v\in\mathcal{A}^*\), and letters \(a,b\in\mathcal{A}\), we have<tbc>

\(d_e(au,bv)=\left\{\begin{array}{ c c }
d_e(u,v) & \text{if}a=b \\
1+min(d_e(u,v),d_e(u,bv),d_e(au,v)) & \text{otherwise}
\end{array}\right.\) (1)

<tbc>and for all _u_, \(d_e(u,\varepsilon)=d_e(\varepsilon,u)=|u|\), where \(\varepsilon\) is the empty string. For any strings \(u,v,u',v'\), we have<tbc>

\(d_e(uv,u'v')\le d_e(u,u')+d_e(v,v').\) (2)

<tbc>For any _n_, we let _U<sub>n,k</sub>=d<sub>e</sub>(X_<sub>1</sub>_...X<sub>n</sub>,Y_<sub>1</sub>_...,Y<sub>n</sub>_) where the _X<sub>i</sub>_ and _Y<sub>i</sub>_ are taken uniformly at random from A={1_,...,k_}. For all _k_, the quantity \(\alpha_k\) is defined as

\(\alpha_k=lim_{n\rightarrow\infty}\frac{\mathbb{E}\left[d_e(X_1\dots X_n,Y_1\dots Y_n)\right]}{n}=lim_{n\rightarrow\infty}\frac{U_{n,k}}{n}.\)

Linearity of expectation and equation (2) imply that the sequence \(\left(\mathbb{E}\left[U_{n,k}\right]\right)_{n\ge 1}\) is subadditive. Thus by Feketes’s lemma, \(\alpha_k\) is well-defined.

Since we will always be working with one specific ambient alphabet A, we omit the _k_, and, from now on, we write for instance _U<sub>n</sub>_ instead of _U<sub>n,k</sub>_. Similarly, in the following the _X<sub>i</sub>_ and _Y<sub>i</sub>_ always denote random variables taken uniformly at random from A={1_,...,k_}. For all \(1\le i,j,\ell,m\le n\), we let<tbc>

\(U_{[i,j],[\ell,m]}=d_e(X_i\dots X_j,Y_\ell\dots,Y_m).\)

<tbc>Finally, we let \(V_n=min_{i\in\{0,\dots,n\}}U_{[1,i],[1,n-i]}\) and

\(\alpha'_k=lim_{n\rightarrow\infty}\frac{\mathbb{E}\left[V_n\right]}{n}.\)

We will show that \(\alpha_k=2\alpha'_k\), and then explain how we compute bounds on \(\alpha'_k\).

### 2.1 From \(\alpha_k\) to \(\alpha'_k\)

We first prove that \(\alpha_k=2\alpha'_k\). The proof is directly inspired by the similar proof for \(\gamma_k\) in \[1\]. We will use the following special case of McDiarmid’s inequality \[15\].

**Theorem 1** (McDiarmid’s inequality)**.** _Let_ \(f:\mathcal{X}_1\times\mathcal{X}_2\times\cdots\times\mathcal{X}_m\rightarrow\mathbb{R}\) _be a function with the property that changing any one argument of f while holding the others fixed changes the value of f by at most c. Consider independent random variables X_<sub>1</sub>_,...,X<sub>m</sub> where_ \(X_i\in\mathcal{X}_i\) _for all i. Then, for any_ \(\varepsilon>0\),<tbc>

\(\mathbb{P}\left[f(X_1,\dots,X_m)-\mathbb{E}\left[f(X_1,\dots,X_m)\right]\ge\varepsilon\right]\le exp\left(-\frac{2\varepsilon^2}{mc^2}\right),\)

<tbc>_and_<tbc>

\(\mathbb{P}\left[f(X_1,\dots,X_m)-\mathbb{E}\left[f(X_1,\dots,X_m)\right]\le-\varepsilon\right]\le exp\left(-\frac{2\varepsilon^2}{mc^2}\right).\)

