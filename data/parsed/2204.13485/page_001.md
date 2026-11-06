# Manipulating the outcome of stable matching and roommates problems

**Abstract**

The stable marriage and stable roommates problems have been extensively studied due to their high applicability in various real-world scenarios. However, it might happen that no stable solution exists, or stable solutions do not meet certain requirements. In such cases, one might be interested in modifying the instance so that the existence of a stable outcome with the desired properties is ensured.

We focus on three different modifications. In stable roommates problems with all capacities being one, we give a simpler proof to show that removing an agent from each odd cycle of a stable partition is optimal. We further show that the problem becomes NP-complete if the capacities are greater than one, or the deleted agents must belong to a fixed subset of vertices.

Motivated by inverse optimization problems, we investigate how to modify the preferences of the agents as little as possible so that a given matching becomes stable. The deviation of the new preferences from the original ones can be measured in various ways; here we concentrate on the \(\ell_1\)-norm. We show that, assuming the Unique Games Conjecture, the problem does not admit a better than 2 approximation. By relying on bipartite-submodular functions, we give a polynomial-time algorithm for the bipartite case. We also show that a similar approach leads to a 2-approximation for general graphs.

Last, we consider problems where the preferences of agents are not fully prescribed, and the goal is to decide whether the preference lists can be extended so that a stable matching exists. We settle the complexity of several variants, including cases when some of the edges are required to be included or excluded from the solution.

**Keywords:** Inverse optimization, Preference extension, Stable matching, Stable roommates problem, Vertex deletion

### 1 Introduction

The stable marriage problem was introduced by Gale and Shapley in 1962 in their seminal paper [13]. Since then, an enormous amount of research has been done in the field; see for example [22] for a survey.

<sup>a</sup>MTA-ELTE Momentum Matroid Optimization Research Group and MTA-ELTE Egerváry Research Group, Department of Operations Research, Eötvös Loránd University, Budapest, Hungary. Email: `kristof.berczi@ttk.elte.hu`. <sup>b</sup>MTA-ELTE Momentum Matroid Optimization Research Group, Department of Operations Research, Eötvös Loránd University, Budapest, Hungary. Email: `csajigergely@student.elte.hu`. <sup>c</sup>MTA-ELTE Momentum Matroid Optimization Research Group and MTA-ELTE Egerváry Research Group, Department of Operations Research, Eötvös Loránd University, Budapest, Hungary. Email: `tamas.kiraly@ttk.elte.hu`.

Kristóf Bérczi<sup>a</sup>

Gergely Csáji<sup>b</sup>

Tamás Király<sup>c</sup>

April 29, 2022

