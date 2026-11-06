# A Faster Subquadratic Algorithm for the Longest Common Increasing Subsequence Problem

Anadi Agrawal and Paweł Gawrychowski

Institute of Computer Science, University of Wrocław, Poland

**Abstract**

The Longest Common Increasing Subsequence (LCIS) is a variant of the classical Longest Common Subsequence (LCS), in which we additionally require the common subsequence to be strictly increasing. While the well-known "Four Russians " technique can be used to find LCS in subquadratic time, it does not seem applicable to LCIS. Recently, Duraj [STACS 2020] used a completely different method based on the combinatorial properties of LCIS to design an O(_n_<sup>2</sup>(loglog_n_)<sup>2</sup>/log<sup>1/6</sup>_n_) time algorithm. We show that an approach based on exploiting tabulation can be used to construct an asymptotically faster \(\mathcal{O}(n^2loglogn/\sqrt{logn})\) time algorithm. As our solution avoids using the specific combinatorial properties of LCIS, it can be also adapted for the Longest Common Weakly Increasing Subsequence (LCWIS).

### 1 Introduction

In the well-known Longest Common Subsequence problem we aim to find the length of the longest subsequence common to two strings _A_[1_..n_] and _B_[1_..n_]. A textbook exercise is to find it in O(_n_<sup>2</sup>) time [10], and using the so-called "Four Russians" technique this has been brought down to O(_n_<sup>2</sup>/log<sup>2</sup>_n_) for constant alphabets [10] and O(_n_<sup>2</sup>loglog_n/_log<sup>2</sup>_n_) for general alphabets [3]. Recently, there was some progress in providing explanation for why a strongly subquadratic \(\mathcal{O}(n^{2-\epsilon})\) time algorithm is unlikely [1,4], and in fact even achieving \(\mathcal{O}(n^2/log^{7+\epsilon} n)\) would have some exciting unexpected consequences [2]. In this paper we consider a related problem defined as follows:

**Problem:** Longest Common Increasing Subsequence (LCIS)

**Input:** integer sequences _A_[1_..n_] and _B_[1_..n_]

**Output:** largest \(\ell\) such that there exist indices \(i_1<\dots<i_\ell\) and \(j_1<\dots<j_\ell\) with the property that (i) _A[i<sub>k</sub>_]=_B[j<sub>k</sub>_], for every \(k=1,\dots,\ell\), and (ii) \(A[i_1]<\dots<A[i_\ell]\).

While this is less obvious than for LCS, LCIS can be also solved in O(_n_<sup>2</sup>) time [11] (and in linear space [9]), and it can be proved that a strongly subquadratic algorithm would refute SETH [6] (although faster algorithms are known for some special cases [7]). However, as opposed to LCS, the usual "Four Russians" approach, that roughly consists in partitioning the DP table into blocks of size \(logn ×logn\), doesn’t seem directly applicable to LCIS. Very recently, Duraj [5] used a completely different approach based on some nice combinatorial properties specific to LCIS to design a subquadratic O(_n_<sup>2</sup>(loglog_n_)<sup>2</sup>/log<sup>1/6</sup>_n_) time algorithm.

