## 6 Implementation and Evaluation

### Implementation.

We implemented a constraint solver MuVal that supports invariant synthesis and ranking function synthesis. For invariant synthesis, we apply an ordinary decision tree learning (see \[12, 14, 18, 22, 35\] for existing techniques). For ranking function synthesis, we implemented the algorithm in Sect. 5 with both eager and lazy strategies for halfspace selection. Our synthesizer uses well-founded relation explained in Sect. 5.5. Given a benchmark, we run our solver for both termination and non-termination verification in parallel, and when one of the two returns an answer, we stop the other and use the answer. MuVal is written in OCaml and uses Z3 as an SMT solver backend. We used clang and llvm2kittel \[1\] to convert C benchmarks to T2 \[3\] format files, which are then translated to pwCSP by MuVal.

### Experiments.

We evaluated our implementation MuVal on C benchmarks from Termination Competition 2020 (C Integer) \[4\]. We compared our tool with AProVE \[10, 13\], iRankFinder \[7\], and Ultimate Automizer \[21\]. Experiments are conducted on StarExec \[2\] (CentOS 7.7 (1908) on Intel(R) Xeon(R) CPU E5-2609 0 @ 2.40GHz (2393 MHZ) with 263932744 kB main memory). The time limit was 300 seconds.

### Results.

Results are shown in  2. Yes/No/TO/U means the number of benchmarks that these tools could verify termination/- could verify non-termination/could not answer within 300 seconds and timed out (<u>Time</u><u>Q</u>ut)/gave up before 300 seconds (<u>U</u><u>Unknown</u>), respectively. We also show scatter plots of runtime in Fig. 7.

MuVal was able to solve more benchmarks than Ultimate Automizer. Compared to iRankFinder, MuVal solved slightly fewer benchmarks, but was faster in a large number of benchmarks: 265 benchmarks were solved faster by MuVal, 68 by iRankFinder, and 2 were not solved by both tools within 300 seconds (here, we regard U (unknown) as 300 seconds). Compared to AProVE, MuVal solved fewer benchmarks. However, there are several benchmarks that MuVal could solve but AProVE could not. Among them is "TelAviv-AmirMinimum\_true-termination.c", which does require piecewise affine ranking functions. MuVal found a ranking function \(f(x,y)=\text{\textbf{if}}x-y\ge 0\text{\textbf{then}}y\text{\textbf{else}}x\text{, while AProVE timed out.}\)

We also observed that using CEGIS with transition examples itself showed its strengths even for benchmarks that do not require piecewise affine ranking functions. Notably, there are three benchmarks that MuVal could solve but the<tbc>

<sup>5</sup> We removed one benchmarks from the result of iRankFinder because the answer was wrong.

\begin{tabular}{ccccc}
 & Yes & No & TO & U \\
MuVal (eager) & 204 & 89 & 42 & 0 \\
MuVal (lazy) & 200 & 84 & 51 & 0 \\
AProVE & 216 & 100 & 16 & 3 \\
iRankFinder & 208 & 92<sup>5</sup> & 0 & 34 \\
Ultimate Automizer & 180 & 83 & 2 & 70 \\
\end{tabular}

2: Numbers of solved benchmarks

