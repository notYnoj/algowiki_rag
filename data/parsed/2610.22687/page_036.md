\begin{tabular}{cccc}
design variables (`ixc`) & objective & equality constraints (`icc`) & inequality constraints (`icc`) \\
2 \(B_\mathrm{t}(R_0)\in[0.01,20]\) T & -14 max _t_burn & 1 \(\langle\beta\rangle\) consistency & 5 \(\langle n_\mathrm{e}\rangle\le n_\mathrm{lim}\) \\
3 \(R_0\in[8,8.6]\) m & & 2 Power balance & 8 \(q_\mathrm{n}\le\) max \\
4 \(\langle T_\mathrm{e}\rangle\in[5,150]\) keV & & 11 Radial build & 13 \(t_\mathrm{burn}\ge\) min \\
5 \(\langle\beta\rangle\in[0.001,1]\) & & 30 \(P_\mathrm{aux}\le\) max & 15 \(P_\mathrm{sep}\ge P_\mathrm{LH}\) \\
6 \(\langle n_\mathrm{e}\rangle\in[2\times 10^{19},1\times 10^{21}]\) m<sup>-3</sup> & & & 16 \(P_\mathrm{net}\ge\) min \\
13 TF inboard leg thickness \(\in[0.3,5]\) m & & & 24 \(\langle\beta\rangle\le\) max \\
16 CS radial thickness \(\in[0.1,10]\) m & & & 26 \(j_\mathrm{CS}\le j_\mathrm{crit}\) (EOF) \\
18 \(q_{95}\in[3.6,50]\) & & & 27 \(j_\mathrm{CS}\le j_\mathrm{crit}\) (BOP) \\
29 Bore radius \(\in[0.1,10]\) m & & & 31 \(\sigma_\mathrm{TF},\mathrm{case}\le\) max \\
37 \(j_\mathrm{CS},\mathrm{EOF}\in[100000,1\times 10^8]\) Am<sup>-2</sup> & & & 32 \(\sigma_\mathrm{TF},\mathrm{conduit}\le\) max \\
41 \(j_\mathrm{CS},\mathrm{BOP}/j_\mathrm{CS},\mathrm{EOF}\in[0.001,1]\) & & & 33 \(j_\mathrm{TF},\mathrm{WP}\le j_\mathrm{crit}\) \\
44 \(f_\mathrm{NI}\in[0.001,1]\) & & & 34 \(V_\mathrm{TF}\le\) max \\
56 \(\tau_\mathrm{Q}\in[0.1,100]\) s & & & 35 \(j_\mathrm{TF},\mathrm{WP}\le j_\mathrm{quench}\) \\
57 TF nose case thickness \(\in[0.05,1]\) m & & & 36 \(\Delta T_\mathrm{TF}\ge\) min \\
58 TF turn conduit thickness \(\in[0.008,0.1]\) m & & & 60 \(\Delta T_\mathrm{CS}\ge\) min \\
59 \(f_\mathrm{Cu}\in[0.5,0.94]\) & & & 62 \(\tau_\alpha/\tau_\mathrm{E}\ge\) min \\
109 \(\langle n_{\alpha,\mathrm{th}}\rangle/\langle n_\mathrm{e}\rangle\in[0.05,0.15]\) & & & 65 \(\sigma_\mathrm{VV},\mathrm{quench}\le\) max \\
122 CS turn steel fraction \(\in[0.001,0.95]\) & & & 68 \(P_\mathrm{sep}B_\mathrm{T}/(q_{95}AR_0)\le\) max \\
135 \(n_\mathrm{Xe}/n_\mathrm{e}\in[1\times 10^{-8},0.01]\) & & & 72 \(\sigma_\mathrm{CS},\mathrm{Tresca}\le\) max \\
 & & & 81 \(n_{e0}\ge n_{\mathrm{e},\mathrm{ped}}\) \\
 & & & 90 \(N_\mathrm{cycles},\mathrm{CS}\ge\) min \\
\end{tabular}

\begin{tabular}{cccc}
design variables (`ixc`) & objective & equality constraints (`icc`) & inequalities (`icc`; evaluated at the solution, not imposed) \\
4 \(\langle T_\mathrm{e}\rangle\in[5,25]\) keV & none (root & 1 \(\langle\beta\rangle\) consistency & 5 \(\langle n_\mathrm{e}\rangle\le n_\mathrm{lim}\) \\
6 \(\langle n_\mathrm{e}\rangle\in[5\times 10^{19},5\times 10^{20}]\) m<sup>-3</sup> & find) & 2 Power balance & 9 \(P_\mathrm{fus}\le\) max \\
29 Bore radius \(\in[0.1,0.8]\) m & & 11 Radial build & 15 \(P_\mathrm{sep}\ge P_\mathrm{LH}\) \\
 & & & 16 \(P_\mathrm{net}\ge\) min \\
 & & & 17 \(f_\mathrm{rad}\le\) max \\
 & & & 24 \(\langle\beta\rangle\le\) max \\
 & & & 30 \(P_\mathrm{aux}\le\) max \\
 & & & 31 \(\sigma_\mathrm{TF},\mathrm{case}\le\) max \\
 & & & 32 \(\sigma_\mathrm{TF},\mathrm{conduit}\le\) max \\
 & & & 33 \(j_\mathrm{TF},\mathrm{WP}\le j_\mathrm{crit}\) \\
 & & & 46 \(I_\mathrm{p}/I_\mathrm{rod}\le\) max \\
 & & & 56 \(P_\mathrm{sep}/R_0\le\) max \\
 & & & 62 \(\tau_\alpha/\tau_\mathrm{E}\ge\) min \\
 & & & 67 \(q_\mathrm{FW},\mathrm{rad}\le\) max \\
 & & & 81 \(n_{e0}\ge n_{\mathrm{e},\mathrm{ped}}\) \\
\end{tabular}

\begin{tabular}{cccc}
design variables (`ixc`) & objective & equality constraints (`icc`) & inequality constraints (`icc`) \\
4 \(\langle T_\mathrm{e}\rangle\in[5,25]\) keV & -5 max _Q_ & 1 \(\langle\beta\rangle\) consistency & 5 \(\langle n_\mathrm{e}\rangle\le n_\mathrm{lim}\) \\
5 \(\langle\beta\rangle\in[0.01,1]\) & & 2 Power balance & 9 \(P_\mathrm{fus}\le\) max \\
6 \(\langle n_\mathrm{e}\rangle\in[5\times 10^{19},5\times 10^{20}]\) m<sup>-3</sup> & & 11 Radial build & 15 \(P_\mathrm{sep}\ge P_\mathrm{LH}\) \\
10 \(H\in[0.8,1.2]\) & & & 16 \(P_\mathrm{net}\ge\) min \\
16 CS radial thickness \(\in[0.03,0.5]\) m & & & 17 \(f_\mathrm{rad}\le\) max \\
18 \(q_{95}\in[3,20]\) & & & 24 \(\langle\beta\rangle\le\) max \\
29 Bore radius \(\in[0.1,0.8]\) m & & & 30 \(P_\mathrm{aux}\le\) max \\
57 TF nose case thickness \(\in[0.01,0.5]\) m & & & 31 \(\sigma_\mathrm{TF},\mathrm{case}\le\) max \\
93 Inboard shield thickness \(\in[0.01,1]\) m & & & 32 \(\sigma_\mathrm{TF},\mathrm{conduit}\le\) max \\
109 \(\langle n_{\alpha,\mathrm{th}}\rangle/\langle n_\mathrm{e}\rangle\in[0.001,1]\) & & & 33 \(j_\mathrm{TF},\mathrm{WP}\le j_\mathrm{crit}\) \\
135 \(n_\mathrm{Xe}/n_\mathrm{e}\in[1\times 10^{-8},0.01]\) & & & 46 \(I_\mathrm{p}/I_\mathrm{rod}\le\) max \\
140 TF winding pack radial thickness \(\in[0.4,0.8]\) m & & & 56 \(P_\mathrm{sep}/R_0\le\) max \\
145 \(f_\mathrm{GW},\mathrm{ped}\in[0.1,1]\) & & & 62 \(\tau_\alpha/\tau_\mathrm{E}\ge\) min \\
152 \(f_\mathrm{GW},\mathrm{sep}\in[0.001,0.1]\) & & & 67 \(q_\mathrm{FW},\mathrm{rad}\le\) max \\
\end{tabular}

XI: `low\_aspect\_ratio\_DEMO`

XII: `spherical\_tokamak\_eval`

XIII: `st\_regression`

