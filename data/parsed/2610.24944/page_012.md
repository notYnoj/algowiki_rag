### Split graphs and prior results.

A split graph has a partition \(V(G)=C\sqcup I\), where _C_ induces a clique and _I_ is independent. Known cases include threshold graphs, whose independent-side neighborhoods are nested by inclusion (Bonamy et al., 2022), and _K_<sub>8</sub>-free chordal graphs, which include _K_<sub>8</sub>-free split graphs (Botler et al., 2021). Our eight-vertex clique part puts the family beyond the latter theorem’s _K_<sub>8</sub>-free hypothesis.

### Neighborhood types and the extension.

For \(x\in I\), let \(S_x=N_G(x)\cap C\). Since _C_ is a clique, every pair \(u,v\in S_x\) forms a triangle _xuv_. Thus _x_ is _triangle-active_ exactly when \(|S_x|\ge 2\); vertices with identical _S<sub>x</sub>_ share one _neighborhood type_. Zeng (2026) proved the conjecture for |_C_|=8 and at most two types. Épi extends this to three types with unrestricted overlaps. Their triangles can compete for the same clique edges, requiring joint covers and packings.

**Theorem 1** (Three neighborhood types)**.** _Let G be a finite simple graph with a specified partition_ \(V(G)=C\sqcup I\)_, where G[C_]=_K_<sub>8</sub> _and I is independent. Suppose that the sets_ \(N_G(x)\cap C\)_, over vertices_ \(x\in I\) _with at least two neighbors in C, take at most three distinct values. Then_ \(\tau_\triangle(G)\le 2v_\triangle(G)\).

Up to clique relabeling and type permutation, there are 872 three-type profiles: 35 have nested neighborhoods and 277 further profiles satisfy Zeng’s maximum-cut criterion. Épi constructs exact cover and packing certificates for the remaining 560 profiles, using 18,444 multiplicity boxes. An independent checker verifies the witnesses and complete profile enumeration. Zeng’s truncation lemma extends the checks to arbitrary multiplicities, establishing the result for an infinite graph family (Appendix A.13).

The proof separates the finite certificate checks from the argument extending them to arbitrary multiplicities, making explicit how the computational evidence establishes the infinite-family statement.

## 6 Épi-turbo: Fast, Low-cost Algorithm Design

### 6.1 Purpose and Design

Algorithmic coding extends Épi’s research process to the development of executable solvers. Given a problem specification and a fixed evaluator, the agent designs, implements and tests an algorithm whose solution quality and runtime are measured on new instances. Épi-turbo is a lightweight configuration for these tasks, designed to develop effective algorithms within a short campaign and a small model budget.

### Shared foundation.

Épi-turbo keeps the parts of Épi that make a result reliable. The verifier checks each candidate under a fixed ruler, and Épi keeps the research state across sessions. Branches keep each method with its code and evidence, so the agent can return to an earlier version. Memory records keep lessons and dead ends for later sessions. Épi-turbo changes how the agent uses its model budget and when the campaign stops.

### Instructions for algorithm tasks.

The task instructions tell the agent how the benchmark measures a program. They give the complete score formula, which includes the quality term and the runtime term. They also tell the agent that the final score comes from instances that the agent does not see. When a program uses a large part of its time limit, Épi-turbo tells the agent. Thus the agent can find a good balance between solution quality and runtime. The instructions do not contain methods or hints for a specific problem.

### Model calls for algorithm design.

Each model call has a cost, and a short task has a small number of calls. Épi-turbo tells the agent that every call costs money, which includes a check on an active job. The agent does short experiments with a time limit in its own session. It sends an experiment to the execution infrastructure only when the experiment needs more time than a session gives. It examines active jobs only when a result can change its next decision. As a result, most of the budget goes to the design and test of algorithms.

### Continuous sessions.

Épi-turbo runs each campaign as one continuous session if possible. The session continues the best method so far and does not restart from an empty context. Before a session ends, the agent records its state, its best candidate and its next steps. The next session reads this record and continues the<tbc>



