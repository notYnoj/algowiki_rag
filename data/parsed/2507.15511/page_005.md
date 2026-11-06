## Collision Entropy.

We define the (base-2) _collision entropy_ of _S_ as

\(H_c(S):=n-log_2|\Sigma(S)|=n-log_2U.\)

This quantity measures the compressibility of the subset sum space. Intuitively, _H<sub>c</sub>(S_) captures how much smaller \(\Sigma(S)\) is than the full power set: when many subsets collide onto the same sum, \(U\checkmark 2^n\) and _H<sub>c</sub>(S_) is large; when most sums are unique, _U_≈2_<sup>n</sup>_ and _H<sub>c</sub>(S_) is near zero.

• If all _a<sub>i</sub>_=1, then every subset sum lies in {0,1_,...,n_} and _U=n_+1=_O(n_), so _H<sub>c</sub>(S_)=\(n-log_2n=\Theta(n)\).<tbc>

• If _S_ is constructed to be collision-free (e.g., a superincreasing sequence), then _U_=2_<sup>n</sup>_, so _H<sub>c</sub>(S_)=0 and no structure is exploitable; IC-SubsetSum runs in worst-case time.

Collision entropy may be informally viewed as a coarse proxy for the Kolmogorov compressibility of the subset sum landscape: the more structured the set, the lower its information content.<br>
_Note._ We use the unnormalized form of collision entropy _H<sub>c</sub>(S_)=_n_-log<sub>2</sub>_U_, which is standard in information theory; the normalized form _H<sub>c</sub>(S)/n_ differs only by a multiplicative constant and is not required for our purposes.

## Role of _U_ in Complexity.

The parameter \(U=|\Sigma(S)|\) governs both the structural difficulty of a Subset Sum instance and the size of its minimal certificate. If \(\Sigma(S)\) is known, then deciding whether some \(T\subseteq S\) sums to a target _t_ reduces to checking whether \(t\in\Sigma(S)\)--a constant-time membership query. Thus, _U_ captures the certificate length for the _decision_ variant.

For the _constructive_ variant, a solution subset must be recovered; here, each subset sum must be paired with a canonical encoding of the realizing subset (e.g., a bitmask). Our algorithm, IC-SubsetSum, builds this richer certificate explicitly, and its runtime and space scale with _U_ and _n_. Designing algorithms whose performance adapts to _U_, rather than worst-case size 2_<sup>n</sup>_, is the central goal of this work.

## Certificates for Subset Sum.

Once the set \(\Sigma(S)\) is known, deciding whether there exists a subset of _S_ summing to a target _t_ reduces to checking if \(t\in\Sigma(S)\). Thus, \(\Sigma(S)\) serves as an _information-theoretically minimal certificate_ for the _decision_ version of Subset Sum: no smaller object suffices to resolve all yes/no queries about subset-sum feasibility.

However, for the _constructive_ version--retrieving an actual subset \(T\subseteq S\) such that \(\sum_{i\in T}a_i=t\)--this is no longer sufficient. In this case, each sum must be paired with a compact encoding of a corresponding witness subset. Our algorithm constructs such a certificate by maintaining, for each \(\sigma\in\Sigma(S)\), a canonical bitmask representing the lex-minimal subset that realizes \(\sigma\).

• The **decision certificate** is \(\Sigma(S)\), with total length \(O(U\cdot log(n\cdot max(S)))\) bits if each sum is represented in binary.<tbc>

• The **constructive certificate** is the set of \((\sigma,\text{bitmask})\) pairs, with total size \(O(U\cdot n)\) bits.

This distinction underlies the runtime and space guarantees of our algorithm, which produces the stronger constructive certificate online. All references to "certificate size" henceforth will clarify which variant is being discussed.

Given a target _t_, if a solution exists, a witness is returned in additional _O(n_) time from our maintained encodings. Unless otherwise stated (e.g., in decision-variant optimizations), all runtime bounds are for full constructive-certificate enumeration of \(\Sigma(S)\), in which each \(\sigma\in\Sigma(S)\) is stored with its canonical (lexicographically minimal) witness bitmask. This invariant is maintained throughout, ensuring correctness even on high-density instances.

