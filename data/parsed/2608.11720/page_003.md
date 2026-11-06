(2) We only rule out algorithms that work with _probability_ 1; our result does not rule out algorithms that work w.h.p.

We argue that, while somewhat nonstandard, this setting is still relevant and nontrivial:

(1) While probability-1 classical algorithms do not usually make much sense, there are several examples of nontrivial distributed quantum algorithms that indeed guarantee success with probability 1 using only finitely many qubits; examples include the quantum algorithm for distributed symmetry-breaking in two-node networks \[Gid14\] and the solution strategy for the GHZ game \[GHZ89\].<tbc>

(2) The finitely dependent colorings \[HL16\] are also error-free, and hence a direct distributed analogue would be a quantum algorithm with success probability 1. Moreover, they are invariant under shifts, which would naturally correspond to a quantum algorithm in the anonymous setting.

1 gives an overview of what is now known about the 3-coloring problem across various models of computing.

### 1.4. Open Questions.

After this work, the main open question is extending our result from algorithms that work with probability 1 to algorithms that work w.h.p. We believe that this is the only essential missing part before we can close the long-standing open question. As soon as we look at algorithms that work w.h.p., the distinction between anonymous networks and networks with unique identifiers essentially disappears (since random identifiers will be unique w.h.p.).

## 2. Technical Overview

The proof of Theorem 1 is in two steps: first, we prove that in any 1-round quantum-PN algorithm, there is a non-zero probability that _n_-2 consecutive nodes output the same value; then, we prove that any zero-error _T_-round coloring algorithm can be turned into a 1-round algorithm (using more colors) that is breaking symmetry with probability one, meaning that no 2_T_+2 consecutive nodes all output the same value. Hence, any zero-error coloring algorithm<tbc>

\begin{tabular}{ccc}
Model & With probability 1 & With high probability \\
deterministic PN & impossible & impossible \\
randomized PN & \(\Theta(n)\) & \(\Theta(log^*n)\) \\
quantum-PN & \(\Theta(n)\) - **_new_** & _O_(log<sup>∗</sup>_n_) \\
deterministic LOCAL & \(\Theta(log^*n)\) & \(\Theta(log^*n)\) \\
randomized LOCAL & \(\Theta(log^*n)\) & \(\Theta(log^*n)\) \\
quantum-LOCAL & _O_(log<sup>∗</sup>_n_) & _O_(log<sup>∗</sup>_n_) \\
finitely dependent & \(\Theta(1)\) & \(\Theta(1)\) \\
non-signaling & \(\Theta(1)\) & \(\Theta(1)\) \\
SLOCAL & \(\Theta(1)\) & \(\Theta(1)\) \\
online-LOCAL & \(\Theta(1)\) & \(\Theta(1)\) \\
\end{tabular}

** 1.** What is now known about the problem of 3-coloring cycles across various models of computing. The values are round complexities or localities; the nontrivial results are from \[CV86; Lin92; Nao91; HL16\]. We have highlighted the new result and

the open questions with colors.

