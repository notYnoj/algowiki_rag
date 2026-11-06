Note that at this point in the algorithm, we should check for the possibility of a second symbol error combined with _l_<sub>1</sub>=1. Following the Algorithm 2 we suppose a second symbol error at _l_<sub>2</sub>=2 and compute _r_<sub>_i_-2</sub>=2 for _i_=3,4,5,6 by using (4.27), and then we verify that<tbc>

\(\mathbf{y}_i^T\neq C^2\mathbf{y}_{i-1}^T,\)

<tbc>for all _i_=3,4,5,6. Since there is no verification if we consider all possibilities for _l_<sub>2</sub>, we would have to assume that a third symbol error at _l_<sub>3</sub>=3 and find the values such that in (4.40), for _i_=4,5,6. For (4.43) and (4.44) we compute<tbc>

\(\widehat{r_{i1}}=3-Z(-1)+Z(-2)=3-17+3=-11\)

<tbc>and

\(\widehat{r_{i2}}=3\cdot 2-3-Z(-1)+Z\big(3-2-Z(-1)+Z(4-6)\big)\)<br>
\(=6-3-Z(-1)+Z\big(1-Z(-1)+Z(-2)\big)=3-17+Z\big(1-17+3\big)\)<br>
\(=3-17+Z(-13)=-14+19=5.\)

for _i_=4,5,6. Then, in fact<tbc>

\(\mathbf{y}_i^T=C^{-11}\mathbf{y}_{i-1}^T+C^5\mathbf{y}_{i-2}^T,\)

<tbc>for all _i_=4,5,6. So, the position of the three symbol errors are _l_<sub>1</sub>=1, _l_<sub>2</sub>=2 and _l_<sub>3</sub>=3. Solving the linear system we obtain the magnitude of the errors

\(\mathbf{e}_1=[11010],\mathbf{e}_2=[01010]\text{and}\mathbf{e}_3=[01110].\)

Therefore, the codeword is

