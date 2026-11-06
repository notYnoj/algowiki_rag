<tbc>per point to `ibm\_fez` and `ibm\_marrakesh`, comparing the resulting hardware approximation ratio (AR) against a shot-matched Aer simulation at the identical parameters.

4 reports all four backend/seed pairs collected. CRVG’s hardware AR exceeds SPSA’s in every pair, but the two seeds illustrate different mechanisms. At seed 42, CRVG and SPSA are essentially tied in simulation (0.623 vs. 0.628); on hardware, CRVG’s AR degrades less from sim to hardware than SPSA’s on both backends (-0.162/-0.099 vs. -0.227/-0.141), and its hardware energy variance is also lower on both backends (36.2/27.9 vs. 44.8/33.7), so the hardware result breaks a simulation-side tie in CRVG’s favor on both metrics. At seed 43, CRVG instead converges to a materially better simulated optimum than SPSA (0.521 vs. 0.347), and that advantage simply carries through to hardware (0.375 vs. 0.242); here CRVG’s sim-to-hardware AR gap (-0.146) is not smaller than SPSA’s (-0.104), and its hardware energy variance is essentially tied with SPSA’s (34.2 vs. 33.5), so this pair does not support a noise-robustness claim, only a better-starting-point one.

We also transpiled and submitted the QAOA ansatz on hardware, but exclude it from any CRVG-vs-SPSA judgment: at this instance size QAOA transpiles to `isa\_depth`≈1280-1310, roughly 13-14\(\times\) deeper than the EfficientSU2 circuit above, and its hardware AR collapsed toward the noise floor for both optimizers. We attribute this to the depth confound rather than to either optimizer, and do not treat it as evidence.

This check is a single instance, two backends, and two seeds, so it is a replicated early signal rather than a settled result, and it does not substitute for the paired, multi-seed, matched-budget confirmatory study described above. Within that scope, it is the first evidence in this line of work that CRVG’s simulation-side behavior is not an artifact of noiseless simulation: its converged parameters transfer to real superconducting hardware at least as well as SPSA’s, and in one of two seeds tested, better.

\begin{tabular}{cccccc}
Seed & Method & Sim AR & HW AR & \(\Delta\) & HW variance \\
42 & SPSA & 0.628 & 0.401 & -0.227 & 44.8 \\
42 & Non-recursive CRVG & 0.623 & **0.461** & -0.162 & **36.2** \\
42 & SPSA & 0.628 & 0.487 & -0.141 & 33.7 \\
42 & Non-recursive CRVG & 0.623 & **0.524** & -0.099 & **27.9** \\
43 & SPSA & 0.347 & 0.242 & -0.104 & 33.5 \\
43 & Non-recursive CRVG & 0.521 & **0.375** & -0.146 & 34.2 \\
\end{tabular}

(a)
MaxCut
(b)
MIS
1.4
1.4
1.3
Sampled-objective calls / SPSA
Sampled-objective calls / SPSA
1.2
1.2
1.1
1.0
1.0
0.9
0.8
0.8
0.7
0.6
0.6
1
3
5
7
1
3
5
7
MaxCut QAOA depth
MIS QAOA depth
non-recursive CRVG
recursive CRVG

Figure 5: Paired sampled-objective-call ratios for local QAOA runs on (a) MaxCut and (b) MIS (formerly Figs. 6 and 8). Each point compares CRVG with SPSA on the same graph and depth; horizontal segments are medians, and the line at one denotes equal exposure. Values below one use fewer calls than SPSA and must be interpreted jointly with the depth-dependent quality and feasibility evidence.

4: Real-hardware approximation ratios and hardware output-energy variance for already-converged EfficientSU2 parameters, one 18-node instance, no on-hardware re-optimization. Two backends (`ibm\_fez` and `ibm\_marrakesh`) are used. \(\Delta\) is hardware AR minus simulated AR.

