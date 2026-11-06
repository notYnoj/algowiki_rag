We achieve Result (1) with the _O(nm_)-time solution in the binary case by exploiting interesting properties of CT-matching on binary strings. Result (2), which extends the quadratic conditional lower bound for episode matching [10], implies that Oizumi et al.’s _O(nm_loglog_n_)-time solution for the CT-MSeq problem [8] is optimal up to logarithmic factors, unless OVH fails. We remark that OVH is implied by the famous Strong Exponential Time Hypothesis (SETH) [11].

## 1.3 LCS under Cartesian-tree model

We then extend our research to the well-studied class of string problem, _longest common subsequences_ (_LCSs_), that is one of the most fundamental models for measuring string similarities.

It is well known that, under the exact matching model, (the length of) an LCS of two given strings _S_ and _T_ of length _n_ can be computed in _O(n_<sup>2</sup>) time and space by standard dynamic programming, or in _O(n_<sup>2</sup>/log_n_) time and space [12] by the so- called "Four-Russians" method in the word RAM [13]. These quadratic and weakly subquadratic time bounds are believed to be essentially optimal, since a strongly subquadratic \(O(n^{2-\epsilon})\)-time solution to LCS with any constant \(\epsilon>0\) refutes OVH. Indeed, while there are a number of algorithms for computing LCS whose running times are dependent on other parameters (e.g. [14-17]), their worst-case time complexities remain \(\Omega(n^2)\).

As previously stated, subsequence matching under OP-matching is NP-hard. It is thus immediate that _order-preserving longest common subsequence_ (_OP-LCS_) is also NP-hard.

These arguments pose the following natural question - Is the _CT-LCS problem_ also polynomial-time solvable? Here, the CT-LCS problem is, given two strings _S_ and _T_ of length _n_, to compute (the length) of a longest string _Q_ such that both _S_ and _T_ have subsequences that CT-match _Q_. We answer this question affirmatively, by presenting the following efficient algorithms and conditional lowerbound:

(3) an _O(n_<sup>6</sup>)-time and _O(n_<sup>4</sup>)-space CT-LCS algorithm for general ordered alphabets.<tbc>

(4) an _O(n_<sup>2</sup>/log_n_)-time and space CT-LCS algorithm for binary alphabets.<tbc>

(5) an \(O(n^{2-\epsilon})\)-time conditional lower bound on the CT-LCS problem for alphabets of size 5, for any constant \(\epsilon>0\), under OVH.

While the _O(n_<sup>6</sup>)-time solution in the general case (Result (3)) is based on the idea of _pivoted Cartesian-trees_ from Oizumi et al. [8], our _O(n_<sup>2</sup>/log_n_)-time solution for the binary case (Result (4)) is built on a completely different approach that exploits interesting properties of CT-matching on binary strings, which we also use for the CT-MSeq problem.

## 1.4 Organization

The rest of this paper is organized as follows: Section 2 gives basic notions. In Section 3, we present combinatorial properties of CT-matching on binary strings, which will play central roles for our CT-MSeq and CT-LCS algorithms presented respectively in Sections 4.1 and 5.2. In Section 4, we present _O(nm_)-time solution for the CT- Mseq problem in the case of binary alphabets and our quadratic conditional lower<tbc>

