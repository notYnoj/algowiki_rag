## A Top-Down Algorithm to Maintain the Graph Hierarchy Efficiently.

We have now defined all concepts necessary and are ready to state the algorithm. For initialization, at time 0, we initialize an incremental data structure I on \(G_{lg\tau}^0\) and then apply in the following order the updates \(\Delta_{lg(\tau)-1}^0,\Delta_{lg(\tau)-2}^0,\dots,\Delta_0^0\). The data structure I then holds the DDGs of all graphs \(G_1,G_2,\dots,G_{k^\prime}\).

Then, to process the next update to _G_, we then invoke AdvanceToNextVersion(). For queries on a particular version of _G<sup>t</sup>_, we can after _t_ invocations of AdvanceToNextVersion() simply query the data structure D that can answer DDG queries about the current graph.

\(t\leftarrow t+1;\)<br>
\(\text{\textbf{2} Let}i_{max}\text{be the largest integer such that}t\text{mod}2^{i_{max}}=0.\text{;}\)<br>
\(\text{\textbf{3} Ask}\mathcal{I}\text{to roll back the weight update sequence}\Delta_0^{t-1},\Delta_1^{t-1},\dots,\Delta_{i_{max}}^{t-1}.\text{;}\)<br>
\(\text{\textbf{4} Apply weight update sequence}\Delta_{i_{max}}^t,\Delta_{i_{max}-1}^t,\dots,\Delta_0^t\text{to}\mathcal{I}.\)

The algorithm essentially exploits that for _j\>i<sub>max</sub>_, we have \(H_j^{t-1}=H_j^t\) by the way we chose _i<sub>max</sub>_ and by observation C.2. This fact can be used to only roll back the updates \(\Delta_0^{t-1},\Delta_1^{t-1},\dots,\Delta_{i_{max}}^{t-1}\) and after this step the data structure D holds effectively the graph \(H_{i_{max}+1}^{t-1}\) which is exactly the graph \(H_{i_{max}+1}^t\). At this point, it thus remains in the last update step in line 4, to apply updates \(\Delta_{i_{max}}^t,\Delta_{i_{max}-1}^t,\dots,\Delta_0^t\) such that at the end D holds the graph _H<sup>t</sup>_ again as stipulated by observation C.3.

## Analysis.

Correctness follows almost immediately from the discussion above, we merely point out that we have to unroll updates in the reverse order that we applied them to to ensure correctness, which is exactly what we do in our algorithm.

For the run-time analysis, we observe that the time to initialize I is \(\tilde{O}(r+\tau\cdot\sqrt{r})\) by our previous discussion. Further, every 2_<sup>i</sup>_ updates, we roll-back \(\Delta_i^{t-1}\) for some _t_ and add weight updates \(\Delta_i^t\) to I. We have by Observation C.3 that each of these update sequences is of size at most 2<sup>_i_-1</sup>. Thus the data structure I can process these updates in time \(\tilde{O}(2^i\cdot\sqrt{r})\). Thus, the amortized update time to handle such batches \(\Delta_i^{t-1}\) for fixed _i_ at all times is \(\tilde{O}(\sqrt{r})\). Note that our analysis was independent of the chosen _i_, and summing over all values of _i_, and adding the preprocessing gives amortized update time \(\tilde{O}(\sqrt{r})\), as desired.

## Improved Preprocessing.

It is not hard to see that we can partition the update sequence to _H_ into disjoint time segments of length \(\lfloor\sqrt{r}\rfloor_2\). We then run the algorithm described above on each segment separately. It is easy to see that the above proof still gives the same guarantees while the preprocessing time of I for each segment is \(\tilde{O}(r+\lfloor\sqrt{r}\rfloor_2\cdot\sqrt{r})=\tilde{O}(r)\).

## De-Amortization.

To de-amortizate the data structure, we use that I is fully-persistent: every _t_ with _t_mod2_<sup>i</sup>_ for some fixed _i_, we start building the data structure I for time _t_+2_<sup>i</sup>_ from the version _t_ over the next 2_<sup>i</sup>_ updates where we spend \(\tilde{O}(\sqrt{t})\) time at each time step. During this time, I is run further in its original version to support other updates. It is not hard to see that this increases the total update time by at most a logarithmic factor and ensures that the data structure achieves worst-case guarantees.

**Algorithm 1:** AdvanceToNextVersion()

