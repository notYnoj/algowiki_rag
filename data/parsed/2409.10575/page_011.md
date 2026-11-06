might have many adjustments. This imbalance can impact the performance of the algorithm, particularly when it is difficult to increase the overall matching size by filling the positions of those agents with fewer unassigned positions. Consequently, a balanced set of adjustments, \(R_M^b\), is constructed through sampling from _R<sub>M</sub>_. Specifically, for each free agent \(f\in F_M\), we randomly select _k_=min{_b(f_)-|_M(f_)|,|_R<sub>M</sub>(f_)|} adjustments from _R<sub>M</sub>(f_) for inclusion in \(R_M^b(f)\). The value of _k_ is chosen to ensure that the number of candidate adjustments for each free agent _f_ does not exceed its unfilled capacity, which is defined as _b(f_)-|_M(f_)|.

Input: - An instance I.<br>
- A matching M.<br>
- Information on the ties in the instance \(\phi\).<br>
Output: A set of candidate adjustments \(R_M^b\)<br>
Function `ObtainAdjustments(I,M):`<br>
   F<sub>M</sub>:= all free agents in M;<br>
   \(R_M,R_M^b:=\emptyset\);<br>
   for \((eachf\in F_M)\) do<br>
   \(\xi_f^M:=\) the set of currently unmatched candidates for f;<br>
   for \((eachx\in\xi_f^M)\) do<br>
   if \((\phi_f(x)\cap M(x)\neq\emptyset)\) then<br>
\(R_M:=R_M\cup(f,x)\)<br>
;<br>
   end<br>
   end<br>
   end<br>
   for \((eachf\in F_M)\) do<br>
   k:=min{b(f)-|M(f)|,|R<sub>M</sub>(f)|};<br>
   X:= randomly select k adjustments from R<sub>M</sub>(f);<br>
   \(R_M^b:=R_M^b\cup X\);<br>
   end<br>
   return \(R_M^b\)

We take the SMTI instance described in  1 as an example to illustrate the effectiveness of adjustments in achieving a larger stable matching. Consider a tie-breaking strategy _S_<sub>1</sub> that assigns \(r_{m_1}^*(w_1)<r_{m_1}^*(w_3)\) and \(r_{w_2}^*(m_2)<r_{w_2}^*(m_4)\). The resulting stable matching \(M_1=\{(m_1,w_1),(m_2,w_2),(m_3,\varnothing),(m_4,\varnothing),(w_3,\varnothing),(w_4,\varnothing)\}\) has a size of two. The balanced set of the adjustments is \(R_{M_1}^b=\{(m_4,w_2),(w_3,m_1)\}\). After implementing adjustment (_m_<sub>4</sub>_,w_<sub>2</sub>), the new tie-breaking strategy _S_<sub>2</sub> results in \(r_{w_2}^*(m_2)>r_{w_2}^*(m_4)\). The corresponding stable matching \(M_2=\{(m_1,w_1),(m_2,w_4),(m_4,w_2),(m_3,\varnothing),(w_3,\varnothing)\}\) has a size of three. The balanced adjustments now are \(R_{M_2}^b=\{(w_3,m_1)\}\). Upon performing<tbc>

**Algorithm 3:** Obtain a set of candidate adjustments

