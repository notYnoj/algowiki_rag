the configuration, feasibility checks and gain criterion. The verifier then evaluates every branch under this shared rule. This gives Épi a consistent basis for comparing methods throughout the investigation.

We also specify the evidence needed for each type of claim. The verifier checks geometric constraints for a construction. For a rigorous bound, we require a certificate with exact arithmetic or controlled numerical error. For a computer-assisted theorem, we require both the finite checks and a mathematical reduction showing why those checks establish the full statement. The agent must develop this reduction or certificate when the task requires one.

Épi’s research environments evolve with verified findings. Improved results provide new reference values for subsequent investigations, while new research questions motivate changes to task formulations, representations and verification requirements. We incorporate these changes when defining the next campaign. For example, a numerical estimate can lead to a certification task whose environment includes certificate representations and rigorous error control. Each campaign uses a fixed evaluation rule to compare methods, and successive campaigns build on the verified findings of earlier work.

## 3.2 Self-improving Research Agents

Épi improves its research methods through accumulated experience. The agent develops and compares alternatives on versioned branches, retains and retrieves experience through hierarchical memory, and uses independent review to reassess its research decisions. Together, these mechanisms allow Épi to refine its approach across experiments and campaigns.

Branches and backtracking. A single approach restricts which formulations and search regions the agent explores. Épi maintains branches to develop alternatives while preserving each method’s code and evidence. Each branch stores an implementation, tests and notes in a versioned repository. The agent saves changes as commits and can create a new branch from an earlier commit. It compares the resulting experiments under the same ruler.

The agent backtracks by returning to a saved implementation and trying a different continuation. It can also revisit an existing branch and extend the work already recorded there. When the agent abandons a branch, it records the reason and retains the branch for later inspection. For a packing problem, the agent might refine



Research continuity
across sessions
Research agent
Research directions
Durable experiments
Frozen evaluation
Research brief
Ruler + gain floor
Verified result
Question time budget
Reference recheck
Branch compare revisit
Runs across sessions
score trajectory
Feedback & learning
Cross-case memory
Independent review
Context
Dead ends
Lessons
Cross-model critique

Épi research architecture

**Figure 1:** Épi’s research architecture. The agent develops methods on versioned branches and retrieves saved history and cross-case lessons. An independent model reviews the evidence. The environment checks each candidate under a fixed ruler and gain floor. The execution infrastructure supports experiments, persistent storage and isolated verifier execution across sessions. Section 2 defines the acceptance rule.

