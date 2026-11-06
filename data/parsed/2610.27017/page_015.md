<tbc>that ensures the smoothing property is shifted noticeably to the right, which verifies the validity of Corollary 3.1. In addition, when \(\omega=1.0512\), the required number of cycles is 1298, while when \(\omega=1.0513\), the iteration still fails to converge after more than 5000 steps. This steep growth phenomenon is far more pronounced than in the case of _d(x,y,t_)=0, reflecting that the parameter variation is more complicated when \(d(x,y,t)\ge 0\).

## 4. Data-driven acceleration strategy

As the discretization number _N_ increases, the discretization of the partial differential equation yields a family of matrices. When solving with parameterized iterative methods, there exists an optimal parameter for each problem size, which can be obtained via fine step grid search and corresponds to the minimal computational cost. As _N_ continues to grow, properties such as the matrix spectrum change, and these optimal parameters usually fluctuate. Such fluctuations generally exhibit nonlinear characteristics and cannot be characterized by rigorous mathematical expressions, determining them via exact eigenvalue computations incurs a high computational cost\[29\].

Gaussian process regression (GPR) provides an effective data-driven strategy for learning such parameters: it<tbc>

100
90
2a0 / /
80
70
60
Min: o=0.9335, Cycle=25
50
Cycle counts
40
30
20
10
0
0
0.2
0.4
0.6
0.8
1
1.1
O

5000
X 1.042 Y 5000
4500
4000
3500
X 1.0417 Y 3043
3000
Cycle counts
2500
2000
1500
X 1.04 Y 795
1000
500
0
1.03
1.032
1.034
1.036
1.038
1.04
1.042
1.044
1.046
1.048
1.05
W

100
90
80
2a0 / /
70
60
50
Cycle counts
40
Min: o=0.9231, Cycle=14
30
20
10
0
0
0.2
0.4
0.6
0.8
1
1.1
O

5000
X 1.0513 Y 5000
4500
4000
3500
3000
Cycle counts
2500
2000
X 1.0512 Y 1298
1500
1000
500
0
1.03
1.035
1.04
1.045
1.05
1.055
1.06
W

(a) The relationship between \(\omega\) and the cycle counts

(b) The iterative behavior near \(\omega=1.0417\)

Figure 2: The iteration curves of the TGM for _d(x,y,t_)=0.

(a) The relationship between \(\omega\) and the cycle counts

(b) The iterative behavior near \(\omega=1.0417\)

Figure 3: The iteration curves of the TGM for _d(x,y,t_)=(1+_x_)<sup>7</sup>(1+_y_)<sup>7</sup>.

