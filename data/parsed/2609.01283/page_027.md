_Proof._ During preprocessing, we compute a min-cost (_s,t_)-max-flow _h_ in _G_. We augment _G_ with 2_f_ zero-cost parallel (_s,t_)-edges, and saturate the first _f_ of them in the preprocessed flow _h_. Computing _h_ takes _m_<sup>1+_o_(1)</sup>log_W_ time using the algorithm of \[CKL<sup>+</sup>23\]. We then construct \(\mathcal{G}_h^*\) and instantiate the all-pairs oracles of Theorem 4.2 on \(\mathcal{G}_h^*\) with capacity bound _k=O(f_), from which the preprocessing time and space follow directly.

For any query _U_, the auxiliary update set **U**<sup>∗</sup> satisfies |**U**<sup>∗</sup>|=_O(f_), since each edge in _F_ contributes _O_(1) edges to **U**<sup>∗</sup>. Plugging |**U**<sup>∗</sup>|=_O(f_) and _k=O(f_) into the query bounds of Theorem 4.2 gives \((|\mathcal{U}^*|\cdot k^2)^\omega=f^{3\omega}\) cost.

### Max-Flow Oracle.

By Theorem 4.3, \(\lambda_{G+U}(s,t)=\lambda_G(s,t)+f-i\), where _i_ is the smallest number of parallel edges required to repair _h_. We binary search over \(i\in[0,2f]\); for each candidate, we set \(U'=(I,F\cup\{e_{i+1},\dots,e_{2f}\})\) and apply Theorem 4.4 to translate the repair test into an (_s_<sup>∗</sup>_,t_<sup>∗</sup>)-max- flow query on \(\mathcal{G}_h^*+\mathcal{U}^*\). Thus a query costs \(\widetilde{O}(f^{3\omega})\) time.

### Nearest Min-Cut Oracle.

We first compute \(\lambda:=\lambda_{G+U}(s,t)\) via the max-flow oracle. For each \(w\in V\backslash\{s,t\}\), we invoke the max-flow oracle on _G+U_+(_w,t_) to test whether \(\lambda_{G+U+(w,t)}(s,t)=\lambda+1\). By Theorem 2.1, the set

\(\big\{w\in V:\lambda_{G+U+(w,t)}(s,t)=\lambda+1\big\}\)

is the source side of the nearest min-cut, and its complement is the sink side. Each of the _n_ auxiliary queries preserves the update size _O(f_) and costs \(\widetilde{O}(f^{3\omega})\), resulting in total query time \(\widetilde{O}(f^{3\omega}\cdot n)\).

### Min-Cost Flow Oracle.

By Theorem 4.4, the minimum cost of an (_s,t_)-flow of value \(\lambda_{G+U}(s,t)\) in _G+U_ is determined by **_c_**<sub>G<sup>∗</sup></sub>(_s_<sup>∗</sup>_,t_<sup>∗</sup>), the minimum cost of an (_s_<sup>∗</sup>_,t_<sup>∗</sup>)-flow of value |_F<sub>h</sub>_| in **G**<sup>∗</sup>. We obtain this using the min-cost flow oracle of Theorem 4.2 in \(\widetilde{O}((|\mathcal{U}^*|\cdot k^2)^\omega\cdot kWn)=\widetilde{O}(f^{3\omega+1}\cdot Wn)\) time. □

## 4.3 Sensitivity Oracles for _s_-Min-Cut and Global Min-Cut

We next present sensitivity oracles for two related cut problems. For a fixed source \(s\in V\) , the _s-min-cut_ value in _G_ is \(\mu_G(s):=min_{v\in V\backslash\{s\}}\lambda_G(s,v)\). The _global min-cut_ value is \(\mu_G:=min_{s\in V}\mu_G(s)\). In this section, we show that the (_s,t_)-max-flow sensitivity oracles of Theorem 4.5 can be lifted, with only a small overhead in preprocessing, into sensitivity oracles for both problems.

Our reduction relies on first computing an optimal augmentation of the graph that maximizes the _s_-min-cut.

**Theorem 4.6** (\[Fra90\], Theorem 3.1)**.** _There exists a polynomial time algorithm to solve the following problem: Given an unweighted directed graph G_=(_V,E_) _with a fixed source s and a number f, output a set_ \(I^*\subseteq V\times V\) _of f edges such that adding the edges of I_<sup>∗</sup> _to G results in the maximum_<tbc>

\begin{tabular}{ccccc}
_Oracle_ & _Prep._ & _Space_ & _Query_ & _Output_ \\
_Max-Flow_ & \(O((fn)^\omega)\) & _O_((_fn_)<sup>2</sup>log_n_) & \(\widetilde{O}(f^{3\omega})\) & \(\lambda_{G+U}(s,t)\) \\
_Nearest Min-Cut_ & \(O((fn)^\omega)\) & _O_((_fn_)<sup>2</sup>log_n_) & \(\widetilde{O}(f^{3\omega} n)\) & _NMC_<sub>_G+U_</sub>(_s,t_) \\
_Min-Cost Flow_ & \(\widetilde{O}(W(fn)^3)\) & _O(W(fn_)<sup>3</sup>log_n_) & \(\widetilde{O}(f^{3\omega+1}Wn)\) & _Min-cost max-flow in G+U_ \\
\end{tabular}

