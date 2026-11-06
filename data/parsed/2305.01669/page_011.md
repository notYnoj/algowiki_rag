<tbc>Newton Step would hence solve Adjoint Computation implying NP-hardness of the former. Moreover, a proposed solution is easily validated efficiently by counting the at most (_q_+1)_n_ flops.

The proof of NP-completeness of the Matrix-Free Newton Step problem relies entirely on algebraic dependences (equality in particular) amongst the elemental partial derivatives. The structure of the underlying DAGs turns out to be trivial. On the other hand, the methods proposed for making DAGs uniformly layered are motivated by purely structural reasoning about the DAGs. All elemental partial derivatives were assumed to be mutually independent. At this stage, the reduction used in the proof of Theorem 4.9 has no consequences on algorithms for the approximate solution of instances of Matrix-Free Newton Step. In fact, similar statements apply to the related proof presented in [16]. Future research is expected to fill this gap.

**5. Conclusion.** The new matrix-free Newton method promises a significant reduction in the computational cost of solving systems of nonlinear equations. This claim is supported by run time measurements for problems with tridiagonal elemental Jacobians. Further challenges need to be addressed for elemental Jacobians with irregular sparsity patterns as well as for computationally expensive residuals.

The matrix-free Newton method relies on the reversal of the DAG. For very large problems the size of the DAG may exceed the available memory resources. The combinatorial DAG Reversal problem asks for a distribution of the available storage such that the overall computational cost is minimized. It is known to be NP-complete [17] as is the related Call Tree Reversal problem [15]. Checkpointing methods [8, 22, 24] offer solutions for a variety of special cases.

Factorization of elemental Jacobians with irregular sparsity patterns yields several well-known combinatorial problems in sparse linear algebra such as Bandwidth [19] or Directed Elimination Ordering [20]. Fill-in needs to be kept low for our method to outperform other state-of-the-art solutions. A rich set of results from past and ongoing efforts in this highly active area of research can be built on.

Another class of potential targets are surrogates with banded layers for computationally expensive nonlinear residuals obtained by machine learning (ML). While the training of such models can be challenging, the inversion of their Jacobian is guaranteed to benefit from the new method. Ongoing research aims to explore a potential extension to ML models with layers exhibiting other suitable sparsity patterns, e.g, with triangular elemental Jacobians.

**Acknowledgement.** The experiments reported on in Figure 3 were performed by Gero Kauerauf as part of his M.Sc. thesis project at RWTH Aachen University.

## REFERENCES

