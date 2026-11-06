# Improved Approximation for Longest Common Subsequence over Small Alphabets

**Abstract**

This paper investigates the approximability of the Longest Common Subsequence (LCS) problem. The fastest algorithm for solving the LCS problem exactly runs in essentially quadratic time in the length of the input, and it is known that under the Strong Exponential Time Hypothesis the quadratic running time cannot be beaten. There are no such limitations for the approximate computation of the LCS however, except in some limited scenarios. There is also a scarcity of approximation algorithms. When the two given strings are over an alphabet of size _k_, returning the subsequence formed by the most frequent symbol occurring in both strings achieves a 1_/k_ approximation for the LCS. It is an open problem whether a better than 1_/k_ approximation can be achieved in truly subquadratic time (\(O(n^{2-\delta})\) time for constant \(\delta>0\)).

A recent result [Rubinstein and Song SODA’2020] showed that a \(1/2+\epsilon\) approximation for the LCS over a binary alphabet is possible in truly subquadratic time, provided the input strings have the same length. In this paper we show that if a \(1/2+\epsilon\) approximation (for \(\epsilon>0\)) is achievable for binary LCS in truly subquadratic time when the input strings can be unequal, then for every constant _k_, there is a truly subquadratic time algorithm that achieves a \(1/k+\delta\) approximation for _k_-ary alphabet LCS for some \(\delta>0\). Thus the binary case is the hardest. We also show that for every constant _k_, if one is given two strings of _equal_ length over a _k_-ary alphabet, one can obtain a \(1/k+\epsilon\) approximation for some constant \(\epsilon>0\) in truly subquadratic time, thus extending the Rubinstein and Song result to all alphabets of constant size.

**2012 ACM Subject Classification Theory of computation** \(\rightarrow\) Design and analysis of algorithms

**Keywords and phrases** approximation algorithms, longest common subsequence, subquadratic

**Digital Object Identifier** 10.4230/LIPIcs.CVIT.2016.23

**Category** Track A: Algorithms, Complexity and Games

**Funding** _Shyan Akmal:_ Supported by NSF Grant CCF-1909429.

_Virginia Vassilevska Williams:_ Supported by an NSF CAREER Award, NSF Grant CCF-1909429, a BSF Grant BSF:2012338, a Google Research Fellowship and a Sloan Research Fellowship.

**Acknowledgements** We thank Jenny Kaufmann for suggesting several helpful revisions.

### 1 Introduction

In a large variety of applications, from spell-checkers to DNA sequence alignment, one seeks to compute how similar two given sequences of letters are. Arguably the most popular measures of sequence similarity are the _longest common subsequence (LCS)_ and the _edit distance_. The LCS of two given sequences _A_ and _B_ (as the name suggests) measures the maximum length of a sequence whose symbols appear in both _A_ and _B_ in the same order. The edit distance, on the other hand, measures how far apart two strings are by counting the minimum number of insertions, deletions and substitutions of characters that must be performed on one string to transform it into the other. These two measures are related: the complement of the LCS is the version of edit distance in which one minimizes only the

Shyan Akmal

MIT EECS and CSAIL, USA

**Virginia Vassilevska Williams** \(\unknown\) MIT EECS and CSAIL, USA

