## 2 Notation and Physical Inputs

### 2.1 PMNS Parameterization

We adopt the Particle Data Group (PDG) conventions \[22\]. Flavor eigenstates \(|\nu_\alpha\rangle\), \(\alpha\in\{e,\mu,\tau\}\), and mass eigenstates \(|\nu_i\rangle\), \(i\in\{1,2,3\}\), are related by the unitary PMNS matrix _U_:

\(|\nu_\alpha\rangle=\sum_{i=1}^3U_{\alpha i}|\nu_i\rangle,UU^\dagger=U^\dagger U=\mathbf{1}.\) (1)

The standard decomposition is \(U=R_{23}\Gamma_\delta R_{13}\Gamma_\delta^\dagger R_{12}\), with _R<sub>ij</sub>_ a real rotation by \(\theta_{ij}\) and \(\Gamma_\delta=\mathrm{diag}(1,1,e^{i\delta_\mathrm{CP}})\). Explicitly, with \(c_{ij}\equiv\mathrm{cos}\theta_{ij}\) and \(s_{ij}\equiv\mathrm{sin}\theta_{ij}\),

\(U=\left(\begin{array}{ c c c }
c_{12}c_{13} & s_{12}c_{13} & s_{13}e^{-i\delta_\mathrm{CP}} \\
-s_{12}c_{23}-c_{12}s_{23}s_{13}e^{i\delta_\mathrm{CP}} & c_{12}c_{23}-s_{12}s_{23}s_{13}e^{i\delta_\mathrm{CP}} & s_{23}c_{13} \\
s_{12}s_{23}-c_{12}c_{23}s_{13}e^{i\delta_\mathrm{CP}} & -c_{12}s_{23}-s_{12}c_{23}s_{13}e^{i\delta_\mathrm{CP}} & c_{23}c_{13}
\end{array}\right).\) (2)

Majorana phases do not affect oscillation probabilities \[23\] and are omitted. The mass- squared differences are \(\Delta m_{21}^2\equiv m_2^2-m_1^2\), \(\Delta m_{31}^2\equiv m_3^2-m_1^2\), and \(\Delta m_{32}^2=\Delta m_{31}^2-\Delta m_{21}^2\). Normal ordering (NO) has \(\Delta m_{31}^2>0\). A useful combination is the electron-weighted splitting \[24, 25\]

\(\Delta m_{ee}^2\equiv c_{12}^2\Delta m_{31}^2+s_{12}^2\Delta m_{32}^2=\Delta m_{31}^2-s_{12}^2\Delta m_{21}^2,\) (3)

which appears in \(\nu_e\) disappearance and in the DMP scheme \[43, 47\].

### 2.2 NuFIT 6.0 Parameter Inputs

Central values are from the NuFIT 6.0 global analysis \[15\] ( 1). The two small<tbc>

\begin{tabular}{ccc}
Parameter & Normal Ordering & Inverted Ordering \\
\(\theta_{12}\) \[\(^\circ\)\] & \(33.68_{-0.70}^{+0.73}\) & \(33.68_{-0.70}^{+0.73}\) \\
\(\theta_{13}\) \[\(^\circ\)\] & \(8.56_{-0.11}^{+0.11}\) & \(8.59_{-0.11}^{+0.11}\) \\
\(\theta_{23}\) \[\(^\circ\)\] & \(43.3_{-0.8}^{+1.0}\) & \(47.9_{-0.9}^{+0.7}\) \\
\(\delta_\mathrm{CP}\) \[\(^\circ\)\] & \(212_{-41}^{+26}\) & \(274_{-25}^{+22}\) \\
\(\Delta m_{21}^2\) \[10<sup>-5</sup>eV<sup>2</sup>\] & \(7.49_{-0.19}^{+0.19}\) & \(7.49_{-0.19}^{+0.19}\) \\
\(\Delta m_{3\ell}^2\) \[10<sup>-3</sup>eV<sup>2</sup>\] & \(+2.534_{-0.023}^{+0.025}\) & \(-2.510_{-0.025}^{+0.024}\) \\
\(\mathrm{sin}^2\theta_{13}\) & 0.02215 & 0.02231 \\
\(\mathrm{sin}^2\theta_{23}\) & 0.470 & 0.550 \\
\(\alpha\equiv\Delta m_{21}^2/|\Delta m_{3\ell}^2|\) & 0.0296 & 0.0298 \\
\(\epsilon_{13}\equiv\mathrm{sin}\theta_{13}\) & 0.149 & 0.149 \\
\(J_\mathrm{CP}^\mathrm{max}\) \[\(\times 10^{-2}\)\] & 3.35 & 3.36 \\
\end{tabular}

1: NuFIT 6.0 best-fit oscillation parameters and \(1\sigma\) ranges, from the global fit including IceCube and Super-Kamiokande atmospheric data (the IC24 with-SK column of \[15, 16\]). For normal ordering (NO) this is the global best fit; the inverted-ordering (IO) column is disfavored by \(\Delta\chi^2=6.1\). Derived quantities (\(\alpha\), \(\epsilon_{13}\), \(J_\mathrm{CP}^\mathrm{max}\)) are computed from the central values in this table.

