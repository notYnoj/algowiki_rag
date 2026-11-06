(a)
6
Panel (a): graph family
Panel (a): simulator
4
Erdös-Rényi
random regular
line-to-full
heavy-hex
statevector
MPS
2
Best CRVG SPSA energy
0
-2
-4
-6
11
16
17 Clean instances ordered by simulator and size (node count)
17
20
22
28
30
(b)
EfficientSU2
(c)
QAOA
2.5
Best CRVG SPSA energy
0.0
-2.5
-5.0
clean
synthetic noise
clean
synthetic noise

(a)
MaxCut
(b)
MIS
0.90
1.0
0.85
0.8
Best sampled approximation ratio
Final feasible-shot fraction
0.6
0.80
0.4
0.75
0.2
0.70
0.0
1
3
5
7
1
3
5
7
QAOA depth
QAOA depth
SPSA
non-recursive CRVG
recursive CRVG

Figure 3: Relative converged performance and stability under synthetic noise. Panel (a) spans the top row and shows best-CRVG-minus-SPSA energy margins across paired clean benchmark instances. Panels (b) and (c) compactly compare clean and synthetic-noise pools for EfficientSU2 and QAOA. Negative values favor CRVG; the lower, unpaired comparisons are descriptive rather than controlled estimates of noise sensitivity.

Figure 4: Complementary QAOA depth diagnostics. Panel (a) reports MaxCut method medians and interquartile ranges of best sampled approximation ratio (formerly Fig. 5a); panel (b) reports MIS final feasible-sample fractions from a separate 256-shot diagnostic resampling (formerly Fig. 7b). The shared view emphasizes SPSA’s comparatively stable behavior across depths and problem classes.

