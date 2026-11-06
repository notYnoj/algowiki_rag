## 1.3 Shortest Paths in Directed Acyclic Unweighted Graphs

Finally, we study MSSP on directed unweighted graphs, whose running time landscapes seem to be more complicated. Consider APSP as an example. APSP for undirected unweighted graphs runs in \(\widehat{O}(n^\omega)\) time \[Sei95\], while APSP for directed unweighted graphs runs in \(\widehat{O}(n^{2+\mu})\) time \[Zwi02\], where \(\mu\le 0.528\) \[ADV<sup>+</sup>25\] is the solution to \(\omega(1,\mu,1)=2+\mu\). As we can see, even representing the running time requires more effort in the directed case.

One can rephrase the running time of Zwick’s algorithm as<tbc>

\(\widetilde{O}\left(\mathrm{max}_{1\le t\le n}\mathsf{T}_\mathrm{MPP}(n,t,n|n/t)\right),\)

<tbc>as observed in \[CVX21\]. In fact, \[CVX21\] showed that the running time for APSP in directed unweighted graphs is exactly<tbc>

\(\widetilde{\Theta}\left(\mathrm{max}_{1\le t\le n}\mathsf{T}_\mathrm{MPP}(n,n/t,n|t)\right).\)

<tbc>Grandoni and Vassilevska Williams \[GV19\] gave an algorithm that can solve MSSP on directed unweighted graphs<sup>7</sup>, and the running time of their algorithm can be phrased as (let _s_=|_S_<sub>in</sub>|)<tbc>

\(\widetilde{O}\left(\mathrm{max}_{1\le t\le n}\mathsf{T}_\mathrm{MPP}(s+t,t,n|n/t)\right),\) (1)

<tbc>Based on the approach in \[CVX21\], we can show the following lower bound for MSSP on directed unweighted graphs:

\(\Omega\left(\mathrm{max}_{1\le t\le n}\mathsf{T}_\mathrm{MPP}(s,t,n|n/\mathrm{min}(s,t),n/t)\right),\) (2)

where T<sub>MPP</sub>(_a,b,c|B_<sub>1</sub>_,B_<sub>2</sub>) denotes the running time for Min-Plus product instances between an \(a\times b\) matrix with entries from \([B_1]\cup\{\infty\}\) and a \(b\times c\) matrix with entries from \([B_2]\cup\{\infty\}\).

Grandoni and Vassilevska Williams’s algorithm \[GV19\] is actually optimal for sufficiently large _s_. To see this, let _s_ be large enough so that the maximizer _t_<sup>∗</sup> for Equation (1) is less than or equal to _s_. In this case, their running time simplifies to \(\widetilde{O}\left(\mathsf{T}_\mathrm{MPP}\left(s,t^*,n|n/t^*\right)\right)\), which matches T<sub>MPP</sub>(_s,t,n|n/_min(_s,t),n/t_) by setting _t=t_<sup>∗</sup>. On the other hand, their running time is not optimal for small values of _s_. By setting _t=n_<tbc>

<sup>7</sup>Their algorithm is actually more general and can be used to solve multiple-source multiple-target shortest paths.

Comparison of Algorithms for computing MSR
2.6
This Work Elkin and Trehan Baseline
2.5
2.4
2.3
Runtime exponent
2.2
2.1
2.0
0.0
0.2
0.4 S_in size exponent
0.6
0.8
1.0

Figure 1: Comparison of running times of algorithms for Multiple-Source Reachability on dense graphs when \(|S_\mathrm{in}|=n^\sigma\). The baseline algorithm (yellow line) runs in time \(\widehat{O}(\mathrm{min}(n^{2+\sigma},n^\omega))\). The algorithm of Elkin and Trehan (blue line) runs in time \(\widehat{O}(n^{1+2\omega(\sigma,1,1)/3})\). Note that the figure also illustrates our improvement over the baseline algorithm for undirected MSSP, since the baseline algorithms are identical for undirected MSSP and Multiple-Source Reachability.

