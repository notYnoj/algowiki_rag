\(m_1:1\succ_1^m2\succ_1^m3w_1:2\succ_1^w3\succ_1^w1m_2:2\succ_2^m3\succ_2^m1w_2:3\succ_2^w1\succ_2^w2m_3:3\succ_3^m1\succ_3^m2w_3:1\succ_3^w2\succ_3^w3\)

There are two rotations \(\rho_1=(1,1),(2,2),(3,3)\) and \(\rho_2=(1,2),(2,3),(3,1)\), with \(\rho_1<\rho_2\), which yield three stable marriages:

- the man-optimal stable marriage **x**_<sup>m</sup>_ in which each man is matched with his first choice, and which corresponds to eliminating no rotation,<tbc>

**-** the woman-optimal stable marriage **x**_<sup>w</sup>_ in which each woman is matched with her first choice, and which corresponds to eliminating both rotations,<tbc>

**-** a "compromise" stable marriage **x**_<sup>c</sup>_ in which each agent is matched with his/her second choice, and which corresponds to eliminating only \(\rho_1\).

We use the disutility function _d_ defined by _d_(1)=0, \(d(2)=1+\epsilon\) and _d_(3)=2 (with \(\epsilon>0\)) and the following GGI weights: \(\lambda=(a,b,c,0,0,0)\) with \(a\ge b\ge c>0\). The disutility vectors of the three stable marriages are then **d**(**x**_<sup>m</sup>_)=(0,0,0,2,2,2), **d**(**x**_<sup>w</sup>_)=(2,2,2,0,0,0) and \(\mathbf{d}(\mathbf{x}^c)=(1+\epsilon,1+\epsilon,1+\epsilon,1+\epsilon,1+\epsilon,1+\epsilon)\).

By using Equation 17 from the proof of Lemma 2, the value of \(\hat{d}_i^m\) for each man _m<sub>i</sub>_ and the value of \(\hat{d}_j^w\) for each woman _w<sub>j</sub>_ are written as follows in terms of \(\hat{y}(\rho_1)\) and \(\hat{y}(\rho_2)\):

\(\hat{d}_i^m=0+\hat{y}(\rho_1)(1+\epsilon)+\hat{y}(\rho_2)(1-\epsilon)\forall i\in\{1,2,3\}\hat{d}_j^w=2-\hat{y}(\rho_1)(1-\epsilon)-\hat{y}(\rho_2)(1+\epsilon)\forall j\in\{1,2,3\}\)

where \(\hat{y}(\rho_1)\ge\hat{y}(\rho_2)\). We see that the three men share the same disutility value, as well as the three women. The GGI value of a feasible solution to \(\widehat{\mathcal{P}}\) is thus completely determined by the common disutility of the men or the common disutility of the women because only the three least satisfied agents are taken into account in \(\lambda\). Consequently, an optimal solution to \(\widehat{\mathcal{P}}\) minimizes \(max\{\hat{d}_1^m,\hat{d}_1^w\}\) for \(\hat{y}(\rho_1)\ge\hat{y}(\rho_2)\). Simple calculations make it possible to conclude that the only optimal solution to \(\widehat{\mathcal{P}}\) is characterized by \(\hat{y}(\rho_1)=\hat{y}(\rho_2)=0.5\).

For this instance, ROUNDING ALGORITHM returns therefore the woman-optimal stable marriage which has the ordered disutility vector (2,2,2,0,0,0) and a GGI value of 2(_a+b+c_). However, an optimal stable marriage is the "compromise" stable marriage, which has the ordered disutility vector \((1+\epsilon,1+\epsilon,1+\epsilon,1+\epsilon,1+\epsilon,1+\epsilon)\) and a GGI value of \((1+\epsilon)(a+b+c)\). By taking the limit for \(\epsilon\) going to 0, we obtain the tightness of the bound.

_Remark 1_ Note that the approach taken in ROUNDING ALGORITHM is valid for any aggregation criterion _F_ on dissatisfactions of agents for which the following condition holds:

\(F(\frac{1}{2}\mathbf{d}(\mathbf{x}))=\frac{1}{2}F(\mathbf{d}(\mathbf{x}))F(\mathbf{d}(\mathbf{x})+\mathbf{r})\ge F(\mathbf{d}(\mathbf{x}))\)

where **r** is any non-negative vector.

_Remark 2_ A general approximation result for the optimization of a generalized Gini index in multiobjective optimization problems has been proposed by Kasperski and Zieliński \[2015\]. For the GGISM problem, it amounts to compute an optimal stable marriage according to the sum of disutilities of pairs (_m<sub>i</sub>,w<sub>j</sub>_), where the disutility of a pair (_m<sub>i</sub>,w<sub>j</sub>_) is defined by \(\lambda_1max\{d(\mathbf{rk}(m_i,w_j)),d(\mathbf{rk}(w_j,m_i))\}+\lambda_2min\{d(\mathbf{rk}(m_i,w_j)),d(\mathbf{rk}(w_j,m_i))\}\). This can be performed in polynomial time by linear programming. The returned solution is a \(N\lambda_1\)- approximation, provided \(\sum_{i=1}^N\lambda_i=1\). To obtain a better guarantee than 2, one should have \(\lambda_1<2/N\). On the contrary, by taking advantage of the specific structure of the stable marriage problem, our approach yields a 2-approximation _whatever weights are used_.

