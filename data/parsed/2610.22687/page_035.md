\begin{tabular}{cccc}
design variables (`ixc`) & objective & equality constraints (`icc`) & inequality constraints (`icc`) \\
2 \(B_\mathrm{t}(R_0)\in[0.01,30]\) T & 1 min _R_<sub>0</sub> & 1 \(\langle\beta\rangle\) consistency & 5 \(\langle n_\mathrm{e}\rangle\le n_\mathrm{lim}\) \\
3 \(R_0\in[8,9]\) m & & 2 Power balance & 8 \(q_\mathrm{n}\le\) max \\
4 \(\langle T_\mathrm{e}\rangle\in[5.5055,100]\) keV & & 11 Radial build & 9 \(P_\mathrm{fus}\le\) max \\
5 \(\langle\beta\rangle\in[0.001,1]\) & & & 13 \(t_\mathrm{burn}\ge\) min \\
6 \(\langle n_\mathrm{e}\rangle\in[2\times 10^{19},1\times 10^{21}]\) m<sup>-3</sup> & & & 15 \(P_\mathrm{sep}\ge P_\mathrm{LH}\) \\
10 \(H\in[0.1,1.2]\) & & & 16 \(P_\mathrm{net}\ge\) min \\
16 CS radial thickness \(\in[0.3,10]\) m & & & 24 \(\langle\beta\rangle\le\) max \\
18 \(q_{95}\in[3,50]\) & & & 25 \(B_\mathrm{max}\le\) max \\
29 Bore radius \(\in[0.1,10]\) m & & & 26 \(j_\mathrm{CS}\le j_\mathrm{crit}\) (EOF) \\
37 \(j_{\mathrm{CS},\mathrm{EOF}}\in[100000,1\times 10^8]\) A m<sup>-2</sup> & & & 27 \(j_\mathrm{CS}\le j_\mathrm{crit}\) (BOP) \\
44 \(f_\mathrm{NI}\in[0.001,1]\) & & & 30 \(P_\mathrm{aux}\le\) max \\
56 \(\tau_\mathrm{Q}\in[0.1,100]\) s & & & 31 \(\sigma_{\mathrm{TF},\mathrm{case}}\le\) max \\
57 TF nose case thickness \(\in[0.05,1]\) m & & & 32 \(\sigma_{\mathrm{TF},\mathrm{conduit}}\le\) max \\
58 TF turn conduit thickness \(\in[0.008,0.1]\) m & & & 33 \(j_{\mathrm{TF},\mathrm{WP}}\le j_\mathrm{crit}\) \\
59 \(f_\mathrm{Cu}\in[0.5,0.94]\) & & & 34 \(V_\mathrm{TF}\le\) max \\
60 \(I_\mathrm{turn}\in[65000,90000]\) A & & & 35 \(j_{\mathrm{TF},\mathrm{WP}}\le j_\mathrm{quench}\) \\
109 \(\langle n_{\alpha,\mathrm{th}}\rangle/\langle n_\mathrm{e}\rangle\in[0.05,0.1]\) & & & 36 \(\Delta T_\mathrm{TF}\ge\) min \\
122 CS turn steel fraction \(\in[0.001,0.95]\) & & & 60 \(\Delta T_\mathrm{CS}\ge\) min \\
135 \(n_{\mathrm{Xe}}/n_\mathrm{e}\in[1\times 10^{-8},0.01]\) & & & 62 \(\tau_\alpha/\tau_\mathrm{E}\ge\) min \\
140 TF winding pack radial thickness \(\in[0.4,2]\) m & & & 65 \(\sigma_{\mathrm{VV},\mathrm{quench}}\le\) max \\
 & & & 68 \(P_\mathrm{sep}B_\mathrm{T}/(q_{95}AR_0)\le\) max \\
 & & & 72 \(\sigma_{\mathrm{CS},\mathrm{Tresca}}\le\) max \\
 & & & 81 \(n_{e0}\ge n_{\mathrm{e},\mathrm{ped}}\) \\
\end{tabular}

\begin{tabular}{cccc}
design variables (`ixc`) & objective & equality constraints (`icc`) & inequalities (`icc`; evaluated at the solution, not imposed) \\
4 \(\langle T_\mathrm{e}\rangle\in[5.5055,100]\) keV & none (root & 1 \(\langle\beta\rangle\) consistency & 5 \(\langle n_\mathrm{e}\rangle\le n_\mathrm{lim}\) \\
6 \(\langle n_\mathrm{e}\rangle\in[2\times 10^{19},1\times 10^{21}]\) m<sup>-3</sup> & find) & 2 Power balance & 8 \(q_\mathrm{n}\le\) max \\
 & & & 9 \(P_\mathrm{fus}\le\) max \\
 & & & 13 \(t_\mathrm{burn}\ge\) min \\
 & & & 15 \(P_\mathrm{sep}\ge P_\mathrm{LH}\) \\
 & & & 16 \(P_\mathrm{net}\ge\) min \\
 & & & 24 \(\langle\beta\rangle\le\) max \\
 & & & 25 \(B_\mathrm{max}\le\) max \\
 & & & 26 \(j_\mathrm{CS}\le j_\mathrm{crit}\) (EOF) \\
 & & & 27 \(j_\mathrm{CS}\le j_\mathrm{crit}\) (BOP) \\
 & & & 30 \(P_\mathrm{aux}\le\) max \\
 & & & 31 \(\sigma_{\mathrm{TF},\mathrm{case}}\le\) max \\
 & & & 32 \(\sigma_{\mathrm{TF},\mathrm{conduit}}\le\) max \\
 & & & 33 \(j_{\mathrm{TF},\mathrm{WP}}\le j_\mathrm{crit}\) \\
 & & & 34 \(V_\mathrm{TF}\le\) max \\
 & & & 35 \(j_{\mathrm{TF},\mathrm{WP}}\le j_\mathrm{quench}\) \\
 & & & 36 \(\Delta T_\mathrm{TF}\ge\) min \\
 & & & 60 \(\Delta T_\mathrm{CS}\ge\) min \\
 & & & 62 \(\tau_\alpha/\tau_\mathrm{E}\ge\) min \\
 & & & 65 \(\sigma_{\mathrm{VV},\mathrm{quench}}\le\) max \\
 & & & 68 \(P_\mathrm{sep}B_\mathrm{T}/(q_{95}AR_0)\le\) max \\
 & & & 72 \(\sigma_{\mathrm{CS},\mathrm{Tresca}}\le\) max \\
 & & & 81 \(n_{e0}\ge n_{\mathrm{e},\mathrm{ped}}\) \\
\end{tabular}

IX: `large\_tokamak\_nof`

X: `large\_tokamak\_eval`

