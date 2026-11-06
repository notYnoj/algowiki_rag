Input: - An instance I.<br>
- A matching M.<br>
- A tie-breaking strategy S.<br>
- Information on the ties in the instance \(\phi\).<br>
- A small probability p<sub>d</sub>.<br>
- Two integer k<sub>u</sub> and k<sub>w</sub>.<br>
Output: - A tie-breaking strategy S.<br>
- A set of agents whose preference lists are altered Q<sub>a</sub>.<br>
Function RefineTieBreakingStrategy(I,M,S):<br>
   \(Q_a:=\emptyset\) ; \(\triangleright\) a set of agents whose preference lists are altered<br>
   \(R_M^b:=\mathtt{ObtainAdjustments}(I,M)\);<br>
   if (a small probability of p<sub>d</sub> or \(R_M^b=\emptyset\)) then<br>
   X:=<br>
randomly<br>
select<br>
_k<sub>u</sub>_<br>
agents<br>
from<br>
_U_<br>
and<br>
_k<sub>w</sub>_<br>
agents<br>
from<br>
_W_<br>
;<br>
   for \((eachv\in X)\) do<br>
   \(Q_a:=Q_a\cup v\);<br>
   for (each tie in v’s preference list) do<br>
   Break the tie arbitrarily and update S;<br>
   end<br>
   end<br>
   else<br>
   (f,x):=<br>
randomly<br>
select<br>
one<br>
adjustment<br>
from<br>
\(R_M^b\)<br>
;<br>
   \(Q_a:=Q_a\cup x\);<br>
   Update S to position f at the highest rank in x’s tie-free preference<br>
list<br>
among<br>
those<br>
agents<br>
in<br>
\(\phi_f(x)\)<br>
;<br>
   end<br>
   return S,Q<sub>a</sub>

intersection \(\phi_f(x)\cap M(x)\) is non-empty, an adjustment is initiated. This adjustment aims to improve f’s rank in x’s tie-free preference list by positioning f at the highest rank among those agents in \(\phi_f(x)\), thereby ensuring f ranks above at least one agent currently matched with x. This adjustment introduces (f,x) as a BP and enhances f’s likelihood of being matched with x. All adjustments in M are stored in R<sub>M</sub>, which can be represented as \(R_M=\{(f,x)|f\in F_M,x\in\xi_f^M,\phi_f(x)\cap M(x)\neq\varnothing\}\). The set of adjustments related to one free agent f is denoted by \(R_M(f)=\{a\in R_M|a[1]=f\}\), where a\[i\] is the i-th element in adjustment a. Additional discussions on the relationship between our proposed tie-adjustment mechanism and the well-established breakmarriage operation are provided in Section S2 of Online Resource 1.<tbc>

2. Construct \(R_M^b\) by sampling from R<sub>M</sub> (lines 12-16). One free agent may have multiple adjustments, and the number of adjustments can vary among different free agents. In some cases, agents with many unassigned positions might have relatively few adjustments, while those with fewer unassigned positions<tbc>

**Algorithm 2:** Refine tie-breaking strategy

