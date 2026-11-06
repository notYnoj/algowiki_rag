A string _Q_ is said to be a _common CT-subsequence_ of two strings _S_ and _T_ if _Q_ is a CT-subsequence of both _S_ and _T_. A string _Q_ is said to be a _longest common CT- subsequence_ (_CT-LCS_) of _S_ and _T_ if there are no common CT-subsequences of _S_ and _T_ longer than _Q_. We show an example of CT-LCS in Fig. 3. The length of CT-LCS of strings _S_ and _T_ is denoted by ct\_lcs(_S,T_).

Our second problem is the following:

_Problem 2_ (Longest common CT-subsequence problem (CT-LCS)) Given two strings _S_ and _T_, compute ct\_lcs(_S,T_).

## 2.3 Hardness assumptions

Let us consider the well-known _k-SAT problem_: Given a propositional logic formula of conjunctive normal form (CNF) which has _n_ variables and at most _k_ literals in each clause, determine whether there exists an interpretation that satisfies the input formula. Impagliazzo and Paturi \[20\] introduces the Strong Exponential Time Hypothesis (SETH), which states that there is no algorithm that solves _k_-SAT inherently faster than exhaustive search.

1
2
3
4
5
6
7
8
T
4
3
6
9
3
13
7
2
2
CT(P)
1
4
3
5
1
2
3
4
5
P
7
5
10
6
12

1
2
3
4
5
6
7
8
1
2
3
4
5
6
7
8
S
12
5
2
14
3
9
4
11
T
3
2
5
9
7
12
8
1
2
2
CT(Q)
CT(Q)
1
4
1
4
3
5
3
5

**Fig. 2** \(P=\langle 7,5,10,6,12\rangle\) is a CT-subsequence of \(T=\langle 4,3,6,9,6,13,7,2\rangle\). Each node in CT(_P_) is labeled by the corresponding position in _P_.

**Fig. 3** \(Q=\langle 5,2,14,3,11\rangle\) is a longest common CT-subsequence of \(S=\langle 12,5,2,14,3,9,4,11\rangle\) and \(T=\langle 3,2,5,9,7,12,8,1\rangle\). Each node in CT(_Q_) is labeled by the corresponding position in _Q_.

