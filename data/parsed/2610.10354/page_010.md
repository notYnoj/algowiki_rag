#### Bounded Monotone Min-Plus Convolution.

Bounded Monotone Min-Plus Convolution is a version of Min-Plus Convolution with structured inputs. A length-_n_ sequence is called bounded monotone if all entries are from \[_O(n_)\], and the sequence is monotonically nondecreasing. Chan and Lewenstein \[CL15\] were the first to study Bounded Monotone Min-Plus Convolution: they showed that when both input sequences are bounded monotone, Min-Plus Convolution can be computed in _O(n_<sup>1.859</sup>) time. This running time has been improved to \(\widetilde{O}(n^{1.5})\) by Chi, Duan, Xie and Zhang \[CDXZ22\], and Bringmann, Dürr and Polak \[BDP24\] generalized their algorithm to the case where only one of the sequences needs to be bounded monotone. Bounded-Monotone Min-Plus Convolution has found a variety of applications, including Jumbled Indexing \[CL15\] and several variants of knapsack \[BC22, BDP24, CLMZ25\]. We show that \[BDP24\]’s algorithm is conditionally optimal:

**Theorem 1.11** (Bounded Monotone Min-Plus Convolution)**.** _Min-Plus Convolution between an arbitrary sequence and a monotone sequence bounded by_ \[_n_\] _cannot be solved in time_ \(O(n^{3/2-\epsilon})\) _(for any constant_ \(\epsilon>0\)_), unless the Strong Min-Plus Convolution Hypothesis fails._

#### Min-Witness Convolution.

Given two length-_n_ Boolean sequences _A,B_, their Min-Witness Convolution _C_ is defined such as _C_\[_k_\] equals the minimum index _i_ where _A_\[_i_\] and _B_\[_k-i_\] are both true. This problem has been listed in papers studying fine-grained complexity of intermediate problems \[LPV20, CVX23\] as a natural target for proving conditional lower bound for, but there has been no nontrivial lower bound so far for this problem. We prove the first super-linear (albeit non-tight) conditional lower bound for Min-Witness Convolution:

**Theorem 1.12** (Min-Witness Convolution)**.** _Min-Witness Convolution cannot be solved in time_ \(O(n^{4/3-\epsilon})\) _(for any constant_ \(\epsilon>0\)_), unless the Strong Min-Plus Convolution Hypothesis fails._

A careful reader might have noticed that our lower bounds for intermediate sequence problems are based on the Strong Min-Plus Convolution Hypothesis, while Fischer \[Fis26\]’s lower bounds for intermediate matrix problems are based on the APSP Hypothesis itself rather than its strong variant. Without relying on Hypothesis 1.7, Fischer first reduced APSP to a version of Min-Plus Product where the universe has low-doubling (rather than simply an interval \[_u_\]), and then obtained APSP-based lower bounds for intermediate matrix problems from this first step. We also manage to prove an analogous version of the first step in Min-Plus Convolution (Lemma 5.3); unfortunately, it seems hard to obtain tight reductions for intermediate sequence problems from it. Intuitively, one reason why it is harder to design reductions to intermediate sequence problems is the following: In Fischer’s universe reduction for APSP, both the inner dimension and the universe of the Min-Plus Product are reduced, which make it easier to further reduce to intermediate matrix problems. In contrast, for sequence problems, there is no analogue of an "inner dimension", so there is less room to work with in downstream reductions.

## 1.6 Proof Ideas

In this section we give a quick high-level overview for the results we have not sketched before.

### 1.6.1 Low-Rank 3SUM in Subquadratic Time

We start with the ideas behind our subquadratic-time algorithm for low-rank 3SUM. Let (_A,B,C_) denote a given 3SUM instance, and assume that \(C\subseteq X+X\) for some small set, \(|X|\le n^{1-\epsilon}\). At<tbc>

