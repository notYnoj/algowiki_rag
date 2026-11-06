the _positive/negative connection demands_ \((x_{ik}^+,p_{ij}^+)\) if the _k_-th positive literal of _X<sub>i</sub>_ occurs in _C<sub>j</sub>_ and \((x_{ik}^-,p_{ij}^-)\) if the _k_-th negative literal of _X<sub>i</sub>_ occurs in _C<sub>j</sub>_ as well as the _SX demand_ (_S,x<sub>i</sub>_).

## 4 An Approximation Algorithm for _s_-Thin Instances

In this section, we present and analyze an aproximation algorithm for _s_-thin instances (where points in _P_ lie on at most _s_ distinct _x_-coordinates). In particular, we allow more than one point to share an _x_-coordinate. However, we still require any two distinct points to have distinct _y_-coordinates. We show an approximation ratio of _O_(log_s_), proving Theorem 2.

An _x-group_ is a maximal subset of _P_ having the same _x_-coordinate. Note that an _O_(log_s_)- approximation for _s_-thin instances can be obtained via a natural "vertical" divide-and-conquer algorithm that recursively divides the _s_ many _x_-groups in two subinstances with roughly _s/_2 many _x_- groups each. (Section E.2 contains a more general version of this algorithm subdividing into an arbitrary number of subinstances.) The analysis of this algorithm uses the number of input points as a lower bound on OPT. However, such a bound is not sufficient for our purpose of deriving an \(O(\sqrt{logn})\)-approximation.

In this section, we present a different algorithm, based on "horizontal" divide-and-conquer (after a pre-processing step to sparsify the set of _y_-coordinates in the input via minimum hitting sets). Using horizontal rather than vertical divide-and-conquer may seem counter-intuitive at first glance as the number of _y_-coordinates in the input is generally unbounded in _s_. Interestingly enough, we can give a _stronger_ guarantee for this algorithm by bounding the cost of the approximate solution against what we call a _boundary independent set_. Additionally, we show that the size of a such a set is always upper bounded by the maximum number of vertically separable demands. This directly implies Theorem 2, since 2OPT is an upper bound on the number of vertically separable demands (c.f. Lemma 6). Even more importantly, our stronger bound allow us to prove Theorem 3 in the next section since vertically separable demands fulfill the subadditivity property mentioned in the introduction. In the proof of Theorem 3, an arbitrary _O_(log_s_)-approximation algorithm would not suffice.

By losing a factor 2 in the approximation ratio, we may assume that the demands are monotone,<tbc>

Cj
(S, cj)
lj1
(pij, lj1)
lj2
(pi'j, lj2)
lj3
(pi"j, lj3)

