### Case 2.

Assume \(s_p\in V(\mathcal{T}_{p+1})\). Denote by C<sub>1</sub> the set of connected components of T-_P_ that are not contained in T_<sub>p</sub>_. Denote C<sub>2</sub>=C(T-_P_)-C<sub>1</sub> (see Figure 3). For every \(\mathcal{H}\in\mathbb{C}_1\), if \(v\in V(\mathcal{H})\), then \(\mathtt{Path}_T(v)\supseteq\{r\}\cup\mathtt{Path}_{T|_\mathcal{H}}(v)\). Therefore the contribution of vertices in _V_(T-T_<sub>p</sub>_) to `cost`(_T_) is at least<tbc>

\(m-w(\mathcal{T}_p)+\sum_{\mathcal{H}\in\mathbb{C}_1}\mathtt{cost}(T|_\mathcal{H}).\) (2)

<tbc>For vertices \(v\in V(\mathcal{T}_p-\mathcal{T}_{p+1})\) we have \(\{r,s_p\}\subseteq\mathtt{Path}_T(v)\). Therefore, using the fact that \(w(\mathcal{T}_p-\mathcal{T}_{p+1})\ge\frac{w(\mathcal{T}_p)}{2}\) , the contribution of vertices in _V_(T_<sub>p</sub>_) to `cost`(_T_) is at least

\(2\cdot w(\mathcal{T}_p-\mathcal{T}_{p+1})+\sum_{\mathcal{H}\in\mathbb{C}_2}\mathtt{cost}(T|_\mathcal{H})\ge w(\mathcal{T}_p)+\sum_{\mathcal{H}\in\mathbb{C}_2}\mathtt{cost}(T|_\mathcal{H}).\) (3)

Summing Equation (2) and Equation (3) yields the required result.

### Case 3.

Assume that there is a _j\<p_ such that K_<sub>p</sub>_=K_<sub>j</sub>_. Since _p_ is minimal, we further assume that case 2 did not occur for indices smaller that _p_. In particular, \(s_p=s_j\notin V(\mathcal{T}_p)\). As in case 2, the contribution of vertices in T-T_<sub>p</sub>_ to `cost`(_T_) is at least as in Equation (2). We have \(r\notin V(\mathcal{T}_p-\mathcal{T}_{p+1})\) and \(v_p\in V(\mathcal{T}_p-\mathcal{T}_{p+1})\cap V(\mathcal{K}_p)\neq\emptyset\), therefore, since T_<sub>p</sub>_-T<sub>_p_+1</sub> is connected, \(V(\mathcal{T}_p-\mathcal{T}_{p+1})\subseteq V(\mathcal{K}_p)\) (see Figure 4). It follows that vertices in T_<sub>p</sub>_-T<sub>_p_+1</sub> have both _r_ and _s<sub>p</sub>_ as ancestors. Since \(w(\mathcal{T}_p-\mathcal{T}_{p+1})\ge\frac{w(\mathcal{T}_p)}{2}\) , the contribution of vertices in T_<sub>p</sub>_ is at least as in Equation (3). As in Case 2, the result follows by summing Equation (2) and Equation (3).

## 4.2 Lower bounds

**Theorem 1.4.** _Let_ \(\Delta\ge 3\) _be integer._

(_i)_ _There is a sequence of instances_ (T_<sub>n</sub>,w<sub>n</sub>_) _such that_ T_<sub>n</sub> has maximum degree at most_ \(\Delta\)_, and for every centroid tree C<sub>n</sub> of_ (T_<sub>n</sub>,w<sub>n</sub>_)<tbc>

<tbc>\(\mathrm{lim}_{n\rightarrow\infty}\frac{\mathtt{cost}_{w_n}(C_n)}{\mathtt{OPT}(\mathcal{T}_n,w_n)}=2-\frac{1}{2^\Delta}.\)<tbc>

Tp
Tp+1
vo
vo
r
vp = r
V1
sp
KP
Tp - Tp+1
vp-1
vp-1

Figure 3: Illustration of the proof of Claim 4.1. Connected components of T-_P_ are represented by light gray circles. (_Left._) Case 1. (_Right._) Case 2. Vertices in T-T_<sub>p</sub>_ have _r_ as ancestor. Vertices in T_<sub>p</sub>_-T<sub>_p_+1</sub> have both _r_ and _s<sub>p</sub>_ as ancestors.

