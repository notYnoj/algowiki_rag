## 6.2 End-to-End Retrieval Latency

Figures 8 and 9 show that most savings come from reducing or overlapping foreground content fetch, while search time changes little. The callback only publishes candidate snapshots; stability checks and page selection run on the background worker, limiting search-side overhead.

Seq\_RPAG isolates the layout benefit: relative to Seq\_ KMeans, it reduces latency by up to 18% on DiskANN and 9% on SPANN, although a few SPANN settings regress by up to 2%. The DiskANN benefit peaks near the largest trained prefix and declines beyond it. This is consistent with RPAG concentrating locality on the co-retrieval patterns represented in its training objective, rather than embedding proximity alone.

ConStore adds SICP to hide part of the remaining fetch behind search. Across per-dataset settings, it reduces end- to-end latency over the best per-document-read baseline by 4-48% on DiskANN and up to 25% on SPANN. Benefits generally grow with _K_ as more content I/O becomes available to overlap; small-_K_ SPANN cases show little benefit. The SICP-only ablation confirms that prefetching benefits even the Random layout. On DiskANN, layout alone is faster at smaller _K_, while prefetch alone becomes more effective at large _K_. Combining both gives the lowest geometric-mean latency at every evaluated _K_ on both engines: grouping reduces the work, and speculation hides part of what remains.

## 6.3 Prefetch Precision and Coverage

We evaluate SICP’s prefetch quality on the RPAG layout used by ConStore in Figures 8 and 9.

Figure 10 shows that many selected candidates survive into the final results: precision is 62.6-98.3% for DiskANN and 70.4-99.9% for SPANN. Both cover over 99% of results at _K_=160.

## 6.4 Scalability

Figure 11 compares ConStore with Seq\_KMeans and Seq\_ RPAG as concurrency grows from one to 32 queries. ConStore retains the lowest latency on both engines. Its single<tbc>

<tbc>search thread per query only publishes snapshots; the worker overlaps bounded content reads with search. RPAG and GCF reduce the content-I/O demand that would otherwise compete with concurrent searches.

Figure 12 compares ConStore with Post-Parallel-Fetch, which parallelizes content reads only after search. Under a 100ms total-P99 SLO and a 95% achieved/offered-QPS gate, ConStore increases sustainable offered QPS by 20% on DiskANN and 12.5% on SPANN. At the baselines’ highest sustainable rates , P99 latency is lower by factors of 1.46\(\times\) and 2.90\(\times\).

Both engines therefore sustain higher load before saturation: bounded search-fetch overlap reduces exposed fetch time without enough added contention to erase the benefit.

Device statistics show that this improvement does not require more read bandwidth (Figure 13). At those same<tbc>

DiskANN
SPANN
Precision (%)
Coverage (%)
100
100
50
50
0
0
10
20
40
80
160
160
10
20
40
80
160
160
Top-K per hop
Top-K per hop
(a) Precision
(b) Coverage

Constore
Seq_RPAG
Seq_KMeans
60
24
40
16
Latency(ms)
Latency(ms)
20
8
0
0
1
2
4
8
16
32
1
2
4
8
16
32
Concurrency T
Concurrency T
(a) SPANN
(b) DiskANN

Post-Parallel-Fetch
ConStore
300
300
200
200
Latency(ms)
Latency(ms)
100
100
0
0
1600
2000
2400
2800
1200
1400
1600
1800
2000
QPS
QPS
(a) DiskANN
(b) SPANN

Post-Parallel-Fetch
ConStore
2000
2000
1500
Read(MB/s)
Read(MB/s)
1500
1600
2000
2400
2800
1200
1400
1600
1800
2000
QPS
QPS
(a) DiskANN
(b) SPANN

**Figure 10.** Prefetch precision and final-K coverage

**Figure 11.** End-to-end latency as query concurrency increases.

**Figure 12.** Latency vs. offered QPS

**Figure 13.** Device read bandwidth vs. offered QPS

