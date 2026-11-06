**Proof.** Consider the following algorithm from [4] for computing _k_-FTRS that bounds in degree of an input node _t_.

**Algorithm 1** Algorithm for computing _k_-FTRS 1 \(S_1\leftarrow\{s\}\); 2 for _i_=1 to _k_ do 3 \(C_i\leftarrow\text{FMC}(S_i,t,\mathcal{G})\); 4 \((A_i,B_i)\leftarrow\text{Partition}(C_i)\); 5 \(S_{i+1}\leftarrow(A_i\cup\text{out}(A_i,\mathcal{G}))\backslash\{t\}\); 6 end 7 \(f_0\leftarrow\text{max-flow from}S_{k+1}\text{to}t\); 8 \(\mathcal{E}(t)\leftarrow\text{Incoming edges of}t\text{present in}E(f_0)\); 9 Return \(\mathcal{G}^*=(\mathcal{G}\backslash\text{In-Edges}(t,\mathcal{G}))+\mathcal{E}(t)\);

We will now show G<sup>∗</sup> is a (_k+f_-1)-FTRS of G. Let _F_ be any set of _k+f_-1 failed edges. If there exists a path _R_ from _s_ to _t_ in G\\_F_ then we shall prove the existence of a path \(\hat{R}\) from _s_ to _t_ in G<sup>∗</sup>\\_F_. Observe that _R_ must pass through each (_s,t_)-cut _C<sub>i</sub>_, for each \(i\in[1,k]\), through an edge, say (_u<sub>i</sub>,v<sub>i</sub>_). If _v<sub>i</sub>=t_ then \((u_i,v_i)\in\mathcal{E}(t)\) and thus _R_ is intact in the graph G<sup>∗</sup>. Now we need to prove for the case when the edge \((u_i,v_i)\notin\mathcal{E}(t)\).

To prove that a path \(\hat{R}\) exists in G<sup>∗</sup>, we will construct a sequence of auxiliary graphs as done in [4], say H_<sub>i</sub>_’s, for each \(i\in[1,k+1]\), as follows:

\(\mathcal{H}_1=\mathcal{G},\mathcal{H}_i=\mathcal{G}+(s,v_1)+\dots+(s,v_{i-1}),i\in[2,k+1].\)

From the induction proof of Lemma 18 of [4], we get max-flow(_s,t,_H<sub>_i_+1</sub>)=1+max-flow(_s,t,_H_<sub>i</sub>_) and since max-flow(_s,t,H_<sub>1</sub>)=max-flow(_s,t,_G)=_f_, we get that max-flow(_s,t,_H<sub>_k_+1</sub>)=_k+f_. Let H<sup>∗</sup>=(H<sub>_k_+1</sub>\\In-Edges(_t_))+E(_t_) i.e. the incoming edges of _t_ are restricted in H<sub>_k_+1</sub> to those present in the set E(_t_). In Lemma 19 of [4] it is shown that max-flow(_s,t,_H<sup>∗</sup>)=max-flow(_s,t,_H<sub>_k_+1</sub>)=_k+f_. Since the flow in H<sup>∗</sup> is greater than |_F_| or the number of faults, we can directly use the Lemma 20 of [4] to see that there exists a path \(\hat{R}\) in G<sup>∗</sup>\\_F_.

The bound on the number of edges also follows from [4]. Lemma 21 of [4] states that \(|C_{i+1}|\le 2|C_i|\) where _C_<sub>_k_+1</sub>=_FMC(S_<sub>_k_+1</sub>_,t,_G). Since |_C_<sub>1</sub>|=_f_, we get the bound on E(_t_)=_C_<sub>_k_+1</sub> as 2_<sup>k</sup>f_. Note that the proof of Lemma 21 of [4] assumes that every vertex has out-degree bounded by two but it can be shown that the Lemma will hold true even when the out-degree of all vertices except the source vertex is bounded by two by using the fact that in the proof of Lemma 21, out(_A<sub>i</sub>_) will never contain the source vertex for any _i_. \(\blacktriangleleft\)

## 4.3 Computing sparse \((\lambda,k)\)-FT-BFP

In this subsection, we will show how to construct a \((\lambda,k)\)-FT-BFP of G from a (_k+f_-1)- FTRS of G. We will start by introducing a lemma from [17], followed by additional lemmas that will help us to obtain a tight construction for FT-BFP.

\(\blacktriangleright\) **Lemma 18** ([17])**.** _Let_ G _be a directed graph with a designated source node s, and let_ H _be a_ \((k+\lambda-1)\)_-FTRS of_ G_. Then,_ H _is also a_ \((\lambda,k)\)_-FT-BFP of_ G.

To strengthen the above lemma, we present a method for constructing a \((\lambda,k)\)-FT- BFP from a \((min\{f,\lambda\}+k-1)\)-FTRS, where _f_ represents the maximum flow from the source node _s_ to a destination node _t_ in the graph.

