elements. Furthermore, each set has one extra element which is unique to that set. The precise values are such that each set in the _i_-th group is solved after querying the first _i_ elements. We give an example in Figure 3 with _k_=3 and _c_=3. If we let BAL query the intervals in the order given by the indices, it is easy to see that it queries \(c\cdot k\) intervals, while the _c_ intervals that are shared by more than one set are enough to solve all sets. In particular, note that BAL does not take into consideration that some elements are shared between different sets. The challenge is how to balance queries between sets in a better way.

We give an algorithm that requires at most \((2+\varepsilon)\cdot opt_k+O\left(\frac{1}{\varepsilon}\cdot lgm\right)\) rounds, for every \(0<\varepsilon<1\). (The execution of the algorithm does not depend on \(\varepsilon\), so the upper bound

round 1 round 2 round 3 S1 S2 S3

I1
I2
S1
I1
I3
S2
I1
I4
S3
I5
I1
I4
S4
I6
I1
I4
I7
S5
I8
I1
I4
I7
S6
I9

**Figure 2** Possible execution of BAL for _m_=3 disjoint sets and _k_=5. Each interval is represented by a box, and the optimum solution is a prefix of each set. The solid boxes are useful queries, the two hatched boxes are wasted queries, and the white boxes are not queried by the algorithm.

**Figure 3** Bad instance for BAL with overlapping sets, with _k_=3 and _c_=3. BAL will query the following rounds: {_I_<sub>1</sub>_,I_<sub>2</sub>_,I_<sub>3</sub>},{_I_<sub>4</sub>_,I_<sub>5</sub>_,I_<sub>6</sub>},{_I_<sub>7</sub>_,I_<sub>8</sub>_,I_<sub>9</sub>}. It is enough to query {_I_<sub>1</sub>_,I_<sub>4</sub>_,I_<sub>7</sub>}.

