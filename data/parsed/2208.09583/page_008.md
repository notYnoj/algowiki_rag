**Remark 8.** It is a well-known fact that, for any two bases _A,B_ of a matroid (_S,_I) of rank _r_, there exists a perfect matching \(a_ib_i(i\in[r])\) between _A_ and _B_ such that \(B+a_i-b_i\in\mathcal{I}\) for every \(i\in[r]\) (see Brualdi \[8\] and also \[40, Corollary 39.12a\] and \[16, Theorem 5.3.4\]). We claim that this property does not immediately imply our Theorem 5.

In our theorem, the base _A_ is assumed to be optimal. This implies the condition \(a\succ b\) for all pairs \(ab\in A\times B\) with \(A-a+b\in\mathcal{I}\) but not for those with \(B+a-b\in\mathcal{I}\). To see this, consider the graphic matroid of _K_<sub>4</sub> with ground set _S_={_e_<sub>1</sub>_,e_<sub>2</sub>_,e_<sub>3</sub>_,e_<sub>4</sub>_,e_<sub>5</sub>_,e_<sub>6</sub>} shown in Figure 8. Suppose that the total order \(\succ\) is defined as \(e_1\succ e_2\succ e_3\succ e_4\succ e_5\succ e_6\). Then, _A_:={_e_<sub>1</sub>_,e_<sub>2</sub>_,e_<sub>4</sub>} is the optimal base with respect to \(\succ\) and its complement _B_:=_S_\\_A_ is also a base. Here, we have \(B+e_4-e_3\in\mathcal{I}\) for \(e_4\in A\) and \(e_3\in B\) while \(e_4\unknown e_3\).

Therefore, the existence of a perfect matching of exchangeability edges combined with the optimality of _A_ does not simply imply Theorem 5.

## 3 Matroid kernel algorithm with interval orders

In this section, we show Theorem 1, which states that max-kernel-po is approximable with a factor 1.5 if the partial orders are interval orders, i.e., (2+2)-free posets.

Like the previous algorithms by Yokoi \[42\] and by the present authors \[12\] (conference version of this paper), our algorithm is described as an application of the Gale-Shapley algorithm to a carefully constructed modified instance. In this modified instance, each element is replicated into three parallel elements, and special total orders are defined on the extended ground set. The origin of the idea comes from Király’s 1.5-approximation algorithm \[30\] for max- smti, which is a variant of the Gale-Shapley algorithm in which each man can propose to each woman at most three times and there are special rules for men’s proposal order and women’s acceptance/rejection.

Our construction of the modified instance is symmetric for the two sides, and the 1.5- approximation ratio depends only on the stability in the modified instance (not on the behaviour of the GS algorithm). This allows for a simple analysis while considering broad class preferences and constraints.

### 3.1 Description of the algorithm

Let \(M_1=(S,\mathcal{I}_1,\succ_1)\) and \(M_2=(S,\mathcal{I}_2,\succ_2)\) be partially ordered matroids on the same ground set _S_ and suppose that \(\succ_1\) and \(\succ_2\) are interval orders. Our algorithm consists of three steps.

1. The algorithm first creates a new instance by replacing each element of _S_ by three parallel elements, and by defining total orders on the extended ground set as explained below.<tbc>

e3
e1
e5
e2
e4
e6

Figure 1: The graphic matroid defined by _K_<sub>4</sub>. When \(e_1\succ e_2\succ e_3\succ e_4\succ e_5\succ e_6\), the thick edges form the optimal base with respect to \(\succ\).

