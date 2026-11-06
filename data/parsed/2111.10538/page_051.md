Now we bound the random variable \(\sum_{j:|T_j|\ge\Delta}\sum_{i\in T_j}\text{lis}^{[\ell_i,r_i]}(\mathsf{sa}_i)X_i/p\). By Chernoff bound, for each _j_ such that \(|T_j|\ge\Delta\), we have<tbc>

\(\mathrm{Pr}\left[\left(1-\frac{\epsilon}{4}\right)p|T_j|\le\sum_{i\in T_j}X_i\le\left(1+\frac{\epsilon}{4}\right)p|T_j|\right]\ge 1-\mathrm{exp}(-\Omega(\epsilon^2p|T_j|))=1-\mathrm{exp}(-\Omega(\mathrm{log}^3n)).\) (18)

<tbc>Notice that for set _T<sub>j</sub>_,<tbc>

\(\frac{(1+\epsilon/4)^{j-1}}{p}\sum_{i\in T_j}X_i\le\sum_{i\in T_j}\frac{1}{p}\text{lis}^{[\ell_i,r_i]}(\mathsf{sa}_i)X_i\le\frac{(1+\epsilon/4)^j}{p}\sum_{i\in T_j}X_i.\) (19)

<tbc>We have

\(\mathrm{Pr}\left[\left(1-\frac{\epsilon}{4}\right)^2\sum_{i\in T_j}\text{lis}^{[\ell_i,r_i]}(\mathsf{sa}_i)\le\sum_{i\in T_j}\frac{1}{p}\text{lis}^{[\ell_i,r_i]}(\mathsf{sa}_i)X_i\le\left(1+\frac{\epsilon}{4}\right)^2\sum_{i\in T_j}\text{lis}^{[\ell_i,r_i]}(\mathsf{sa}_i)\right]\ge\mathrm{Pr}\left[\left(1-\frac{\epsilon}{4}\right)^2\sum_{i\in T_j}\text{lis}^{[\ell_i,r_i]}(\mathsf{sa}_i)\le\frac{(1+\epsilon/4)^{j-1}}{p}\sum_{i\in T_j}X_i\wedge\frac{(1+\epsilon/4)^j}{p}\sum_{i\in T_j}X_i\le\left(1+\frac{\epsilon}{4}\right)^2\sum_{i\in T_j}\text{lis}^{[\ell_i,r_i]}(\mathsf{sa}_i)\right]\ge\mathrm{Pr}\left[\left(1-\frac{\epsilon}{4}\right)^2\left(1+\frac{\epsilon}{4}\right)^j|T_j|\le\frac{(1+\epsilon/4)^{j-1}}{p}\sum_{i\in T_j}X_i\wedge\frac{(1+\epsilon/4)^j}{p}\sum_{i\in T_j}X_i\le\left(1+\frac{\epsilon}{4}\right)^{j+1}|T_j|\right]\ge\mathrm{Pr}\left[\left(1-\frac{\epsilon}{4}\right)p|T_j|\le\sum_{i\in T_j}X_i\wedge\sum_{i\in T_j}X_i\le\left(1+\frac{\epsilon}{4}\right)p|T_j|\right]=1-\mathrm{exp}(-\Omega(\mathrm{log}^3n)),\text{(20)}\)

<tbc>where the first inequality follows from Equation (19), the second inequality follows from the definition of _T<sub>j</sub>_ and the last inequality follows from Equation (18). By Equation (16), (17), (21) and union bound, we have

\(\mathrm{Pr}\left[\left(1-\frac{\epsilon}{4}\right)^2\left(\mathsf{q}(\mathsf{ps})-\frac{\epsilon\lambda n}{100t}\right)\le\sum_{j:|T_j|\ge\Delta}\sum_{i\in T_j}\frac{1}{p}\text{lis}^{[\ell_i,r_i]}(\mathsf{sa}_i)X_i\le\left(1+\frac{\epsilon}{4}\right)^2\mathsf{q}(\mathsf{ps})\right]\ge\mathrm{Pr}\left[\left(1-\frac{\epsilon}{4}\right)^2\sum_{j:|T_j|\ge\Delta}\sum_{i\in T_j}\text{lis}^{[\ell_i,r_i]}(\mathsf{sa}_i)\le\sum_{j:|T_j|\ge\Delta}\sum_{i\in T_j}\frac{1}{p}\text{lis}^{[\ell_i,r_i]}(\mathsf{sa}_i)X_i\le\sum_{j:|T_j|\ge\Delta}\left(1+\frac{\epsilon}{4}\right)^2\sum_{i\in T_j}\text{lis}^{[\ell_i,r_i]}(\mathsf{sa}_i)\right]\ge 1-O\left(\frac{\mathrm{log}n}{\epsilon}\right)\mathrm{exp}(-\Omega(\mathrm{log}^3n))=1-\mathrm{exp}(-\Omega(\mathrm{log}^3n)).\text{(21)}\)

