**Proposition 3** _If the domination rules include target-coalitions that do not overlap with any coalition in the precondition, there are instances and starting states such that every sequence cycles._

_Proof._ Consider the following small example with _N_={1_,...,_6}, C={{1,2}, {3,4}, {5,6}}, C_<sub>g</sub>_=C, and weights _w(C_)=1 for all \(C\in\mathcal{C}\). There are no generation rules: \(T=\emptyset\) (in addition to C_<sub>g</sub>_=C). For the domination rules, we consider non-overlapping coalitions in precondition and target:

\(D=\{(\{\{1,2\}\},\{3,4\}),(\{\{3,4\}\},\{5,6\}),(\{\{5,6\}\},\{1,2\})\}.\)

The initial state is C_<sub>start</sub>_={1,2}.

Now with {1,2} existing, {3,4} is dominated and cannot be formed although it is a candidate coalition. The other candidate coalition {5,6} is undominated and represents the unique improvement step. As {5,6} dominates {1,2} (but not vice versa), we lose {1,2} when {5,6} is formed. Now {4,3} is the unique undominated candidate coalition and is formed. Thereby, we lose {5,6}, and {1,2} becomes undominated. Now {1,2} is formed, {4,3} is deleted, and the cycle is complete. \(\sqcap\sqcup\)

Consistent generation and domination rules arise in a large variety of settings, not only in basic matching games but also in some interesting extensions.

**Corollary 1.** _Consistent generation and domination rules are present in_

- _locally stable matching if agents can create k_=1 _matching edges and have lookahead_ \(\ell=2\) _in_ \(G=(V,M\cup L)\).<tbc>

**-** _socially stable matching, even if agents can create_ \(k\ge 1\) _matching edges._<tbc>

**-** _considerate matching, even if agents can create_ \(k\ge 1\) _matching edges._<tbc>

**-** _friendship matching, even if agents can create_ \(k\ge 1\) _matching edges._

Due to space restrictions we cannot give a detailed description of the embedding into coalition formation games with constraints. In most cases the embedding is quite straightforward. Agents and edge set are kept as well as the benefits. The generation and domination rules often follow directly from the definitions. However, we want to shortly discuss the more complex mapping of _k_-matching for _k\>_1 into coalition formation games with constraints. By definition no agent is allowed to participate in more than one coalition at the same time. Thus we cannot directly embed _k_-matching. Instead we have to map every agent _u_ to _k_ copies _u_<sub>1</sub>_,...,u<sub>k</sub>_ who can match one vertex each. With these "independent" copies we now encounter the problem that {_u<sub>i</sub>,v<sub>j</sub>_} and \(\{u_{i^\prime},v_{j^\prime}\}\) should not exist simultaneously. This issue can easily be handled via the domination rules, but, as {_u<sub>i</sub>,v<sub>j</sub>_} and \(\{u_{i^\prime},v_{j^\prime}\}\) do not share any agents, rules of the form \((\{\{u_i,v_j\}\},\{u_{i^\prime},v_{j^\prime}\})\) would not be consistent. Thus for every edge {_u,v_} we introduce an auxiliary vertex _a<sub>u,v</sub>_. Potential coalitions then are given by {_u<sub>i</sub>,v<sub>j</sub>,a<sub>u,v</sub>_} instead of {_u<sub>i</sub>,v<sub>j</sub>_}. The exact embedding for every type of game can be found in the appendix. Additionally an exemplar proof for correctness is stated.

