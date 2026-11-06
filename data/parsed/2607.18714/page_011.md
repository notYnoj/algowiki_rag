<tbc>the lemma. By definition, \(\alpha_\alpha\) is the closest vertex to s on the st path whose distance from \(pivot_\alpha(\alpha_\alpha)\) is at most 1. If \(b_\alpha\) were closer, it would violate this definition. Hence \(\alpha_\alpha\) lies closer to s than \(b_\alpha\), or both vertices coincide. We now prove the second part of the lemma. Since p<sub>s</sub> lies closer to s than p<sub>t</sub> on the st path we obtain the following relation.

\(|p_sp_t|=|st|-|sp_s|-|tp_t|\)

<tbc>Since p<sub>s</sub> lies on the boundary of \(ball_\alpha(s)\), \(|sp_s|=|spivot_\alpha(s)|-1\). Similarly, \(|tp_t|=|tpivot_\alpha(t)|-1\). Thus, we get:<tbc>

\(=|st|-(|spivot_\alpha(s)|-1)-(|tpivot_\alpha(t)|-1)\)

<tbc>Using Theorem 4.1, \(|spivot_\alpha(s)|\ge\left\lfloor\frac{|st|}{2}\right\rfloor-c'+1\). Similarly, \(|tpivot_\alpha(t)|\ge\left\lfloor\frac{|st|}{2}\right\rfloor-c'+1\). Substituting these, we get:

\(\le|st|-2\left(\left\lfloor\frac{|st|}{2}\right\rfloor-c'\right)\)<br>
\(=|st|-2\left\lfloor\frac{|st|}{2}\right\rfloor+2c'\)<br>
\(\le|st|-(|st|-1)+2c'\)<br>
\(=2c'+1\)

Setting \(c=2c'+1\), we get:

\(=c\)

We now follow our approach as described in the overview. For each \(x\in V\) , we compute a set ESTIMATEDCLOSE(x) as defined in the overview. For each candidate vertex x, we divide the algorithm into two cases based on the size of ESTIMATEDCLOSE(x):

## 4.1 Sparse Case: \(|ESTIMATEDCLOSE(x)|\le n^{0.875}\)

In this case, we repeat Algorithm 1. We first call the function BUILDCLOSE, in which we construct the set ESTIMATEDCLOSE(x) for each \(x\in V\) . We then run Algorithm 3, which is essentially Algorithm 1 from the overview with two changes: we process x only when ESTIMATEDCLOSE(x) is small, and we pair x only with vertices in ESTIMATEDCLOSE(x).

Using the analysis from the overview, and setting x := p<sub>s</sub> as in Algorithm 1, we obtain an additive c+1 approximation of the st path using Equation (1). We now analyze the running time of the algorithm.

\begin{tabular}{cc}
\multicolumn{2}{c}{**Algorithm 2:** BUILDCLOSE} \\
1 & foreach \(x\in V\) do \\
2 & ESTIMATEDCLOSE(x) \(\leftarrow\emptyset\) \\
3 & foreach \(y\in V\) do \\
4 & if \(est(x,y)\le 2c+1\) \\
5 & then \\
\multirow{2}{*}{\_} & add y to \\
 & ESTIMATEDCLOSE(x) \\
\end{tabular}

\begin{tabular}{cc}
\multicolumn{2}{c}{**Algorithm 3:**} \\
1 & foreach \(x\in V\) such that \\
2 & \(|ESTIMATEDCLOSE(x)|\le n^{0.875}\) do \\
3 & foreach \(y\in ESTIMATEDCLOSE(x)\) do \\
4 & foreach \((s,t)\) in \(cluster_\alpha(x)\times cluster_\alpha(y)\) do \\
5 & est(s,t)= \\
\multirow{2}{*}{\_} & min \\
 & est(s,t), \\
\end{tabular}

