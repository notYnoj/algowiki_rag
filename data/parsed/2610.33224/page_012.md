### 6.4 Recall versus Bandwidth, and the Limits of \(\ell_1\) Ranking

4 gives the full trade-off curve behind the Holo-NN rows of  3 for both encrypted protocols. Because LinPIR and CKKS evaluate the same linear operator _y=H_F(_q_), recall is a function of _M_ alone, and each backend’s wire cost is a deterministic function of _M_ given its measured ciphertext sizes. All figures are for the bare 1-RTT protocol: the FISTA ranking, with no verification fetch and no reranking against plaintext vectors.

The sweep doubles as a consistency check on  1. Its _M_=380,100 row is the SIFT-1M 75% regime of that table, and it reproduces all three published figures.

The two conventions diverge sharply, and the divergence is informative. At _M_=300,000 Holo-NN locates _the_ nearest neighbor within its top ten for 93.0% of queries, but recovers only 61.6% of each query’s _ten_ nearest neighbors in that same top ten. The missing neighbors have not been lost: raising the cutoff to fifty recovers 92.0% of them, from a candidate set that is still \(20,000\times\) smaller than the database.

The gap is also strikingly persistent in _M_. Over the sweep, 1-recall@10 climbs from 63.4% to 98.5% and is effectively saturated by _M_=500,000, whereas 10-recall@10 moves only from 33.3% to 73.0% and is still rising roughly linearly when 1-recall has flattened. Adding measurements sharpens the question "is the true nearest neighbor in this list" long before it sharpens "are these ten the right ten". A budget that resolves the first question almost perfectly leaves the second one a quarter unanswered.

This is the expected behavior of \(\ell_1\) recovery on a correlated support, not a defect of the measurement operator. A query’s ten true nearest neighbors are, by construction, mutually near-identical, so their feature vectors G(_t<sub>i</sub>_) are highly correlated and the corresponding columns of _H=A_G(_T_) are nearly collinear. Faced with a group of near-collinear atoms that jointly explain the measurement,<tbc>

<tbc>the LASSO \[42\] does not distribute the coefficient across the group; it concentrates the mass on a single representative and shrinks the remainder toward zero \[50\]. The surviving representative is reliably _a_ member of the true neighbor set -- which is why 1-recall is high -- while its near-duplicates are demoted in magnitude though not eliminated, which is why they reappear as the cutoff widens.

The implication is that Holo-NN, in its present form, is best understood as an unusually cheap, tunable, high- coverage approximate nearest-neighbor algorithm rather than a precise ranker, even in the limit of computation and bandwidth. Where a downstream exact-distance stage is available -- a client that already holds the candidate payloads, or a private retrieval step as in Section 3.4 -- the relevant quantity is the coverage figure, and 92.0% of the true ten neighbors for 5.37 MB in 0.82s (HEIR- GPU CKKS), 11.13 MB (64-bit CKKS), or 265.4 MB with zero persistent server state (LinPIR) in one round trip compares favorably with Panther’s 88.85% for 92.9 MB and SANNS’s ≈90% for 1.77 GB -- though the comparison is not strict, since SANNS and Panther deliver their top-ten sets already ranked within a top ten while Holo-NN is a top fifty, awaiting a reranking stage. Where no such stage exists, the ranking Holo-NN emits is materially weaker than Compass’s. Substituting an Elastic Net \[50\] (\(\ell_1+\ell_2\)) or Group LASSO \[47\] proximal operator for the \(\ell_1\) soft threshold would be expected to redistribute mass across correlated groups and close much of this gap, at no cost in bandwidth, round trips or server work, since it changes only the client’s local recovery step. We leave this to future work.

## 7 Conclusion

We presented **Holo-NN**, a holographic approximate nearest neighbor retrieval architecture that reformulates nearest neighbor search as an underdetermined linear Compressive Sensing problem. By precomputing a degree-1 compressed database representation offline (\(H=AG=A\mathcal{G}(T)\in\mathbb{R}^{M\times B}\)), Holo-NN executes blind, privacy- preserving retrieval via a single linear operator requiring \(M\checkmark N\) measurements in a single non-interactive round trip, with no client-side index state and no pre- processing stream. Because _H_ is constructed offline on the server, the index operator can profile the empirical bandwidth-recall trade-off directly on the target dataset, while our Asymmetric FlyHash projection removes the double-quantization loss that a symmetric sparse code would incur on high-dimensional semantic manifolds.

Holo-NN works in plaintext as a generic high-confidence, approximate nearest neighbor algorithm. Because blind forms of the algorithm function as single-round private linear operations, they scale well to LinPIR or other private linear operations while retaining naturally scalable, embarrassingly parallel computational models that are well suited to modern hardware. Moreover, this framing<tbc>

\begin{tabular}{ccccccccccc}
\multicolumn{2}{c}{_M_ **Cheddar 32b** **Cheddar** **GP** & **CKKS 64b** & **LinPIR** **Wire** & 1-r@1 & 1-r@10 & **10-r@10** & 10-r@50 & **MRR@10** \\
98,300 & **2.10** MB & **0.26** s & 4.24 MB & 91.1 MB & 32.5 & 63.4 & **33.3** & 57.0 & **0.417** \\
150,000 & **3.01** MB & **0.42** s & 6.36 MB & 135.8 MB & 40.5 & 75.8 & **43.8** & 72.5 & **0.518** \\
200,000 & **3.80** MB & **0.54** s & 7.95 MB & 179.0 MB & 48.2 & 84.2 & **51.8** & 82.0 & **0.601** \\
250,000 & **4.59** MB & **0.67** s & 9.54 MB & 222.2 MB & 53.5 & 89.3 & **57.3** & 88.0 & **0.652** \\
300,000 & **5.37** MB & **0.82** s & 11.13 MB & 265.4 MB & 58.2 & 93.0 & **61.6** & 92.0 & **0.702** \\
327,600 & **5.77** MB & **0.86** s & 11.66 MB & 289.2 MB & 59.7 & 93.3 & **63.8** & 93.0 & **0.718** \\
380,100<sup>†</sup> & **6.68** MB & **1.00** s & 13.78 MB & 334.6 MB & 62.0 & 95.6 & **66.8** & 95.1 & **0.741** \\
500,000 & **8.65** MB & **1.30** s & 17.50 MB & 438.2 MB & 69.5 & 98.5 & **73.0** & 98.0 & **0.801** \\
\end{tabular}

4: Holo-NN on SIFT-1M (_N_=10<sup>6</sup>, _D_=128, _B_=16,384), 1,000 official queries, 80 FISTA iterations. **Cheddar 32b Wire** (and RTX 3090 server GPU latency **Cheddar GPU**) uses two 256 KiB 32-bit RNS query ciphertexts plus \(\lceil M/8192\rceil\times 128\) KiB single-limb responses; **CKKS 64b Wire** (OpenFHE/Phantom) is 1.05 MB query plus \(\lceil M/16384\rceil\times 0.53\) MB responses; **LinPIR Wire** is 6.19 MB inline key+query upload plus \(\lceil M/4096\rceil\times 3.54\) MB BFV responses (zero persistent server keys).

<sup>†</sup> Matches the first SIFT-1M operating point (_M_=380,100) of  1, providing a direct cross-pipeline consistency check.

