We will now present a simpler construction which demonstrates that, when prioritising size over stability, the minimum maximum number of blocking pairs that any agent is contained in increases arbitrarily, even in the smi setting.

**Proposition 3.6.** _For every non-negative integer k, there exists an_ smi _instance_ \(I=(A,\succ)\) _with n_=2(_k_+1) _agents such that_ \(min_{M\in\mathcal{M}^+}max_{a_i\in A}|bp_i(M)|=k\).

_Proof._ We give a construction with the following 2(_k_+1) agents \(A=\mathcal{A}\cup\mathcal{B}=\{a_1,a_2,\dots,a_{k+1}\}\cup\{b_1,b_2,\dots,b_{k+1}\}\). For all _j_ (\(1\le j\le k\)), the agent _a<sub>j</sub>_ ranks _b_<sub>_k_+1</sub> in first position and _b<sub>j</sub>_ in second position, while _b<sub>j</sub>_ only ranks _a<sub>j</sub>_ (so, necessarily, in first position). Finally, _b_<sub>_k_+1</sub> ranks all _a<sub>j</sub>_ (for \(1\le j\le k+1\)) agents in position _j_. Agent _a_<sub>_k_+1</sub> only ranks _b_<sub>_k_+1</sub>. We illustrate the construction in Figure 3.

Clearly, the only maximum-cardinality matching is the perfect matching \(M=\{\{a_j,b_j\}|1\le j\le k+1\}\). However, it is easy to observe that \(bp(M)=\{\{a_j,b_{k+1}\}|1\le j\le k\}\). Therefore \(bp_{b_{k+1}}(M)=\{a_j|1\le j\le k\}\) and so \(min_{M^\prime\in\mathcal{M}^+}max_{a_i\in A}|bp_i(M')|=|bp_{b_{k+1}}(M)|=k\) as required.

Using this construction, we can observe an even stronger lower bound and hence observe the following tight asymptotic bound for solutions to Minimax-AlmostStable-Max-smi (and hence also for Minimax-AlmostStable-Max-sri).

**Theorem 3.7.** _In the worst case,_ \(OPT=\Theta(n)\)_, where_ OPT _is the optimal solution value of_ Minimax-AlmostStable-Max-smi _and n is the number of agents._

_Proof._ This follows from the infinite family of instances constructed in the proof of Proposition 3.6. Notice that there, _n_=2(OPT+1), so, \(OPT=\frac{n}{2}-1=\Omega(n)\). Clearly, \(OPT\le n-1=O(n)\) as no agent can block with more agents than they have on their preference list. Thus, \(OPT=\Theta(n)\) as required.

## 4 Computational Intractability Results

### 4.1 Decision Problems and Preliminary Results

As noted in the previous sections, we now proceed to proving surprisingly strong intractability results for the computation of minimax almost-stable matchings. For our investigation, we first define decision problems associated with our central optimisation problems of interest. The following decision problem corresponds to Minimax-AlmostStable-sri.

a1
b1
1
2
1
a2
b2
1
2
1
1
2
b3
1
k+1
3
1
1
k
1
2
1
ak
bk

Figure 3: Illustration of the lower-bound construction for maximum-cardinality matchings in smi.

