<tbc>value bound selects exactly the successors in (4). Thus all _D_ scores and successor witnesses are correct. Lemma 3.1 proves the returned result optimal.

Preprocessing has the cost stated above. Offline structure construction and the two sweeps together take \(O(Mlg_+^2M)\) time. The final scan and reconstruction take _O(M_) time. Row lists, input ranks, and match records need _O(S+M_) space; one dominance structure needs _O(M_lg<sub>+</sub>_M_) space and can be released between sweeps. The _M_=0 case returns immediately after preprocessing and satisfies the same bound. \(\sqcap\sqcup\)

### Strictness and immediate updates.

Row batching makes the index invariant explicit. Immediate updates within a row are also correct here: all matches in that row have the same value rank, and the query stops at _y(v_)-1, excluding every such update. This applies to both sweeps. It is a property of strict monotonicity; replacing the query bound by _y(v_) is incorrect even with batching, because equal- valued matches in different rows could then extend each other. For example, two identical constant sequences have LCBS length one. The supplied diagnostic implementation checks immediate and batched updates against the same independent oracle.

### When does the bound help?

The sparse bound is asymptotically smaller than the dense bound when \(Slg_+S+Mlg_+^2M=o(nm)\). The sorting term must be included, particularly for unbalanced lengths. Merely assuming \(M\checkmark nm\) is not sufficient because each match incurs a logarithmic overhead. For dense inputs the simple scan can be faster and uses less auxiliary space. Neither the theorem nor the experiments assert universal superiority over the dense baseline or over potential adaptations of faster LCIS algorithms.

## 6. A conditional worst-case barrier

The inclusion of increasing subsequences among bitonic ones does not alone reduce LCIS optimization to LCBS: a decreasing phase might improve the optimum. A fresh increasing suffix eliminates that possibility in an optimal solution.

**Lemma 6.1. (Padding identity)**<br>
Let \(Z=\langle z_1,\dots,z_K\rangle\) be strictly increasing, with all its symbols fresh and greater than every symbol occurring in _A_ or _B_. For \(K\ge 1\),

\(LCBS(A\circ Z,B\circ Z)=max\{LCBS(A,B),LCIS(A,B)+K\}.\) (5)

### Proof:

A common subsequence using no fresh symbol has length at most LCBS(_A,B_) when bitonic. A bitonic common subsequence using a fresh symbol must be purely increasing: original symbols precede all fresh symbols in both inputs, the transition to the fresh suffix is increasing, and fresh symbols appear in increasing order. A prior decrease would therefore be followed by an increase, while a later decrease is impossible. Its original part has length at most LCIS(_A,B_) and its fresh part has length at most _K_. Conversely, an original LCBS remains feasible, and appending all of _Z_ to an LCIS gives a

