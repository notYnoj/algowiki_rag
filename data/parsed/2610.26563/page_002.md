Aggregation of two matrix multiplications is a technique employed by Victor Pan in his matrix multiplication constructions \[25, 27\]. We recall his construction here as a trilinear form identity. For \(A,B,D,U,V,W\in\mathbb{C}^{n\times n}\), define<tbc>

\(S=\sum_{i,j,h}(a_{ij}+u_{jh})(b_{jh}+v_{hi})(d_{hi}+w_{ij}),\) (1)

\(p_{ih}=\sum_j(a_{ij}+u_{jh}),q_{ij}=\sum_h(b_{jh}+v_{hi}),r_{jh}=\sum_i(d_{hi}+w_{ij}).\) (2)

<tbc>Then

\(\mathrm{tr}(ABD)+\mathrm{tr}(UVW)=S-\sum_{i,j}a_{ij}q_{ij}w_{ij}-\sum_{j,h}u_{jh}b_{jh}r_{jh}-\sum_{h,i}p_{ih}v_{hi}d_{hi}.\) (3)

Hence, two independent products of \(n\times n\) matrices may be computed using _n_<sup>3</sup>+3_n_<sup>2</sup> bilinear multiplications. Leveraging border rank, Pan reduces the count further to _n_<sup>3</sup>+2_n_<sup>2</sup> \[26, Eq. (3.1)\].

In his 1982 work, Pan remarks that his construction computes _AB+BA_ with fewer nonscalar multiplications than his construction for _AB_ \[26, Remark 6.1, p. 33\]. In recent years, a family of algorithms has also been introduced for symmetric tensor contraction \[35\]. For example, for symmetric \(A,B\in\mathbb{R}^{n\times n}\), _C=AB+BA_ may be computed by forming the symmetrized aggregate

\(z_{ijk}=(a_{ij}+a_{ik}+a_{jk})(b_{ij}+b_{ik}+b_{jk}),i<j<k,\) (4)

and applying lower-order corrections, using a total of _n_<sup>3</sup>/6+_O(n_<sup>2</sup>) bilinear multiplications \[35\]. A similar sum over subsets works for higher-order tensor contractions \[35\]. Instead of symmetrization, we consider an analogous aggregation of independent tensor contractions. In Section 5, we show that aggregation of independent tensor contractions is exactly the task performed by the filtered powers of the little and big Coppersmith-Winograd tensors.

We give a direct tensor-contraction formulation of exact decompositions for compatible sets of independent matrix-matrix products. We achieve this using tensor products of a simple centering embedding from C_<sup>n</sup>_ into the zero-sum subspace of C<sup>_n_+1</sup>. We further augment the centering embedding with a weighting, yielding a weighted embedding from C_<sup>n</sup>_ to C<sup>_n_+2</sup> that eliminates both linearly reducible and replicated cross terms. For square matrix products, each contraction is a trilinear form corresponding to a balanced tripartition of 3_N_ indices, and our approach can simultaneously compute any set of such contractions, so long as no recombination of parts from different selected tripartitions is itself a tripartition. This combinatorial condition is the same one addressed by Coppersmith and Winograd using Salem-Spencer sets \[15, 29\].

Besides the exact-rank constructions for independent square matrix products, we also consider aggregation of contractions corresponding to incomplete and unbalanced tripartitions. We show that this space includes the big Coppersmith-Winograd tensor construction \[15\] (Section 5.1). Further, using a standard border-rank degeneration approach \[9\], we loosen the compatibility conditions on tripartitions, enabling aggregation of a larger number of independent matrix-matrix products.

We quantify the parameter conditioning of these graded constructions, estimating the fraction of working- precision digits retained. Our bounds quantify the sensitivity of the bilinear algorithms obtained by the border-rank (graded) constructions to perturbations of their factor maps and bilinear products. These characterizations enable us to target constructions with a specified limiting fraction of retained accuracy, such as half the digits guaranteed by the classical error bound as working precision increases.

With the general aggregation framework established, we then use numerical search to find sets of tripartitions that are compatible for aggregation. The asymptotic exponential growth rate of classical conflict-free tripartition families is characterized by Coppersmith and Winograd \[15\], while numerical search enables us to find constructions of moderate size. Our constructions improve on the prior exact and border-rank multiplication-count bounds compared here for certain moderate numbers _p_ of independent matrix-matrix products and matrix dimensions _q_.

In one of the simplest new constructions, we show that 14 matrix multiplications of matrices of dimension _n_<sup>3</sup> can be aggregated and computed with (_n_+1)<sup>9</sup> bilinear multiplications, instead of the naive 14_n_<sup>9</sup> (Appendix F). We catalogue and compare the new constructions to prior art in Section 8. Figure 4 shows an<tbc>

