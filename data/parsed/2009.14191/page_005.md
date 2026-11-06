<tbc>even with a strict order of the agents as a master poset if each agent is allowed to declare an arbitrary set of 2-sets unacceptable (Theorem 4.34), contrasting the polynomial-time solvability when every agent accepts every (_d_-1)-set of other agents (Proposition 4.1).

### 1.3 Structure of the paper

After introducing basic notation in Section 2, we consider 3-Dimensional Stable Roommates with master list of (_d_-1)-sets of agents in Section 3 and show its NP-completeness. Then, we turn to master posets of agents. We show in Section 4.1 that 3-Dimensional Stable Roommates is easy if the master list is strictly ordered. Moreover, we consider the case that preferences are incomplete, or that the master list is a poset and investigate parameters measuring the similarity to a strict order in Sections 4.2 and 4.3. In Section 4.4, we show that 3-Dimensional Stable Roommates is NP-complete if the master list is strict, but every agent may declare an arbitrary subset of (_d_-1)-sets to be not acceptable. Finally, we conclude in Section 5.

## 2 Preliminaries

Let \[_n_\]:={1,2,3_,...,n_} and \[_n,m_\]:={_n,n_+1_,...,m_}. A set of cardinality _d_ will also be called _d-set_. For a set _X_ and an integer _d_, we denote by \(\genfrac(){pt}{2}{X}{d}\) the set of size-_d_ subsets of _X_. A _preference list_ \(\succ\) over a set _X_ is a strict order of _X_. We call a set of pairwise disjoint _d_-subsets of a set _A_ of agents a _d-dimensional matching_. Usually, _d_ is clear from the context; if so, then we may only write "matching". Given a _d_-dimensional matching _M_ and an agent _a_, we denote by _M(a_) the (_d_-1) set _t_ such that \(t\cup\{a\}\in M\); if for _a_ no such (_d_-1)-set exists, then \(M(a):=\emptyset\). We say that an agent _a prefers_ a (_d_-1)-set _t_ to a (_d_-1)-set \(t'\) if \(t\succ_a\) _t_ where \(\succ_a\) is the preference list of _a_. Any agent prefers any (_d_-1)-set not containing itself to being unmatched. A _blocking d-set_ for a _d_-dimensional matching _M_ is a set of _d_ agents {_a_<sub>1</sub>_,a_<sub>2</sub>_,...,a<sub>d</sub>_} such that, for all \(i\in[d]\), either _a<sub>i</sub>_ is unmatched in _M_ or \(\{a_1,a_2,\dots,a_d\}\backslash\{a_i\}\succ_{a_i}\{b_1^i,b_2^i,\dots,b_{d-1}^i\}\), where \(\{b_j^i:j\in[d-1]\}\cup\{a_i\}\in M\). A matching is called _stable_ if it does not admit a blocking _d_-set. Now, we are ready to define our central problem.

\begin{tabular}{cc}
Setting/Parameter & Complexity \\
Master list of 2-sets & NP-complete for _d_=3 (Theorem 3.8) \\
Master poset of agents: & \\
Linear master poset of agents & linear time (Proposition 4.1) \\
_max. number_ \(\kappa\) of incomparable agents & \(O(n^2)+(\kappa^22^{12\kappa})^{O(\kappa^22^{12\kappa})}n\) (Theorem 4.6) \\
Width of master poset & W\[1\]-hard for _d_=3 (Theorem 4.15) \\
Incomplete preferences, strictly ordered master poset & NP-complete for \(d\ge 3\) (Theorem 4.34) \\
Deletion distance to strictly ordered master poset & W\[1\]-hard for _d_=3 (Theorem 4.27) \\
\end{tabular}

1: Results overview: six variations of Multidimensional Stable Roommates. All three studied parameters measure the similarity of the master poset to a strict order. Note that the parameter "max. number \(\kappa\) of incomparable agents" is weaker than the parameter "Width of master poset", and both parameters are incomparable to the parameter "Deletion distance to strictly ordered master poset".

