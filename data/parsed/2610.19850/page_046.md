## 5 Hardness results

We provide in this section polynomial reductions from 3-SAT to two extension problems: Minimal (_a,b_)-separator Extension and PMC Extension. Finally, we show that in, our reduced instance for PMC Extension,the constraint on forbidden vertices can be withdrawn. This allows us to conclude the NP-hardness of PMC Subset, which is PMC Extension with the restriction \(F=\emptyset\).

### 5.1 NP-hardness of minimal separator extension

We focus on the problem consisting in extending a minimal (_a,b_)-separator. To the best of our knowledge, the computational complexity of this problem is unknown. An example of yes-instance is given in Figure 16.

We propose a polynomial reduction from 3-SAT to Minimal (_a,b_)-separator extension. This hardness result will be used as an intermediary step to handle the computational complexity of PMC Extension in subsection 5.2. Given a CNF 3-SAT formula \(\Phi\), we build a corresponding graph \(G(\Phi)\) which is an instance of Minimal (_a,b_)-separator extension.

**Theorem 12.** Minimal (_a,b_)-separator extension _is NP-Complete._

_Proof._ Obviously, the problem belongs to NP since checking whether a set _S_ is a minimal (_a,b_)-separator, contains _M_ and does not intersect _F_, can be done in polynomial time. We will now reduce from 3-SAT. We work on the specific case \(F=\emptyset\). Let _x_<sub>1</sub>_,...,x<sub>n</sub>_ be the Boolean variables, _x<sub>i</sub>_ and <o>_x<sub>i</sub>_</o> the possible expressions for a literal involving variable _x<sub>i</sub>_. Let \(\Phi=\wedge_{j=1}^mC_j\) be a CNF 3-SAT formula with the clauses _C<sub>j</sub>_, made up of at most three literals. We denote by <o>_C<sub>j</sub>_</o> the negation of _C<sub>j</sub>_.

**Construction.** We transform the formula \(\Phi\) into a graph \(G(\Phi)\). We propose a 6-vertex gadget to represent variables. It models the selection of a Boolean value for variable _x<sub>i</sub>_.<tbc>

minimal (a,b)-separator extension
Input: A graph G=(V,E), a,b ∈ V with (a,b)notin E, a set M V of mandatory vertices, a set F V of forbidden ones such that M F=0.
Question: Is there a minimal (a,b)-separator S Vbackslash a,b such that M S and S F=0 ?
S
f1
m1
b
a
m2
f2

Figure 16: An instance of Minimal (_a,b_)-separator Extension with a graph _G_, vertices _a,b_, sets _M_={_m_<sub>1</sub>_,m_<sub>2</sub>} and _F_={_f_<sub>1</sub>_,f_<sub>2</sub>}. A solution is given in blue.

