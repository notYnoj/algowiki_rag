circuit for equal outputs. We can however ensure that this scenario neither comes up by assuming that the circuit creates different outputs for different inputs e.g. by extending the output with the input in the lowest positions.

With these modifications, the proof works analogously to the proof of Proposition 21.

Reducing from sensitive LocalLexMax-4-SAT allows us now to make all remaining reductions tight.

\(\blacktriangleright\) **Proposition 23.** _The reduction from sensitive_ LocalLexMax-4-SAT _to Abelian_ Polm _and to finding approximate Nash equilibria is tight._

**Proof.** We first see that the transition graphs of the instances obtained by the reduction contains the transition graph of LocalLexMax-4-SAT, since every improving flip of LocalLexMax-4-SAT is directly represented as a single flip in the new instances. Hence, we can take all feasible solutions as R and fulfill the first two points.

For the third point, we have to make sure that there are no internal improving flips that change the assignment while the fulfilled clauses stay the same. Because if there were, then this would not be an improving move in the LocalLexMax-4-SAT instance but might be in the newly created instances since it changes the delay on some more important resource from 3 to 2 while the delay on some less important resource increases from 1 to 2. Similarly, in the Polm instance this would mean that some very important fulfilling position by the order has a one and after applying it we map the one to some less important fulfilling position.

By Proposition 22 we know however that these internal improving flips can never occur and any flip changes the truth value of at least some clause. Thus, any improving flip in the f(I) instance here is an improving flip in the original instance _I_.

For cyclic Polm from the previous section the same proof idea works, but as R we choose the permutations that define an assignment, i.e. there are no ones at bad-color positions.

## E FP-completeness for LocalLexMax-2-SAT

In contrast to the decision variant 2-SAT, which is NL-complete, and the arbitrarily-weighted LocalMax-2-SAT, which is PLS-complete[19], we show that LocalMax-2-SAT with lexicographic costs (i.e. LocalLexMax-2-SAT) is FP-complete. We have already seen a polynomial time algorithm in the introduction; now we will show hardness.

\(\blacktriangleright\) **Proposition 24.** LocalLexMax-2-SAT _is FP-hard._

**Proof.** We reduce from the circuit evaluation problem. We are given a circuit _C_ and an input \(\mathbf{x}\in\{0,1\}^n\). The gates of _C_ are given in topological order. The goal is to compute \(C(\mathbf{x})\in\{0,1\}^m\), i.e., the output of the circuit. We can assume that the circuit consists only of NAND-gates. We use a variable _xi<sub>i</sub>_ for each input and a variable _g<sub>j</sub>_ for each gate.

The highest clauses fix the input variables to the current input. Afterwards, we use the following three clauses for each gate. If gate _g<sub>j</sub>_ has inputs _y_<sub>1</sub> and _y_<sub>2</sub>, we produce the following block containing three clauses:

1. \(\neg y_1\rightarrow g_j\)

2. \(\neg y_2\rightarrow g_j\)

3. \(\neg g_j\)

The blocks are ordered according to the topological ordering of the circuit; within each block they are ordered as shown above.

