# Panache: One-Pass Motif Discovery at Every Window Length

### Abstract

Motif discovery, the search for recurring patterns within a time series, is a core primitive of exploratory data analysis. A pattern, however, is defined by its duration, which analysts rarely know in advance. To resolve this unknown duration, an interval of window lengths is defined, and the accepted method is to try every length in that interval. Existing pan matrix profile (PMP) methods compute one z-normalized matrix profile per length, so _L_ lengths cost _L_ quadratic self-joins over the same series. We introduce Panache, to our knowledge the first one-pass streaming algorithm for z-normalized PMP motif discovery. It replaces the repeated self-joins with a single scan whose runtime is near-linear in the series length. The key observation is that mean-centering a subsequence changes only its DC Fourier coefficient, so the non-DC spectrum of every z-normalized subsequence can be maintained online by sliding-DFT recurrences and running statistics. This spectral state is the key under which similar subsequences collide in an occupancy-controlled hash directory and, through Parseval’s theorem, yields a lower bound that rejects most colliding pairs before any exact computation. Panache computes every data-dependent parameter itself, leaving only a resource budget to tune. At the default budget, it recovers all top-20 pan-motifs against exact fixed-exclusion ground truth on 17 UCR configurations, and is faster than every CPU and GPU baseline benchmarked in this paper. On Wafer at five million samples over 51 lengths, Panache completes one pass in 2.9 minutes and emits the exact motifs in 6.0 minutes, against 7.95 hours for the fastest exact CPU baseline and 38.3 minutes for Scamp on an H100 GPU.

### CCS Concepts

• Information systems \(\rightarrow\) Data mining; • Theory of computation \(\rightarrow\) Streaming, sublinear and near linear time algorithms.

### Keywords

time series, matrix profile, motif discovery, locality-sensitive hashing, streaming algorithms

### 1 Introduction

Time-series motif discovery looks for subsequences that recur in the same series [16, 26]. The difficulty is that a motif is not defined until a duration is chosen. A window length _m_ represents a duration. It determines which subsequences are compared and what it means for two occurrences to have the same shape. Too short a window fragments the event; too long a window mixes the event with its context. In exploratory data analysis, this duration is often the unknown rather than an input the analyst can set reliably.

The matrix profile [33] replaced the varying definitions of a motif with a single formulation. For a chosen window length _m_, a fixed- length algorithm starts by initializing a window and computing its z-normalized distance to all valid non-overlapping windows of<tbc>

<tbc>the same length in the entire series (Figure 1). The window that achieved the smallest of these distances is the nearest neighbor. When the same window advances by one position, distances are recomputed across the entire series again. This process is repeated from the start of the series to the end, producing a quadratic self- join, and one self-join yields one row, the matrix profile _P<sub>m</sub>_, which stores each window’s nearest-neighbor distance. Each stored entry is a cell, and motifs are the cells of _P<sub>m</sub>_ with the smallest distances rather than the outcome of a separate combinatorial search. The speed of these algorithms comes from recurrences that reuse dot products while two windows of the same length slide together. The reuse makes each evaluation cheap, but it never makes evaluations fewer. This formulation is why fixed-length motif discovery has mature exact algorithms [15, 38–40].

The pan matrix profile (PMP) [23] replaces the duration choice with an interval of lengths. It computes a matrix profile for every length and stacks each profile for every \(m\in[m_\mathrm{min},m_\mathrm{max}]\). Existing PMP algorithms achieve this generality through repetition. The computations performed at one length are never reused at another, because every length changes the set of windows, the overlap rule that rejects trivial matches, the mean and standard deviation that z-normalize every window, and the length-_m_ Fourier basis used by the FFT steps. The recurrences never cross lengths either. Every single window length forces its own rescan of the entire series, and that just by taking one slide. The cost increases with every length in the interval.

We present Panache, to our knowledge the first one-pass streaming algorithm for z-normalized PMP motif discovery. Panache scans the series once while maintaining a single multi-length search state. Each sample is consumed on arrival and advances the whole multi-length state at once. No length and no slide ever forces a rescan of the series. From this state it selects which subsequence<tbc>

compute da(i, j) for every valid start j
wj
gray: excluded starts, 11-j < excl dashed: first valid window, overlapping wj
m
advance one position, recompute across the entire series every starting position one cell per start: the smallest distance, achieved by its nearest neighbor
min
xL lengths
Pm
one quadratic self-join per length; the PMP stacks one row for every m E [mmax mmax]

Tej Sanibh Ranade <br>
tsranade1@gmail.com <br>
Independent Researcher

**Figure 1: Existing PMP representation on a sample of ECG200. Window** _w<sub>i</sub>_ **is evaluated against all windows in the series. Every slide causes the repetition. Every different window length requires the same process in the PMP.**

