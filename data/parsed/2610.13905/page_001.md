Fast and Stable Arbitrary Precision Approximate Matrix Multiplication

**Abstract**

We present several new and surprising results on the theory and practice of Arbitrary Precision Approximate (APA) matrix multiplication, which refers to algorithms that output merely approximations to matrix multiplication even in exact arithmetic. While APA algorithms have been around for nearly half a century, and despite the fact that they have potentially lower (asymptotic) cost than many fast exact matrix multiplication schemes, they have not been studied as closely, to the extent that relatively little is known about their numerical properties. In this paper, we shine a spotlight on these algorithms by presenting three important results. First, we provide a new search algorithm for APA routines that is easy to use, automatically generates encoding matrices with functional entries, and can match or beat the best known APA algorithms for several sizes. In particular, we improve the upper bound on the border rank of \(\langle 2,4,5\rangle\) matrix multiplication. Second, we combine this insight with alternative bases to minimize the number of additions in an APA algorithm, thereby improving its leading coefficient. Finally, we prove the same kind of stability that characterizes fast exact matrix multiplication for an algorithm of Bini [_Calcolo_ 1980] that computes an exact product of two matrices using a modified APA scheme (with or without alternative bases).

**Keywords:** Matrix multiplication, arbitrary precision, border rank, alternative bases, floating-point stability

**MSC Class:** 65F99

## 1 Introduction

In 1969, Strassen [59] fundamentally changed the field of numerical linear algebra when he demonstrated that the classical algorithm for matrix multiplication is not optimal. Strassen’s discovery sparked a still ongoing effort to derive, analyze, and implement _fast_ matrix multiplication algorithms, which are broadly defined as any matrix multiplication routine with computational complexity \(O(n^\omega)\) for \(2\le\omega<3\). At the time of writing, Dupont et al. [27] hold the record for the smallest value of \(\omega\) achieved by an algorithm, and it remains open whether the lower bound \(\omega\ge 2\) is attainable. Research aimed at reaching this lower bound (or proving it cannot be done) is motivated by both the wide applicability of matrix multiplication in scientific computing/machine learning and the fact that many linear algebra operations have been shown to reduce to matrix multiplication [20], including recently nonsymmetric eigenvalue problems [5, 22].

Most practical fast matrix multiplication algorithms, including Strassen’s [59], are based on routines for multiplying small matrices. The key idea here is straightforward: an algorithm for multiplying \(m_0\times k_0\) and \(k_0\times n_0\) matrices can be used to compute the product of arbitrary \(A\in\mathbb{C}^{m\times k}\) and \(B\in\mathbb{C}^{k\times n}\) by breaking the input into blocks

\(A=\left(\begin{array}{ c c c c } A_{11} & \cdots & A_{1k_0} \\ \vdots &  & \vdots \\ A_{m_01} & \cdots & A_{m_0k_0} \end{array}\right)B=\left(\begin{array}{ c c c c } B_{11} & \cdots & B_{1n_0} \\ \vdots &  & \vdots \\ B_{k_01} & \cdots & B_{k_0n_0} \end{array}\right)\) (1.1)

<sup>∗</sup>University of California, San Diego <sup>†</sup>University of California, Berkeley <sup>‡</sup>Independent Researcher <sup>§</sup>The Hebrew University of Jerusalem \(\unknown\)Corresponding author (ryan.schneider@berkeley.edu)

Ioana Dumitriu<sup>∗</sup> Olga Holtz<sup>†</sup> Abraham Hsu<sup>‡</sup> Nicholas Liskij<sup>†</sup> Yoav Moran<sup>§</sup> Ryan Schneider<sup>†</sup><sup>¶</sup> Oded Schwartz<sup>§</sup> Shuncheng Yuan<sup>∗</sup>

