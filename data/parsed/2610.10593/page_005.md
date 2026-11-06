## 2.2 Certified entropy penalties

The maximum-entropy penalties can be bounded without certifying the solution of an auxiliary optimization problem. Let \(\alpha\) be a distribution on an allowed set of shapes _D_, and let \(H_D^\mathrm{max}(\alpha)\) be the maximum entropy of a distribution on _D_ having the same three marginals as \(\alpha\). Choose arbitrary strictly positive factors _f<sub>X</sub>,f<sub>Y</sub>,f<sub>Z</sub>_, and put

\(t_u=\prod_{w\in\{X,Y,Z\}}f_w(u_w),U_D(\alpha;f)=\mathrm{log}_2\left(\sum_{u\in D}t_u\right)-\sum_{u\in D}\alpha(u)\mathrm{log}_2t_u.\) (4)

Then \(H_D^\mathrm{max}(\alpha)\le U_D(\alpha;f)\). Indeed, if \(\rho\) has the prescribed marginals, then

\(\sum_u\rho(u)\mathrm{log}_2t_u=\sum_u\alpha(u)\mathrm{log}_2t_u.\)

Nonnegativity of the relative entropy of \(\rho\) with respect to the distribution \(t/\sum_ut_u\) proves the inequality. Therefore

\(\widehat{P}_D(\alpha;f)=U_D(\alpha;f)-H(\alpha)\) (5)

is a valid upper bound on the combination-loss penalty. Its use can only reduce the retained exponent supplied by the construction. The factors are optimized along with the other parameters, but their optimality is not required for the certificate.

For completeness, the local quantities evaluated by the implementation can be written as follows. Extend the notation _H_ to a nonnegative vector by \(H(v)=-\sum_tv_t\mathrm{log}_2v_t\), with 0log<sub>2</sub>0=0. For child weights _a<sub>u</sub>_, distributions \(\beta_u^w\), and a set _S_ of exceptional child shapes, define

\(\eta_w(a,\beta;S)=\sum_{u\in S}a_uH(\beta_u^w)+\sum_t\left[H(v_t)-H\left(\left[\sum_Lv_t(L)\right]\right)\right],v_t=\sum_{u\notin Su_w=t}a_u\beta_u^w.\) (6)

Here _H_([_b_])=-_b_log<sub>2</sub>_b_; hence each bracket in (6) is the mass of _v<sub>t</sub>_ times the entropy of its normalization. At a positive occurrence _v_ in region _r_, write (_x,y,z_)=(_p<sub>r</sub>(X),p<sub>r</sub>(Y),p<sub>r</sub>(Z_)) and \(a_u=\alpha_{v,r}(u)+\alpha_{v,r}(s-u)\). The three local retained quantities are

\(c_{v,r,X}=H((\alpha_{v,r})_x)-\widehat{P}_{D_s}(\alpha_{v,r};f_{v,r}),c_{v,r,Y}=H(B_{v,r}^y)-\eta_y(a,\beta;\{u:u_z=0\}),c_{v,r,Z}=H(B_{v,r}^z)-\eta_z(a,\beta;\{u:u_x=0\text{or}u_y=0\}).\) (7)

The subscripts _X,Y,Z_ on _c_ denote extraction roles, rather than physical coordinates.

Let _m<sub>v</sub>_ be the mass of an occurrence. Root occurrences have mass \(m_v=\alpha^*(s_v)\), and masses are propagated by

\(m_{c(v,r,u)}+=m_vA_{v,r}\big(\alpha_{v,r}(u)+\alpha_{v,r}(s_v-u)\big).\) (8)

Contributions from all references to a shared child are added. The stage role totals are

\(R_{\ell,k}=\sum_{v\text{positive at level}\ell} m_v\sum_{r=1}^6A_{v,r}c_{v,r,k},\ell\in\{4,3\},k\in\{X,Y,Z\}.\) (9)

