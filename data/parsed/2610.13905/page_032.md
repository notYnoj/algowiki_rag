particular, it is still open to prove numerical stability for an approximate matrix multiplication algorithm obtained from a floating-point, least-squares solution to the tensor decomposition problem (1.3); several such algorithms exist in the literature \[35, 36, 56\] and should, like APA matrix multiplication, be considered for practical use.

## 7 Acknowledgements

This work was done in part while the authors were visiting the Simons Institute for the Theory of Computing. Support was provided by a UC Multicampus Research Program Award M25PL9060. The project also received funding from the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation program (grant agreements 818252 and 101113120) and was supported by grant 1354/23 of the Israel Science Foundation (founded by the Israel Academy of Sciences and Humanities). Additional support was provided by the Science Accelerator and by the Frontiers in Science initiative of the Ministry of Innovation, Science and Technology. Finally, R.S. is supported by NSF grant MSPRF 2402027. Special thanks to James Demmel for suggesting the topic of APA matrix multiplication and to Dan Romik for helpful comments.

### AI Declaration:

Artificial intelligence (AI) tools assisted in the production of the code used to run our search algorithm in Section 2 and the numerical examples in Section 5. An LLM also provided feedback on an earlier draft of this paper, suggesting the special case for sparsification discussed in Section 3.2.3 and highlighting an error in the proof of Theorem 4.6, which was corrected by a human. The authors take full responsibility for the correctness of all results presented in this work.

## References

Smirnov (3, 3, 3; 20)
Schönhage (3, 3, 3; 21)
Our (2, 2, 3; 10)
4
20
4
100
10-3
15
3
3
shrinkage 1/B
10-6
normalized error
10
10-9
2
2
5
10-12
1
1
10-15
10
20
30
40
2
4
6
8
5
10
15
20
25
interpolation points r
interpolation points r
interpolation points r

Figure 6: Algorithm 5 runs with various APA routines. For each choice of _r_, we use the evaluation points \(\varepsilon_j=\beta\cdot e^{2\pi ij/r}\) for several choices of \(0<\beta<1\). The colorbar corresponds to normalized forward error \(\|\widehat{C}-C\|/(\|A\|\|B\|)\) in the maximum-entry norm. A triangle marks the smallest error achieved on each plot.

