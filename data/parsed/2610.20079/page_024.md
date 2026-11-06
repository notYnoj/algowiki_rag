Each level processes \(\Theta(h)\) bits, and integer width is _O_(log_N_), so the depth is _O_(log_N/h_). For \(N\ge M^2\), we have \(p\ge h\) and \(logN\le 2p\). Multiplying the per-level cost by the depth and using \(a\le h\) proves the claimed bound.

Execute depth first, storing each pending bucket’s start, length, and bit-group position on a disk task stack in a constant number of words. Append sorted buckets to the final output stream. Memory holds only the active task and buffers. The recursion depth is _O_(log_N_), and temporary disk space is polynomial. Finally apply Corollary A.3.

## 8.3 An Alternative Using Individual Record Accesses

The following algorithm does not use the coding construction. We use it when _M_ is below the fixed memory threshold.

**Lemma 8.3** (A linear number of individual record accesses)**.** For every \(M\ge 2B\), an array of _N_ integers of \(w=\Theta(logN)\) bits can be sorted in _O(N_) block transfers, using at most _M_ words of memory and polynomial disk space.

_Proof._ Use least-significant-digit radix sorting: process bit groups from the lowest to the highest, preserving the order of records with equal current-group values in each pass. On disk, handle \(\lfloor logN\rfloor\) bits per pass, so only a constant number of passes is needed. A pass initializes \(\Theta(N)\) counters, counts bit-group values record by record, and scans the counters to compute bucket starting positions. It then reads records in input order, writes each to the next free position of its bucket, and updates that position pointer. Equal values are written in read order, preserving the order established by earlier low-order groups. Each record accesses a constant number of disk locations, for _O(N_) transfers per pass.

Random writes use read-modify-write with one physical block buffer; the remaining memory holds the current record and control state. If _M_ is a bounded number of words, storing a constant number of state words on disk adds only a constant number of transfers per record. The counters, temporary arrays, and addresses satisfy the required space bounds.

## 8.4 Proof of the Main Sorting Theorem

Combining the preceding algorithms according to input size proves Theorem 3.1.

_Proof of Theorem 3.1._ Keep _a_=log(_M/B_), _h_=log_M_, _p_=log(_N/M_), and \(\tau=1-\varepsilon\). If the input fits in memory, reading, sorting, and writing it takes _O(N/B_) block transfers. For \(M\le N\le M^2\), Lemma 7.2 gives local sorting. Its constant startup cost is absorbed by \(N/B\ge 2\), and \(logN\ge h\) gives

\(1+(h/a)^\tau=1+\frac{h}{a^\tau h^\varepsilon}\le 1+\frac{logN}{a^\tau h^\varepsilon}.\)

For \(N\ge M^2\), Proposition 8.2 gives cost factor \(1+p/(a^\tau h^\varepsilon)\), which also satisfies (2) because \(p\le logN\).

All these algorithms are deterministic, correct on every input, and satisfy the memory and polynomial disk-space requirements. Corollary A.3 covers every memory-to-block-size ratio. If _M_ is below the fixed threshold, then _B_ is bounded, and the _O(N_) cost in Lemma 8.3 is also _O(N/B_). Taking the fixed constant \(\varepsilon=1.5\times 10^{-5}>0\) proves the theorem.

