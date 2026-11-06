<tbc>OpenAI \[Ope26a\] recently proved \(\omega\le 9/4\) through a different use of polynomial multiplication and Strassen’s asymptotic spectrum \[Str88\]. A finite construction first separates tensor blocks that are independent on two legs but share the third. The resulting entropy inequality is applied to polynomial multiplication tensors. A determinant construction gives discrete concavity in the input lengths, and a three-sector decomposition gives a shifted tripling inequality. Together, these inequalities force a spectral profile to grow faster than the interpolation rank bound permits unless \(\omega\le 9/4\). An earlier manuscript in the same release obtained a bound below 2.258 \[Ope26b\].

For graphs with more than three vertices, it is useful to compare the exponent per edge, \(\tau(G)=\mathrm{log}_2\widetilde{\text{R}}(\mathsf{GT}_2(G))/|E(G)|\), defined for graphs with at least one edge in Definition 2.22. Christandl, Vrana, and Zuiddam \[CVZ19, Corollary 1.2.6\] generalized the Coppersmith-Winograd method and proved \(\tau(K_n)\le\mathrm{log}_7(9/2)<0.772943\) for every integer \(n\ge 4\). Their proof combines higher-order auxiliary tensors with a lower bound on the asymptotic subrank of tight tensors. Brand et al. \[BCK<sup>+</sup>26, Appendix C of the full version\] subsequently refined the four-party analysis, yielding the uniform bound \(\tau(K_n)\le 0.772318\) for \(n\ge 4\). They also used graph tensors to study the distinction between asymptotic rank and arithmetic circuit complexity for tensors with more than three legs. Christandl and Zuiddam \[CZ19\] developed tensor surgery, which transfers rank bounds through operations on the underlying graphs.

Two cut parameters give a useful perspective on these upper bounds. For every graph _G_ with at least two vertices,

\(\mathrm{log}_2\widetilde{\text{R}}\big(\mathsf{GT}_2(G)\big)\ge\mathrm{MaxCut}(G),\mathrm{log}_2\widetilde{\text{Q}}\big(\mathsf{GT}_2(G)\big)=\mathrm{MinCut}(G).\)

Here \(\widetilde{\text{Q}}\) is the asymptotic subrank from Definition 2.13, and the cuts are defined in Definition 2.23. The rank lower bound follows by flattening across a cut. The subrank identity is due to Vrana and Christandl \[VC17\]; we give a graph version of their proof in Theorem B.4. Thus, the minimum cut completely determines the asymptotic subrank. Whether the maximum cut likewise determines the asymptotic rank is the question posed by Christandl, Vrana, and Zuiddam \[CVZ19, Question 1.3.2\]. For a triangle, this question is exactly whether \(\omega=2\).

\begin{tabular}{ccc}
Year & Work & Upper bound on \(\omega\) \\
1969 & Strassen \[Str69\] & log<sub>2</sub>7_\<_2.808 \\
1979-1980 & Bini et al.; Bini \[BCRL79, Bin80\] & 2.7799 \\
1981 & Schönhage \[Sch81\] & _\<_2.522 \\
1986-1987 & Strassen \[Str86, Str87\] & _\<_2.479 \\
1990 & Coppersmith-Winograd \[CW90\] & _\<_2.375477 \\
2010 & Stothers \[Sto10, DS13\] & _\<_2.373690 \\
2012 & Vassilevska Williams \[VW12\] & _\<_2.372900 \\
2014 & Le Gall \[LG14\] & _\<_2.372864 \\
2021 & Alman-Vassilevska Williams \[AW21\] & _\<_2.372860 \\
2023 & Duan-Wu-Zhou \[DWZ23\] & _\<_2.371867 \\
2024 & Vassilevska Williams et al. \[VXXZ24\] & \(\le\)2.371552 \\
2025 & Alman et al. \[ADW<sup>+</sup>25\] & _\<_2.371339 \\
2026 & Dupont et al. \[DEK<sup>+</sup>26\] & _\<_2.371177 \\
2026 & OpenAI \[Ope26a\] & \(\le\)9/4=2.25 \\
\end{tabular}

1: Selected upper bounds for the triangle graph tensor, equivalently the matrix multiplication exponent. Years refer to the cited publications or manuscripts. Decimal bounds are rounded upward when necessary. The Vassilevska Williams row uses the corrected expanded version of the 2012 paper; the OpenAI row uses the October 2, 2026 manuscript.

