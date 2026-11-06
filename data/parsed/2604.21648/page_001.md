# OPTIMAL TRANSFER OPERATORS FOR NONSYMMETRIC TWO-GRID METHODS<sup>†</sup>

**Abstract.** Algebraic Multigrid (AMG) methods have been proven to be effective solvers for large-scale linear algebraic systems _Ax=b_ with Hermitian positive definite (HPD) matrix _A_. For such problems the convergence in the _A_-norm is well understood, but for nonsymmetric indefinite systems fewer results exist. Recently, convergence results for more general _B_-norms induced by certain HPD matrices were established. There, orthogonal projections built by compatible transfer operators are used.

Here, we present a theoretical framework for the convergence of nonsymmetric algebraic two-grid methods for arbitrary _B_-inner products and induced _B_-norms which naturally includes the HPD case and all recent results for the nonsymmetric case. For this purpose, we consider two different two-grid error operators with the first one being the natural generalization of the error operator in the HPD case. The second operator has been studied before and is simpler, but requires the additional assumption of normality in some inner product of the smoothing step _M_<sup>-1</sup>_A_ to achieve convergence. We prove new convergence results, generalize some previous results and explain the differences and similarities of both operators together with the necessity of the normality. Moreover, we establish optimal compatible interpolation and restriction operators for both two-grid methods that minimize the error norm.

**Key words.** algebraic multigrid; nonsymmetric; indefinite; two-grid methods; convergence analysis; compatible transfer operators; _B_-normal matrices

**MSC codes.** 65F08, 65F10, 65F15, 65F35, 65F50

**1. Introduction.** We consider large-scale linear algebraic systems _Ax=b_ with nonsingular, nonsymmetric and indefinite system matrix _A_. For symmetric (Hermitian) positive definite (SPD or HPD) _A_, algebraic multigrid (AMG) methods have established themselves as efficient solvers and preconditioners and many theoretical results on the convergence, spectral properties and optimal transfer operators have been proven [8, 9, 23, 32, 36]. There are several nonsymmetric and indefinite problems for which AMG methods have been developed and studied [22, 27, 25, 37, 5] or spectral analysis has been done [31, 29, 28, 34, 11]. In [39, 2, 1, 35] optimal compatible transfer operators leading to orthogonal projections for nonsymmetric matrices were considered.

However, a general framework for rigorous norm-based analysis remains to be found. For the simplified error propagation operator with coarse-grid correction and only one pre- or post-smoothing step, results for certain norm choices have been proven. These works include [24, 5, 26] for the \(\sqrt{A^H}A\)-norm, [39] for the _M_-norm (where _M_<sup>-1</sup> is the smoother) and [2] for arbitrary norms. In this article, we introduce a general framework for nonsymmetric algebraic two-grid methods that allows for the analysis of norm-based convergence in any norm given by some HPD matrix _B_. We consider two different error propagation operators, both with an arbitrary number of pre- and post-smoothing steps. The first operator is the natural generalization of the error operator in the HPD case. The second operator has a simpler structure and is easier to apply because it uses the same matrix as pre- and post-smoother. It was analyzed in [16] where norm-based convergence results have been proven for a special class of norms. These norms are based on a diagonalization of _M_<sup>-1</sup>_A_ which was also

<sup>†</sup>Submitted to the editors DATE. <sup>‡</sup>Institute of Mathematics, Technische Universität Berlin, (nabben@math.tu-berlin.de). <sup>§</sup>Institute of Mathematics, Technische Universität Berlin, (rooch@math.tu-berlin.de).

REINHARD NABBEN<sup>‡</sup> AND LUDWIG ROOCH<sup>§</sup>

arXiv:2604.21648v2 [math.NA] 24 Apr 2026

