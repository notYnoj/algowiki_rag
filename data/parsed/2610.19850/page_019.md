meration problem comes out. Takata \[28\] used this framework in a smart way to enumerate all minimal (_a,b_)-separators of a graph, extending the component _C<sub>G</sub>(a,S_) instead of the separator _S_ itself.

Unfortunately, as for various extension problems, we show in the remainder that PMC Extension is NP-hard. Nevertheless, for our main contribution, we will tackle the problem of deciding whether a set contains a PMC. This problem, denoted as PMC Superset, is the subproblem of PMC Extension with \(M=\emptyset\). Following Observation 1, if _X_ is not shy - _i.e._ admits a full component - then none of its subsets can be shy. Therefore, we can directly assume that if our input set _X_ is not shy, then the answer to the decision problem PMC Superset is necessarily no for _X_. The definition of PMC Superset follows.

PMC Superset<br>
**Input:** A graph _G_=(_V,E_) and a shy set \(X\subseteq V\).<br>
**Question:** Is there a PMC \(\Omega\subseteq X\) of _G_?

## 3 PMC superset problem

In this section, we will focus on the following question: given a set of vertices \(X\subseteq V(G)\), is there any chance that some subset of _X_ is a PMC? This question was defined as the PMC Superset problem in subsection 2.4. Note that a naive algorithm would check all subsets of _X_ in time exponential in the size of _X_. Our objective is to present an algorithm for this decision problem in time polynomial in _n_=|_V(G_)|. This contribution will be important for showing that our final algorithm PMC-Traversal finds all PMCs.

### 3.1 A polynomial-time algorithm for reducing shy sets

As a first step, we present a very simple and natural algorithm called conflict-greedy which, given a shy set \(X\subseteq V(G)\) of some graph _G_, computes a subset of _X_. conflict- greedy will be used in the next subsections as a crucial subroutine to solve PMC Superset.

Before presenting this subroutine, we explain why it does not solve PMC Superset itself. Unfortunately, the subset computed by conflict-greedy is not necessarily a PMC. This is due to this simple fact: there exists shy sets which are not PMC supersets.

Figure 5a provides such example. The set \(X=S\cup\{a,b\}\) represented is shy as connected components \(\{a'\}\) and \(\{b'\}\) are not full for _X_. However, _X_ is not a PMC: it does not fulfil the reachability property because \(b\notin R_G(a,X)\). Furthermore, no proper subset of _X_ is shy. Removing _a_ creates a full component: set \(X'=X\backslash\{a\}=S\cup\{b\}\) admits a full component \(\{b'\}\). By symmetry, the same statement holds for _X_\\{_b_}. Finally, for any \(s\in S\), the set \(X''=X\backslash\{s\}\) admits also a full component \(\{s,a',b'\}\). In summary, for any vertex \(x\in X\), set _X_\\{_x_} is not shy and hence is not a PMC. Since any proper subset of _X_ is a subset of some _X_\\{_x_}, according to Observation 1, any proper subset of _X_ is not shy and thus is not a PMC. Figure 5b shows that with a tiny modification of the graph of Figure 5a, the shy set _X_ is now a PMC superset. Indeed, \(\Omega=S\cup\{a\}\) is a PMC as \(\{a'\}\) is not a full component anymore.

Below is a technical lemma to help us analyze our algorithm conflict-greedy, presented on the next page.

