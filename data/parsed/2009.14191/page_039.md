## 4.4.2 Cut-off gadget

A cut-off gadget for an agent _a_ consists of _a_ together with five agents \(x_2^a,\dots,x_6^a\). The only acceptable 3-sets are \(\{a,x_5^a,x_6^a\}\), \(\{x_2^a,x_4^a,x_6^a\}\), and \(\{x_3^a,x_4^a,x_5^a\}\). See Figure 4 for an example.

Each agent derives its preferences from \(\{x_2^a,x_4^a\}\succ\{a,x_5^a\}\succ\{a,x_6^a\}\succ\{x_3^a,x_4^a\}\succ\{x_3^a,x_5^a\}\succ\{x_2^a,x_6^a\}\succ\{x_4^a,x_5^a\}\succ\{x_4^a,x_6^a\}\succ\{x_4^a,x_6^a\}\succ\{x_5^a,x_6^a\}\). Note that this list can be derived from \(a\succ x_2^a\succ x_3^a\succ x_4^a\succ x_5^a\succ x_6^a\).

We now observe that a cut-off gadget does not admit a stable matching, implying that one of the agents has to be matched outside the gadget. As agent _a_ is the only agent which accepts 2-sets containing agents not contained in the cut-off gadget, it follows that _a_ is matched to a 2-set outside the cut-off gadget.

**Lemma 4.29.** _A cut-off gadget does not admit a stable matching._

_Proof._ Note that any acceptable 3-set contains two agents from \(\{x_4^a,x_5^a,x_6^a\}\). Thus, any matching contains only one 3-set of a cut-off gadget. For each of the three possible matchings, we give a blocking 3-set in  3.

We observe that if agent _a_ is matched outside the cut-off gadget, then the cut-off gadget does not contain a blocking 3-set.

**Observation 4.30.** _The cut-off gadget without a admits a stable matching, namely_ \(\{x_3^a,x_4^a,x_5^a\}\).

Having described the gadgets needed for the reduction, we can now describe the complete reduction.

## 4.4.3 The reduction

Our reduction is structured similarly to the NP-completeness proof of 3-Dimensional Stable Marriage with Incomplete Cyclic Preferences by Biró and McDermid \[5\]. In both reductions, there is one agent for each man and each woman. Each such agent is forced to be<tbc>

\begin{tabular}{cc}
Matching & Blocking 3-set \\
\(\{a,x_5^a,x_6^a\}\) & \(\{x_2^a,x_4^a,x_6^a\}\) \\
\(\{x_2^a,x_4^a,x_6^a\}\) & \(\{x_3^a,x_4^a,x_5^a\}\) \\
\(\{x_3^a,x_4^a,x_5^a\}\) & \(\{a,x_5^a,x_6^a\}\) \\
\end{tabular}

a
X3
a
X5
X4
X6
X2

Figure 4: The acceptable 3-sets of a cut-off gadget.

3: The blocking 2-sets in the subinstance from Lemma 4.29.

