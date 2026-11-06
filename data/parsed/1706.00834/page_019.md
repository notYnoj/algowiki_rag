<tbc>multigraph by H=(_V,M_). A subproblem is never solved more than once in a dynamic programming. Therefore base directed graph B(H) is acyclic and H is a multi-DAG.

There is a loss associated with any sink node in T . Also with the recursions at the internal node _v_ a local loss will be added to the loss of the subproblems that depends on _v_ and the chosen multiedge \(m\in M_v^{(\mathrm{out})}\) leaving _v_. We can handle arbitrary "min-sum" recurrences:

\(\mathrm{OPT}(v)=\left\{\begin{array}{ c c }
L_\mathcal{T}(v) & v\in\mathcal{T} \\
\mathrm{min}_{m\in M_v^{(\mathrm{out})}}\{\sum_{u:(v,u)\in m}\mathrm{OPT}(u)+L_M(m)\} & v\in V-\mathcal{T}.
\end{array}\right.\)

The problem of repeatedly solving an arbitrary min-sum dynamic programming problem over trials now becomes online learning of multipaths in H. Note that due to the correctness of the dynamic programming, every possible solution to the dynamic programming can be encoded as a multipath in H and vice versa.

The loss of a given multipath is the sum of _L<sub>M</sub>(m_) over all multiedges _m_ in the multipath plus the sum of _L_<sub>T</sub>(_v_) for all sink nodes _v_ at the bottom of the multipath. To capture the same loss, we can alternatively define losses over the multiedges _M_. Concretely, for each multiedge _m_=(_v,U_) define \(\ell_m:=L_M(m)+\sum_{u\in U}\unknown_{\{u\in\mathcal{T}\}}L_\mathcal{T}(u)\) where \(\unknown_{\{\cdot\}}\) is the indicator function<sup>7</sup>.

**5. Applications**

In this section, we apply our algorithms to various instances of online dynamic programming. In each instance, we define the problem, explore the dynamic programming representation and obtain the regret bounds.

7. The alternative losses over the multiedges may not be in \[0,1\]. However, it is straight-forward to see if \(\ell_m\in[0,b]\) for some _b_, the regret bounds for CH and EH will scale up accordingly.

Expanded Hedge
Dynamic Programming starting from S E V
Component Hedge
m := wm fm(v), m E Mv (out)
w E R|M|
f E R|M|
Stochastic Product Form
Mean Form
Preserving Mean
Stochastic
"Conditional Outflow" in parallel
Multiplicative Updates
Multiplicative Updates
Weight Pushing
m := fm (out)
m E Mv (out)
Projection

Figure 3: Mapping between Stochastic Product Form in EH and Mean Form in CH.

