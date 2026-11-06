### 4.3 Approximation guarantee

_Proof of Theorem 4.1._ By Lemma 4.3, there are at most 4|_E|/k_ blocking pairs which are not (2_/k_)-blocking. By Lemma 4.2, all (2_/k_)-blocking pairs are incident with _B_. Finally, by Lemma 4.4, the bad men contribute at most \(4\delta|E|\) blocking pairs for \(\delta\le 1/2\). Therefore, the total number of blocking pairs is at most \(4(\delta+1/k)|E|\). Choosing \(\delta=\varepsilon/8\) and \(k=\lceil 8/\varepsilon\rceil\) gives the desired result.

### 4.4 Run-time Guarantee

**Theorem 4.7.** \(\text{\textbf{ASM}}(P,\varepsilon,n)\) runs in \(O(\varepsilon^{-3}log^5(n))\) communication rounds.

_Proof._ Notice that the only communication between processors occurs in **ProposalRound**. \(\text{\textbf{ASM}}(P,\varepsilon,n)\) iterates **QuantileMatch**(_P,k_) a total of \(O(\varepsilon^{-2}logn)\) times, while quantile match invokes \(\text{\textbf{ProposalRound}}(Q,k,A)O(\varepsilon^{-1})\) times. Finally, each step of **ProposalRound** can be performed in _O_(1) communication rounds, except for Step 3, which calls **MaximalMatching**. By \[6\], **MaximalMatching** runs in _O_(log<sup>4</sup>_n_) communication rounds. Thus, \(\text{\textbf{ASM}}(P,\varepsilon,n)\) requires \(O(\varepsilon^{-3}log^5(n))\) communication rounds, as claimed.

**Remark 4.8.** While the CONGEST model allows for unbounded local computation in each round, the local computations required by **ASM** are quite simple. In fact, each communication round can easily be implemented in nearly-linear time in _n_. Thus the synchronous run-time of **ASM** is \(\tilde{O}(n)\). To our knowledge, this gives the first distributed algorithm whose synchronous run-time is sub-quadratic in _n_, even for unbounded preferences.

## 5 Randomized Algorithms

The main source of complexity in **ASM** comes from finding a maximal matching. While Hanń ́ckowiak, Karo ́nski, and Panconesi’s algorithm \[6\] is the most efficient known deterministic algorithm, faster randomized algorithms are known. Specifically, we consider the algorithm of Israeli and Itai \[8\]. They describe a simple randomized distributed algorithm which finds a maximal matching in expected _O_(log_n_) rounds. By simply replacing **MaximalMatching** with a truncated version Israeli and Itai’s algorithm, we obtain a faster randomized algorithm for finding almost stable matchings. We refer the reader to Appendix A for details on the guarantees for Israeli and Itai’s algorithm.

### 5.1 General preferences

**Theorem 5.1.** There exists a randomized distributed algorithm, \(\text{\textbf{RandASM}}(P,\varepsilon,n,\delta)\), which for any \(\delta,\varepsilon>0\) finds a \((1-\varepsilon)\)-stable matching with probability at least \(1-\delta\) in \(O(\varepsilon^{-3}log^2(n/\delta\varepsilon^3))\) rounds.

_Proof sketch._ We take **RandASM** to be exactly the same as **ASM**, except that we use Israeli and Itai’s algorithm \[8\] for the **MaximalMatching** subroutine. Specifically, for **MaximalMatching**, we iterate **MatchingRound** (see Appendix A) \(O(log(n/\delta\varepsilon^3))\) times. By Corollary A.2, each call to **MaximalMatching** will succeed in finding a maximal matching with probability at least \(1-O(\delta\varepsilon^3/logn)\). Since **RandASM** calls **MaximalMatching** \(O(\varepsilon^{-3}/logn)\) times, by the union bound, every call to **MaximalMatching** succeeds with probability at least \(1-\delta\). The remaining analysis of **RandASM** is identical to that of **ASM**.

