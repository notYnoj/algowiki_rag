• S : the Big-M formulation, with Constraints (18), (20), and (22) to (25) from the DCMF<sub>env</sub> relaxation, provides a relaxation based on the \(s_{\epsilon,\theta}\) function introduced in Section 3.2.<tbc>

• T : the Big-M formulation, with Constraints (18), and (21) to (25) from the DCMF<sub>env</sub> relaxation provides a relaxation based on the \(t_{\epsilon,\zeta}\) function introduced in Section 3.3 ; this formulation is comparable to the one presented in \[16\].

The heuristics and relaxations were tested on two sets of instances. The first set is from the Survivable Network Design Library (SND-Lib, \[26\]) on which, for every link \((u,v)\in A\), a reverse link (_v,u_) with capacity _c_<sub>(_u,v_)</sub> was added if it did not exist. Information on these instances is shown in  1. The second set includes 126 randomly generated instances (connected Erdös-Rényi graphs, viewed as symmetric directed graphs with symmetric arc costs: _c_<sub>(_u,v_)</sub>=_c_<sub>(_v,u_)</sub>). These randomly generated instances range from 25 to 200 commodities, 10 to 50 vertices and 30 to 475 arcs.

For each demand \(k\in K\), a set _P<sup>k</sup>_ of the 10 shortest paths, weighted by \(\frac{1}{c_a}\), was generated through Yen’s algorithm \[35\]. For each instance, the same delay \(d=1.1\times\mathrm{max}_{k\in K,p\in P^k}\sum_{a\in p}\frac{1}{c_a}\) was used as the maximum delay for every commodity \(k\in K\). This maximum delay ensures that every path could carry some traffic.

## 6.1 Heuristics

We first compare the lower bounds obtained by these 3 heuristics H_<sub>all paths</sub>_, H_<sub>greedy</sub>_ and H_<sub>threshold</sub>_ defined in Section 5. The heuristic H_<sub>threshold</sub>_ uses the threshold parameter \(S^*=2-\frac{2}{|P|}+\frac{b\tilde{\gamma}}{u|P|}\) defined in the proof of Proposition 5.2.

Figures 5a and 5b show the gaps between these heuristic and the DCMF<sub>env</sub> relaxation, which provides the tightest known relaxation to the delay- constraint problem, as shown in Section 3. Gaps are defined as: \(gap=\frac{\gamma_H^*}{\gamma_{env}^*}-1\), with \(\gamma_H^*\) the objective value of the heuristic and \(\gamma_{env}^*\) the optimal solution of the DCMF<sub>env</sub> relaxation. In Figure 5b, instances are grouped by the number |_K_| of commodities and presented as a box plot (the box<tbc>

