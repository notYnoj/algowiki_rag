## A.3 Proof of Lemma 1

We will consider each setting individually. Further while we describe the embedding for each case we will only give a proof of correctness for friendship matching with _k_=1 as the proofs for all cases are very similar and this is one of the most complex ones.

**Locally Stable Matching** To embed an instance of locally stable matching given by graph _G_, link set _L_, and edge benefits into our framework, we apply the embedding indicated in Proposition 1. Note that for the standard case of _k_=1 matching edges and lookahead \(\ell=2\), we obtain consistent generation and domination rules. If we change to _k\>_1 matching edges or lookahead of \(\ell>2\), consistency of generation rules becomes violated, as two edges can appear in the precondition. This follows from the exponential lower bounds in [16,19].

**Socially Stable Matching** To embed an instance of socially stable matching given by graph _G_=(_V,E_), link set _L_, and edge benefits _b_ into our framework, we use _N=V_ , C=_E_, and \(\mathcal{C}g=L\cap E\). There are no additional generation rules \(T=\emptyset\), and the benefits are obviously given by _w=b_. The domination rules implement only the necessary preference-based improvement of coalitions _D=D<sub>w</sub>_. Obviously, generation and domination rules are consistent.

If we change to _k\>_1 matching edges per agent, then, in principle, we violate a condition of our framework - that in every state, every agent can be part of at most one coalition. A simple way to embed the games correctly into the framework is to represent each agent _u_ by _k_ auxiliary agents _u_<sub>1</sub>_,...,u<sub>k</sub>_, who can match to one partner each. The edges between two agents become a complete bipartite graph between the corresponding auxiliary agents. Note that in the new game, _u<sub>i</sub>,u<sub>j</sub>_ and \(v_{i^\prime},v_{j^\prime}\) can now build two edges among _u_ and _v_. This can be prohibited using an auxiliary agent _a<sub>u,v</sub>_ for each matching edge \(\{u,v\}\in E\), and replacing every coalition {_u<sub>i</sub>,v<sub>j</sub>_} by {_u<sub>i</sub>,v<sub>j</sub>,a<sub>u,v</sub>_}, for _i,j_=1_,...,k_.

More formally, we define

Obviously, generation and domination rules are consistent.

**Considerate Matching** To embed an instance of friendship matching given by graph _G_=(_V,E_), link set _L_, and edge benefits _b_, we use _N=V_ , C=C_g=E_,<tbc>

\(N=\{v_i|v\in V,i=1\dots k\}\cup\{a_{u,v}|\{u,v\}\in E\}\)<br>
\(\mathcal{C}=\{\{u_i,v_j,a_{u,v}\}|\{u,v\}\in E,i,j=1\dots k\}\)<br>
\(\mathcal{C}g=\{\{u_i,v_j,a_{u,v}\}|\{u,v\}\in E\cap L,i,j=1\dots k\}\)<br>
\(w(\{u_i,v_j,a_{u,v}\})=b(u,v)\text{for}\{u,v\}\in E,i,j=1\dots k\)<br>
\(T=\emptyset\)<br>
\(D=D_w\)

