standard deviation \(\sigma=67.8\)), which is only slightly more than _n_ and significantly less than the worst-case upper bound of _n_<sup>2</sup>.

The second dataset, called PlanetLab, consists of _t_=18 snapshots of a graph on _n_=490 nodes. The average prediction error that we calculated equals \(\eta_\mathrm{mean}=12810.8\) (with the standard deviation \(\sigma=4887.4\)), which is close to _n_<sup>1.5</sup>≈10846.6.

We conclude that it is not unreasonable to hope for \(\eta\checkmark n^2\) in practice. Of course, it would be more desirable to not only calculate the prediction error but also to implement our algorithm and directly measure its running time. An obstacle to that is that our algorithm requires a fast matrix multiplication algorithm, and those theoretically fast algebraic algorithms are famously known for being impractical. This does not necessarily mean that our algorithm is hopelessly impractical as well. Indeed, given that matrix multiplication lies at the core of deep neural networks, people put a lot of engineering effort, both at software and hardware levels, to make it fast in practice. Such optimizations could also make an implementation of our algorithm competitive, but this is beyond the scope of this theory paper.

## References

**1** Anders Aamand, Justin Y. Chen, Siddharth Gollapudi, Sandeep Silwal, and Hao WU. Improved approximations for hard graph problems using predictions. In _Proceedings of the 42nd International Conference on Machine Learning, ICML 2025_. JMLR.org, 2025. URL: `https: //proceedings.mlr.press/v267/aamand25c.html`.

**2** Ittai Abraham, Shiri Chechik, and Sebastian Krinninger. Fully dynamic all-pairs shortest paths with worst-case update-time revisited. In _Proceedings of the Twenty-Eighth Annual ACM-SIAM Symposium on Discrete Algorithms, SODA 2017_, pages 440-452. SIAM, 2017. `doi:10.1137/1.9781611974782.28`.

**3** Josh Alman, Ran Duan, Virginia Vassilevska Williams, Yinzhan Xu, Zixuan Xu, and Renfei Zhou. More asymmetry yields faster matrix multiplication. In _Proceedings of the 2025 Annual ACM-SIAM Symposium on Discrete Algorithms (SODA 2025)_, pages 2005-2039. SIAM, 2025. `doi:10.1137/1.9781611978322.63`.

**4** Noga Alon and Joel H Spencer. _The probabilistic method_. John Wiley & Sons, 2016.

**5** Antonios Antoniadis, Marek Eliás, Adam Polak, and Moritz Venzin. Approximation algorithms for combinatorial optimization with predictions. In _The Thirteenth International Conference on Learning Representations, ICLR 2025_. OpenReview.net, 2025. URL: `https://openreview. net/forum?id=AEFVa6VMu1`.

**6** Benny Applebaum. Pseudorandom generators with long stretch and low locality from random local one-way functions. _SIAM Journal on Computing_, 42:2008-2037, 2013. `doi:10.1137/ 120884857`.

**7** Xingjian Bai and Christian Coester. Sorting with predictions. In _Advances in Neural Information Processing Systems 36: Annual Conference on Neural Information Processing Systems 2023, NeurIPS 2023_, 2023. URL: `http://papers.nips.cc/paper\_files/paper/ 2023/hash/544696ef4847c903376ed6ec58f3a703-Abstract-Conference.html`.

**8** Aaron Bernstein, Danupon Nanongkai, and Christian Wulff-Nilsen. Negative-weight single- source shortest paths in near-linear time. _J. ACM_, 72(4):1-34, 2025. Announced at FOCS 2022. `doi:10.1145/3742890`.

**9** Aditya Bhaskara, Moses Charikar, Eden Chlamtac, Uriel Feige, and Aravindan Vijayaraghavan. Detecting high log-densities: an o(n1⁄4) approximation for densest k-subgraph. In _Proceedings of the Forty-Second ACM Symposium on Theory of Computing, S 2010_, pages 201--210. ACM, 2010. `doi:10.1145/1806689.1806719`.

**10** Jan van den Brand. Complexity term balancer. `jvdbrand.com/complexity/`. Tool to balance complexity terms depending on fast matrix multiplication.

