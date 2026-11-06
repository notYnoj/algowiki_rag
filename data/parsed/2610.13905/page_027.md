## 5 Numerical Examples

In this section, we present a collection of numerical experiments aimed at verifying the theoretical results from the previous section. The first two explore the validity/tightness of our stability bounds (with and without alternative bases), while the third tests the effectiveness of the truncation idea discussed in Section 4.4. All experiments were done in Matlab and follow a common setup described in Section 5.1. Importantly, these experiments do not demonstrate the performance of APA matrix multiplication in a high-performance environment, which we leave to future work. Takeaways include the following:

1. Theorem 4.6 and Theorem 4.7, though not tight, effectively gauge the (relative) stability of APA routines.<tbc>

2. While alternative basis algorithms have a weaker stability bound, they perform no worse in practice.<tbc>

3. Truncation can significantly improve the run time of an APA matrix multiplication algorithm, trading mild accuracy loss for speed.

### 5.1 Experimental Setup

We implement several APA matrix multiplication routines, including some existing algorithms and some new ones found in our search. All implementations are recursive and run to the corresponding base case. That is, we do not default to classical or fast exact matrix multiplication at any point. Unless stated otherwise, we implement the full interpolation (i.e., Algorithm 4) using roots of unity to obtain an exact product (matching the setting of Theorem 4.7). In each experiment, we measure (relative) forward error via \(\|\widehat{C}-C\|/(\|A\|\|B\|)\), where \(\widehat{C}\) is the computed value of _C=AB_ and \(\|\cdot\|\) in the maximum-entry norm. Since we use random input matrices, each reported value of this error metric is the mean over ten independent draws of _A_ and _B_.

All algorithms for computing \(\widehat{C}\) are run in IEEE-754 binary64, whose corresponding unit roundoff is \(\mathbf{u}=2^{-53}\approx 1.11\times 10^{-16}\). To get a surrogate for the exact product _C=AB_, we convert _A_ and _B_ into symbolic form and evaluate the product in 32-digit arithmetic; relative error is then computed by evaluating \(\widehat{C}-C\) symbolically before rounding to double precision. All measurements were taken on an Apple M4 running macOS 26.5.1, with experiments performed in MATLAB version R2025b (25.2.0.3042426, Update 1) using the Symbolic Math Toolbox 25.2 and the Parallel Computing Toolbox 25.2.

### 5.2 Verifying Theorem 4.6

We start by testing how accurately the stability bounds from Section 4 predict the practical performance of an APA algorithm. We specifically aim to answer the following questions: How tightly does Theorem 4.6 bound the measured error for different input distributions? Do these bounds "rank" algorithms, in terms of stability, appropriately?

For our first experiment, we test a \(\langle 3,3,3;21\rangle\) APA algorithm found in our search against two existing APA algorithms for the same size - i.e., a \(\langle 3,3,3,20\rangle\) algorithm of Smirnov \[56\] and a \(\langle 3,3,3;21\rangle\) algorithm of Schönhage \[51\] (all in the standard basis). The details of these algorithms are summarized in  3. We also include the classical algorithm - which is not just norm-wise stable but in fact entry-wise stable - as a baseline. Input matrices _A_ and _B_ are drawn from the following three distributions: Unif(-1,1), Unif(0,1), and N(0,1).

Results are shown in Figure 3, where each panel corresponds to one input distribution. For each algorithm/input type, we plot both the empirical performance (with a dashed line) against the corresponding<tbc>

\begin{tabular}{ccc}
APA Algorithm & \(\omega\) & Degree (_d_) \\
Smirnov \(\langle 3,3,3,20\rangle\) \[56\] & 2.7268 & 10 \\
Schönhage \(\langle 3,3,3,21\rangle\) \[51\] & 2.7712 & 2 \\
Ours \(\langle 3,3,3,21\rangle\) & 2.7712 & 5 \\
\end{tabular}

3: Three APA algorithms for \(\langle 3,3,3\rangle\) matrix multiplication.

