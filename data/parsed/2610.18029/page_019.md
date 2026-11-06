The degree one and degree two rows in  1 are cumulative: the degree two result includes all reductions already made by the degree one rules.

## 5.2 Improving the classical pruning

The original preprocessing pipeline in [5] includes two methods to bound the resulting MWC size, and as a result eliminate vertices. We establish a minimum MWC size simply by exhibiting an example of a clique, and a vertex colouring gives an upper bound on the best clique that can contain each vertex.

The correctness of the pruning stage does not require either sampled object to be optimal. It requires only that the lower bound solution is a valid clique and that the upper bound colouring is proper. At present, we derive both the minimum clique size and vertex colouring based on simply (polynomial-time) greedy algorithms.

As such, there are instances for which these approximations will necessarily far from optimal [11, 9]. Therefore, we seek to improve on these approximation using the hybrid quantum- classical sampler, _LeapHybridSampler_, on the D-Wave platform, which while only partially quantum, allows us to tackle much larger problems sizes that purely quantum platforms would allow. Crucially, in switching to a D-Wave solver for these problems rather than the greedy algorithm on a fixed, predetermined ordering based on the number of conflicts each vertex has, we allow ourselves to obtain any (hopefully closer-to-optimal) vertex colouring.

We verify and correct each candidate classically before using it. For both tasks, this is known to be possible in polynomial time. For a candidate clique, we check every pair of selected vertices, and simply greedily remove any conflicts. For a candidate colouring, we check that the endpoints of every edge have different colours, and change one endpoint to a brand new colour in the case of any conflicts. Furthermore, we retain the original classical greedy examples. Thus, stochastic sampling can affect the strength of the reduction but not its correctness, and at worst, we recover the performance of the original classical preprocessing (albeit with a longer run time).

300 250 200 D-Wave Reduction Vertices 150 100 50 0
0 50 100 150 200 250 300 Degree 2 Reduction Vertices

1200 1000 800 D-Wave Reduction Edges 600 400 200 0
0 200 400 600 800 1000 1200 Degree 2 Reduction Edges

(a) Vertices

(b) Edges

Figure 8: The reduction of number of graph vertices and edges for SARS-CoV-2 samples between the degree 2 and D-Wave reductions.

