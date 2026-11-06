## 2.1 The Subset Sum and _k_-SUM Problems

**Definition 2.1.** _An instance of_ Subset Sum _consists of a list A of n integers and a target_ \(t\in\mathbb{Z}\)_. The task is to determine whether there exists a subset_ \(S\subseteq[n]\) _such that_<tbc>

\(\sum_{i\in S}A[i]=t.\)

<tbc>**Definition 2.2.** _An instance of k_-SUM _consists of k lists A_<sub>1</sub>_,...,A<sub>k</sub> of integers, each of size n, and a target_ \(t\in\mathbb{Z}\)_. The task is to find_ \((i_1,\dots,i_k)\in[n]^k\) _satisfying_

\(A_1[i_1]+\cdots+A_k[i_k]=t,\)

_or to report that no such tuple exists._

It is common to assume in _k_-SUM that the target _t_ is zero, which is achieved by replacing every _A_<sub>1</sub>\[_i_\] with _A_<sub>1</sub>\[_i_\]-_t_. It is also common to assume that the bit-length of all integers in the _k_-SUM problem is at most _k_log_n+O_(loglog_n_), that is, that every integer has absolute value \(\widetilde{O}(n^k)\); this can be achieved by the standard fingerprinting technique \[ALW14\].

## 2.2 Prime Numbers

Given an integer \(M\ge 2\), one can generate a uniformly random prime from {_M,...,_2_M_} in expected time log<sup>_O_(1)</sup>_M_ as follows. One selects a uniformly random integer from {_M,...,_2_M_} and tests it for primality in time log<sup>_O_(1)</sup>_M_ \[Len02, AKS04\]. By the prime number theorem \[Had96, dlVP96\], the expected number of trials is _O_(log_M_). We also use the following estimate.

**Proposition 2.3.** _Let_ \(M\ge 2\) _and_ \(z\neq 0\) _be integers. The probability that a uniformly random prime from_ {_M,...,_2_M_} _divides z is_

\(O\big(\frac{log|z|}{M}\big).\)

_Proof._ Suppose that _d_ distinct primes from {_M,...,_2_M_} divide _z_. Their product divides |_z_|, and hence \(M^d\le|z|\), which implies \(d\le log|z|/logM\). By the prime number theorem \[Had96, dlVP96\], the interval contains \(\Omega(M/logM)\) primes, and therefore the probability in question is _O_(log|_z|/M_).

## 2.3 Quantum Primitives

Our algorithm employs the standard circuit model augmented with coherent read-write quantum random-access memory, denoted QRAQM. We count each single- or two-qubit gate as one operation and assume that coherent random access to any entry of a list represented using _m_ qubits can be performed in time polylogarithmic in _m_. See \[NS20, Sch21\] for a formal definition.

We use the following standard primitives in our algorithm.

### Coherent dictionaries.

**Theorem 2.4** (\[Amb07, Section 6.2\])**.** _Let M=n_<sup>_O_(1)</sup>_, and let_ U _be a totally ordered universe whose elements have_ polylog(_n)-bit encodings. In the_ QRAQM _model, a dynamic set_ \(D\subseteq\mathcal{U}\) _of at most M elements can be stored in_ \(\widetilde{O}(M)\) _space and constructed in_ \(\widetilde{O}(M)\) _time. The structure supports coherent successor lookup, insertion, and deletion in_ \(\widetilde{O}(1)\) _time, up to inverse-polynomial error._

