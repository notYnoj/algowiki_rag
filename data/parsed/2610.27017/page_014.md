<tbc>and the source term _f_ is derived from the exact solution. Take \(\gamma_1=1.1\), \(\gamma_2=1.7\), _N_=64, _M_=4, and consider the linear system at the first time level. We apply the TGM to solve the linear system obtained from discretization, terminate the iteration when<tbc>

\(\frac{\|Au-b\|_\infty}{\|b\|_\infty}<10^{-7},\)

<tbc>and count the number of cycles. Specifically,

(1): The _d(x,y,t_)=0: We set \(\omega=0.0001\) as the initial value and traverse to \(\omega=1.1\) with a step size of 0.0001. Denoting one TGM iteration as one cycle, we record the cycle counts required to reach the stopping tolerance for different values of \(\omega\), and plot the corresponding iteration curve, namely Fig. 2a. A direct calculation gives

\(\frac{2a_0}{\|f_{\gamma_1,\gamma_2}\|_\infty}\approx 1.0417,\)

which is marked by a red line in Fig. 2a.

As can be seen from Fig. 2a, the choice of the relaxation parameter \(\omega\) significantly affects the iteration efficiency of the TGM. For example, when \(\omega=0.9335\), the required number of cycles is the smallest, only 25; whereas in other regions, the corresponding cycle counts increase markedly, even exceeding 100. In addition, all values of \(\omega\) to the left of the red line ensure the convergence of the TGM, which verifies the effectiveness of Theorem 3.1.

Fig. 2b shows the steep growth phenomenon near \(\omega=1.0417\): when \(\omega=1.04\), the number of cycles required to reach the convergence tolerance is 795; when \(\omega=1.0417\), the required number of cycles increases sharply to 3043; and when \(\omega=1.042\), the TGM still fails to converge after more than 5000 iterations. These phenomena indicate that the choice of \(\omega\) has a great influence on both the convergence and the convergence speed of the TGM, so selecting an appropriate \(\omega\) is necessary for accelerating convergence.

(2): _d(x,y,t_)=(1+_x_)<sup>7</sup>(1+_y_)<sup>7</sup>: Similar to the results obtained in (1), Fig. 3a shows a sweep of the number of cycles required to reach convergence accuracy under different values of \(\omega\). It can be seen that the number of iterations is minimized at \(\omega=0.9231\), requiring only 14 cycles. In Fig. 2b, the parameters to the right of \(\omega=1.0417\) basically make the number of iterations required by TGM exceed 5000, whereas in Fig. 3b, the parameters to the left of \(\omega=1.0513\) all allow TGM to converge. It can be seen that the boundary parameter<tbc>

N=64
1.06
1.08
1.05
1.07
1.06
max(1.445,1.445,1.0615)
1.05
1.04
2a0
1.03
1.02
1.03
1.01
1
1.02
2
1.8
1.6
1.8
1.01
1.4
1.6
1.4
1.2
1.2
Y2
1
1
Y1

Figure 1: The range of \(\frac{2a_0}{\|f_{\gamma_1,\gamma_2}\|_\infty}\) when _N_=64.

