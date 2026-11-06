<tbc>For \(D\in\{3,5,7\}\) and \(q\in\{2,3,5\}\), SA exceeds this bound on every tested instance at each budget of 16, 1,024, and 65,536 sweeps. Each instance has one anneal per budget, with its targets held fixed. At _n_=65536, increasing the budget from 1,024 to 65,536 sweeps improves the mean satisfaction fraction by at most 2.74 percentage points across these nine singleton-target cases, with the largest increase at (_q,r,D_)=(5,1,3). At 65,536 sweeps, the means from eight instances at _n_=4096 differ from those at _n_=65536 by less than 0.08 percentage points.

We also chose each target independently and uniformly among the _r_-element subsets of F_<sub>q</sub>_, for _q_=3,5 and _r_=2_,...,q_-1.  4 collects the 65,536-sweep SA results for all studied target sizes, alongside the DQI values \(F_{r/q}(\mathrm{min}\{\delta_\mathrm{cyc}(D,q),1-r/q\})\) from Corollary 1 under the decoder assumption in the caption. SA exceeds these DQI values in every case.

## Acknowledgments

We thank Noah Shutty, Gilles Zemor, and Earl Campbell for helpful discussions. The JPMorganChase team thanks Rob Otter for the executive support of the work and all of their colleagues at the Global Technology Applied Research center for helpful feedback and support throughout the project.

O.P. was supported by the U.S. Department of Energy, Office of Science, Accelerated Research in Quantum Computing, Fundamental Algorithmic Research toward Quantum Utility (FAR-Qu). This article has been authored by an employee of National Technology & Engineering Solutions of Sandia, LLC under Contract No. DE-NA0003525 with the U.S. Department of Energy (DOE). The employee owns all right, title and interest in and to the article and is solely responsible for its contents. The United States Government retains and the publisher, by accepting the article for publication, acknowledges that the United States Government retains a non-exclusive, paid-up, irrevocable, world-wide license to publish or reproduce the published form of this article or allow others to do so, for United States Government purposes. The DOE will provide public access to these results of federally sponsored research in accordance with the DOE Public Access Plan `https://www.energy.gov/downloads/doe-public-access-plan`.

\begin{tabular}{cccccccc}
 & & \multicolumn{2}{c}{_D_=3} & \multicolumn{2}{c}{_D_=5} & \multicolumn{2}{c}{_D_=7} \\
_q_ & _r_ & SA & DQI & SA & DQI & SA & DQI \\
2 & 1 & 0.9223 & 0.7500 & 0.8337 & 0.6250 & 0.7840 & 0.5833 \\
3 & 1 & 0.8870 & 0.6667 & 0.7636 & 0.5000 & 0.6969 & 0.4444 \\
3 & 2 & 1.0000 & 0.9259 & 0.9990 & 0.8143 & 0.9696 & 0.7691 \\
5 & 1 & 0.8497 & 0.6000 & 0.6968 & 0.4000 & 0.6148 & 0.3333 \\
5 & 2 & 0.9999 & 0.8000 & 0.9159 & 0.6192 & 0.8438 & 0.5511 \\
5 & 3 & 1.0000 & 0.9328 & 1.0000 & 0.8000 & 0.9812 & 0.7419 \\
5 & 4 & 1.0000 & 0.9983 & 1.0000 & 0.9423 & 1.0000 & 0.9059 \\
\end{tabular}

** 4:** Mean satisfied fractions for random target sets of size _r_ at _n_=65536 and _c_=0.9. SA uses one 65,536-sweep anneal per instance, with eight independent graph/target instances for _r_=1 and four for _r\>_1; all standard errors are below \(1.4\times 10^{-4}\). DQI gives the asymptotic mean satisfaction fraction with optimized binomial amplitudes, assuming a target-independent decoder reliable up to the ML cycle bound. For intermediate target sizes, these values do not bound decoders that exploit the individual target sets. Values are rounded to four decimal places; a displayed 1.0000 can therefore include a small number of unsatisfied constraints.

