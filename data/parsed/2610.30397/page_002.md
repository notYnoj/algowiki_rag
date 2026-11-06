the currently activated row. When a row is opened by an _ACTIVATE_ command, the entire row is copied into the row buffer, and subsequent _READ_ or _WRITE_ operations access data from this buffered row at column granularity. Accessing a different row in the same bank requires closing the current row with _PRECHARGE_ command and activating the new row [7]. This organization creates a timing side channel. If two addresses map to the same bank but different rows, repeatedly accessing them sequentially causes row-buffer conflicts, since each access must evict the previously opened row and reopen the other one, leading to higher latency [8]. In contrast, accesses to different banks do not have any conflicts due to bank parallelism. By measuring these latency differences, same bank address pairs can be distinguished from different bank address pairs, which forms the basis of many DRAM address mapping reverse engineering techniques [8], [11].

LPDDR5 complicates this problem further because it supports multiple bank modes, including BG mode, 8B mode, and 16B mode [1]. As a result, even knowing a part number of the DRAM chip does not necessarily reveal the number of banks in a target system. However, many prior works [5], [8], [11] need the number of banks as input. Consequently, these methods are less suitable for modern LPDDR5 systems and DRAM-agnostic approaches are needed.

### B. DRAM Addressing

The memory controller implements a set of DRAM address mapping functions that map a physical address to a DRAM tuple, e.g., channel, rank, bank group, bank, row, and column. Prior work has shown that many of these functions can be modeled as linear functions over GF(2), i.e., XOR combinations of physical address bits [8], [9]. Under this view, each output bit of an addressing function is represented by a binary bank mask over physical address bits. Evaluating the bank mask on an address means XORing the selected bits. In this paper, we use the term _bank mask_ to denote one such XOR- based function component.

Traditional software-based reverse engineering often recovers DRAM address mapping functions by exhaustive search. DRAMA, and many subsequent methods derived from the same general idea, measure row-buffer conflicts and then enumerate candidate XOR functions to find the set that best explains the observed conflict relation [3], [5], [6], [8], [11]. This approach can work well, but the search space grows rapidly with the number of candidate bits and independent mapping functions. It also tends to require platform-specific knowledge to remain tractable on modern systems [9], [11].

Knock-Knock replaces this exhaustive-search paradigm with a linear-algebraic formulation [9]. Its key idea is that if two physical addresses map to the same bank, then every addressing function must have the same output on both addresses. Let _a_ and _b_ be two same-bank addresses, and let \(\Delta=a\oplus b\). Equivalently, \(a\oplus b\oplus\Delta=0\). Since each bank mask _m_ is modeled as a linear parity function over GF(2), the equality<tbc>

<tbc>of bank outputs implies

Therefore, for any valid bank mask _m_, we obtain \(m\cdot\Delta=0(mod2)\), where the dot product is taken over GF(2). Thus, every empirically identified same bank pair induces one homogeneous linear constraint on the unknown bank masks. By stacking many such constraints into a difference matrix _D_, the valid bank masks must lie in the nullspace of _D_ over GF(2): \(D\cdot m^T=0\). Instead of enumerating all candidate functions, Knock-Knock therefore computes a basis of this nullspace and interprets it as the recovered bank mask basis.

Using this approach, the problem is no longer an exponential search over all XOR combinations, but a polynomial-time linear algebra on constraints extracted from timing measurements. In addition, the method is black-box and platform- agnostic.

## III. METHODS

Our approach has two steps. The first step, **Latency measurement**, allocates a fraction of the whole memory and repeatedly measures the latency of sequentially accessing two randomly selected addresses, thereby collecting a large number of latency samples. The second step, **Threshold sweep**, iterates a possible range of latencies and performs same-bank pairs extraction, bank mask computation, group verification and single function verification.

The details of **Threshold sweep** are described below.

• **Histogram generation**: A histogram of all measured latencies and a list of possible thresholds is generated.

• **Same-bank pairs extraction**: Our approach iterates a range of possible thresholds and for each threshold, same- bank pairs are extracted based on it. If a pair of addresses reside in different rows in the same bank, the latency of accessing them sequentially is higher than the latency of accessing other types of address pairs. As a result, those address pairs with higher latencies than the threshold will be considered to be same bank pairs.

• **Bank mask computation**: Same-bank pairs are used by the Knock-Knock algorithm [9] to compute the bank masks. Same-bank pairs are randomly sampled from the candidate set. For each sampled pair, the XOR of the two addresses is computed, and the resulting XOR vectors are stacked row by row to form a difference matrix. Then, the nullspace of the difference matrix is computed, and Gaussian elimination over GF(2) is applied to the resulting nullspace basis vectors to obtain their reduced row echelon form (RREF). The resulting RREF basis gives the final bank masks.

• **Group verification** and **Single function verification**: Our approach verifies the bank masks based on the algorithm proposed in [2]. Verification is needed because the recovered bank masks are inferred results, and whether they are consistent with the observed latency behavior

m(a) = m(b)
(mod 2)
(mod 2)
where the dot product is taken over GF(2). Thus,
every empirically identified same bank pair induces one homogeneous linear constraint on the unknown bank masks. By stacking many such constraints into a difference matrix D,
valid bank masks must lie in the nullspace of D over GF(2):
D . mT = 0. Instead of enumerating all candidate functions, Knock-Knock therefore computes a basis of this nullspace and interprets it as the recovered bank mask basis.
Using this approach, the problem is no longer an exponential search over all XOR combinations, but a polynomial-time linear algebra on constraints extracted from timing measurements. In addition, the method is black-box and platform- agnostic.
Our approach has two steps. The first step, Latency measurement, allocates a fraction of the whole memory and repeatedly measures the latency of sequentially accessing two randomly selected addresses, thereby collecting a large number of latency samples. The second step, Threshold sweep, iterates a possible range of latencies and performs same-bank pairs extraction, bank mask computation, group verification and single function verification.
The details of Threshold sweep are described below.
Histogram generation: A histogram of all measured latencies and a list of possible thresholds is generated.
Same-bank pairs extraction: Our approach iterates a range of possible thresholds and for each threshold, same-bank pairs are extracted based on it. If a pair of addresses reside in different rows in the same bank, the latency of accessing them sequentially is higher than the latency of accessing other types of address pairs. As a result, those address pairs with higher latencies than the threshold will be considered to be same bank pairs.
Bank mask computation: Same-bank pairs are used by the Knock-Knock algorithm [9] to compute the bank masks. Same-bank pairs are randomly sampled from the candidate set. For each sampled pair, the XOR of the two addresses is computed, and the resulting XOR vectors are stacked row by row to form a difference matrix. Then, the nullspace of the difference matrix is computed, and Gaussian elimination over GF(2) is applied to the resulting nullspace basis vectors to obtain their reduced row echelon form (RREF). The resulting RREF basis gives the final bank masks.
Group verification and Single function verification: Our approach verifies the bank masks based on the algorithm proposed in [2]. Verification is needed because the recovered bank masks are inferred results, and whether they are consistent with the observed latency behavior

