<tbc>loss \(\alpha+O(1)=(1+o_\alpha(1))\alpha\), which is asymptotically the smallest possible since every bicriteria comparison must have \(\beta\ge\alpha\). Second, the same lower bound shows that any constant-factor approximation must cross the \(2\alpha\) threshold, while our \((\alpha,2\alpha+O(1))\)-bicriteria _O_(1)-approximation does so by only an additive constant. Thus, for large \(\alpha\), our results identify \(2\alpha\) as the sharp threshold for beating the logarithmic Set Cover barrier, and achieve essentially the smallest bicriteria loss possible on the logarithmic-approximation side of this threshold.

We emphasize that our main focus is the regime where \(\alpha\) is large. This is precisely the regime in which the standard theoretical guarantee for greedy search becomes meaningful for high-accuracy nearest-neighbor search: on an \(\alpha\)-navigable graph, greedy search achieves approximation ratio \(\frac{\alpha+1}{\alpha-1}+\varepsilon\). Since \(\frac{\alpha+1}{\alpha-1}=1+\frac{2}{\alpha-1}\), obtaining a \((1+\varepsilon)\)-approximate nearest neighbor through this analysis requires \(\alpha=\Theta(1/\varepsilon)\), after choosing the additive accuracy parameter \(\varepsilon\) appropriately. In this sense, our construction gives a nearly tight bicriteria approximation in the theoretically relevant high-accuracy regime.

We note that in practice, the values of \(\alpha\) used or observed in proximity graphs are often smaller than 2 \[SDK<sup>+</sup>19\]. However, the nearest neighbor approximation guarantee of greedy search on \(\alpha\)-navigable graphs for small choices of \(\alpha\) is still poorly understood, and this is beyond the scope of the present work.

## 1.2 Technical Overview.

We give an overview of the main ideas behind our upper bound. We start with the Set Cover viewpoint, which explains the _O_(log_n_) barrier in previous work. We then describe a simple but slower ordered-greedy procedure, which exposes the packing principle behind the \(2\alpha\) threshold. Our algorithm can be viewed as an acceleration of the ordered-greedy procedure, achieved by replacing the source-specific greedy choices with globally shared representatives.

### The Set Cover viewpoint.

For a fixed source point _s_, the \(\alpha\)-navigability constraints can be written as a Set Cover instance. The universe is _P_\\{_s_}, and each candidate out-neighbor \(u\neq s\) corresponds to the set

\(Z_\alpha(s,u)=\left\{t\in P\backslash\{s\}\middle|\mathsf{d}(u,t)<\frac{\mathsf{d}(s,t)}{\alpha}\right\}.\)

Choosing out-neighborhoods for _s_ is therefore exactly the problem of covering all targets \(t\in P\backslash\{s\}\) by sets \(Z_\alpha(s,u)\). Constructing a sparsest \(\alpha\)-navigable graph amounts to solving one such Set Cover instance for every source _s_.

\begin{tabular}{cccc}
Guarantee & Approx. & Time & Reference \\
(1,1)-bicriteria & _O_(log_n_) & \(\widetilde{O}(n^2)\) & \[CDFC<sup>+</sup>26\] \\
\((\alpha,\alpha)\)-bicriteria & _O_(log_n_) & \(\widetilde{O}\left(min\{n\cdot OPT_\alpha,n^{2.5}\}\right)\) & \[CDFC<sup>+</sup>26, KPW26\] \\
\((\alpha,\alpha)\)-bicriteria & \(\Omega(logn)\) & Polynomial time & \[KPW26\] \\
\((\alpha,2(1+\varepsilon)\alpha)\)-bicriteria & _O_(log_n_) & \(\widetilde{O}(n^\omega log\Delta/\varepsilon)\) & \[KPW26\] \\
\((\alpha,\alpha+O(1))\)-bicriteria & _O_(log_n_) & \(\widetilde{O}(n^2log\Delta)\) & This work \\
\((\alpha,2\alpha+O(1))\)-bicriteria & _O_(1) & \(\widetilde{O}(n^2log\Delta)\) & This work \\
\((\alpha,2\alpha-\eta)\)-bicriteria & \(\Omega(logn)\) & Polynomial time & This work \\
\end{tabular}

1: Upper and lower bounds for sparse navigable graphs in general metrics. Here \(OPT_\alpha\) denotes the minimum number of edges in an \(\alpha\)-navigable graph, \(\Delta\) is the aspect ratio, and \(\omega\) is the matrix multiplication exponent. We use the bicriteria notation of Definition 1.2.

