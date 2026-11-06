<tbc>In this classical deterministic setting, the complexity of the task is very well-understood since the 1990s: \(\Theta(log^*n)\) communication rounds is sufficient \[CV86; GPS88\] and necessary \[Lin92\]. Even if we allow randomness and only require a correct solution with high probability (w.h.p., with probability 1-1/poly(_n_)), it is known that \(\Theta(log^*n)\) rounds are still necessary \[Nao91\].

But does anything change if we switch from classical LOCAL to the quantum-LOCAL model \[GKM09; AF14\], where each node is a quantum computer and can exchange qubits with its neighbors? While we have seen a lot of progress in understanding which distributed problems admit quantum advantage and which problems remain hard in quantum-LOCAL \[GKM09; AF14; LNR19; DKLMMSS24; ACdLLMMPRRS25; BBCdELLMORSTV25; BCdEKLOSS26; BCCdELMOS25; BG26\], the seemingly elementary question of 3-coloring cycles has remained open, even though essentially the same question was already posed in the very first paper that introduced the quantum-LOCAL model \[GKM09\]. Nobody has been able to rule out the possibility that there is, for example, a quantum-LOCAL algorithm that 3-colors cycles in a constant number _O_(1) of rounds of communication.

## 1.2. Barrier: Finitely Dependent Colorings.

There is a barrier that has so far prevented progress on this question. To our knowledge, all known lower bounds in the quantum-LOCAL model are _indirect_: they do not directly study the quantum-LOCAL model (or any model of quantum computing), but they study strictly stronger models, such as finitely dependent distributions \[BGM93; HL16; ACdLLMMPRRS25\], non-signaling distributions \[GKM09; AF14\], and the online-LOCAL model \[AELMSS23; ACdLLMMPRRS25\]. These lower bounds fundamentally build on the idea that distributed quantum algorithms cannot violate physical causality--information must be carried by communicated systems and correlated event must share a common cause.

Unfortunately, this avenue is blocked for the case of symmetry-breaking problems, and especially for the case of 3-coloring cycles. It is known that there exists a finitely dependent distribution of 3-colorings in cycles \[HL16\]. It follows that a hypothetical constant-round quantum algorithm for 3-coloring cycles would not violate causality, and hence purely causality-based arguments cannot be used.

Therefore, any proof that shows the impossibility of efficient 3-coloring in quantum-LOCAL must be "genuinely quantum", in the sense that it cannot as a byproduct rule out finitely dependent distributions, non-signaling distributions, or online-LOCAL algorithms.

We point out that there is a paper that rules out one-round, one-sided algorithms for 3-coloring \[LR22; GKZ19\] and, very recently, a paper proving that 3-coloring \(\Delta\)-ary trees with \(\Delta\ge 300\) requires \(\Omega(log^*\Delta)\) rounds \[FMZ26\]. Both lower bounds are about the non-signaling model, i.e., causality-based--fundamentally different techniques are needed for stronger lower bounds.

## 1.3. Our Contribution.

In this work, we present the _first "genuinely quantum" lower bound for the task of distributed_ 3_-coloring_; our lower bound _separates quantum algorithms from finitely dependent distributions._ We prove that there is no _o(n_)-round quantum algorithm using finitely many qubits in anonymous cycles that produces a 3-coloring with probability 1; the precise statement is as follows:

**Theorem 1.** _For every fixed_ \(c\ge 3\) _and every even_ \(n\ge 4\)_, any quantum-PN algorithm that properly c-colors directed n-cycles with probability_ 1 _takes_ \(T(n)>\lfloor n/2\rfloor-2\) _rounds._

We note that our result comes with two assumptions:

(1) We work in the quantum-PN model; this is the _anonymous_ version of quantum-LOCAL (with finitely many qubits). In particular the nodes do not have unique identifiers.

