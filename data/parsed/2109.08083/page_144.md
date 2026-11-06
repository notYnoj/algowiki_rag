<tbc>Proof. We consider the effect of the parity modification and greedy cover on Proposition 6.66. In total, the process removed at most \(2.5t_0^{1-\epsilon} p_\mathrm{gr}\) vertices from each of the four parts. Any properties relating to vertices, edges and subsets all contained within _I_<sub>_t_<sub>20</sub></sub> remain the same as in _H<sup>c</sup>_. Otherwise, for property (i), and every 0- valid subset \(S\subseteq\mathcal{T}\) , we have from Corollary 6.67 that \(|V(H^c[S])|=\Theta\left(t_0p_\mathrm{gr}\right)\), since \(S\unknown\subseteq I_{t_{20}}\). Thus we have that<tbc>

\(|V(H^c[S])|\ge|V(H_0[S])|\ge|V(H^c[S])|-2.5t_0^{1-\epsilon} p_\mathrm{gr},\)

<tbc>where \(|V(H^c[S])|-2.5t_0^{1-\epsilon} p_\mathrm{gr}=(1-O(t_0^{-\epsilon}))|V(H^c[S])|\). Thus, \(|V(H_0[S])|=(1\pm O(t_0^{-\epsilon}))|V(H^c[S])|\). That is, there exists a constant _C_<sub>0,1</sub> such that

\(|V(H_0[S])|=(1\pm C_{0,1}t_0^{-\epsilon})\sum_{v\in V(H[S])}(1-d_{w_H^o}(v)),\)

for every 0-valid subset _S_.

For (ii)-(v) we argue in a similar way. For (iv), we consider _J_-layer inter vals of size at least \(t_0^{1-\epsilon/2}\). We have from Corollary 6.67 that \(|V_{o/e}^J(H^c[S])|\ge\Theta\left(t_0^{1-\epsilon/2}p_\mathrm{gr}\right)\). Hence \(|V_{o/e}^J(H^c[S])|-2.5t_0^{1-\epsilon} p_\mathrm{gr}=(1-O(t_0^{-\epsilon/2}))|V_{o/e}^J(H^c[S])|\). So there exists a constant _C_<sub>0,4</sub> such that

\(|V_{o/e}^J(H_0[S])|=(1-C_{0,4}t_0^{-\epsilon/2})\sum_{v\in V_{o/e}^J(H[S])}(1-d_{w_H^o}(v)),\)

for every _J_-layer interval of size at least \(t_0^{1-\epsilon/2}\).

Now, for (ii), we have that for every open and closed 0-valid tuple where (_S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>) are not contained in _I_<sub>_t_<sub>20</sub></sub>, that \(|S_1|=\Theta(t_0)\). By Corollary 6.67, it follows that \(|E_{H^c}(v,S_1,S_2,S_3)|=\Theta\left(|E_\mathcal{T}(v,S_1,S_2,S_3)|p_\mathrm{gr}^3\right)=\Theta\left(t_0p_\mathrm{gr}^3\right)\). Now, since \(2.5t_0^{1-\epsilon} p_\mathrm{gr}\) vertices may have been removed in each part, and each such vertex could feasibly dictate one unique edge in _E<sub>H<sup>c</sup></sub>(v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>), it follows that<tbc>

\(|E_{H^c}(v,S_1,S_2,S_3)|\ge|E_{H_0}(v,S_1,S_2,S_3)|\ge|E_{H^c}(v,S_1,S_2,S_3)|-10t_0^{1-\epsilon} p_\mathrm{gr}.\)

<tbc>From above, we have that \(|E_{H^c}(v,S_1,S_2,S_3)|-10t_0^{1-\epsilon} p_\mathrm{gr}=(1-O(p_\mathrm{gr}^{-2}t_0^{-\epsilon}))\). It follows that there exists an absolute constant _C_<sub>0,2</sub> such that

\(|E_{H_0}(v,S_1,S_2,S_3)|=(1\pm C_{0,2}p_\mathrm{gr}^{-2}t_0^{-\epsilon})\sum_{e\in E_H(v,S_1,S_2,S_3)}\prod_{u\in e\backslash\{v\}}(1-d_{w_H^o}(u)),\)

for every 0-valid tuple (_v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>). Similarly, for an edge allowable function _f_ where _f(e_) has the same order for every \(e\in H\), it is clear that the relative impact has the same order.

The same argument holds for (v), however, again an _J_-layer interval may have size \(t_0^{1-\epsilon/2}\), and hence as for (iv), we have that

\(|E_{H_0}(v,I^J,O/E)|=(1\pm C_{0,5}p_\mathrm{gr}^{-2}t_0^{-\epsilon/2})\sum_{e\in E_H(v,I^J,O/E)}\prod_{u\in e\backslash\{v\}}(1-d_{w_H^o}(u)),\)

for _I<sup>J</sup>_ an _J_-layer interval, \(v\notin J\), and _C_<sub>0,5</sub> some absolute constant.

Finally, for (iii), note that every additional vertex removed from _H<sup>c</sup>_ to _H_<sub>0</sub> is in at most _O(j<sub>i</sub>_) relevant zero-sum configurations for an _i_-bad edge _e_ and every \(i\in[c_g]\), and _O(t_<sub>1</sub>) configurations for an edge of type \((\alpha,\beta,0)_i\) with \(\alpha\neq 0\) and \(i\in[c_g]\). Additionally, using fact 3.24 and Theorem 3.28, we have that these types of edge are in \(\Theta\left(j_it_0p_\mathrm{gr}^{12}\right)\) and \(\Theta\left(t_0^2p_\mathrm{gr}^{12}\right)\) relevant configurations respectively. Thus

