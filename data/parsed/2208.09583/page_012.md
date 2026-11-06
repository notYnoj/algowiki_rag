We can reduce max-smiss to the stable marriage problem with interval orders as follows. Given an instance of max-smiss, from the total order \(\succ_v\) of each \(v\in U\cup W\), define a partial order \(\succ'_v\) by \(e\succ'_vf\Leftrightarrow e\succ_vf,e\in A\). Then \(\succ'_v\) is an interval order. Indeed, we can easily observe that, if \(e\succ'_vf\) and \(g\succ'_vh\) hold for distinct _e,f,g,h_, then \(e\succ'_vh\) or \(g\succ'_vf\). It is also not hard to see that a socially stable matching in the original instance is a stable matching with respect to the interval orders \(\{\succ'_v\}_{v\in U\cup W}\). Thus, the maximum stable marriage with interval orders and its generalization to max-kernel-po are inapproximable within \(\frac{3}{2}-\delta\) under UGC.

## 4 Inapproximability with General Partial Orders

In this section, we consider the case where preferences may be arbitrary partial orders. In particular, we investigate max-smpo, the maximum stable marriage problem with partial orders. Interestingly, in this case the structure of the problem changes significantly compared to the case with weak orders (i.e., max-smti), as shown in Section 4.1. In fact, beating the trivial 2-approximation becomes UGC-hard, as shown in Section 4.2.

### 4.1 Structural observations

Here we provide some structural observations on max-smpo. The first one shows that the main tool which is used to show the 1.5-approximability in previous approaches for max-smti cannot be used for partial order preferences. The previous 1.5-approximation algorithms for max-smti, such as one in \[32\], are designed so that, for the output stable matching _M_ and any stable matching _N_, there is no maximal alternating path in \(M\cup N\) consisting of one _M_-edge and two _N_-edges. In the case of arbitrary partial orders, it may happen that for any stable matching _M_, there exists another stable matching _N_, such that a maximal alternating path with one _M_-edge and two _N_-edges exists, as the next example shows.

**Example 13.** Consider the instance in Figure 2. We claim that, in this example, for any stable matching _M_, there is another stable matching _N_, such that in \(M\cup N\) there is a maximal alternating path of length 3, with two _N_-edges and one _M_-edge. It is easy to verify that the following<tbc>

e2
f2
u2
w2
e1
f1
e3
f3
e4
v
f4
w1
u1
e5
h
f5
g
v: (f4 > e1) (f4 > h) (e4 > f1) (e4 > g)
u1 : e4 > e5
u2 : e3 > e2
w1 : f4 > f5
w2 : f3 > f2

Figure 2: Illustration of Example 13. The green stable matching is _M_<sub>2</sub> and the blue one is _M_<sub>3</sub>.

