# Pinning Down the Strong Wilber 1 Bound for Binary Search Trees

**Abstract**

The dynamic optimality conjecture, postulating the existence of an _O_(1)-competitive online algorithm for binary search trees (BSTs), is among the most fundamental open problems in dynamic data structures. Despite extensive work and some notable progress, including, for example, the Tango Trees (Demaine et al., FOCS 2004), that give the best currently known _O_(loglog_n_)-competitive algorithm, the conjecture remains widely open. One of the main hurdles towards settling the conjecture is that we currently do not have approximation algorithms achieving better than an _O_(loglog_n_)-approximation, even in the offline setting. All known non- trivial algorithms for BST’s so far rely on comparing the algorithm’s cost with the so-called Wilber’s first bound (WB-1). Therefore, establishing the worst-case relationship between this bound and the optimal solution cost appears crucial for further progress, and it is an interesting open question in its own right.

Our contribution is two-fold. First, we show that the gap between the WB-1 bound and the optimal solution value can be as large as \(\Omega(loglogn/logloglogn)\); in fact, the gap holds even for several stronger variants of the bound. Second, we provide a simple algorithm, that, given an integer _D\>_0, obtains an _O(D_)-approximation in time \(exp\left(O\left(n^{1/2^{\Omega(D)}}logn\right)\right)\). In particular, this gives a constant-factor approximation sub-exponential time algorithm. Moreover, we obtain a simpler and cleaner efficient _O_(loglog_n_)-approximation algorithm that can be used in an online setting. Finally, we suggest a new bound, that we call _Guillotine Bound_, that is stronger than WB, while maintaining its algorithm-friendly nature, that we hope will lead to better algorithms. All our results use the geometric interpretation of the problem, leading to cleaner and simpler analysis.

<sup>∗</sup>Aalto University, Finland. Email: `challermsook@gmail.com`. Supported by European Research Council (ERC) under the European Unions Horizon 2020 research and innovation programme (grant agreement No. 759557) and by Academy of Finland Research Fellows, under grant No. 310415 <sup>†</sup>Toyota Technological Institute at Chicago. Email: `cjulia@ttic.edu`. Part of the work was done while the author was a Weston visiting professor at the Department of Computer Science and Applied Mathematics, Weizmann Institute of Science. Supported in part by NSF grant CCF-1616584. <sup>‡</sup>Toyota Technological Institute at Chicago. Email: `saranurak@ttic.edu`.

Parinya Chalermsook<sup>∗</sup>

Julia Chuzhoy<sup>†</sup>

Thatchaphol Saranurak <sup>‡</sup>

December 24, 2019

arXiv:1912.02900v2 [cs.DS] 21 Dec 2019

