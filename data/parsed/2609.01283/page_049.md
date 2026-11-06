## 8.4 Subset Sensitivity for \(\alpha\)-Factors and Matching

We now lift the \(\alpha\)-factor oracles of Section 7.2 to the subset model. Recall that in Theorem 7.1, we reduced the \(\alpha\)-factor problem to matroid parity, which allowed us to handle two regimes in the general setting: the _k_-bounded case (Section 7.2.1), and the arbitrary-degree case (Section 7.2.2), where an update on _G_ is reduced to an update on an auxiliary graph _H_ of dimension _O(nf_) using Theorem 7.7. To obtain subset sensitivity, we replace the general sensitivity oracle for linear matroid parity (Theorem 6.2) with its subset sensitivity counterpart (Theorem 8.11), which fixes a susceptible set _E<sub>Q</sub>_ of size \(\sigma\) during preprocessing. The following results are obtained by a straightforward combination of Theorem 7.1 and Theorem 8.11.

### The _k_-Bounded Case

We obtain the following oracle for the case when \(\alpha(v)\unknown k\) for all \(v\in V\) .

**Theorem 8.12.** _Let G_=(_V,E,c_) _be an undirected graph with integer edge costs in_ \[-_W,W_\]_, degree bounds_ \(\alpha\unknown k\)_, and a susceptible edge set E<sub>Q</sub> of size_ \(\sigma\)_. Then there exist the following subset sensitivity oracles that, for any update set_ \(U\subseteq E_Q\) _with f_=|_U|, answer queries on G+U with high probability:_

_Proof._ Recall from Section 7.2.1 that when \(max_v\alpha(v)\unknown k\), the underlying matrix _A_ for the matroid parity problem is of size \(kn\times 2m\) (yielding a rank _r=kn_), and each edge corresponds to one pair in the matroid ground set. Therefore, plugging _r=kn_ into Theorem 8.11 directly yields the desired oracle.

### Arbitrary Degree Bounds via Auxiliary Graphs

We now remove the assumption \(\alpha\unknown k\). As established in Section 7.2.2, a direct expansion is prohibitively large, so we retain the auxiliary graph _H_ and the bijection of Theorem 7.7: a query on _G+U_ is answered by an equivalent query on a \(\beta\)-factor of _H+U<sub>H</sub>_, where _H_ has degree bounds \(\beta\unknown 2f\), dimension _N<sub>H</sub>=O(nf_), and update size |_U<sub>H</sub>_|=_O(f_). In the subset model, the susceptible edges _E<sub>Q</sub>_ of _G_ translate, under the encoding of Section 7.2.2, to a susceptible set \(E_Q^H\) in _H_: each susceptible edge \((a,b)\in E_Q\) affects only its Layer 1 copy (_a_<sub>1</sub>_,b_<sub>1</sub>) or Layer 2 copy (_a_<sub>2</sub>_,b_<sub>2</sub>), together with the associated parallel and sink edges at _a_ and _b_. Hence, \(|E_Q^H|=O(\sigma)\), and we can instantiate the _k_-bounded subset oracle of Theorem 8.12 on _H_ using the parameter _k_:=2_f_.

**Theorem 8.13.** _Let G_=(_V,E,c_) _be an undirected graph with integer edge costs in_ \[-_W,W_\]_, arbitrary degree bounds_ \(\alpha\)_, and a susceptible edge set E<sub>Q</sub> of size_ \(\sigma\)_. Then there exist the following subset sensitivity oracles that, for any update set_ \(U\subseteq E_Q\) _with f_=|_U|, answer queries on G+U with high probability:_

_Proof._ First, we compute a fixed initial \(\alpha\)-factor of minimum-cost, and refer to it as _M_. Finding the \(\alpha\)-factor of _G_ takes \(O(T_\alpha)\) time \[Ans85, DHZ20\]. Then we construct the graph _H_ and the function \(\beta\).

\begin{tabular}{ccccc}
_Oracle_ & _Prep._ & _Space_ & _Query_ & _Output_ \\
_Existence_ & \(O(\sigma^2(kn)^{\omega-2}+(kn)^\omega)\) & \(O(\sigma^2)\) & \(O(f^\omega)\) & _Whether G+U has an_ \(\alpha\)_-factor_ \\
_Min-Cost_ & \(\widetilde{O}(W\sigma^2(kn)^{\omega-1}+W(kn)^{\omega+1})\) & \(\widetilde{O}(Wkn\sigma^2)\) & \(\widetilde{O}(Wknf^\omega)\) & _Weight of a min-cost_ \(\alpha\)_-factor of G+U_ \\
\end{tabular}

\begin{tabular}{ccccc}
_Oracle_ & _Prep._ & _Space_ & _Query_ & _Output_ \\
_Existence_ & \(O(\sigma^2(fn)^{\omega-2}+(fn)^\omega+T_\alpha)\) & \(O(\sigma^2)\) & \(O(f^\omega)\) & _Whether G+U has an_ \(\alpha\)_-factor_ \\
_Min-Cost_ & \(\widetilde{O}(W\sigma^2(fn)^{\omega-1}+W(fn)^{\omega+1})\) & \(\widetilde{O}(Wfn\sigma^2)\) & \(\widetilde{O}(Wnf^{\omega+1})\) & _Weight of a min-cost_ \(\alpha\)_-factor of G+U_ \\
\end{tabular}

