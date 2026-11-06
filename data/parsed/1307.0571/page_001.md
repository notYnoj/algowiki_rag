# Efficient Sequential and Parallel Algorithms for Planted Motif Search

**Abstract.** Motif searching is an important step in the detection of rare events occurring in a set of DNA or protein sequences. One formulation of the problem is known as (_l,d_)-motif search or Planted Motif Search (PMS). In PMS we are given two integers _l_ and _d_ and _n_ biological sequences. We want to find all sequences of length _l_ that appear in each of the input sequences with at most _d_ mismatches. The PMS problem is NP- complete. PMS algorithms are typically evaluated on certain instances considered challenging. This paper presents an exact parallel PMS algorithm called PMS8. PMS8 is the first algorithm to solve the challenging (_l,d_) instances (25,10) and (26,11). PMS8 is also efficient on instances with larger _l_ and _d_ such as (50,21). This paper also introduces necessary and sufficient conditions for 3 _l_-mers to have a common _d_-neighbor.

**Keywords:** Planted Motif Search, PMS, Parallel Algorithms, MPI

## 1 Introduction

This paper presents an efficient exact parallel algorithm for the Planted Motif Search (PMS) problem also known as the (_l,d_) motif problem [11]. A string of length _l_ is caller an _l_-mer. The number of positions where two _l_-mers _u_ and _v_ differ is called their Hamming distance and is denoted by _Hd(u,v_). For any string _T_, _T[i..j_] is the substring of _T_ starting at position _i_ and ending at position _j_. The PMS problem is the following. Given _n_ sequences _S_<sub>1</sub>_,S_<sub>2</sub>_,...,S<sub>n</sub>_ of length _m_ each, from an alphabet \(\Sigma\) and two integers _l_ and _d_, identify all _l_-mers \(M,M\in\Sigma^l\), that occur in at least one location in each of the _n_ sequences with a Hamming distance of at most _d_. More formally, _M_ is a motif if and only if \(\forall i,1\le i\le n,\exists j_i,1\le j_i\le m-l+1\), such that \(Hd(M,S_i[j_i..j_i+m-1])\le d\).

The PMS problem is essentially the same as the Closest Substring problem. These problems have applications in PCR primer design, genetic probe design, discovering potential drug targets, antisense drug design, finding unbiased consensus of a protein family, creating diagnostic probes and motif finding (see e.g., [10]). Therefore, efficient algorithms for solving the PMS problem are very important in biology and bioinformatics.

A PMS algorithm that finds all the motifs for a given input is called an exact algorithm. All known exact algorithms have an exponential worst case runtime because the PMS problem is NP-complete [10]. An exact algorithm can be built using two approaches. One is sample driven: for all (_m-l_+1)_<sup>n</sup>_ possible combinations of _l_-mers coming from different strings, generate the common

Marius Nicolae and Sanguthevar Rajasekaran

Dept. of Computer Science and Engineering, Univ. of Connecticut, Storrs, CT, USA `{marius.nicolae,rajasek}@engr.uconn.edu`

