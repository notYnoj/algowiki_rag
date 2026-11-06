Then \(\delta\mathbf{u}_j^{(n)}=\mathbf{e}_j^{n,0}\). Subtracting (30) from the two moment SGS updates (31) and (32) gives the moment error evolution

\(\left(\mathbf{I}-\frac{\omega}{\varepsilon}\mathbf{L}\right)\mathbf{e}_j^{n,s+1/2}=(1-\nu)\mathbf{e}_j^{n,s}+\frac{\nu}{2}\left(\mathbf{I}+\frac{\mathbf{A}}{C_{M+1}}\right)\mathbf{e}_{j-1}^{n,s+1/2}+\frac{\nu}{2}\left(\mathbf{I}-\frac{\mathbf{A}}{C_{M+1}}\right)\mathbf{e}_{j+1}^{n,s},\) (C.3)

\(\left(\mathbf{I}-\frac{\omega}{\varepsilon}\mathbf{L}\right)\mathbf{e}_j^{n,s+1}=(1-\nu)\mathbf{e}_j^{n,s+1/2}+\frac{\nu}{2}\left(\mathbf{I}+\frac{\mathbf{A}}{C_{M+1}}\right)\mathbf{e}_{j-1}^{n,s+1/2}+\frac{\nu}{2}\left(\mathbf{I}-\frac{\mathbf{A}}{C_{M+1}}\right)\mathbf{e}_{j+1}^{n,s+1}.\) (C.4)

For later use, we will split each moment error into its first three and last _M_-2 components:

\(\mathbf{e}_j^{n,r}=\left(\begin{array}{ c }
\mathbf{H}_j^{n,r} \\
\mathbf{K}_j^{n,r}
\end{array}\right),\mathbf{H}_j^{n,r}=\left(\begin{array}{ c }
e_{0,j}^{n,r} \\
e_{1,j}^{n,r} \\
e_{2,j}^{n,r}
\end{array}\right),\mathbf{K}_j^{n,r}=\left(\begin{array}{ c }
e_{3,j}^{n,r} \\
\vdots \\
e_{M,j}^{n,r}
\end{array}\right),r=0,\frac{1}{2},1,\frac{3}{2},\dots,\gamma_1.\) (C.5)

For the hydrodynamic SGS stage, similarly define

\(\mathbf{E}_j^{n,\ell}:=\mathbf{U}_j^{(n,\ell)}-\mathbf{U}_j,\mathbf{U}_j=(u_{j,0},u_{j,1},u_{j,2})^\mathsf{T},\ell=0,\frac{1}{2},1,\frac{3}{2},\dots,\gamma_2.\) (C.6)

The initialization of the hydrodynamic stage \(\mathbf{U}_j^{(n,0)}=(u_{j,0}^{(n,\gamma_1)},u_{j,1}^{(n,\gamma_1)},u_{j,2}^{(n,\gamma_1)})^\mathsf{T}\) gives \(\mathbf{E}_j^{n,0}=\mathbf{H}_j^{n,\gamma_1}\), and the two Hydro- SGS updates (33) and (34) give

\(\mathbf{E}_j^{n,\ell+1/2}=(1-\nu)\mathbf{E}_j^{n,\ell}+\frac{\nu}{2}\left(\mathbf{I}+\frac{\mathbf{A}_h}{C_{M+1}}\right)\mathbf{E}_{j-1}^{n,\ell+1/2}+\frac{\nu}{2}\left(\mathbf{I}-\frac{\mathbf{A}_h}{C_{M+1}}\right)\mathbf{E}_{j+1}^{n,\ell}-\frac{\nu}{2C_{M+1}}\mathbf{b}\left(e_{3,j+1}^{n,\gamma_1}-e_{3,j-1}^{n,\gamma_1}\right),\) (C.7)

\(\mathbf{E}_j^{n,\ell+1}=(1-\nu)\mathbf{E}_j^{n,\ell+1/2}+\frac{\nu}{2}\left(\mathbf{I}+\frac{\mathbf{A}_h}{C_{M+1}}\right)\mathbf{E}_{j-1}^{n,\ell+1/2}+\frac{\nu}{2}\left(\mathbf{I}-\frac{\mathbf{A}_h}{C_{M+1}}\right)\mathbf{E}_{j+1}^{n,\ell+1}-\frac{\nu}{2C_{M+1}}\mathbf{b}\left(e_{3,j+1}^{n,\gamma_1}-e_{3,j-1}^{n,\gamma_1}\right).\) (C.8)

Finally, the reconstruction step (35) gives the complete outer error after one FIM iteration:

\(\delta\mathbf{u}_j^{(n+1)}=\left(\begin{array}{ c }
\mathbf{E}_j^{n,\gamma_2} \\
\mathbf{K}_j^{n,\gamma_1}
\end{array}\right).\) (C.9)

We now apply the specific form of \(\delta\mathbf{u}_j^{(n)}\) in (37) to find the error-propagation matrix \(\mathbf{T}(\varepsilon,k)\) in (38). Plugging \(\delta\mathbf{u}_j^{(n)}=\widehat{\mathbf{e}}^{(n)}(k)e^{\mathrm{i}jk\Delta x}\) into (C.3)-(C.8) gives

\(\widehat{\mathbf{e}}^{(n+1)}(k)=\underbrace{\left([\mathbf{M}_\mathrm{hb}(k)]^{-1}\mathbf{N}_\mathrm{hb}(k)[\mathbf{M}_\mathrm{hf}(k)]^{-1}\mathbf{N}_\mathrm{hf}(k)\right)^{\gamma_2}\left([\mathbf{M}_\mathrm{kb}(\varepsilon,k)]^{-1}\mathbf{N}_\mathrm{kb}(k)[\mathbf{M}_\mathrm{kf}(\varepsilon,k)]^{-1}\mathbf{N}_\mathrm{kf}(k)\right)^{\gamma_1}\widehat{\mathbf{e}}^{(n)}(k)}_{\widehat{\mathbf{T}}(\varepsilon,k)},\) (C.10)

where **M**<sub>kf</sub>, **N**<sub>kf</sub>, **M**<sub>kb</sub>, **N**<sub>kb</sub> arise from the moment SGS stage:

\(\mathbf{M}_\mathrm{kf}(\varepsilon,k):=\mathbf{I}-\frac{\omega}{\varepsilon}\mathbf{L}-\frac{\nu}{2}\left(\mathbf{I}+\frac{\mathbf{A}}{C_{M+1}}\right)e^{-\mathrm{i}k\Delta x},\mathbf{N}_\mathrm{kf}(k):=(1-\nu)\mathbf{I}+\frac{\nu}{2}\left(\mathbf{I}-\frac{\mathbf{A}}{C_{M+1}}\right)e^{\mathrm{i}k\Delta x},\)<br>
\(\mathbf{M}_\mathrm{kb}(\varepsilon,k):=\mathbf{I}-\frac{\omega}{\varepsilon}\mathbf{L}-\frac{\nu}{2}\left(\mathbf{I}-\frac{\mathbf{A}}{C_{M+1}}\right)e^{\mathrm{i}k\Delta x},\mathbf{N}_\mathrm{kb}(k):=(1-\nu)\mathbf{I}+\frac{\nu}{2}\left(\mathbf{I}+\frac{\mathbf{A}}{C_{M+1}}\right)e^{-\mathrm{i}k\Delta x},\)

and **M**<sub>hf</sub>, **N**<sub>hf</sub>, **M**<sub>hb</sub>, **N**<sub>hb</sub> arise from the hydrodynamic SGS stage. The detailed expressions of these four matrices will be omitted, and only their block structures are shown below:

\(\mathbf{M}_\mathrm{hf}(k):=\left(\begin{array}{ c c c }
* & \mathbf{0} & \mathbf{0} \\
\mathbf{0} & \mathbf{I}_{M-2}
\end{array}\right),\mathbf{N}_\mathrm{hf}(k):=\left(\begin{array}{ c c c }
* & * & \mathbf{0} \\
\mathbf{0} & \mathbf{I}_{M-2}
\end{array}\right),\mathbf{M}_\mathrm{hb}(k):=\left(\begin{array}{ c c c }
* & \mathbf{0} & \mathbf{0} \\
\mathbf{0} & \mathbf{I}_{M-2}
\end{array}\right),\mathbf{N}_\mathrm{hb}(k):=\left(\begin{array}{ c c c }
* & * & \mathbf{0} \\
\mathbf{0} & \mathbf{I}_{M-2}
\end{array}\right).\) (C.11)

Here ∗ denotes a potentially nonzero block.

