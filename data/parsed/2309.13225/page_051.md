a blocking vertex, the edge that we take from its dominating vertex is lighter than the edge on the path we would have traversed, ensuring that the additive error incurred is at most twice the weight of some edge in the path. Since the blocking vertices are distinct, this allows us to bound our overall error in terms of the weights of the _k_ heaviest edges on the path _P_.

However, since weights can be large and not necessarily bounded by _O(n_), in order to compute a fast (min,+) product, we must make a sacrifice in the accuracy of the (min,+) product and settle for an approximate product. By choosing an appropriate error parameter \(\varepsilon\), we can compute an efficient approximate (min,+) product while incurring only a \((1+\varepsilon)\)-multiplicative factor in our approximation.

## Analysis

Following Theorem 5.6, we exhibit an \((1+\varepsilon,2w_{u,v}(2))\) as an example, and note that the general algorithm for \(\beta\ge 2\) follows similarly.

For \(\beta=2\), we set _k_=5 and _k_<sub>0</sub>=2. If \(P\subset E_3\), then the **SparseAPASP** algorithm obtains a +2_w<sub>u,v</sub>_(2) approximation following Lemma 6.4. Suppose therefore \(P\unknown\subset E_3\). As in the unweighted case, we decompose _G_ into log_n_ levels with degree thresholds \(t_i=\frac{n}{2_i}\) and compute dominating sets _C<sub>i</sub>_ of size \(\tilde{O}(n/t_i)\) and edge sets _F<sub>i</sub>_ of size _O(nt_<sub>_i_-1</sub>) so that all invocations of **Dijkstra** require \(\tilde{O}(n^2)\) time.

Let \(P\subset F_j\) but \(P\unknown\subset F_{j+1}\) and let \(e=(a,b)\in F_j\backslash F_{j+1}\). Then, _a_<sup>∗</sup>=_r(a,C<sub>j</sub>_) and \(\text{rank}_a(a^*)\le t_j\). Let \(e'=(c,d)\) be the edge closest to _u_ such that \(e'\notin E_5\) and _c_ the endpoint closest to _u_. Let _c_<sup>∗</sup>=_r(c,D_<sub>4</sub>) so rank_<sub>c</sub>(c_<sup>∗</sup>)_\<s_<sub>4</sub>. In the overview, we will assume \(e'\neq e\) as otherwise we obtain a +2_w<sub>u,v</sub>_ approximation.

\(\hat{\delta}(a^*,c^*)\le\mathsf{wt}(a^*,a)+\delta(a,c)+\mathsf{wt}(c,c^*)\)<br>
\(\hat{\delta}(a^*,v)\le\mathsf{wt}(a^*,a)+\delta(a,v)\)

Then, the approximate (min,+) product computes,

\(\hat{\delta}(v,c^*)\le\left(1+\frac{\varepsilon}{3}\right)(\delta(v,c)+2\mathsf{wt}(a^*,a)+\mathsf{wt}(c,c^*))\)

Then, \((v,c^*,c)\circ P_{c,u}\subset G_{5,u}\) so that **Dijkstra** computes,

\(\hat{\delta}(v,u)\le\hat{\delta}(v,c^*)+\mathsf{wt}(c^*,c)+\delta(c,u)\)<br>
\(\le\left(1+\frac{\varepsilon}{3}\right)(\delta(v,c)+2\mathsf{wt}(a^*,a)+\mathsf{wt}(c,c^*))+\mathsf{wt}(c^*,c)+\delta(c,u)\)<br>
\(\le\left(1+\frac{\varepsilon}{3}\right)(\delta(v,u)+2\mathsf{wt}(a^*,a)+2\mathsf{wt}(c,c^*))\)<br>
\(\le\left(1+\frac{\varepsilon}{3}\right)\left(\delta(v,u)+2\mathsf{wt}(e)+2\mathsf{wt}(e')\right)\)<br>
\(\le(1+\varepsilon)\delta(u,v)+2w_{u,v}(2)\)

We note that the general argument follows from a similar adaptation to Theorem 5.6.

## Algorithm

Algorithm 9 closely follows Algorithm 6. Observe that the only differences are the usage of **WeightedDecompose** in place of **Decompose** and the usage of **ApproximateMinPlus** in place of **MonotoneMinPlus**.

We present the algorithm pseudocode and detailed analysis below.

