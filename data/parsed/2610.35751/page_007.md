Input: DVQ graph G=(V,E), deletion set D, affected nodes V<sub>affected</sub>, out-degree bound R, thresholds CL<sub>1</sub>,CL<sub>2</sub>, threshold \(\tau\) and \(\theta_{th}\) Output: Repaired graph on nodes \(V'=V\backslash\mathcal{D}\)<br>
foreach \(v\in V_{affected}\) do<br>
   \(C\leftarrow\{PF_v^1,\dots,PF_v^l\}\); // Candidate set<br>
   \(C'\leftarrow\emptyset\); // Repaired candidate set<br>
   \(Out\leftarrow N_{out}(v)\backslash\mathcal{D}\);<br>
   \(In\leftarrow N_{in}(v)\backslash\mathcal{D}\);<br>
   \(CL(v)\leftarrow\frac{R-|Out|}{R}\) ;<br>
   if \(0<CL(v)\le CL_1\) then // Mild<br>
   \(C'\leftarrow Out\cup In\);<br>
   else if \(CL_1<CL(v)\le CL_2\) then // Moderate<br>
   \(C_{affected}\leftarrow\{PF_v^i\in C|PF_v^i\cap\mathcal{D}\neq\emptyset\}\);<br>
   \(Out^2\leftarrow\bigcup_{PF\in C_{affected}}\bigcup_{p\in PF}(N_{out}(p)\backslash\mathcal{D})\);<br>
   \(C'\leftarrow Out\cup In\cup Out^2\);<br>
   else // Severe<br>
   \(\ell_\mathrm{min}\leftarrow\mathrm{argmin}_i\text{i}\text{s.t.}PF_v^i\cap\mathcal{D}\neq\emptyset\);<br>
   \(C_{high}\leftarrow\{PF_v^i\in C|i\ge\ell_\mathrm{min}\}\);<br>
   \(Out^2\leftarrow\bigcup_{PF\in C_{high}}\bigcup_{p\in PF}(N_{out}(p)\backslash\mathcal{D})\);<br>
   \(C'\leftarrow Out\cup In\cup Out^2\);<br>
   \(N_{out}(v)\leftarrow\text{ACAR}(C',R,\tau,\theta_{th})\);

affected-layer repair, and multi-layer repair to handle nodes with mild, moderate, and severe connectivity loss, respectively.

<u>_Historical-Pareto-Frontier Repair_</u>. The candidate set \(\mathcal{C}'\) consists of _v_’s active out-neighbors _Out_ and active in-neighbors _In_ (line 8). Due to the low connectivity loss, this strategy leverages the in-neighbors of affected nodes to efficiently reduce connectivity degradation with minimal overhead. In particular, it avoids any distance computations during candidate selection, thereby significantly reducing the overall repair cost. The key idea is that, due to the reverse edges introduced during index construction, the in-neighbors of a node have previously served as its candidate out-neighbors.

<u>_Affected-Layer Repair_</u>. The candidate set \(\mathcal{C}'\) consists of _Out_, _In_, and an additional expanded set _Out_<sup>2</sup> derived from the affected layers of Pareto frontiers (i.e., layer 2 in Figure 7b). Specifically, CA-PFR first locates the affected layers in C that contain deleted nodes, denoted by C_<sub>affected</sub>_ (line 10). It then expands the nodes in these affected layers to form the expanded set _Out_<sup>2</sup> (line 11). This expansion strategy is motivated by the observation that neighbors in layers below the affected layers are rarely updated during repair. By expanding nodes in these affected layers, CA-PFR can effectively restore local connectivity while avoiding unnecessary exploration.

<u>_Multi-Layer Repair_</u>. The candidate set \(\mathcal{C}'\) consists of _Out_, _In_ and an expanded set _Out_<sup>2</sup> derived from all high layers (i.e., the "High" region in Figure 7b). Specifically, CA-PFR first locates the lowest affected layer containing deleted nodes and denotes its layer ID as \(\ell_\mathrm{min}\) (line 14). It then collects all layers of Pareto frontiers whose layer IDs are not smaller than \(\ell_\mathrm{min}\), denoted by C_<sub>high</sub>_ (line 15), and gathers the active out-neighbors of nodes in these layers to form _Out_<sup>2</sup> (line 16). This expansion strategy is designed not only to address significant connectivity loss caused by deletions, but also to mitigate connectivity deficiencies inherited from the index construction phase, thereby further improving overall graph connectivity. For example, in the LAION dataset, approximately 2.77% of nodes in the initial index exhibit connectivity loss below<tbc>

<tbc>_CL_<sub>2</sub><tbc>

<tbc>before deletions. After 30 batches of deletions, the graph connectivity does not degrade. Instead, the number of nodes with connectivity loss below _CL_<sub>2</sub> decreases by 3.82\(\times\).

Finally, the repaired candidate set \(\mathcal{C}'\) of the affected node _v_ is refined to obtain the final out-neighbors _N<sub>out</sub>(v_) (line 18), thereby completing the structural repair of node _v_ in the index.

**Example 3:** To better illustrate how CA-PFR adaptively repairs the in-neighbors affected by a deleted node, we focus on the case of severe connectivity loss, corresponding to node _v_<sub>7</sub>, as shown in Figure 8. For the affected node _v_<sub>7</sub>, CA-PFR first computes its connectivity loss CL(_v_<sub>7</sub>)=3/4. Since CL(_v_<sub>7</sub>) exceeds _CL_<sub>2</sub> (i.e., 1/2), CA-PFR classifies _v_<sub>7</sub> as exhibiting severe connectivity loss and thus triggers the multi-layer repair strategy. Specifically, CA-PFR employs Multi-Layer Repair to construct the final candidate set, i.e., _v_<sub>0</sub>_,v_<sub>2</sub>_,v_<sub>3</sub>_,v_<sub>4</sub>_,v_<sub>5</sub>_,v_<sub>6</sub>. Finally, node _v_<sub>7</sub> connects to _v_<sub>0</sub>_,v_<sub>4</sub>_,v_<sub>5</sub> and _v_<sub>6</sub> after the AR computation, as shown in Figure 8c. Notably, this strategy compensates for inherent connectivity deficiencies in the initial index. For example, in the initial graph index (see Figure 2a), reaching _v_<sub>4</sub> from _v_<sub>3</sub> follows the path \(v_3\rightarrow v_7\rightarrow v_2\rightarrow v_4\) (3 hops). In contrast, after multi-layer repair (see Figure 8c), _v_<sub>3</sub> can reach _v_<sub>4</sub> via _v_<sub>7</sub> in only 2 hops, thereby reducing search latency. \(\sqcap\sqcup\)

Asynchronous Reverse Graph Maintenance. During deletion, ACTIVE requires in-neighbor information to locate and repair affected nodes. Since the graph-based index stores only out-neighbors, obtaining in-neighbors would otherwise require scanning the entire graph topology _G<sub>out</sub>_. To avoid this overhead, ACTIVE maintains a lightweight reverse graph topology _G<sub>in</sub>_, where for each node _v_, \(N_{out}^{G_{in}}(v)=N_{in}^{G_{out}}(v)\). Unlike _G<sub>out</sub>_, whose edges store dual- vector distances and active ranges, _G<sub>in</sub>_ stores only in-neighbor IDs, accounting for merely 2.34% of the combined size of _G<sub>out</sub>_ and the dual-vector data in the HM dataset. Since batch updates modify edges in _G<sub>out</sub>_, ACTIVE asynchronously maintains _G<sub>in</sub>_ in the background to minimize synchronization overhead.

**Distance Storage and Memory Overhead.** In ACTIVE , we store only the distances between each node and its neighbors with respect to the two attribute vectors as edge metadata in the adjacency list, which are reused during historical-Pareto-frontier repair and active range computation. When an edge is accessed, its distance values can be read in the same memory access without an additional lookup. During index updates, these distances are inserted or removed together with the edge metadata. Despite the modest additional storage overhead , this design improves update throughput and is therefore practically meaningful. For fairness, all baselines also store dual-vector distances in Section 6.

## 5.3 Computational Overhead Analysis

As the complexity of AR computation has been discussed in Section 4.3, we focus on the complexity of candidate repair in CA-PFR. Given a deleted node, CA-PFR adaptively augments the candidate set C for each affected node \(v\in V_{affected}\), yielding a repaired candidate set \(\mathcal{C}'\). Therefore, the computational complexity for repairing an affected node _v_ is \(O(|\Delta C|)\), where \(\Delta C=\mathcal{C}'\backslash\mathcal{C}\) denotes<tbc>

