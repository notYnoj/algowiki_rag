\begin{tabular}{cccc}
symbol & meaning & symbol & meaning \\
_B_<sub>t</sub>(_R_<sub>0</sub>) & toroidal field on axis & _P_<sub>fus</sub>_,P_<sub>net</sub> & fusion power, net electric power \\
_R_<sub>0</sub> & plasma major radius & _P_<sub>sep</sub>_,P_<sub>LH</sub> & power across the separatrix, L-H threshold power \\
_A_ & aspect ratio & _P_<sub>aux</sub> & injected auxiliary power \\
\(\langle T_\mathrm{e}\rangle\) & volume-averaged electron temperature & _f_<sub>rad</sub> & radiated power fraction \\
\(\langle n_\mathrm{e}\rangle\) & volume-averaged electron density & _q_<sub>n</sub> & neutron wall load \\
_n_<sub>e0</sub>_,n_<sub>e,ped</sub> & electron density on axis, at the pedestal & _q_<sub>div</sub>_,q_<sub>FW,rad</sub> & divertor heat load, first-wall radiation load \\
_n_<sub>lim</sub> & density limit & _B_<sub>max</sub> & peak field on the coil \\
\(\langle n_{\alpha,\mathrm{th}}\rangle\) & thermal alpha density & _j_CS_,j_TF_,_WP & CS, TF winding pack current density \\
_n_<sub>Xe</sub> & xenon impurity density & _j_crit_,j_quench & critical current density, quench (hot-spot) limit \\
_f_GW,ped_,f_GW,sep & Greenwald fraction of the pedestal, separatrix & EOF, BOP & end of flat-top, beginning of pulse \\
 & density & & \\
\(\langle\beta\rangle\) & volume-averaged total beta & \(\sigma_{\mathrm{TF},\mathrm{case},}\) & TF coil case, conduit stress \\
_H_ & confinement enhancement factor (hfact; _f_ren in \[14\]) & \(\sigma_{\mathrm{TF},\mathrm{conduit}}\) & \\
 & safety factor at the 95% flux surface & \(V_{\mathrm{TF},}\tau_\mathrm{Q}\) & TF quench dump voltage, discharge time \\
_q_<sub>95</sub> & non-inductive fraction of the plasma current & \(\Delta T_{\mathrm{TF},}\Delta T_\mathrm{CS}\) & superconductor temperature margin \\
_f_NI & plasma current, centre-post current & _I_<sub>turn</sub> & TF current per turn \\
_I_<sub>p</sub>_,I_<sub>rod</sub> & alpha particle, energy confinement time & _f_Cu & copper fraction of the TF cable \\
\(\tau_\alpha,\tau_\mathrm{E}\) & fusion gain & _N_cycles,CS & achievable CS stress cycles \\
_Q_ & & _d_min_,w_coil & minimal distance between coils, coil toroidal width \\
 & burn time (pulse length) & \(d_\mathrm{pc},\sum d\) & plasma-coil distance, required radial build \\
_t_burn & cost of electricity & \(\sigma_{\mathrm{VV},\mathrm{quench},}\) & vacuum vessel stress during a TF quench, CS \\
CoE & & \(\sigma_{\mathrm{CS},\mathrm{Tresca}}\) & Tresca stress \\
\end{tabular}

\begin{tabular}{cccc}
design variables (`ixc`) & objective & equality constraints (`icc`) & inequality constraints (`icc`) \\
2 \(B_\mathrm{t}(R_0)\in[4,10]\) T & 6 min CoE & 2 Power balance & 8 \(q_\mathrm{n}\le\) max \\
3 \(R_0\in[10,30]\) m & & 16 \(P_\mathrm{net}\ge\) min & 17 \(f_\mathrm{rad}\le\) max \\
4 \(\langle T_\mathrm{e}\rangle\in[3,15]\) keV & & & 18 \(q_\mathrm{div}\le\) max \\
6 \(\langle n_\mathrm{e}\rangle\in[3\times 10^{19},3\times 10^{20}]\) m<sup>-3</sup> & & & 24 \(\langle\beta\rangle\le\) max \\
10 \(H\in[0.1,1.2]\) & & & 32 \(\sigma_{\mathrm{TF},\mathrm{conduit}}\le\) max \\
56 \(\tau_\mathrm{Q}\in[1,50]\) s & & & 34 \(V_{\mathrm{TF},}\le\) max \\
59 \(f_\mathrm{Cu}\in[0.3,0.9]\) & & & 35 \(j_{\mathrm{TF},\mathrm{WP}}\le j_\mathrm{quench}\) \\
109 \(\langle n_{\alpha,\mathrm{th}}\rangle/\langle n_\mathrm{e}\rangle\in[0.0001,0.4]\) & & & 62 \(\tau_\alpha/\tau_\mathrm{E}\ge\) min \\
 & & & 65 \(\sigma_{\mathrm{VV},\mathrm{quench}}\le\) max \\
 & & & 67 \(q_{\mathrm{FW},\mathrm{rad}}\le\) max \\
 & & & 82 \(d_\mathrm{min}\ge w_\mathrm{coil}\) \\
 & & & 83 \(d_\mathrm{pc}\ge\sum d\) \\
\end{tabular}

\begin{tabular}{cccc}
design variables (`ixc`) & objective & equality constraints (`icc`) & inequality constraints (`icc`) \\
4 \(\langle T_\mathrm{e}\rangle\in[4,25]\) keV & 7 min capital & 2 Power balance & 24 \(\langle\beta\rangle\le\) max \\
6 \(\langle n_\mathrm{e}\rangle\in[3.005\times 10^{19},5.005\times 10^{20}]\) m<sup>-3</sup> & cost & 16 \(P_\mathrm{net}\ge\) min & 84 \(\langle\beta\rangle\ge\) min \\
10 \(H\in[0.1,2]\) & & & \\
\end{tabular}

VI: Symbols used in the PROCESS configurations

VII: `stellarator\_helias`

VIII: `helias\_5b`

