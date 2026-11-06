<tbc> 3 presents a comparison of all three methods. SA gives the largest mean cut fraction in all 21 cases, exceeding the TPM limit by 0.94-6.98 percentage points and the DQI upper bound by 3.64-20.87 points. Seven cases yield perfect cuts on all 16 graphs. The theoretical entries are asymptotic; the SA entries are finite-size measurements. On four evaluation graphs per parameter pair, the SA cut fractions after only 1,024 sweeps exceed both theoretical references. Increasing the budget from 65,536 to 262,144 sweeps improves the nonperfect means by less than 0.095 percentage points. At _n_=16384, using eight additional graphs per degree and 65,536 sweeps, the means differ from those at _n_=65536 by at most 0.071 percentage points.

## 4.2 Random Max-2-LINSAT

For other Max-2-LINSAT objectives, we first chose independent uniform singleton targets _C<sub>i</sub>_={_v<sub>i</sub>_}, so an oriented edge is satisfied when _x<sub>v</sub>-x<sub>u</sub>=v<sub>i</sub>_. Here _r_=1 and \(\theta(a)=1/(q-1)\) for every target vector. Substituting Eqs. (77) and (78) into the semicircle formula gives the reliable-decoding upper bound<tbc>

\(F_{1/q}(\delta_\mathrm{cyc}(D,q))=\frac{1+(q-1)Z_q(\delta_\mathrm{cyc}(D,q))}{q}=\frac{1}{q}+\frac{q-1}{q(D-1)}.\) (96)

\begin{tabular}{ccccccc}
_D_ & Method & _q_=2 & _q_=3 & _q_=5 & _q_=7 & _q_=11 \\
 & Random & 0.50000 & 0.66667 & 0.80000 & 0.85714 & 0.90909 \\
3 & DQI & 0.75000 & - & - & - & - \\
 & TPM & 0.89183 & - & - & - & - \\
 & SA & 0.92243 & - & - & - & - \\
4 & DQI & 0.66667 & 0.85553 & - & - & - \\
 & TPM & 0.83333 & 0.95549 & - & - & - \\
 & SA & 0.86671 & 1.00000 & - & - & - \\
5 & DQI & 0.62500 & 0.81427 & - & - & - \\
 & TPM & 0.79517 & 0.93381 & - & - & - \\
 & SA & 0.83374 & 0.99893 & - & - & - \\
6 & DQI & 0.60000 & 0.78764 & 0.92160 & - & - \\
 & TPM & 0.76772 & 0.91595 & 0.98105 & - & - \\
 & SA & 0.80354 & 0.98571 & 1.00000 & - & - \\
7 & DQI & 0.58333 & 0.76911 & 0.90588 & - & - \\
 & TPM & 0.74675 & 0.90112 & 0.97455 & - & - \\
 & SA & 0.78393 & 0.96962 & 1.00000 & - & - \\
13 & DQI & 0.54167 & 0.71999 & 0.85919 & 0.91607 & 0.96358 \\
 & TPM & 0.67891 & 0.84677 & 0.94473 & 0.97328 & 0.99060 \\
 & SA & 0.70968 & 0.90178 & 0.99950 & 1.00000 & 1.00000 \\
17 & DQI & 0.53125 & 0.70707 & 0.84569 & 0.90341 & 0.95320 \\
 & TPM & 0.65596 & 0.82638 & 0.93148 & 0.96439 & 0.98596 \\
 & SA & 0.68357 & 0.87517 & 0.98809 & 1.00000 & 1.00000 \\
\end{tabular}

** 3:** Fractions of edges cut for Max-_k_-Cut. DQI is the upper bound \(b_q\big(\delta_\mathrm{cyc}(D,q)\big)\) for the optimized reliable-cutoff performance in (91); TPM is the infinite-girth limit in (94). SA is the mean best cut fraction from one 65,536-sweep anneal on each of 16 independent Linial-Simkin graphs with _n_=65536 and girth at least \(\mathrm{max}\{5,\lfloor 0.9\mathrm{log}_{D-1}n\rfloor\}\). Temperature endpoints were selected on separate tuning graphs. All SA standard errors are below \(3.4\times 10^{-5}\); every SA entry of 1.00000 represents perfect cuts on all 16 graphs. Values are rounded to five decimals, and dashes mark the excluded cases \(q\ge D\).

