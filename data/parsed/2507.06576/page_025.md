<tbc>Let _l(e_)=1 for all \(e\in E\). We partition the set of edges _E_ based on their distance from _v_<sub>0</sub> as follows:<tbc>

\(E_1=\{e\in E|l(v_0,e)=0\},E_2=\{e\in E|l(v_0,e)=1\},E_3=\{e\in E|l(v_0,e)=2\}.\)

<tbc>Note that _E_<sub>1</sub> is the set of incident edges to _v_<sub>0</sub>, and _E_<sub>1</sub>_,E_<sub>2</sub>_,E_<sub>3</sub> is a partition of _E_. Now we are going to define an instance of the minimum multicut problem on _G_. We first assign costs to edges as follows:<tbc>

\(c(e)=\left\{\begin{array}{ c c }
k & e\in E_1 \\
2 & e\in E_2 \\
1 & e\in E_3
\end{array}\right.\)

<tbc>be the cost function, and let \(S=\{(u,v)\in V\times V|l(u,v)\ge 4\}\) be the set of source-sink pairs. We will denote this multicut instance by _M_. It is easy to see that \(x=\{x_e=\frac{1}{4}|e\in E\}\) is a feasible fractional solution to _M_ with cost

\(\frac{k\cdot k+2\cdot k^2\cdot 2+4k^2\cdot 1}{4}=\frac{9\cdot k^2}{4}.\)

We will now show that the cost of any feasible multicut (i.e. an integral solution) is at least 5_k_<sup>2</sup>-9_k_. This will imply that the integrality gap for this instance is at least \(\frac{20}{9}-\frac{4}{k}\), which can be arbitrarily close to \(\frac{20}{9}\) . More precisely, for any \(\epsilon>0\), we can set \(k>\frac{4}{\epsilon}\) to obtain a lower bound of \(\frac{20}{9}-\epsilon\).

Recall that for a graph _H_, we use _V(H_) and _E(H_) to denote the set of vertices and edges in _H_, and for \(E'\subseteq E(H)\), we use \(c(E')\) to denote the total cost of edges in \(E'\). Let _F_ be a feasible multicut solution to _M_. Let \(t=|E_1\cap F|\). For now assume that 0_\<t\<k_. Without loss of generality, assume that \((v_0,v_i)\in F\) for _i_=1_,...,t_.

**Claim 6.** \(c(F\cap E(H''_i))\ge 4\cdot(k-1)+k\) _for i_=1,2_,...,t._

_Proof._ We will prove the claim for _i_=1. The proof for other values of _i_ is identical. Denote _H_<sub>1</sub>_,...,H<sub>k</sub>_ as the _k_ copies of _H_ incident at _v_<sub>1</sub>. For each \(1\le i\le k\), we call _H<sub>i</sub>_ good if \(rad_F(v_1)\le 1\), and we call it bad otherwise. It is not too difficult to see that there is at most one bad _H<sub>i</sub>_. Suppose that _H_<sub>1</sub>_,H_<sub>2</sub> are bad graphs, then there exists \(a\in V(H_1),b\in V(H_2)\) such that \(l(a,v_1),l(b,v_1)\ge 2\). But this is a contradiction since _a_ and _b_ are within the same component as _v_<sub>1</sub> after the removal of _F_, and are at a distance 4 apart, i.e. they are a source-sink pair in the multicut instance _M_. Thus, there are at least _k_-1 good graphs attached to _v_<sub>1</sub>. By doing a simple case analysis, it can be verified that \(c(F\cap E(H_i))\ge 4\) if _H<sub>i</sub>_ is good. Combining the above with the fact that the edge between _v_<sub>0</sub>_,v_<sub>1</sub> is included in _F_, we obtain the statement of the claim.

Note that _v_<sub>_t_+1</sub>_,...,v<sub>k</sub>_ are within the same component as _v_<sub>0</sub> after the removal of _F_. For each \(t+1\le j\le k\), we call \(H''_j\) _good_ if \(rad_F(v_0)\le 1\) in \(H''_j\), otherwise we call it _bad_. Using a similar argument as in the proof of Claim 8, one can show that there at most 1 bad \(H''_j\). Thus, we have at least _k-t_-1 good \(H''_j\)’s.

**Claim 7.** \(c(F\cap E(H''_j))\ge 5\cdot k\) _if_ \(H''_j\) _is_ good _for_ \(t+1\le j\le k\).

vo
v1
Vk
H'1
H'k
G

