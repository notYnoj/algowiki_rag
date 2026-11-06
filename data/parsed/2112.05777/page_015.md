**Swap** A swap consists of swapping two adjacent agents in the preference relation of an agent. As sampling preference profiles that are at a certain swap distance from a given one turns out to be practically infeasible with more than 40 agents \[Boehmer et al., 2021a\], we always perform the same number of swaps in the preferences of each agent: If we are to perform _i_ Swap operations, then for each agent separately we replace its preferences by uniformly at random sampled preferences that are at swap distance _i_ from its original preferences (using the procedure described by Boehmer et al. \[2021a\]).

In Section 6.1, we present formulations of ISM and IASM as Integer Linear Programs (ILPs) which we use to solve these problems. Our subsequent experiments are divided into three parts: In Section 6.2, we analyze the relationship between the difference between P<sub>1</sub> and P<sub>2</sub> and the size \(|M_1\triangle M_2|\) of the symmetric difference between _M_<sub>1</sub> and _M_<sub>2</sub> for different methods to compute a stable matching _M_<sub>2</sub> in P<sub>2</sub>. In Section 6.3, we consider the relationship between the number of agent pairs that block _M_<sub>1</sub> in P<sub>2</sub> and the minimum symmetric difference between _M_<sub>1</sub> and a stable matching _M_<sub>2</sub> in P<sub>2</sub>. In Section 6.4, we study the trade-off between allowing _M_<sub>2</sub> to be blocked by some pairs and \(|M_1\triangle M_2|\).

## 6.1 (I)LP tion of INCREMENTAL (ALMOST) STABLE MARRIAGE

In our experiments, to compute the new matching _M_<sub>2</sub>, we solve an (integer) linear programming formulation of INCREMENTAL (ALMOST) STABLE MARRIAGE using Gurobi Optimization, LLC \[2021\]. We now start by presenting an ILP formulation for IASM and afterwards point out how it can be adapted to an LP formulation for ISM. We write \(m\unknown_w^{\mathcal{P}_2}m'\) to denote that _w_ weakly prefers _m_ to \(m'\) in profile P<sub>2</sub>.

For our ILP, we introduce two binary variables _x<sub>m,w</sub>_ and _y<sub>m,w</sub>_ for each pair \((m,w)\in U\times W\). Setting _x<sub>m,w</sub>_ to one corresponds to matching _m_ to _w_ in _M_<sub>2</sub> and setting _y<sub>m,w</sub>_ to one allows _m_ and _w_ to form a blocking pair for the matching _M_<sub>2</sub> in P<sub>2</sub>. Given an instance \(\mathcal{I}=(A=U\cup W,\mathcal{P}_1,\mathcal{P}_2,M_1,k,b)\) of IASM, we solve the following ILP:

\(min\sum_{(m,w)\in U\times W}x_{m,w}-2\cdot\sum_{(m,w)\in M_1}x_{m,w}\text{such that}\) (1)

\(\sum_{w^\prime\in W:w^\prime\unknown_m^{\mathcal{P}_2}w}x_{m,w^\prime}+\sum_{m^\prime\in U:m^\prime\unknown_w^{\mathcal{P}_2}m}x_{m^\prime,w}\ge 1-y_{m,w},\forall(m,w)\in U\times W\) (2)

\(\sum_{w\in W}x_{m,w}\le 1,\forall m\in U\sum_{m\in U}x_{m,w}\le 1,\forall w\in W\) (3)

\(\sum_{(m,w)\in U\times W}y_{m,w}\le b\) (4)

From a solution to the ILP, we construct a matching _M_<sub>2</sub> by including a pair (_m,w_) if and only if _x<sub>m,w</sub>_=1. By Constraint (3), in _M_<sub>2</sub>, each agent is matched to at most one partner. Moreover, by Constraint (2), a pair (_m,w_) can only block _M_<sub>2</sub> if _y<sub>m,w</sub>_=1, as in case _y<sub>m,w</sub>_=0, Constraint (2) enforces that either _m_ or _w_ are matched to an agent they weakly prefer to _w_ or _m_, respectively. In case _y<sub>m,w</sub>_=1, Constraint (2) is trivially fulfilled for this man-woman pair. Constraint (4) imposes that at most _b_ man-woman pairs may block _M_<sub>2</sub>. It is easy to see that each matching _M_ that admits at most _b_ blocking pairs corresponds to a feasible solution of the ILP. It remains to argue why _M_<sub>2</sub> minimizes the symmetric difference with _M_<sub>1</sub>. This is ensured by Line (1) which, as |_M_<sub>1</sub>| is fixed, is equivalent to minimizing \(|M_1\triangle M_2|=|M_1|+|M_2|-2|M_1\cap M_2|\).

To adapt the ILP from above to ISM, we need to set _b_ to zero. Moreover, we replace Line (1) by \(max\sum_{(m,w)\in M_1}x_{m,w}\) (if we want to find the solution minimizing the symmetric difference with _M_<sub>1</sub>) and by \(min\sum_{(m,w)\in M_1}x_{m,w}\) (if we want to find the solution maximizing the symmetric difference<tbc>

