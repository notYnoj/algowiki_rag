### Step 1: Reduction to Verification via Additive Approximation.

First, by a standard reduction (see e.g. Section 4.1 of \[JPSX26\]), we observe that it suffices to reduce to the following witness finding problem.

**Definition 3.1.** _Given_ \(A,B,C\in\mathbb{Z}^{N\times N}\)_, the_ (min,+)_-Witness Equality problem asks to check for all i,j, whether there exists_ \(k\in[N]\) _such that A_\[_i,k_\]+_B_\[_k,j_\]=_C_\[_i,j_\].

**Lemma 3.2** (Tight Reduction to Verification)**.** _Suppose_ (min,+)_-Witness Equality can be computed in time T(N,U_) _whenever A,B have entries in_ \[_U_\] _and C has entries in_ \[2_U_\]_. Then the_ (min,+)_-Product of two_ \(N\times N\) _integer matrices with entries in_ \[_U_\] _can be computed in time_

\(O\left((T(N,U)+N^2)logU\right).\)

We defer the proof of Lemma 3.2 and focus on providing an algorithm for (min,+)-Witness Equality. The idea is essentially that from \(\lceil A/2\rceil*\lceil B/2\rceil\), we can obtain a +2-approximation of _A∗B_. Then, invoking the oracle for (min,+)-Witness Equality _O_(1) times, we can check all 3 possible values of (_A∗B_)\[_i,j_\] for each _i,j_. We say (_i,j_) is accurate if there exists \(k\in[N]\) such that _A_\[_i,k_\]+_B_\[_k,j_\]=_C_\[_i,j_\]. By Lemma 3.2, it suffices to check for whether every pair (_i,j_) is accurate.

### Step 2: Finding a Sparse Certificate.

In this step, our goal is to efficiently prune triples (_i,k,j_) for which \(A[i,k]+B[k,j]\neq C[i,j]\). Fix parameters \(1\le B,S\le N\) whose values we will determine later and let \(P\gg BlogU\) for some sufficiently large constant. Split the inner dimension \[_N_\] into _O(N/B_) contiguous blocks of size _B_. A block _K_ is a _block witness_ for output pair (_i,j_) if there exists \(k\in K\) such that _A_\[_i,k_\]+_B_\[_k,j_\]=_C_\[_i,j_\]. Since _K_ are disjoint and cover \[_N_\], observe that (_i,j_) is accurate if and only if there is a block witness _K_.

To find block witnesses efficiently, we begin by finding a set of candidate witnesses. Let \(p\in[P,2P]\) be a prime. For a block _K_ and prime _p_, we say _K_ is a _candidate block witness_ with respect to _p_ for (_i,j_) if there exists \(k\in K\) satisfying

\(A[i,k]+B[k,j]\equiv C[i,j]modp.\)

We have the following claim.

**Claim 3.3** (Candidate Block Witness)**.** _Fix_ \(i,j\in[N]\)_. If K is a block witness, then K is a candidate block witness with respect to p for any choice of prime p._

_Let p_∼\[_P,_2_P_\] _be a randomly sampled prime. If K is not a block witness, then K is not a candidate block witness with respect to p with probability_ \(\ge 1/2\) _over the choice of p._

_Proof of Claim 3.3._ The first claim is trivial, so we focus on the second. Since _K_ is not a block witness, for \(k\in[K]\) define<tbc>

\(\Delta_k:=A[i,k]+B[k,j]-C[i,j]\neq 0.\)

<tbc>Note that \(0<|\Delta_k|\le 3U\) so that \(\Delta_k\) has at most \(O(log_PU)=O\left(\frac{logU}{logP}\right)\) prime factor in the range \[_P,_2_P_\]. By the prime number theorem, there are \(\Theta(P/logP)\) primes in the range \[_P,_2_P_\] so that for a random choice of prime _p_∼\[_P,_2_P_\], the probability that \(\Delta_k\equiv 0modp\) is at most

\(O\left(\frac{logU}{logP}\frac{logP}{P}\right)=O\left(\frac{logU}{P}\right).\)

A union bound ensures that \(\Delta_k\equiv 0modp\) for any \(k\in K\) with probability at most _O(B_log_U/P_). By our choice of \(P\gg BlogU\), the probability can be upper bounded by 1/2.

This motivates the following approach: sample _O_(log_n_) primes independently in the range \[_P,_2_P_\]. We say _K_ is a _candidate block witness_ if _K_ is a candidate block witness with respect to all sampled primes _p_. Any block that is a block witness will be a candidate block witness, whereas any block that is not a block witness will be a candidate block witness with inverse polynomial probability. Our first goal is to generate candidate block witnesses algorithmically. To do so, we give a subroutine that given block _K_ and prime _p_, checks whether _K_ is a candidate block witness with respect to _p_.

