Accordingly, we have

\(\|\widehat{C}-\widetilde{C}\|=\|\mathfrak{c}-\mathfrak{c}\|=\left\|\left(\tilde{\nu}^{-1}\otimes I_{m/m_0}\right)\left(\widetilde{W}_\nu\otimes I_{m/m_0}\right)\genfrac(){pt}{2}{E_1}{\vdots}{E_t}\right\|\le\left\|\tilde{\nu}^{-1}|\cdot|\widetilde{W}_\nu|\genfrac(){pt}{2}{\|E_1\|}{\vdots}{\|E_t\|}\right\|_\infty\le\left((1+\delta)^{6(L-1)}-1\right)(k/k_0^L)E^{L-1}\left\|\tilde{\nu}^{-1}|\cdot|\widetilde{W}_\nu|\genfrac(){pt}{2}{\left(\sum_{i=1}^{m_0k_0}|\widetilde{U}_\phi(i,1)|\|\tilde{\phi}(:,i)\|_1\right)\left(\sum_{i=1}^{k_0n_0}|\widetilde{V}_\psi(i,1)|\|\tilde{\psi}(:,i)\|_1\right)}{\vdots}\left(\sum_{i=1}^{m_0k_0}|\widetilde{U}_\phi(i,t)|\|\tilde{\phi}(:,i)\|_1\right)\left(\sum_{i=1}^{k_0n_0}|\widetilde{V}_\psi(i,t)|\|\tilde{\psi}(:,i)\|_1\right)\right\|_\infty\|A\|\|B\|\le\left((1+\delta)^{6(L-1)}-1\right)(k/k_0^L)E^{L-1}\left\|\left(|\tilde{\nu}^{-1}|\cdot|\widetilde{W}_\nu|\right)\left((|\tilde{\phi}|\cdot|\widetilde{U}_\phi|)^T\mathbb{1}\odot(|\tilde{\psi}|\cdot|\widetilde{V}_\psi|)^T\mathbb{1}\right)\right\|_\infty\|A\|\|B\|\le\left((1+\delta)^{6L}-(1+\delta)^6\right)(k/k_0^L)E^L\|A\|\|B\|\text{(A.21)}\)

for 1 the vector of all ones. Here, we note that \(\|(|\tilde{\nu}^{-1}|\cdot|\widetilde{W}_\nu|)((|\tilde{\phi}|\cdot|\widetilde{U}_\phi|)^T\mathbb{1}\odot(|\tilde{\psi}|\cdot|\widetilde{V}_\psi|)^T\mathbb{1})\|_\infty\) is the stability factor corresponding to \(\widetilde{U}_\phi\), \(\widetilde{V}_\psi\), \(\widetilde{W}_\nu\), \(\tilde{\phi}\), \(\tilde{\psi}\) and \(\tilde{\nu}^{-1}\), which is at most \((1+\delta)^6E\).

To similarly bound the first term of (A.13), we write<tbc>

\(\mathfrak{c}=\left(\nu^{-1}\otimes I_{m/m_0}\right)\left(W_\nu\otimes I_{m/m_0}\right)\genfrac(){pt}{2}{M_1}{\vdots}{M_t}\) (A.22)

<tbc>for \(M_j=\left\langle\left(U_\phi(:,j)^T\otimes I_{m/m_0}\right)\left(\phi^T\otimes I_{m/m_0}\right)\mathfrak{a}\), \(\left(V_\psi(:,j)^T\otimes I_{k/k_0}\right)\left(\psi^T\otimes I_{k/k_0}\right)\mathfrak{b}\right\rangle_{L-1}\). Since \(\langle\cdot,\cdot\rangle_{L-1}\) is bi linear, we can express \(M_j-\widetilde{M}_j\) as<tbc>

\(\sum_{1\le i_1\le m_0k_01\le i_2\le k_0n_0}\left[\left(\sum_{i_1^\prime=1}^{m_0k_0}U_\phi(i'_1,j)\phi(i_1,i'_1)\right)\left(\sum_{i_2^\prime=1}^{k_0n_0}V_\psi(i'_2,j)\psi(i_2,i'_2)\right)-\left(\sum_{i_1^\prime=1}^{m_0k_0}\widetilde{U}_\phi(i'_1,j)\tilde{\phi}(i_1,i'_1)\right)\left(\sum_{i_2^\prime=1}^{k_0n_0}\widetilde{V}_\psi(i'_2,j)\tilde{\psi}(i_2,i'_2)\right)\right]\langle\mathfrak{a}(i_1),\mathfrak{b}(i_2)\rangle_{L-1},\) (A.23)

<tbc>for any \(1\le j\le t\), where a(_i_<sub>1</sub>) and b(_i_<sub>2</sub>) are \((m/m_0)\times(k/k_0)\) and \((k/k_0)\times(n/n_0)\) subblocks of a and b with block row indices _i_<sub>1</sub> and _i_<sub>2</sub>, respectively. Now by (4.4)<tbc>

\(\|\langle\mathfrak{a}(i_1),\mathfrak{b}(i_2)\rangle_{L-1}\|\le(k/k_0^L)E^{L-1}\|A\|\|B\|,\) (A.24)

<tbc>so we have (combining the sums in (A.23))<tbc>

\(\|M_j-\widetilde{M}_j\|\le(k/k_0^L)E^{L-1}\|A\|\|B\|\sum_{1\le i_1,i_1^\prime\le m_0k_01\le i_2,i_2^\prime\le k_0n_0}\left|U_\phi(i'_1,j)\phi(i_1,i'_1)V_\psi(i'_2,j)\psi(i_2,i'_2)-\widetilde{U}_\phi(i'_1,j)\tilde{\phi}(i_1,i'_1)\widetilde{V}_\psi(i'_2,j)\tilde{\psi}(i_2,i'_2)\right|\le((1+\delta)^4-1)(k/k_0^L)E^{L-1}\|A\|\|B\|\sum_{1\le i_1,i_1^\prime\le m_0k_01\le i_2,i_2^\prime\le k_0n_0}|U_\phi(i'_1,j)\phi(i_1,i'_1)V_\psi(i'_2,j)\psi(i_2,i'_2)|=((1+\delta)^4-1)(k/k_0^L)E^{L-1}\|A\|\|B\|\sum_{1\le i_1^\prime\le m_0k_01\le i_2^\prime\le k_0n_0}|U_\phi(i'_1,j)|\|\phi(:,i'_1)\|_1|V_\psi(i'_2,j)|\|\psi(:,i'_2)\|_1=((1+\delta)^4-1)(k/k_0^L)E^{L-1}\|A\|\|B\|\left((|\phi|\cdot|U_\phi|)^T\mathbb{1}\odot(|\psi|\cdot|V_\psi|)^T\mathbb{1}\right)_j\text{(A.25)}\)

<tbc>for \(((|\phi|\cdot|U_\phi|)^T\mathbb{1}\odot(|\psi|\cdot|V_\psi|)^T\mathbb{1})_j\) the _j_-th entry of \(((|\phi|\cdot|U_\phi|)^T\mathbb{1}\odot(|\psi|\cdot|V_\psi|)^T\mathbb{1})\). In this case, we have<tbc>

\(\|\mathfrak{c}-\mathfrak{c}\|=\left\|\left(\nu^{-1}\otimes I_{m/m_0}\right)\left(W_\nu\otimes I_{m/m_0}\right)\genfrac(){pt}{2}{M_1-\widetilde{M}_1}{\vdots}{M_t-\widetilde{M}_t}+\Delta W\genfrac(){pt}{2}{\widetilde{M}_1}{\vdots}{\widetilde{M}_t}\right\|\le\left\|\left(\nu^{-1}\otimes I_{m/m_0}\right)\left(W_\nu\otimes I_{m/m_0}\right)\genfrac(){pt}{2}{M_1-\widetilde{M}_1}{\vdots}{M_t-\widetilde{M}_t}\right\|+\left\|\Delta W\genfrac(){pt}{2}{\widetilde{M}_1}{\vdots}{\widetilde{M}_t}\right\|,\text{(A.26)}\)

