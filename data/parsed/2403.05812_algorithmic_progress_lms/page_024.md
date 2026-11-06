If we repeat this argument _n_ times (going from an \((n+1)\times(n+1)\) matrix to the trivial case of a \(n\times n\) matrix, then we conclude that

\(detB_{n+1}=(1-\rho)^n(1+n\rho),\) (28)

as desired. Now to work out the overall determinant of _P_, we simply have to multiply the determinants of the individual blocks, and we are done.

### I.3 Inverse

We now want to determine the third term in \(l(\theta)\), i.e. \(\frac{1}{2\sigma^{2n}}\epsilon^TP^{-1}\epsilon\). One way to reduce the computational cost of this calculation is to take advantage of _P_ being block diagonal, where the inverse _P_<sup>-1</sup> can be determined by inverting the individual blocks. That is, for blocks _B<sub>i</sub>_ the inverse of the correlation matrix is

\(P^{-1}=\left(\begin{array}{ c c c c c }
B_1^{-1} & 0 & \dots & 0 & 0 \\
0 & B_2^{-1} & \dots & 0 & 0 \\
\vdots &  & \ddots &  & \vdots \\
0 & 0 & \dots & B_{n-1}^{-1} & 0 \\
0 & 0 & \dots & 0 & B_n^{-1}
\end{array}\right).\) (29)

To invert a single block _B_, first observe that each block _B_ is such that the elements are

\(B_{ij}=\left\{\begin{array}{ c c }
1 & \text{if}i=j, \\
\rho & \text{otherwise.}
\end{array}\right.\) (30)

Now let _D_ be the diagonal matrix with diagonal entries \(D_{ii}=1-\rho\). Then we have that \(B=D+\rho vv^T\), where _v_ is a vector of ones. We can now calculate the inverse _B_<sup>-1</sup> by application of the Sherman-Morrison formula. In particular we have

\(B^{-1}=(D+\rho vv^T)^{-1}=D^{-1}-\frac{\rho D^{-1}vv^TD^{-1}}{1+\rho v^TD^{-1}v}.\) (31)

Since the inverse of _D_ is just \(D_{ii}^{-1}=\frac{1}{1-\rho}\), assuming that the correlation \(\rho\neq 1\). To simplify notation, we define \(c=\frac{1}{\rho}+\frac{n}{1-\rho}\). We then have

\(B_{ij}^{-1}=\left\{\begin{array}{ c c }
\frac{1}{1-\rho}-\frac{1}{c(1-\rho)^2} & i=j \\
-\frac{1}{c(1-\rho)^2} & i\neq j
\end{array}\right.,\) (32)

and calculating the associated quadratic form \(\frac{1}{2\sigma^{2n}}\epsilon^TP^{-1}\epsilon\) follows trivially.

## J Cross validation for model choice

We determined our primary model for estimating doubling times using formal model selection procedures. In particular, we considered a range of 15 candidate model numbers and a range of possible regularization strengths \(\delta\in\{0,0.001,0.0025,0.005,0.01,0.02\}\). We consider each "model" as a _pair_, consisting of a particular model number and a regularization strength \(\delta\). We then perform leave-one-out cross validation on all of these models. Here we show the results of this analysis.

Our candidate models are defined by varying three degrees of freedom:

1. Which parameters to make benchmark-specific (e.g. having three separate parameters for the exponent on training dataset size, one for each of WT103, PTB and WT2).<tbc>

2. Whether to explicitly model algorithmic progress in parameters _N_, data _D_, or both.

In general we do not include the irreducible loss in the model (i.e. we usually set _E_=0, in the equation 3)--this is described in more detail in section H. In  10 we list the definitions of all models that we looped through in leave-one-out cross validation. For this, we first define some common terms for simplification:

