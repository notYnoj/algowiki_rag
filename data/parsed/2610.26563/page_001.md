# Simultaneous Matrix Multiplication by Tensor Contraction Aggregation

**Abstract**

We present an interpretation of the fast matrix multiplication algorithms of Coppersmith and Winograd as aggregations of tensor contractions. This point of view provides a direct connection to older constructions by Pan and to more recent work on bilinear algorithms for symmetric tensor contraction. Further, we provide a simple explicit approach for exact aggregation of tensor contractions, each one yielding an independent matrix-matrix product. These constructions and border rank adaptations thereof do not come close to improving the best known bounds on \(\omega\) (the matrix multiplication exponent), but provide explicit moderate-size fast matrix multiplication algorithms that achieve a better exponent than Strassen’s algorithm and have potential practical value. These finite constructions improve the multiplication-count bounds of the reference algorithms compared here for selected numbers and dimensions of independent square matrix products. In particular, using \(\langle m,m,m\rangle\) to denote the matrix multiplication tensor for matrices of dimension _m_, we obtain constructions that give bounds such as the border rank bound

\(\underline{R}\big(\langle n^2,n^2,n^2\rangle^{\oplus 9}\big)\le(n+1)^6+6(n+1)^5,\)

and the exact rank bound

\(R\big(\langle n^3,n^3,n^3\rangle^{\oplus 14}\big)\le(n+1)^9.\)

We quantify the accuracy of such constructions in finite precision, and provide border-rank constructions that reduce cost with limiting retained fractions of accuracy at least 1/2, 1/3, or 1/4 relative to the classical matrix-multiplication approach under the stated error model.

### 1 Introduction

Independent matrix-matrix products are a key subject in the theoretical study of the matrix multiplication exponent, \(\omega\). Schönhage’s asymptotic sum theorem [30] gives upper bounds on \(\omega\) based on constructions for independent matrix-matrix products, and the extensively studied method of Coppersmith and Winograd [15] provides efficient border-rank constructions for such sets of products. Exact-rank bounds for balanced restrictions of these tensor powers, and hence for balanced compatible families of independent products, were established by Flavi, Jelisiejew, and Michałek [20]. Their work builds on the group-tensor formulation of Alman and Vassilevska Williams [3]. At the same time, independent matrix-matrix products are in themselves a common computational kernel, frequently arising in dense and sparse linear algebra, for instance when multiplying block-sparse matrices [11]. In recent years, standard software interfaces and libraries have been developed for independent matrix-matrix multiplications [1]. In this paper, we develop a new, more practical point of view on the Coppersmith–Winograd construction by considering aggregation of tensor contractions.

\*Siebel School of Computing and Data Science, University of Illinois Urbana-Champaign, USA. **solomon2@illinois.edu**. †Department of Computer Science, Saarland University, Saarbrücken, Germany. **mblaeser@cs.uni-saarland.de**.

Edgar Solomonik<sup>∗</sup>

Markus Bläser<sup>†</sup>

