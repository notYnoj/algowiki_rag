or a negated occurrence of some variable _V<sub>i</sub>_. Now we construct an instance _I_ of 1-Max- AlmostStable-sri as follows. Let \(A=A_F\cup A_V\cup A_C\) be the set of 20_n_+3_m_ agents, where

\(A_F=\{f_i^{\alpha,z};1\le i\le n\wedge 1\le\alpha\le 8\wedge 1\le z\le 2\},\)<br>
\(A_V=\{v_i^T,v_i^F,v_i^1,v_i^2;1\le i\le n\},\text{and}\)<br>
\(A_C=\{x_j^s;1\le j\le m\wedge 1\le s\le 3\}.\)

These three disjoint sets of agents correspond to those from forcing gadgets, variable gadgets, and clause gadgets, respectively, all of which we will introduce now.

Specifically, for every variable \(V_i\in V\) , we create a **variable gadget** _G<sub>V<sub>i</sub></sub>_ consisting of the four vertices \(v_i^T,v_i^F,v_i^1,v_i^2\) (and more inherited from the use of forcing gadgets). We construct the preferences of the variable gadget as follows:

\(v_i^T:v_i^1x_1(v_i^T)x_2(v_i^T)v_i^2\)<br>
\(v_i^F:v_i^1x_1(v_i^F)x_2(v_i^F)v_i^2\)<br>
\(v_i^1:v_i^Tv_i^FG_{F(v_i^1)}\)<br>
\(v_i^2:v_i^Tv_i^FG_{F(v_i^2)}\)<br>
\((+\text{agents inherited from use of}G_{F(v_i^z)}\text{gadgets})\)

where \(x_1(v_i^T)\) and \(x_2(v_i^T)\) will be specified later. The construction is illustrated in Figure 4.

The **forcing gadget**, denoted by \(G_{F(v_i^z)}\) for a given agent \(v_i^z\) (where \(z\in\{1,2\}\)), attaches to each agent \(v_i^z\) and contributes the eight agents \(f_i^{1,z},f_i^{2,z},\dots,f_i^{8,z}\). Let \(v_i^z\)’s preference list before attachment of the gadget be denoted by \(P_{v_i^z}\) (in the variable gadget above, \(P_{v_i^z}=(v_i^Tw_i^F)\). Then, after attachment of the gadget, let \(v_i^z\)’s preference list consist of \(P_{v_i^z}\) followed by all other agents \(f_i^{\alpha,z}\) within the gadget in increasing order of \(\alpha\):<tbc>

\(v_i^z:P_{v_i^z}f_i^{1,z}f_i^{2,z}f_i^{3,z}f_i^{4,z}f_i^{5,z}f_i^{6,z}f_i^{7,z}f_i^{8,z}\)

<tbc>The main idea of this gadget is to force agent \(v_i^z\) to be matched to someone on \(P_{v_i^z}\) in any matching where no agent is in more than one blocking pair. While \(v_i^z\) has this special function and preference list, the remaining agents have symmetric preference lists. The construction is strongly inspired by the construction in Proposition 3.4. Specifically, the preference lists of the remaining agents in \(G_{F(v_i^z)}\) are constructed such that they form nested preference cycles. We construct the remainder of the gadget such that \((v_i^z,f_i^{1,z},f_i^{2,z})\) is a preference cycle at the top of the preference lists of the new \(f_i^{\alpha,z}\) agents, and similarly for \((f_i^{3,z},f_i^{4,z},f_i^{5,z})\) and \((f_i^{6,z},f_i^{7,z},f_i^{8,z})\). Subsequently, the remainder of the preference lists are constructed such that we get the preference cycles \((\{v_i^z,f_i^{1,z},f_i^{2,z}\},\{f_i^{3,z},f_i^{4,z},f_i^{5,z}\},\{f_i^{6,z},f_i^{7,z},f_i^{8,z}\})\), i.e., all agents<tbc>

