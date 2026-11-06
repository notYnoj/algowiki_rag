<tbc>We are now able to deduce Pólya’s \[49\] result that T(_n_) has a perfect matching only if _n_ is not divisible by 2 or 3.

Corollary 3.19. _Suppose that_ T(_n_) _has a perfect matching. Then_ \(n\equiv 1,5mod6\).

Proof. Suppose that T(_n_) has a perfect matching. Then \(\mathbf{1}\in\mathcal{L}(\mathcal{T})\). By Lemma 3.18 we have that \(\sum_iv_i^X=\sum_iv_i^Y=\sum_iv_i^{X+Y}\), \(\sum_iv_i^X+\sum_iv_i^Y=\sum_iv_i^{X+Y}mod(n)\), \(\sum_iv_i^X-\sum_iv_i^Y=\sum_iv_i^{X-Y}mod(n)\) and furthermore that \(2\sum_i^2v_i^X+2\sum_i^2v_i^Y=\sum_i^2v_i^{X+Y}+\sum_i^2v_i^{X-Y}\). It is clear that the first of these holds for all values of _n_. Both the second and the third are true if and only if \(\frac{n(n+1)}{2}\equiv 0mod(n)\) which is true if and only if _n_ is odd. The final statement implies that \(2\sum_{i\in[n]}i^2=0mod(n)\) and since we know that _n_ must be odd this reduces to \(\sum_{i\in[n]}i^2=0mod(n)\). Using that \(\sum_{i\in[n]}i^2=\frac{n(n+1)(2n+1)}{6}\) yields that \(n\equiv 1,2mod3\), completing the proof. □

## 3.3. Zero-sum configurations

### 3.3.1. Overview.

We define a _zero-sum configuration_ to be any collection of vertices, such that these vertices induce two distinct perfect matchings, _M_<sup>+</sup> and _M_<sup>-</sup>. We refer to such a configuration in this way, since, giving each edge in _M_<sup>+</sup> a weight +1 and each edge in _M_<sup>-</sup> a weight -1, we have that every vertex covered by the configuration sees exactly one positive edge and one negative edge in the configuration, thus giving a ‘zero-sum’ weight at each vertex. In the language of linear maps above, given \(\Phi\in\{-1,0,1\}^{E(\mathcal{T})}\) we define \(\Phi^+\in\{0,1\}^{E(\mathcal{T})}\) to be the vector such that<tbc>

\(\Phi_e^+=\left\{\begin{array}{ c c }
1 & \text{if}\Phi_e=1, \\
0 & \text{otherwise.}
\end{array}\right.\)

<tbc>Similarly, we define \(\Phi^-\in\{0,-1\}^{E(\mathcal{T})}\) to be the vector such that

\(\Phi_e^-=\left\{\begin{array}{ c c }
-1 & \text{if}\Phi_e=-1, \\
0 & \text{otherwise.}
\end{array}\right.\)

Then we have that for \(\Phi\in\{-1,0,1\}^{E(\mathcal{T})}\), the set of vertices which have non-zero support on either \(\partial\Phi^+\) or \(\partial\Phi^-\) is a zero-sum configuration if and only if \(\partial\Phi=\mathbf{0}\). Whilst there can be many ways to form such configurations, we shall restrict our consideration to a specific family of zero-sum configurations, and henceforth, when referring to a zero-sum configuration, we shall be considering exclusively those which can be described in the following way. Our zero-sum configurations consist of 16 vertices, so that each of the matchings _M_<sup>+</sup> and _M_<sup>-</sup> consist of four edges. Every configuration we are concerned with has free variables _a,b,c,s_, and we set _d_:=_b+c-a_. Then a zero-sum configuration _Z_ has _positive matching M_<sup>+</sup>(_Z_) consisting of<br>
(_a,b+s,a+b+s,a-b-s_),<br>
(_b,d+s,b+d+s,b-d-s_),<br>
(_c,a+s,a+c+s,c-a-s_),<br>
(_d,c+s,c+d+s,d-c-s_),<br>
and _negative matching M_<sup>-</sup>(_Z_) consisting of<br>
(_a,c+s,a+c+s,a-c-s_),<br>
(_b,a+s,a+b+s,b-a-s_),

