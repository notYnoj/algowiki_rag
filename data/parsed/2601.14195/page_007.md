Minimax-AlmostStable-Max-smi<br>
**Input:** smi instance \(I=(A,\succ)\).<br>
**Output:** A matching \(M\in\mathcal{M}^+\) such that \(max_{a_i\in A}|bp_{a_i}(M)|=min_{M^\prime\in\mathcal{M}^+}max_{a_i\in A}|bp_{a_i}(M')|\).

Now, in Section 3.2, we will first look at the compatibility of different notions of almost- stability and show that minimax almost-stability is fundamentally different from the others. We will then, in Section 3.3, provide further structural insights into the structure of these problems.

## 3.2 Differentiating Almost-Stability Notions

Minimax almost-stability differs fundamentally from aggregate stability metrics (such as minimising the number of blocking pairs \[1, 10, 12\]) by prioritising the worst-off agent (in terms of the number of favourable deviation opportunities). Furthermore, it contrasts the minimisation of blocking agents \[10, 12\], which likely requires fewer agents with a stronger incentive to deviate, therefore causing a greater risk of unravelling.

We give the following examples to highlight the differences between these three notions. These are for the sri setting, but similar examples apply for Max-smi.

**Proposition 3.1.** _A matching that admits a minimum number of blocking agents might not admit a minimum number of blocking pairs, and vice versa._

_Proof._ Consider the sri instance with preferences as follows:

\(a_1:a_2a_3a_4\)<br>
\(a_2:a_3a_1\)<br>
\(a_3:a_1a_2\)<br>
\(a_4:a_5a_6a_1\)<br>
\(a_5:a_6a_4\)<br>
\(a_6:a_4a_5\)

Then _M_={{_a_<sub>2</sub>_,a_<sub>3</sub>},{_a_<sub>5</sub>_,a_<sub>6</sub>}} admits four blocking agents (_a_<sub>1</sub>_,a_<sub>3</sub>_,a_<sub>4</sub>_,a_<sub>6</sub>), which is minimal (as agents _a_<sub>1</sub>_,a_<sub>2</sub>_,a_<sub>3</sub> form a directed cycle in the first and second preference list positions, and _a_<sub>4</sub>_,a_<sub>5</sub>_,a_<sub>6</sub> do too), but three blocking pairs ({_a_<sub>1</sub>_,a_<sub>2</sub>},{_a_<sub>1</sub>_,a_<sub>3</sub>},{_a_<sub>4</sub>_,a_<sub>6</sub>}). The matching \(M'=\{\{a_1,a_4\},\{a_2,a_3\},\{a_5,a_6\}\}\), on the other hand, admits the same blocking agents, but only admits two blocking pairs (this is easy to see as \(M\subset M'\), so \(bp(M')\subseteq bp(M)\), and the blocking pair \(\{a_1,a_4\}\in bp(M)\) is a match in \(M'\)).

Now consider the sri instance with preferences as follows:

\(a_1:a_2a_3a_4a_5a_6\)<br>
\(a_2:a_3a_1a_4a_5a_6\)<br>
\(a_3:a_1a_2a_4a_5a_6\)<br>
\(a_4:a_5a_1a_4a_5a_6\)<br>
\(a_5:a_1a_2a_3a_4a_6\)<br>
\(a_6:a_1a_2a_3a_4a_5\)

Then _M_={{_a_<sub>1</sub>_,a_<sub>4</sub>},{_a_<sub>2</sub>_,a_<sub>3</sub>},{_a_<sub>5</sub>_,a_<sub>6</sub>}} admits two blocking pairs ({_a_<sub>1</sub>_,a_<sub>3</sub>},{_a_<sub>4</sub>_,a_<sub>5</sub>}), which is minimal (this can be verified computationally), but four blocking agents (_a_<sub>1</sub>_,a_<sub>3</sub>_,a_<sub>4</sub>_,a_<sub>5</sub>). On the other hand, the matching \(M'=\{\{a_1,a_6\},\{a_2,a_3\},\{a_4,a_5\}\}\) also admits two blocking pairs ({_a_<sub>1</sub>_,a_<sub>3</sub>},{_a_<sub>1</sub>_,a_<sub>5</sub>}), but only admits three blocking agents (_a_<sub>1</sub>_,a_<sub>3</sub>_,a_<sub>5</sub>).

