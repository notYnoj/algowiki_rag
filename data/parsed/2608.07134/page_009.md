Let us summarize the entire step of handling _many deletions_. Suppose the operation sequence S with _n_ insertions contains more than _n/_2 successful deletions, and suppose we execute `ReverseHeapEval(S)` with a soft max-heap with error parameter \(\varepsilon=1/4\). Then, at the end of the execution, the soft heap contains at least _n/_4 uncorrupted elements, all of which belong to \(\mathcal{D}(\varnothing,\mathcal{S})\). By the previous discussion, we can remove the insertions of these elements, together with their corresponding deletions, in linear time, reducing the problem from S to \(\mathcal{S}'\), thereby reducing the problem size by a constant factor.

The heap evaluation algorithm. We can now state the complete linear-time heap evaluation procedure (Algorithm 2). The correctness of the algorithm follows from the discussion above. Note that every iteration of the while-loop takes O(_n_) time, and after each iteration, _n_ decreases by a factor of at least 4/3. Summing the geometric series yields O(_n_) total time, proving Theorem 1.1.

### 2.1 Maximum-Profit Unit-Time Scheduling

As a corollary of Theorem 1.1, we give a linear-time algorithm for the single-machine _maximum- profit unit-time scheduling_ (mputs) problem. In this problem, we have _n_ unit-time jobs released at time 0, each job _j_ with an integer due date _d<sub>j</sub>_ and a nonnegative profit _w<sub>j</sub>_. The task is to schedule the execution of the jobs on a single machine, without overlap, maximizing the sum of profits of jobs completed by their due dates.<sup>7</sup> In the standard scheduling notation, this problem is \(1|p_j=1|\sum_jw_jU_j\). We show the following result.

<sup>7</sup> An alternative interpretation of the problem is the following: given a bipartite graph in which each vertex on the left is connected to a prefix of vertices on the right, the task is to compute a matching that maximizes the total weight of the matched vertices on the left.

LinearTimeHeapEval(S) begin Remove unsuccessful deletions from S A ← ∅ // Accumulating answer while S is nonempty do 5
n ← number of insertions in S 6
δ ← number of deletions in S 7
if δ ≤ n/2 then 8
Hmin ← SoftMinHeap() with ε = 1/4 Run TrivialHeapEval(S) with Hmin instead of the min-heap 9
U ← the set of uncorrupted elements in Hmin 10 A ← A ∪ U Remove insertions of elements in U from S 11 else Hmax ← SoftMaxHeap() with ε = 1/4 Run ReverseHeapEval(S) with Hmax instead of the max-heap 12 13 14 15 16 U ← the set of uncorrupted elements in Hmax Remove insertions of elements in U and corresponding deletions from S return A 18 Algorithm 2 Linear-time algorithm for the heap evaluation problem.

