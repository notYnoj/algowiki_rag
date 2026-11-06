<tbc>parameter \((\beta,t,d)\), where \(\beta\) is the number of blocking pairs, _t_ is the increase in size to a stable matching, and _d_ is the maximum length of a preference list.

In a recent preprint, Chen, Roy and Simola \[13\] proved that it is W\[1\]-hard with respect to the optimal value to even approximate MinBP-AlmostStable-sri and MinBP-AlmostStable- Max-smi within any computable function depending only on this optimal value.

We will denote the decision problems "Does there exist a matching _M_ of _I_ such that \(|bp(M)|\le k?\)" and "Does there exist a perfect matching _M_ of bipartite instance _I_ such that \(|bp(M)|\le k?\)" by _k_-BP-AlmostStable-sri and _k_-BP-AlmostStable-Perfect-smi, respectively. Both problems are known to be NP-complete \[1, 9, 10, 11\], but in XP with respect to _k_ \[1, 10\]. It has been shown that minimising the number of blocking agents instead also remains computationally intractable \[10, 12, 11\].

Different definitions of almost-stability have also been considered from a communication- complexity perspective, e.g., by Floréen et al. \[18\] and Ostrovsky and Rosenbaum \[41\]. Work on almost-stable matchings for other problems has also been conducted (e.g., see \[29, 39, 14, 24\]). Other alternative solution concepts for sri instances that are different from almost-stable matchings have also been explored (see, for example, \[30, 17, 42, 33, 43, 27, 28\]). An alternative perspective on minimising instability in smi was offered by Biermann \[8\], who argued that, instead of counting blocking pairs, one should count a subset thereof that comprises a possible and economically reasonable transformation of the market. Similar perspectives have been studied for sri by Atay, Mauleon and Vannetelbosch \[3\], for example.

## 3 Introducing Minimax Almost-Stability

### 3.1 Motivation and Problem Definitions

In many real-world matching markets, agents contained in multiple blocking pairs not only have an increased opportunity to deviate and potentially cause unravelling, but they may also feel unfairly treated, knowing that they are in a position in which they could be better off after a decentralised reorganisation. To address this, we initiate the study of minimax almost-stable matchings, which optimise the solution for the worst-off agent by minimising the maximum number of blocking pairs any agent is involved in. This approach provides strong individual- level fairness guarantees and is particularly relevant in high-stakes multi-agent settings where agents may feel a critical need to be well-off. The two natural optimisation problems that we newly introduce and study in this paper are formally defined below. The first one, denoted by Minimax-AlmostStable-sri, aims for a matching of an sri instance with a minimal maximum number of blocking pairs for any agent.

Minimax-AlmostStable-sri<br>
**Input:** sri instance \(I=(A,\succ)\).<br>
**Output:** A matching \(M\in\mathcal{M}\) such that \(max_{a_i\in A}|bp_{a_i}(M)|=min_{M^\prime\in\mathcal{M}}max_{a_i\in A}|bp_{a_i}(M')|\).

The second problem, denoted by Minimax-AlmostStable-Max-smi, is motivated naturally by the setting where the central requirement is to maximise the size of the matching and, subject to this, we aim to minimise the maximum number of blocking pairs that any agent is contained in. We study this in the restricted setting of smi, as we will show that even in this setting the problem turns out to be highly intractable. However, the problem could also be defined more generally in the sri context, which we will denote by Minimax-AlmostStable-Max-sri.

