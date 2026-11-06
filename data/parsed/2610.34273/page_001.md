# Asymptotic Rank of Complete Graph Tensors

Huanyi Zhou<sup>∗</sup>

**Abstract**

Graph tensors extend the matrix multiplication tensor by placing a two-party identity tensor on every edge of a graph and keeping one tensor leg at every vertex. We study the asymptotic rank of the tensor associated with the complete graph. For every integer \(n\ge 2\), over the complex numbers, we prove

The upper bound matches the maximum-cut lower bound for every even _n_ and differs from it by only 1/4 for every odd _n_. In particular, the exponent per edge is below 2/3 for every \(n\ge 5\), answering a question of Christandl, Vrana, and Zuiddam.

Our proof extends the polynomial multiplication approach underlying OpenAI’s bound \(\omega\le 9/4\). The main step separates any fixed number of shared tensor legs simultaneously, using only linearly many direct-sum copies in the number of blocks. This yields an entropy inequality for higher-order tensors. We apply it to the tensor for multiplying _n_-1 polynomials, whose rank is linear in the input length. Discrete concavity and a shifted tripling inequality then force a lower bound on a symmetrized spectral profile. Comparing this growth with polynomial interpolation gives the stated upper bound while preserving all _n_ tensor legs.

We also prove an operational barrier for these higher-order polynomial constructions. For \(n\ge 3\), the specified formal reduction rules cannot certify an exponent below _n_<sup>2</sup>/4 for GT<sub>2</sub>(_K<sub>n</sub>_), even after taking tensor powers and allowing subexponential overhead and common auxiliary factors. This extends the symmetric three-leg barrier of Amanov, van den Berg, and Zuiddam and explains the remaining gap for odd complete graphs within this method.

<sup>∗</sup>Tsinghua University. zhouhuan24@mails.tsinghua.edu.cn.

\(\left|\frac{n^2}{4}\right|\le log_2\widetilde{R}\big(\mathsf{GT}_2(K_n)\big)\le\frac{n^2}{4}.\)

