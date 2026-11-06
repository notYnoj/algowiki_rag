<tbc>and improving numerical stability. Most importantly, such neural preconditioners are completely matrix-free through construction to application, which is desirable especially for large problems where IChol decomposition may become prohibitively expensive.

## 4.2 Volume transfer of trained neural preconditioners

In this section, we examine the transferability of the trained framework. We use N<sub>_L_16</sub> in  1 as the base model and apply it to various lattice gauge configurations. We report the average iteration counts in the CG solver before and after applying the trained neural preconditioner on our testing<tbc>

Unprecond. FNO-precond.
FCN-precond. IChol-precond.
105
104
Condition number
103
102
L=8
L=16
L=32
L=64

100
L = 8
1600
Unprecond.
L = 16
FNO-precond.
10-1
L = 32
1400
IChol-precond.
L = 64
10-2
Unprecond.
1200
10-3
FNO-precond.
Average relative residual
IChol-precond.
Number of iterations
1000
10-4
800
10-5
600
10-6
400
10-7
200
10-8
0
0
250
500
750
1000
1250
1500
1750
L = 8
L = 16
L = 32
L = 64
Iteration

Fig. 3. Comparison of the average condition numbers among the unpreconditioned systems and neural network-preconditioned systems on the testing set with various lattice sizes. Both FNO- and FCN- based neural preconditioners significantly reduce the system condition numbers in all cases.

(a)

(b)

Fig. 4. (a) comparison of the average number of iterations required for a given tolerance in the CG solver for the unpreconditioned, FNO-preconditioned, and IChol-preconditioned linear systems with various lattice sizes. The neural network-preconditioned CG solver requires significantly fewer number of iterations than the unpreconditioned case. (b) shows the CG iteration counts along with the lattice sizes for such systems. While IChol-preconditioners still lead to the fewest iterations, the trained FNO-preconditioners show promise of effectively accelerating the CG convergence on linear systems with unseen operators in a matrix- and solve-free manner.

