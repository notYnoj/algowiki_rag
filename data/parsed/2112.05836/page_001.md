# How Compression and Approximation Affect Efficiency in String Distance Measures

Arun Ganesh<sup>∗</sup>, Tomasz Kociumaka<sup>†</sup>, Andrea Lincoln<sup>†‡</sup>, and Barna Saha<sup>†</sup>

_University of California, Berkeley_

**Abstract**

Real-world data often comes in compressed form. Analyzing compressed data directly (without first decompressing it) can save space and time by orders of magnitude. In this work, we focus on fundamental sequence comparison problems and try to quantify the gain in time complexity when the underlying data is highly compressible. We consider grammar compression, which unifies many practically relevant compression schemes such as the Lempel-Ziv family, dictionary methods, and others. For two strings of total length _N_ and total compressed size _n_, it is known that the edit distance and a longest common subsequence (LCS) can be computed exactly in time \(\widetilde{o}(nN)\), as opposed to _O(N_<sup>2</sup>) for the uncompressed setting. Many real-world applications need to align multiple sequences simultaneously, and the fastest known exact algorithms for median edit distance and LCS of _k_ strings run in _O(N<sup>k</sup>_) time, whereas the one for center edit distance has a time complexity of _O(N_<sup>2_k_</sup>). This naturally raises the question if compression can help to reduce the running time significantly for \(k\ge 3\), perhaps to _O(N_<sup>k/2</sup>_n_<sup>_k/_2</sup>) or, more optimistically, to _O(Nn_<sup>_k_-1</sup>).<sup>1</sup>

Unfortunately, we show new lower bounds that rule out any improvement beyond \(\Omega(N^{k-1}n)\) time for any of these problems assuming the Strong Exponential Time Hypothesis (SETH), where again _N_ and _n_ represent the total length and the total compressed size, respectively. This answers an open question of Abboud, Backurs, Bringmann, and Künnemann (FOCS’17).

In presence of such negative results, we ask if allowing approximation can help, and we show that approximation and compression together can be surprisingly effective for both multiple and two strings.

We develop an \(\widetilde{o}(N^{k/2}n^{k/2})\)-time FPTAS for the median edit distance of _k_ sequences, leading to a saving of nearly half the dimensions for highly-compressible sequences. In comparison, no \(O(N^{k-\Omega(1)})\)-time PTAS is known for the median edit distance problem in the uncompressed setting. We obtain an improvement from \(\widetilde{o}(N^{2k})\) to \(\widetilde{o}(N^{k/2+o(k)}n^{k/2})\) for the center edit distance problem. For two strings, we get an \(\widetilde{o}(N^{2/3}n^{4/3})\)-time FPTAS for both edit distance and LCS; note that this running time is _o(N_) whenever \(n\checkmark N^{1/4}\). In contrast, for uncompressed strings, there is not even a subquadratic algorithm for LCS that has less than polynomial gap in the approximation factor. Building on the insight from our approximation algorithms, we also obtain several new and improved results for many fundamental distance measures including the edit, Hamming, and shift distances.

### 1 Introduction

With the information explosion, almost all real-world data comes in a compressed form. While compression is primarily intended to save storage space and transmission bandwidth, processing compressed data directly often provides an opportunity to reduce computation time and energy by several orders of magnitude. In this work, we focus on sequential data such as natural-language texts, biological sequences (nucleic acid sequences, including DNA, and amino acid sequences, including proteins), and computer codes. Sequential data often contains highly repetitive pattern. Modern technology (e.g., high-throughput sequencing) has led to an astonishingly rapid accumulation of such data, so much so that without proper data compression and algorithms over compressed data, it is not possible to utilize the wealth of information in them [BPS13, BDY16, PW18, GWH19, HPWO19].

<sup>∗</sup>Supported in part by an NSF 1816861 grant. <sup>†</sup>Supported in part by NSF 1652303, 1909046, and HDR TRIPODS 1934846 grants, and an Alfred P. Sloan Fellowship. <sup>‡</sup>Supported in part by a Simons NTT Research Fellowship. <sup>1</sup>In this paper, we assume that _k_ is a constant; thus, the \(O(\cdot)\) and \(\Omega(\cdot)\) notation may hide factors with exponential dependence on _k_.

