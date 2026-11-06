(a)
Brusselator closure
(b)
Brusselator closure
(c)
Brusselator closure
103
103
103
wall time (s)
102
102
101
101
100
10-6
10-4
10-2
101
102
103
104
105
gradient error
active parameters
degrees of freedom
(d)
Cahn-Hilliard closure
(e)
Cahn-Hilliard closure
(f)
Cahn-Hilliard closure
103
103
103
wall time (s)
102
102
102
101
101
101
100
10-3
10-2
10-1
102
103
104
105
gradient error
active parameters
degrees of freedom
diff-soup JIDA
Julia SciML forward mode
SUNDIALS
reverse mode

Figure 10: Work-precision and scaling diagrams for the gradient of a loss function with respect to the closure weights of the Brusselator (a, b, c) and the Cahn-Hilliard problem (d, e, f) for `diff-soup` (blue), the CVODES and IDAS sensitivity methods of SUNDIALS (red), and `SciMLSensitivity` with `FBDF` in Julia (purple), with the line style and marker denoting forward or reverse mode as described in the legend. All benchmarks are run according to the procedure described in Section 7.1. Notably, data points are omitted where the solve did not finish or exceeded the wall cap. The work-precision diagrams hold the state and the network fixed, the parameter diagrams grow the active weights at fixed tolerance, and the state diagrams grow the degrees of freedom at fixed network width for the `diff-soup` lanes alone. The vertical dashed line marks the noise floor of the reference gradient. (a) The Brusselator work-precision diagram at _N_<sub>dof</sub>=32,768 and \(n_\theta=128\) shows `diff-soup` in reverse mode outperforming the adjoint solvers by one to two orders of magnitude at every tolerance. (b) The Brusselator parameter scaling diagram shows the reverse-mode cost of every library independent of the number of weights while the forward-mode cost grows with it, with `diff-soup` alone completing forward mode beyond the smallest network. (c) The Brusselator state scaling diagram shows both modes of `diff-soup` growing as a power law in the degrees of freedom, with reverse mode reaching the largest size. (d) The Cahn-Hilliard work-precision diagram at _N_<sub>dof</sub>=16,384 and \(n_\theta=128\) shows a similar order of magnitude improvement, with every library reaching comparable gradient errors. (e) The Cahn-Hilliard parameter scaling diagram shows the same separation as (b), with forward mode on the CPU completing at most the smallest network. (f) The Cahn-Hilliard state scaling diagram shows both `diff-soup` modes growing as a slightly steeper power law and reaching the largest size.

