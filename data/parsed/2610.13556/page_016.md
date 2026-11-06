<tbc>For an integer array \(\mathbf{x}=(x_{\tau i})\) and a map \(a:U\rightarrow[k]\), use the following predicates and linear forms:

\(R(\mathbf{x},\mathbf{N}):x_{\tau i}\ge 0\text{for all}\tau,i,\sum_ix_{\tau i}=N_\tau\text{for all}\tau,\)<br>
\(P_a(\mathbf{x}):a\text{is proper on}G[U],x_{\tau i}=0\text{whenever}i\in a(\tau),\)<br>
\(\mu_i(a,\mathbf{x})=|a^{-1}(i)|+\sum_\tau x_{\tau i}.\)

Here properness of the fixed map _a_ is a Boolean constant. The first predicate says that **x** describes a word; adding the second says that the word is proper. Write \(\mu(a,\mathbf{x})=(\mu_i(a,\mathbf{x}))_{i=1}^k\).

Let \(c,a:U\rightarrow[k]\) represent, respectively, an original coloring and a disturbance. The predicate<tbc>

\(A_{c,a}(\mathbf{x},\mathbf{z},\mathbf{N}):R(\mathbf{x},\mathbf{N})\wedge P_c(\mathbf{x})\wedge R(\mathbf{z},\mathbf{N})\)<br>
\(\wedge\mu(c,\mathbf{x})=\mu(a,\mathbf{z})\)

<tbc>says that the disturbed description (_a,_**z**) has a feasible profile, witnessed by the proper description (_c,_**x**). For a target map \(b:U\rightarrow[k]\), put \(d_U(a,b)=|\{u\in U:a(u)\neq b(u)\}|\). Define \(T_{a,b}(\mathbf{z},\mathbf{y},\mathbf{h};\mathbf{N},\ell)\) by the conjunction of

\(R(\mathbf{y},\mathbf{N}),P_b(\mathbf{y}),\mu(b,\mathbf{y})=\mu(a,\mathbf{z}),\)<br>
\(0\le h_{\tau i}\le z_{\tau i},h_{\tau i}\le y_{\tau i}\text{for every}\tau,i,\)<br>
\(d_U(a,b)+\sum_\tau N_\tau-\sum_{\tau,i}h_{\tau i}\le\ell.\)

By Theorem 5.4, this predicate has witnesses **y**,**h** exactly when a same-profile proper target with core map _b_ is within distance \(\ell\). Indeed, the greatest possible total agreement in each type is \(\sum_imin\{z_{\tau i},y_{\tau i}\}\), and is attainable for every fixed realization of the source. The variables \(h_{\tau i}\) encode these agreements using only linear constraints.

Let \(\Psi_a(\mathbf{z};\mathbf{N},\ell)\) abbreviate \(\vee_{b:U\rightarrow[k]}\exists\mathbf{y}\exists\mathbf{h}T_{a,b}(\mathbf{z},\mathbf{y},\mathbf{h};\mathbf{N},\ell)\). Consider the formula

\(\Phi(\mathbf{N},\ell)=\wedge_{c,a:U\rightarrow[k]}\forall\mathbf{x}\forall\mathbf{z}(A_{c,a}(\mathbf{x},\mathbf{z},\mathbf{N})\Longrightarrow\Psi_a(\mathbf{z};\mathbf{N},\ell)).\) (5.1)

All quantified arrays range over the integers. After substituting \(N_\tau=n_\tau\), this formula holds precisely when \(B(G)\le\ell\). Every admissible disturbance has at least one proper profile witness, so the implication requires a repair for it. A disturbance with an infeasible profile has no such witness and imposes no condition. Although the witness is universally quantified, the permitted repairs depend only on the disturbance, not on which witness was used. For weak villainy, delete the profile equality from _T<sub>a,b</sub>_ only; the source-feasibility predicate _A<sub>c,a</sub>_ is unchanged. The resulting formula is equivalent to \(B_\mathrm{w}(G)\le\ell\).

Both formulas have length bounded by a function of _s_: there are \(k\le s+1\) colors, 2_<sup>s</sup>_ types, and at most _k_<sup>2_s_</sup> pairs of core maps. All coefficients and core constants are bounded in _s_. Crucially, **N** and \(\ell\) remain free during quantifier elimination. Thus the elimination time, the output length, and its coefficient lengths are bounded by a computable function of _s_, independently of the numerical type sizes. Substituting their actual values and evaluating the resulting formula takes _g(s_)(log(_n_+1))<sup>_O_(1)</sup> time. This is a uniform algorithm: the formulas are generated from the given graph on _U_ and then processed by an effective elimination procedure. Binary search on \(0\le\ell\le n\), together with input processing, computes both values in the claimed time. □

## 5.4. Graphs with a small complement cover.

Suppose next that _W=V(G_)\\_U_ is a clique. The chromatic number need not be bounded, but its computation still depends on only a bounded part of the graph.

