## Appendix C.2. Order analysis of the error-propagation matrix

We now write the matrices \(\mathbf{T}(\varepsilon,k)\), \(\mathbf{M}_\mathrm{kf}(\varepsilon,k)\) and \(\mathbf{M}_\mathrm{kb}(\varepsilon,k)\) in block form, separating the hydrodynamic and nonequilibrium components:

\(\mathbf{T}(\varepsilon,k)=\left(\begin{array}{ c c }
\mathbf{T}^{11}(\varepsilon,k) & \mathbf{T}^{12}(\varepsilon,k) \\
\mathbf{T}^{21}(\varepsilon,k) & \mathbf{T}^{22}(\varepsilon,k)
\end{array}\right),\mathbf{M}_\mathrm{kf}(\varepsilon,k)=\left(\begin{array}{ c c }
\mathbf{M}_\mathrm{kf}^{11}(k) & \mathbf{M}_\mathrm{kf}^{12}(k) \\
\mathbf{M}_\mathrm{kf}^{21}(k) & \mathbf{M}_\mathrm{kf}^{22}(\varepsilon,k)
\end{array}\right),\mathbf{M}_\mathrm{kb}(\varepsilon,k)=\left(\begin{array}{ c c }
\mathbf{M}_\mathrm{kb}^{11}(k) & \mathbf{M}_\mathrm{kb}^{12}(k) \\
\mathbf{M}_\mathrm{kb}^{21}(k) & \mathbf{M}_\mathrm{kb}^{22}(\varepsilon,k)
\end{array}\right),\)

where we have incorporated the fact that some blocks of **M**<sub>kf</sub> and **M**<sub>kb</sub> are independent of \(\varepsilon\). We would like to show that \(\mathbf{T}^{21}(\varepsilon,k)\) and \(\mathbf{T}^{22}(\varepsilon,k)\) are \(O(\varepsilon)\), which implies that the nonequilibrium components of a bounded error become \(O(\varepsilon)\) after one FIM iteration.

Notice that \(\mathbf{M}_\mathrm{kf}^{22}(\varepsilon,k)\) has the form<tbc>

\(\mathbf{M}_\mathrm{kf}^{22}(\varepsilon,k)=\frac{\omega}{\varepsilon}\mathbf{I}_{M-2}+\widetilde{\mathbf{M}}_\mathrm{kf}^{22}(k),\)

<tbc>and \(\mathbf{M}_\mathrm{kf}^{11}(k)\) is invertible for all _k_ under the parameter range (C.1). We can then define the Schur complement of the upper-left block by<tbc>

\(\mathbf{S}_\mathrm{kf}(\varepsilon,k):=\frac{\omega}{\varepsilon}\mathbf{I}_{M-2}+\widetilde{\mathbf{M}}_\mathrm{kf}^{22}(k)-\mathbf{M}_\mathrm{kf}^{21}(k)[\mathbf{M}_\mathrm{kf}^{11}(k)]^{-1}\mathbf{M}_\mathrm{kf}^{12}(k).\)

<tbc>One sees that \([\mathbf{S}_\mathrm{kf}(\varepsilon,k)]^{-1}=O(\varepsilon)\) as \(\varepsilon\rightarrow 0\). Thus, by suppressing the dependence on \(\varepsilon\) and _k_, the block inversion formula gives

\(\mathbf{M}_\mathrm{kf}^{-1}=\left(\begin{array}{ c c }
(\mathbf{M}_\mathrm{kf}^{11})^{-1}+(\mathbf{M}_\mathrm{kf}^{11})^{-1}\mathbf{M}_\mathrm{kf}^{12}\mathbf{S}_\mathrm{kf}^{-1}\mathbf{M}_\mathrm{kf}^{21}(\mathbf{M}_\mathrm{kf}^{11})^{-1} & -(\mathbf{M}_\mathrm{kf}^{11})^{-1}\mathbf{M}_\mathrm{kf}^{12}\mathbf{S}_\mathrm{kf}^{-1} \\
-\mathbf{S}_\mathrm{kf}^{-1}\mathbf{M}_\mathrm{kf}^{21}(\mathbf{M}_\mathrm{kf}^{11})^{-1} & \mathbf{S}_\mathrm{kf}^{-1}
\end{array}\right)=\left(\begin{array}{ c c }
O(1) & O(\varepsilon) \\
O(\varepsilon) & O(\varepsilon)
\end{array}\right).\) (C.12)

Similarly, one can also show that blocks of \([\mathbf{M}_\mathrm{kb}(\varepsilon,k)]^{-1}\) are of the same order. Together with (C.10) and (C.11), one can conclude that

\(\mathbf{T}^{11}(\varepsilon,k)=O(1),\mathbf{T}^{12}(\varepsilon,k)=O(1),\mathbf{T}^{21}(\varepsilon,k)=O(\varepsilon),\mathbf{T}^{22}(\varepsilon,k)=O(\varepsilon).\)

This allows us to analyze the leading-order amplification factors by considering only the hydrodynamic components of the error, which is the focus of the next two subsections.

## Appendix C.3. Leading-order amplification factors

The preceding subsection shows that the lower block row of \(\mathbf{T}(\varepsilon,k)\) is \(O(\varepsilon)\). For any eigenvalue branch with a nonzero limit, the last _M_-2 components of a normalized eigenvector are therefore \(O(\varepsilon)\). Thus its leading part can be nonzero only in the first three components, and we can perform formal asymptotic expansions:

\(\mathbf{H}_j^{n,r}=\mathbf{H}_j^{n,r,(0)}+\varepsilon\mathbf{H}_j^{n,r,(1)}+\cdots,\mathbf{K}_j^{n,r}=\varepsilon\mathbf{K}_j^{n,r,(1)}+\cdots,\mathbf{E}_j^{n,\ell}=\mathbf{E}_j^{n,\ell,(0)}+\varepsilon\mathbf{E}_j^{n,\ell,(1)}+\cdots.\) (C.13)

The next step is to insert these expansions into (C.3)-(C.4) and (C.7)-(C.8) and collect the leading-order terms. To avoid writing the same pair of equations twice, let \((\mathbf{X}_j^0,\mathbf{X}_j^{1/2},\mathbf{X}_j^1)\) denote either<tbc>

\(\left(\mathbf{H}_j^{n,s,(0)},\mathbf{H}_j^{n,s+1/2,(0)},\mathbf{H}_j^{n,s+1,(0)}\right)\text{or}\left(\mathbf{E}_j^{n,\ell,(0)},\mathbf{E}_j^{n,\ell+1/2,(0)},\mathbf{E}_j^{n,\ell+1,(0)}\right).\) (C.14)

<tbc>In both cases,

\(\mathbf{X}_j^{1/2}=(1-\nu)\mathbf{X}_j^0+\frac{\nu}{2}\left(\mathbf{I}+\frac{\mathbf{A}_h}{C_{M+1}}\right)\mathbf{X}_{j-1}^{1/2}+\frac{\nu}{2}\left(\mathbf{I}-\frac{\mathbf{A}_h}{C_{M+1}}\right)\mathbf{X}_{j+1}^0,\) (C.15)

\(\mathbf{X}_j^1=(1-\nu)\mathbf{X}_j^{1/2}+\frac{\nu}{2}\left(\mathbf{I}+\frac{\mathbf{A}_h}{C_{M+1}}\right)\mathbf{X}_{j-1}^{1/2}+\frac{\nu}{2}\left(\mathbf{I}-\frac{\mathbf{A}_h}{C_{M+1}}\right)\mathbf{X}_{j+1}^1.\) (C.16)

It is easy to see that when \(\mathbf{X}_j^0=\mathbf{a}\mathbf{v}_\mu e^{\mathrm{i}jk\Delta x}\) for any eigenvector \(\mathbf{v}_\mu\) of **A**_<sub>h</sub>_ associated with eigenvalue \(\mu\), it holds that<tbc>

\(\mathbf{X}_j^{1/2}=\phi_\mu^{(0)}(k)\mathbf{a}\mathbf{v}_\mu e^{\mathrm{i}jk\Delta x},\mathbf{X}_j^1=\psi_\mu^{(0)}(k)\phi_\mu^{(0)}(k)\mathbf{a}\mathbf{v}_\mu e^{\mathrm{i}jk\Delta x},\)

