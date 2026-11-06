_Proof._ By Corollary 6.3, there exists a constant _c_<sub>0</sub>_\>_0 such that<tbc>

\(\mathbb{E}_R\big[\sum_{v=1}^n\mathrm{Inf}(f_{v,R})\big]\ge c_0nk.\)

<tbc>Set \(\alpha:=c_0/2\), and for each seed _r_ define<tbc>

\(H_r:=\{v\in[n]:\mathrm{Inf}(f_{v,r})\ge\alpha k\}.\)

<tbc>Since \(\mathrm{Inf}(f_{v,r})\le k\) for every _v_ and _r_,<tbc>

\(\sum_{v=1}^n\mathrm{Inf}(f_{v,r})\le|H_r|k+(n-|H_r|)\alpha k.\)

<tbc>Taking expectations over _R_ and rearranging shows that

\(\mathbb{E}_R[|H_R|]\ge\gamma n\)

for some constant \(\gamma>0\).

If a Boolean function depends on at most _T_ input coordinates, then its total influence is at most _T_. Likewise, the deterministic decision-tree depth _D(f_) satisfies \(\mathrm{Inf}(f)\le D(f)\). Therefore every coordinate counted by _H<sub>r</sub>_ depends on \(\Omega(k)\) message bits and has decision-tree depth \(\Omega(k)\).

## 6.2 A Meta-Corollary for Low-Influence Representation Classes

For a class G_<sub>k</sub>_ of Boolean functions on {0,1}_<sup>k</sup>_, define<tbc>

\(\mathrm{dist}(f,\mathcal{G}_k):=\mathrm{inf}_{g\in\mathcal{G}_k}\mathbf{Pr}_{m\in\{0,1\}^k}\big[f(m)\neq g(m)\big].\)

<tbc>**Corollary 6.5** (A meta-corollary for randomized low-influence classes)**.** _Let_ \(\alpha,\gamma>0\) _be the constants from Corollary 6.4. Let_ G_<sub>k</sub> be any class of Boolean functions on_ {0,1}_<sup>k</sup> satisfying_<tbc>

\(\mathrm{sup}_{g\in\mathcal{G}_k}\mathrm{Inf}(g)\le\beta(k).\)

<tbc>_If_ \(\beta(k)\le\alpha k/2\)_, then_<tbc>

\(\mathbb{E}_R\big[\big|\{v\in[n]:\mathrm{dist}(f_{v,R},\mathcal{G}_k)\ge\alpha/4\}\big|\big]\ge\gamma n.\)

<tbc>_Proof._ For any two Boolean functions \(f,g:\{0,1\}^k\rightarrow\{0,1\}\),<tbc>

\(\big|\mathrm{Inf}(f)-\mathrm{Inf}(g)\big|\le 2k\mathbf{Pr}_{m\in\{0,1\}^k}\big[f(m)\neq g(m)\big].\)

<tbc>Indeed, for each \(i\in[k]\),

\(\big|\mathbf{Pr}_m\big[f(m)\neq f(m^{\oplus i})\big]-\mathbf{Pr}_m\big[g(m)\neq g(m^{\oplus i})\big]\big|\le 2\mathbf{Pr}_m\big[f(m)\neq g(m)\big],\)

and summing over _i_ proves the claim.

Now fix a seed _r_ and let _v_ be any coordinate with \(\mathrm{Inf}(f_{v,r})\ge\alpha k\). For every \(g\in\mathcal{G}_k\) we then have<tbc>

\(\mathbf{Pr}_m\big[f_{v,r}(m)\neq g(m)\big]\ge\frac{\mathrm{Inf}(f_{v,r})-\mathrm{Inf}(g)}{2k}\ge\frac{\alpha k-\beta(k)}{2k}\ge\alpha/4.\)

<tbc>Thus

\(\big|\{v\in[n]:\mathrm{dist}(f_{v,r},\mathcal{G}_k)\ge\alpha/4\}\big|\ge\big|\{v\in[n]:\mathrm{Inf}(f_{v,r})\ge\alpha k\}\big|.\)

Taking expectations over _R_ and applying Corollary 6.4 proves the displayed lower bound. The final sentence is immediate.

