<tbc>_M_=5597; the shaded interval indicates this observation, not an estimated exact threshold. Both axes are logarithmic, and the line segments only connect measurements.

At _N_=600, the dense routine is faster for alphabet sizes 4, 16, and 64. The sparse routine becomes faster at the tested alphabet size 256, and its advantage grows as matches become rarer. The measured ratio ranges from approximately 0.21 at \(\sigma=4\) to 26.32 at \(\sigma=4096\). In the \(\sigma=N\) series it increases from 2.39 at _N_=200 to 11.19 at _N_=1600. These observations illustrate the cost of managing matches and the benefit of avoiding a full grid scan. They do not locate a universal crossover.

We have not implemented and validated LCBS adaptations of the adaptive LCIS methods of Chan et al. [5] and Kutz et al. [6], so the experiments compare only our two reference implementations. A like-for-like comparison through Proposition 2.1 must include both passes, per-match outputs, and reconstruction; timing an LCIS-only solver would measure a different task. This omission establishes no barrier to adaptation, and the results imply no superiority over those methods. The study also excludes optimized native implementations and peak-memory measurements; its single machine, synthetic inputs, and small seed sample do not support broad application claims. Python allocation, dictionary lookup, cache effects, and system load influence absolute times. Earlier application-oriented measurements are not used because their original scripts and logs were unavailable.

## 8. Conclusion

LCBS can be solved constructively by joining compatible increasing and decreasing endpoint states at a common match. Reporting these states is the precise interface needed to reuse LCIS techniques.

1
Dense
Observed
switch interval
Match-sensitive
0.1
Median runtime (seconds)
0.01
n = m = 600
0.001
102
103
104
105
Median number of matches M

Figure 2. Runtime comparison on the six density-series configurations with _n=m_=600. Each point uses the same aggregate runtime and median match count as  1. Dashed squares denote the dense baseline; solid circles denote the match-sensitive implementation. The shaded band lies between adjacent tested configurations where the faster method changes. No measurements within that band or universal crossover are claimed.

