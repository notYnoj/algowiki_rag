<tbc>prefetches, so one early snapshot cannot consume the entire overlap window. To reduce I/O requests, a page-aware planner maps selected document IDs to content extents and coalesces nearby extents into page-aligned read windows. In ConStore this planner is GCF (§5.4); over an insertion-order payload file, where co-retrieved documents rarely share pages, it degenerates to one aligned window per document. The worker records scheduled documents and windows so later prefetches and the residual fetch do not repeat the same work.

The foreground search is unchanged and continues to its natural completion. It does not observe prefetch decisions, so it returns the same final top-_K_ as a non-instrumented run. After search returns, SICP computes the residual demand: final top-_K_ documents that are not already covered by prefetch. This residual fetch can run while the prefetch worker finishes outstanding work, and it avoids documents already scheduled by prefetch so the same content is not fetched twice. If speculation misses, the remaining final documents are fetched normally. Figure 6 walks through these steps for one query.

**Bounded I/O overhead.** SICP bounds speculative work at three levels: the number of prefetches, the maximum documents admitted per prefetch, and the per-prefetch I/O budget. It also tracks what previous prefetches have already selected, so a candidate that remains near the head of the queue is not planned repeatedly. The extra I/O beyond the sequential baseline is limited to windows for speculative candidates that do not survive into the final top-_K_; final documents that were not prefetched are still served by the residual path.

For one prefetch, the ideal wall-clock saving is bounded by min(_T_prefetch\_io, _T_search\_tail), where _search\_tail_ is the remaining vector-search time after the prefetch is issued and _prefetch\_io_ is the worker’s content-I/O time for that prefetch. With multiple prefetches, the same accounting applies repeatedly: content I/O completed before the search returns is removed from the foreground fetch path, while any worker wait or residual fetch remains visible.

## 4.2 Prefetching Strategy

The strategy answers two questions continuously throughout the search: _when_ should the next prefetch start, and _what_ additional content should it fetch? A simple all-or-nothing trigger - fire once and prefetch the whole current top-\(K'\) - is brittle. It overcommits when the remaining search tail is short, and it cannot react when later callbacks promote new documents into the head of the queue. SICP instead treats the search tail as a series of small budgets. Each prefetch spends only a bounded amount of I/O, deduplicates against previous prefetches, and leaves all misses to the residual fetch. The strategy has three components.

**(1) Progress and stability checks - when to fire.** These checks reduce wasted reads from early candidate churn while retaining time to overlap useful I/O. At every progress callback, the prefetch worker considers issuing a prefetch only if the callback is new and the per-query prefetch cap has not been reached. The first check is progress: DiskANN must have completed enough hops, and SPANN must have processed enough SSD posting-list entries. The second check is candidate stability. SICP compares the ranked top-\(K'\) document set against the previous check using set-overlap similarity. After the head remains stable for a configured number of checks, the worker may fire. A late-progress threshold prevents pathological waiting when the search tail is almost gone. Later prefetches reuse the same checks but also require a minimum number of newly promoted documents, so SICP does not issue a prefetch for a tiny or duplicate delta.

**(2) Budgeted page-aware prefetch - what to fetch.** Budgeting limits speculative device pressure, while coalescing reduces the requests needed to fetch selected candidates. When prefetching, the prefetch worker ranks the current candidate snapshot and forms a bounded pool: at most \(K\cdot\alpha\) documents, further capped by a per-prefetch maximum. Documents already selected by earlier prefetches are excluded. The remaining candidates are passed to a budgeted selector, which chooses a prefix under the prefetch I/O budget. The page-aware planner (GCF in ConStore, §5.4) then translates<tbc>

DiskANN
SPANN
Search Phase
# P1
# P2
# Pn
Content Fetch
Sequential
Speculative Inline Content Prefetch
Candidate Snapshot
Prefetched Docs
Search Thread
Residual
Time saved
Stability Monitor
Prefetch Worker
$3.4 Group Content Fetch
Trigger Decision
Prefetch Plan
Ranked Candidates
Candidate Ranker
Budgeted Selector

Search thread
p1
p2
p3
p4
a
a
a
a
Prefetched
Candidate snapshot
b
b
b
b
b
Residual fetch
C
C
C
e
e
Candidate
d
d
C
C
C
4 KB page
X
X
d
f
Stability
.67
11.0
Final
Prefetch worker
W1:
W2:
3
abcd
e
2
Content Reads
abcd
4
e
1
Stability gate
2
Rank + dedup
3
Budgeted select
4
Page-aware plan

**Figure 5.** Speculative Inline Content Prefetch (SICP) timeline.

**Figure 6.** SICP example for one query.

