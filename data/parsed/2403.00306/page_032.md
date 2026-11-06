## 2.5.3 Consensus String

To further summarize the profile matrix, we can form a consensus string from the most popular element in each column of the alignment matrix. It is the nucleotide with the largest entry in the profile matrix. Figure 2.17 shows the alignment matrix for s = (8,19,3,5,31,27,15), the corresponding profile matrix, and the resulting consensus string ATGCAACT.

## 2.5.4 Evaluating Motifs

By varying the starting positions in _s_, we can construct a large number of different profile matrices from a given sample. Some profiles represent high conservation of a pattern while others represent no conservation at all. An imprecise formulation of the Motif Finding problem is to find the starting positions _s_ corresponding to the most conserved profile.

### Scoring Function

If _P(s_) denotes the profile matrix corresponding to starting positions s, then we will use _MP(s_)(_j_) to denote the largest count in column _j_ of _P(s_). For the profile P(s) in Figure 2.17, _MP(s_)(1)=5_,MP(s_)(2)=5 , and _MP(s_)(8)=6. Given starting positions s, the consensus score is defined to be \(Score(s,DNA)=\sum_{j=1}^lMP(s)(j)\). In our case, _Score(s,DNA_)=5+5+6+4+5+5+6+6=42. _Score(s,DNA_) can be used to measure the strength of a profile corresponding to the starting positions _s_.

## 2.5.5 Defining The Motif Finding Problem

the Motif Finding problem can be formulated as selecting starting positions _s_ from the sample that maximize _Score(s,DNA_).

**Motif Finding Problem:**

_Given a set of DNA sequences, find a set of l-mers, one from each sequence, that maximizes the consensus score._

**Input:** A \(t\times n\) matrix of DNA, and l, the length of the pattern to find.

**Output:** An array of t starting positions _s_=(_s_<sub>1</sub>_,s_<sub>2</sub>_,...,s<sub>t</sub>_) maximizing _Score(s, DNA)._

