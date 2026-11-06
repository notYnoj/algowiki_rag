## 6.4 An \(O(n^\kappa)\) Time Algorithm via Bootstrapping

In this section, we present a general framework to reduce the running time for LIS approximation at the expense of worse approximation factor.

Let us move a step backward and analyze the previous algorithm for obtaining an \(O(\lambda^3)\) approximate solution. We first divide the input array into \(\sqrt{n}\) subarrays of size \(\sqrt{n}\) and after constructing the pseudo-solutions, we sample \(O(\lambda^4)\) subarrays to estimate the size of the solution for pseudo- solutions. The reason we set the size of the subarrays to \(\sqrt{n}\) is that there is a trade-off between the first and the last steps of the algorithm. More precisely, if we have more than \(\sqrt{n}\) subarrays then the number of samples we draw in the beginning would exceed \(O_\lambda(\sqrt{n})\). On the other hand, having fewer than \(\sqrt{n}\) subarrays results in larger subarrays which would be costly in the last step.

If one favors the running time over the approximation factor, the following improvement can be applied to the algorithm: In the last step of the algorithm, instead of sampling the entire subarrays and computing lis for every pseudo-solution, we recursively call the same procedure to approximate the size of the solution for each subarray. This way, having large subarrays would no longer be an issue and therefore we can have fewer subarrays to improve the number of samples we draw in the first step of the algorithm.

More formally, in order to obtain a running time of \(O(\mathrm{poly}(\lambda)n^\kappa)\) for any constant \(0<\kappa<1\), we set the size of each subarray to \(n^{1-\kappa}\) and therefore after constructing the pseudo-solutions, the problem boils down to approximating the solution for \(\mathrm{poly}(\lambda)\) many subarrays of length \(n^{1-\kappa}\). By running the same algorithm, we would have \(n^\kappa\) subarrays of length \(n^{1-2\kappa}\) in the second iteration. After \(1/\kappa-1\) iterations, the subarrays are small enough and we can access all their elements in time \(O(\mathrm{poly}(\lambda)n^\kappa)\). Of course, this imposes a factor of \(\mathrm{poly}(\lambda)\) to the approximation.

By generalizing the ideas from previous subsections, we show that if there is an algorithm for LIS with approximation factor \(f(\lambda)\), then we can get a \(\left(f\left(\frac{\lambda^4}{2^{32}}\right)\cdot\frac{\lambda^4}{2^{33}}\right)\)-approximate LIS algorithm with better running time using the \(f(\lambda)\)-approximate algorithm as a subroutine.

**Lemma 6.9.** _Assume we partition the sequence into_ \(\zeta\) _subarrays, where_ \(\zeta\) _is polynomially related to the length of the input sequence. For parameter_ \(\lambda\in(0,1)\)_, let_ Oracle _be a_ \(f(\lambda)\)_-approximate LIS algorithm (with respect to a domain interval) with running time_ \(g(n,\lambda)\) _and success probability_ \(1-\mathrm{exp}(-\Omega(\mathrm{log}^2n))\) _where n is the length of the input sequence. Then Algorithm 11 using_ Oracle<tbc>

LIS [e,r](a)
> ne
Divide a into ne subarrays
|a| < ne
Construct the candidate solution domains
Use the O(|a|) solution
Sample poly(A) many subarrays
Construct the pseudo-solutions

Figure 5: The flowchart of the \(O_\lambda(n^\epsilon)\) time algorithm is shown.

