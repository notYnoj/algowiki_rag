## 8 Lexicographic PLS-complete problems

in TOP correct; (2) flip input variables in BOTTOM to make them agree with TOP’s output; (3) flip gate variables in BOTTOM to make all gates there correct; (4) flip input variables in TOP to make them agree with BOTTOM’s output. By that time most likely some gates of TOP will be incorrect again (by us having meddled with its input variables) and so we go back to step (1) and repeat. By creating the right clauses and choosing appropriate weights we can make sure that each flip increases the weight of the satisfied clauses as long as the value outputs of the circuits increase.

**The active and the inactive circuit.** To make this idea work, we need an additional variable _f_, the flip variable, which indicates which circuit we consider to be _active_: TOP (if _f_=1) or BOTTOM (if _f_=0). The idea is now that gates in the active circuit should be correctly evaluated at all times and that _f_ should be flipped only when both circuits are correctly evaluated and the currently inactive circuit has better output than the other: if \((v_1^A\dots v_m^A)>_\mathrm{lex}(v_1^I\dots,v_m^I)\) where \(A\in\{\mathrm{T},\mathrm{B}\}\) denotes the active circuit and _I_ the inactive circuit. See Figure 1 for an illustration.

**The clauses.** We will now describe in detail the clauses of our 4-CNF formula _F_. They come in groups, which we list from most-important to least-important.

**1. Every gate in the active circuit should be correct.** When a gate _g<sub>j</sub>_ has inputs _y_<sub>1</sub> and _y_<sub>2</sub>, we write

\(f\rightarrow(g_j^T\leftrightarrow\mathrm{NAND}(y_1^T,y_2^T))\) (4.1)

and express this as a conjunction of four 4-clauses. Similarly, for the case that BOTTOM is active:

\(\neg f\rightarrow(g_j^B\leftrightarrow\mathrm{NAND}(y_1^B,y_2^B))\) (4.2)

