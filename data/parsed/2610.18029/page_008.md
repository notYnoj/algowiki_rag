## 3.1.1 Exact Maximum Clique Solvers

We benchmarked _IncMaxCLQ_ and _CliSAT_ on the unweighted graphs saved from our modified version of Cherry’s _compat_ tool.

Figure 1 shows the time taken as a function of the number of nodes in the graph. Both _CliSAT_ and IncMaxCLQ show a polynomial base-line for CPU growth, which can cover the bulk of the execution runs. However there are outliers which are expected to follow an exponential CPU growth. The tools can be ran with a fixed time limit, returning the best result found within that time.

Both of these tools are feasible even for relatively large numbers of nodes, and they are both considerably faster than Cherry’s implementation which ran for over a month on some of these data sets. However Cherry’s implementation is enumerating all maximum weighted cliques rather than returning a single exemplar and is thus not comparable in complexity. We could replace the greedy lower-bound clique size step in Cherry’s algorithm with _CliSAT_ to use the exact figure instead. However improving Cherry’s exact implementation is out of the scope of this work and it is unlikely to have a significant impact given the exhaustive search is still required.

## 3.1.2 Approximate Maximum Clique Solvers

The approximate solvers run for a defined length of time, returning the best clique found within that time. They also report the time taken to find that best clique, which can help with tuning the time limit, but they do not bail out early unless they can prove there is no larger clique present. Armed with knowledge of the actual maximum clique size (such as from a _CliSAT_ run), all of these approximate clique finders could be made to exit once they have found the maximum clique (or a sufficient number of them for _AClique_).

CliSAT MaxCLQ 100 10000 1000 10 100 Time (s) Time (s) 1
10 1
0.1 0.1 0.01 0.01 0
500 1000 1500 2000 2500 3000 3500 0
500 1000 1500 2000 2500 3000 3500 No. Nodes No. Nodes

Figure 1: Benchmarks of exact maximum clique solvers, _IncMaxCLQ_ and _CliSAT_. The results derived from graphs taken from random subsets of size 100 to 20,000 sequences in increments of 50. Times are the total execution time.

