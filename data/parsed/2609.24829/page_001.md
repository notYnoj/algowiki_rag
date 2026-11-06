# Parameter-Free Triangle Counting

**Abstract**

Given an undirected, unweighted graph, the triangle counting problem seeks the number of occurrences of three-cycles in a graph dataset. Triangle and, more generally, subgraph counting are classical and important problems in graph algorithms. These problems are central to a wide variety of applications, including community detection, computing the clustering coefficient, motif discovery in protein networks, and broad social network analysis. In many of these applications, the graph datasets are so voluminous or are collected via incremental updates that we model them as streams of updates to an underlying graph. It is in this model that we seek to count the number of triangles _T_ in a graph _G_=(_V,E_) with _n_ vertices and _m_ edges.

There are a number of foundational results for the streaming triangle counting problem, both theoretical in nature and developed for practical application. There is, however, one major drawback to _all_ previous constant space algorithms: to achieve both a constant factor approximation to the triangle count and to obtain the sublinear space guarantees of these algorithms, one needs to know _a priori_ a constant factor approximation of the triangle count. Thus, to obtain the best space guarantees for estimating the number of triangles, one must already have a good estimation of the number of triangles! This requirement is inherently circular.

We initiate the study of _parameter-free streaming triangle counting_, without any _a priori_ knowledge of _T_ or any quantities depending on _T_, provided _m_, the length of the stream. We describe a family of _O(p_) pass parameter-free triangle counting algorithms that guarantee a mixed multiplicative and additive approximation of _T_ and use \(\widetilde{O}\left(\frac{m+T}{\sqrt{T}}\right)\) expected space. Moreover, this family leads to an _O_(loglog(_n_)) pass algorithm that gives a \((1+\varepsilon)\) multiplicative approximation of _T_ with the same space complexity. These algorithms rely on the notion of a _verified_ parametrized algorithm: An algorithm that is parametrized by \(\tau\) and which provides either an approximation of _T_ when \(\tau\le T\), or declares that \(T<\tau\). Furthermore, we demonstrate a lower bound: any parameter-free algorithm that provides a multiplicative approximation for all values of _T_ must use \(\Theta(m)\) space, even on streams where the actual triangle count is moderately large.

<sup>∗</sup>Department of Applied Mathematics, Yale University <sup>†</sup>Department of Statistics and Data Science, Yale University <sup>‡</sup>Department of Computer Science, Yale University <sup>§</sup>Manning College of Information & Computer Sciences, University of Massachusetts Amherst

Asaf Etgar<sup>∗</sup><br>
Anna Gilbert<sup>†</sup><br>
Quanquan Liu<sup>‡</sup><br>
Andrew McGregor<sup>§</sup>

