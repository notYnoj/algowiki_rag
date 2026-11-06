## Appendix

## A Instance parameters

1 provides an overview of the chosen parameters for the exemplary linear parameter sweep in the main text (Figs. 2, 3 and 5).

We now describe how we choose the parameters used in our example. For this we calculate the minimal gap and the overlap with the final solution for several parameters to find a region with large minimal gap and large overlap. Note that this is only done to find good parameters for our small example, where we already know the solution. For large systems such a calculation would beyond classical numerical capabilities, which is why the problem poses a potential application for a quantum simulator.

The minimal gap in the spectrum (e.g. the one shown in Fig. 3) depends on the final queens interaction energy _U_<sub>Q</sub>, the final trapping energy _U_<sub>T</sub>, the tunneling amplitude _J_ and the final excluded diagonals penalty _U_<sub>D</sub>. To find proper values for these parameters we determine the minimal gap in a wide parameter range. In order to get the minimal gap, some of the Hamiltonian’s lowest eigenenergies are calculated for discrete time steps during the sweep. Subsequently, the minimum of the difference between the groundstate and the first exited state at all time steps is taken to be the minimal gap. The values of the minimal gap have to be scrutinized carefully since its accuracy depends on the resolution of the discrete time steps. Therefore a more detailed analysis of the minimal gap might require a more careful analysis, especially for high interaction strengths.

To analyze how well the quantum system reproduces the solution of the _N_-queens problem we study the overlap

\(F=|\langle\phi|\psi\rangle|\) (37)

between the state \(|\phi\rangle\) that corresponds to the solution of the chosen instance of the queens problem introduced in Fig. 1 and the state at the end of an adiabatic sweep \(|\psi\rangle\) (i.e. the ground state of our spectrum on the right side). This is necessary because we do not switch off the kinetic Hamiltonian in our example, and thus the "perfect" solution is only obtained in the limit of large energy penalties _U_<sub>Q</sub>, _U_<sub>D</sub> and _U_<sub>T</sub>.

Figure 8(a) suggests that in order to increase the minimal gap the ratio _U_<sub>Q</sub>_/U_<sub>D</sub> has to be chosen as small as possible. We vary the ratio by fixing _U_<sub>D</sub> and varying _U_<sub>Q</sub>. Therewith, Fig. 8(a) indicates that _U_<sub>Q</sub> should be as small as possible. However, as it can be seen in Fig. 8(b), a small _U_<sub>Q</sub> also decreases the overlap with the solution and the physical system does not resemble the desired solution of the queens problem anymore. We therefore have to make a compromise between a reasonably large overlap and an optimized minimal gap.

\begin{tabular}{ccc}
Parameter & Symbol & Value \\
System size & _N_ & 5 \\
Final queens interaction energy & _U_<sub>Q</sub> & _J_ \\
Final excluded diagonals penalty & _U_<sub>D</sub> & 5_J_ \\
Final trapping energy & _U_<sub>T</sub> & 2_J_ \\
Sweep time & \(\tau\) & \(49\hbar/J\) \\
Excluded sum-diagonals & & {2,3,6,9} \\
Excluded difference-diagonals & & {1,2,8,9} \\
Trapping sites & & {(3,5)} \\
Number of modes per direction & _M_ & 5 \\
\end{tabular}

1: Parameters of the exemplary instance used in the figures in the main text.

