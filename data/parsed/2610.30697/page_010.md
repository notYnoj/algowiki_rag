vice memory thus scales with _m_ rather than _D_ for wide embeddings, admitting large datasets like Deep-100M and DataComp onto a single GPU.

### 4.8 Parameter Sensitivity

Figure 12 evaluates the two parameters of LyCHE, the lifted width _m_ and the number of lists, which test how tight the certified bound must be and how the partition trades list size against fineness. The left panel plots the throughput at 200 probed lists against _m_. On ImageNet DINOv2, the throughput grows from 2,542 queries per second at _m_=127 to 11,015 at _m_=255 and 219,325 at _m_=507, because the verified vectors per query fall from 90,008 to 18,438 and 151. Deep-10M and SIFT1M follow the same trend up to 382,500 and 516,305 queries per second at their widest rows. GIST1M peaks at _m_=507 (130,112 QPS), where _m_=763 costs more than it saves. Wider rows pay off until the verified vectors approach the 32 of the first verification round.

The right panel plots recall against throughput for 256, 1,024, and 4,096 lists on ImageNet DINOv2 at the same shares of probed lists. With 20% of the lists probed, LyCHEe serves 199,023, 215,598, and 96,728 queries per second at recall 0.9982, 0.9990, and 0.9997. Fewer and larger lists fill more of each tensor-core tile, because more queries of a batch probe the same list, whereas more lists raise the recall at a given share. The default of 1,024 lists for a million vectors balances both effects, with throughput varying by \(<2.3\times\) across a 16-fold list range.

### 4.9 Ablation Study

3 isolates the two key components of LyCHEe, namely the list-local anchor threshold (Section 3.3) and the ordered bound verification (Algorithm 1). The global variant spreads the same budget of _b_=1,024 anchors evenly over the whole dataset, as CertEx does. Such a threshold does not guarantee \(U(\mathbf{q})\ge r_k(\mathbf{q})\) (Section 3.3), although its anchors lie mostly far from the query and make it much looser in practice than the _k_-th distance within the probed lists. Recall therefore stays at or above 0.999, whereas the survivors per query grow by 75.6\(\times\), 47.3\(\times\), and 256.8\(\times\) on ImageNet DINOv2, SIFT1M, and BIGANN-10M. The throughput drops accordingly by 18.8\(\times\), 2.0\(\times\), and 7.5\(\times\).

Without the ordered verification, every survivor is verified at full precision. The full-vector reads then grow by 16.0\(\times\), 6.5\(\times\), and 10.0\(\times\) on the same datasets, so that the throughput drops by 6.4\(\times\) (from 223,688 to 34,812 QPS on ImageNet DINOv2), 2.7\(\times\), and 3.4\(\times\). Both components are therefore necessary, since the threshold bounds the survivors, whereas the ordered verification bounds their full- precision reads.

## 5 Conclusion

High-recall search on inverted files spends its memory traffic on full-precision scans of the probed lists, while graph indexes saturate below the high-recall targets. LyCHEe bounds the _k_-th distance within the probed lists from their own anchors, screens the probed vectors on tensor cores with certified lower bounds, and verifies the few survivors in increasing order of their bounds, which returns exactly the answer of IVF-Flat on the same lists. On eleven datasets of up to one billion vectors and against ten GPU and CPU baselines, LyCHEe is up to 185\(\times\) faster than IVF-Flat at equal recall.

## References

\begin{tabular}{ccccc}
Dataset & Variant & Survivors & Verified & QPS \\
\multirow{3}{*}{DINOv2} & LYCHE (default) & **2,410** & **151** & **223,688** \\
 & w/ global threshold & 182,207 & 151 & 11,913 \\
 & w/o ordered verif. & 2,410 & 2,410 & 34,812 \\
\multirow{3}{*}{SIFT1M} & LYCHE (default) & **208** & **32** & **575,043** \\
 & w/ global threshold & 9,841 & 32 & 289,306 \\
 & w/o ordered verif. & 208 & 208 & 214,500 \\
\multirow{3}{*}{BIGANN-10M} & LYCHE (default) & **319** & **32** & **371,279** \\
 & w/ global threshold & 81,930 & 32 & 49,235 \\
 & w/o ordered verif. & 319 & 319 & 108,300 \\
\end{tabular}

DINOv2 GIST1M SIFT1M Deep-10M 256 lists 1024 lists 4096 lists Width, 200 probed lists Lists, DINOv2 300k 100k 200k Queries per second 10k 100k 25 27 29 .99 .999 .9999 Lifted width m Recall at 10

Figure 12: Parameter sensitivity to lifted width and lists.

3: Ablation of key components (_n<sub>p</sub>_=200).

