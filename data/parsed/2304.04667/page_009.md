2. \(d_G(s'),d_G(t')\ge|V'|/(20log_{4/3}n)\).<tbc>

3. (_S<sub>p,i</sub>,C<sub>p,i</sub>,S<sub>i,p</sub>_) corresponds to a minimum \(s't'\)-cut in _G_.

Finally, we run the algorithm _O_(log_n_) times, concluding that for every node pair, with high probability (\*\*) occurs in at least one of the recursion trees.

## Converting to Las Vegas

The algorithm above may, with non zero probability, produce erroneous answers. This occurs for a pair _u,v_ if the pivots separating _u_ and _v_ belong to _C<sub>u,v</sub>_ in all _O_(log_n_) repetitions (and the pair _u,v_ was not queried directly). A natural starting point to address this issue is to increase the number of repetitions to _x_ for some _x\>\>_log_n_, instead of just _O_(log_n_) as in the Monte Carlo algorithm. By doing so, we can argue that the Max-Flow values that are at most _x_ will be preserved by a global analysis claim _and verification_ that no pivot was chosen too many times in instances of size at least \(\tilde{\Omega}(x)\) (throughout all repetitions). As a result, a sufficient number of distinct pivots must have been chosen, ensuring that at least one of the pivots separating _u_ and _v_ does not belong to _C<sub>u,v</sub>_. This could make the basis of a correct Las Vegas algorithm; unfortunately, the running time becomes _xmT(m_), which is too high as _x_ is only bounded by _n_. However, the part responsible for this high running time is the reinforcement queries rather than the basic recursion, and so there is still a hope.

Indeed, in the Las Vegas algorithm we are more strategic in performing reinforcement queries. We would like to perform such queries only for pairs that were required in at least _x_ repetitions, thus bounding the total number of distinct queries throughout all repetitions by \(\tilde{O}(m)\). Accordingly, we would claim that if a pair _u,v_ was _not_ required in at least _x_ repetitions (and thus was not queried directly) then it is surely separated many times, and so by many distinct pivots, in the basic recursion structure. Similar to before, this ensures that at least one of those pivots must not belong to _C<sub>u,v</sub>_, making the corresponding answer correct. However, even this only brings the total running time to _xnT(m_) which equals _n_<sup>2</sup>_m_ in the worst case. To further speed up the algorithm, we operate in stages focusing on a range \[_k,_2_k_) of Max-Flow values each time, thus incurring a factor _O_(log_n_) to the running time. Consequently, the relevant nodes, i.e, _terminals_, in each \[_k,_2_k_) stage are the nodes whose degrees are at least _k_, totaling at most _m/k_ nodes. At the same time, the minimum instance size we need to consider, as well as the number of repetitions required to ensure a sufficiently high number of distinct pivots for the terminals at this stage, is only \(\tilde{O}(k)\). This brings the total running time to \(\tilde{O}(m\cdot T(m))\), as required.

Note that unlike properties (\*) and (\*\*) detailed above, no local property can naturally be described in the Las Vegas version of our algorithm. However, a more global property is appropriate:

(\*\*\*) For every pair \(s',t'\) such that Max-Flow\((s',t')\in[k,2k)\), when the algorithm terminates at least one of the following holds in the \[_k,_2_k_) stage.<tbc>

1. \(s'\in S_{i,p}\) and \(t'\in C_{p,i}\), or \(s'\in C_{p,j}\) and \(t'\in S_{j,p}\), in at least _k_ repetitions for some _i_’s and _j_’s.<tbc>

2. \(s',t'\) are together in final instances of at least _k_ repetitions.<tbc>

3. (_S<sub>p,i</sub>,C<sub>p,i</sub>,S<sub>i,p</sub>_) in at least one of the repetitions corresponds to a minimum \(s't'\)-cut in _G_.

## 1.3.2 Nondeterministic algorithms

Several papers \[CGI<sup>+</sup>16, AKT20b, Li21\] have proposed nondeterministic algorithms as a means to restrict the applicability of SETH for conditional lower bounds. This method was introduced by Carmosino et al. \[CGI<sup>+</sup>16\], who also demonstrated that several problems, including APSP and 3SUM, are unlikely to have conditional lower bounds under SETH, assuming that NSETH holds.

