In Section 4 we circumvented the second issue by only considering sensitivities that decrease the objective function, and establishing a lower bound on their occurrence independent of the ordering \(\sigma\). Here we are also able to handle the second issue by shooting for a sufficient condition for sensitivity rather than a criterion. We do so by requiring that for no pair of distinct orderings \(\sigma_1\) and \(\sigma_2\), condition (21) holds (unless the two affected leaves are siblings). Similar to the case of binary trees, we guarantee that (21) fails based on parity considerations given the product condition.

For the analysis we again assume without loss of generality that _T_ has no nodes of degree 1. We use the same notation as in Section 5: Let \(\ell_\mathrm{lo}\) denote the affected leaf that is smaller with respect to \(\rho\), and \(\ell_\mathrm{hi}\) the other affected leaf. Let _L<sub>i</sub>_ denote the leaf set \(L_i\doteq\mathrm{L}(T_{u_i})\), where _u_<sub>1</sub>_,...,u<sub>k</sub>_ are the children of \(v=\mathrm{LCA}(\ell_\mathrm{lo},\ell_\mathrm{hi})\). We also write _u_<sub>lo</sub> for the child of _v_ that contains \(\ell_\mathrm{lo}\) in its subtree, and _L_<sub>lo</sub> for the leaf set of the subtree rooted at _u_<sub>lo</sub>, and define \(\ell_\mathrm{hi}\), _u_<sub>hi</sub>, and _L_<sub>hi</sub> similarly. See Figure 12 for a sketch of the setting.

We slightly abuse notation and let \(\sigma\) denote both the ordering of the entire tree _T_ as well as the ranking of the children of _v_. By the analysis of Section 5, we have that for two orderings \(\sigma_1\) and \(\sigma_2\) the situation (21) can only occur if \(\sigma_1(u_\mathrm{lo})<\sigma_1(u_\mathrm{hi})\), \(\sigma_2(u_\mathrm{lo})>\sigma_2(u_\mathrm{hi})\), and

\(\mathrm{RInv}_\rho(T_v,\rho,\sigma_1)-\mathrm{RInv}_\rho(T_v,\rho,\sigma_2)=-1=\mathrm{DInv}_\rho(\{\ell_\mathrm{lo}\},\{\ell_\mathrm{hi}\}).\) (22)

For any two disjoint sets of leaves, (20) lets us write

\(\mathrm{XInv}_\rho(A,B)=\frac{1}{2}\mathrm{DInv}_\rho(A,B)+\frac{1}{2}|A|\cdot|B|.\) (23)

Applying (23) to all the terms involved in (4), we have

\(\mathrm{RInv}_\rho(T_v,\rho,\sigma)=\sum_{1\le i<j\le k}\mathrm{XInv}_\rho(L_i,L_j)\cdot\mathbb{I}[\sigma(i)<\sigma(j)]\)<br>
\(+\sum_{1\le i<j\le k}\mathrm{XInv}_\rho(L_j,L_i)\cdot\mathbb{I}[\sigma(i)>\sigma(j)]\)<br>
\(=\frac{1}{2}\sum_{1\le i<j\le k}\big(\mathrm{DInv}_\rho(L_i,L_j)\cdot(-1)^{\mathbb{I}[\sigma(i>\sigma(j)]}+|L_1|\cdot|L_2|\big)\)<br>
\(\mathrm{RInv}_\rho(T_v,\rho,\sigma_1)-\mathrm{RInv}_\rho(T_v,\rho,\sigma_2)=\sum_{1\le i<j\le k\sigma_1(i)<\sigma_2(j)\sigma_2(i)>\sigma_2(j)}\mathrm{DInv}_\rho(L_i,L_j)+\sum_{1\le i<j\le k\sigma_1(i)>\sigma_2(j)\sigma_2(i)<\sigma_2(j)}\mathrm{DInv}_\rho(L_i,L_j)\)

v
k
u1
ulo
uhi
uk
lo
lhi

Figure 12: Sensitivity for general trees

