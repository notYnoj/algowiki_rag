**Algorithm 9** \(\text{\texttt{WeightedAdditiveAPASP}}(G,\beta)\)

**Input :** Unweighted, undirected Graph _G_=(_V,E_) with _n_ vertices; approximation parameter \(\beta\)

**Output:** Distance estimate \(\hat{\delta}:U\times V\rightarrow\mathbb{Z}\) such that \(\delta(u,v)\le\hat{\delta}(u,v)\le\delta(u,v)+\beta\) for all \(u,v\in V\)

135 Phase 0: Set up and Decompose Graph

136 \(\hat{\delta}(u,v)\leftarrow\left\{\begin{array}{ c c }
1 & (u,v)\in E \\
\infty & \text{o/w}
\end{array}\right.\)

137 \(k\leftarrow 3\beta-1\)

138 \(x\leftarrow\) solution to \(\omega\left(1-\frac{|k/3|}{|k/3|+2}x,1-x,1-\frac{|k/3|-1}{|k/3|+2}x\right)=2+\frac{x}{|k/3|+2}\)

139 \(s_{k-i}\leftarrow n^{i\cdot\frac{x}{|k/3|+2}}\) for all \(1\le i\le\lfloor k/3\rfloor+2\)

140 \(k_0\leftarrow k-(\lfloor k/3\rfloor+2)=k-\lfloor k/3\rfloor-2\)

141 (_D_<sub>_k_<sub>0</sub></sub>_,D_<sub>_k_<sub>0</sub>+1</sub>_,...,D<sub>k</sub>),(E_<sub>_k_<sub>0</sub></sub>_,E_<sub>_k_<sub>0</sub>+1</sub>_,...,E<sub>k</sub>),_\(E^*\leftarrow\text{\texttt{WeightedDecompose}}(G,(s_{k_0},s_{k_0+1},\dots,s_{k-1}))\)

142 Phase 1: Estimate Distances on High-Degree Paths

143 \(t_i\leftarrow\frac{n}{2^i}\) for all \(1\le i\le l-1=\lceil(1-x)\mathrm{log}n\rceil\)

144 (_C_<sub>1</sub>_,C_<sub>2</sub>_,...,C<sub>l</sub>),(F_<sub>1</sub>_,F_<sub>2</sub>_,...,F<sub>l</sub>),_\(F^*\leftarrow\text{\texttt{WeightedDecompose}}(G,(t_1,t_2,\dots,t_{l-1}))\)

145 for \(0\le i\le l\) do

146 **for** \(w\in C_i\) **do**

147 \(X_i(w)\leftarrow\text{\texttt{Dijkstra}}(w)\) on _G<sub>i</sub>_=(_V,F<sub>i</sub>_)

148 \(\hat{\delta}(w,v)\leftarrow\mathrm{min}(\hat{\delta},X_i(w,v))\) for all \(v\in V\)

149 Construct \(|D_{k_0+2}|\times|C_i|\) matrix _A<sub>i</sub>_ where _A<sub>i</sub>(v,w_)=_X<sub>i</sub>(w,v_)

150 Construct \(|C_i|\times|V|\) matrix _B<sub>i</sub>_ where _B<sub>i</sub>(w,v_)=_X<sub>i</sub>(w,v_)

151 \(\hat{\delta}\leftarrow\mathrm{min}\left(\hat{\delta},\text{\texttt{ApproximateMinPlus}}\left(A_i,B_i,1+\frac{\varepsilon}{3}\right)\right)\)

152 Phase 2: Estimate Distances on Low-Degree Paths

153 for \(k_0+1\le j\le k\) do

154 **for** \(w\in D_j\) **do**

155 \(G_{j,w}=(V,E_j\cup(u\times V)\cup E^*)\)

156 \(\hat{\delta}\leftarrow\text{\texttt{Dijkstra}}(G_{j,w},w,\hat{\delta})\)

To verify the correctness of our algorithm, we will require the following analog of Lemma A.3. Note that this is equivalent to Lemma 5.2 in Cohen and Zwick \[CZ01\].

**Lemma 6.4.** _Let G be an undirected, weighted graph with n vertices and m edges and weight function_ \(w:E\rightarrow\mathbb{R}\)_. Let n=s_<sub>_k_<sub>0</sub></sub>_\>s_<sub>_k_<sub>0</sub>+1</sub>_\>...\>s_<sub>_k_-1</sub>_\>s<sub>k</sub>_=0 _be degree thresholds._

_For_ \(k_0+1\le j\le i\)_, let_ \(\delta_j\) _denote the estimate after the j-th iteration. Let P be a path between_ \(u\in D_j\) _and_ \(v\in V\) _such that_ \(P\subset E_{k_0+1}\)_. Define the set_ \(L(P,j)=\{k_0+1\le i\le j-1\text{\textit{s.t.}}P\cap(E_i\backslash E_{i+1})\neq\emptyset\}\)_. Then, there is a set_ \(\mathcal{E}_j\subset P\) _such that_ \(|\mathcal{E}_j|\le|L(P,j)|\), \(\mathcal{E}_j\cap E_j=\emptyset\)_, and_ \(\delta_j(u,v)\le\text{\texttt{wt}}(P)+2\text{\texttt{wt}}(\mathcal{E}_j)\).

_Proof._ We proceed by induction. In the base case, let |_L(P,j_)|=0 so that \(P\subset E_j\). In particular, since \(u\in D_j\), when we execute `Dijkstra` in the _j_-th iteration, we find _P_ so that \(\hat{\delta}_j(u,v)=\text{\texttt{wt}}(P)\).

Now, let |_L(P,j_)|_\>_0. Let _e_<sub>0</sub> be the closest edge to _v_ not in _E<sub>j</sub>_. Then, \(e_0\in E_l\backslash E_{l+1}\) for some _l\<j_. Let _w_ be the endpoint of _e_<sub>0</sub> closest to _v_. Since \(\mathrm{deg}(w)\ge s_l\), there is some \(w^*=r(w,D_l)\in D_l\) such that rank_<sub>w</sub>(w_<sup>∗</sup>_,w)\<s<sub>l</sub>_ so that \((w^*,w)\in E_{l+1}\subset E_l\). In particular, rank_<sub>w</sub>(w_<sup>∗</sup>_,w)\<s<sub>l</sub>\<_rank_<sub>w</sub>(e_<sub>0</sub>). If we consider the sub-path \(P_{u,w}\subset P\), we have \(L(P_{u,w},l)\subset L(P,j)\cap\{k_0+1,k_0+2,\dots,l-1\}\). Now, applying the inductive hypothesis to the path \(P_{u,w}\cup(w,w^*)\),<tbc>

\(\hat{\delta}_l(w^*,u)\le w(P_{u,w})+\text{\texttt{wt}}(w^*,w)+2\text{\texttt{wt}}(\mathcal{E}_l)\)

