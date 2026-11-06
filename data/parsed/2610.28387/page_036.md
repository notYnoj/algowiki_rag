for _k_=2,3,4, respectively. These are the definitions in (2.3), which proves (2.4). The kernels \(H_2^{[XY]}\) and \(H_3^{[XY]}\) in (2.5) and (2.6) are the quantities inside the expectations in (2.4), evaluated at _m_ distinct pairs; therefore \(\mathbb{E}\{\mathbf{H}_m(Z_I)\}=\unknown_m\) for _m_=2,3. The \[_YX_\] direction follows by exchanging the coordinates.

## B.2 Complete U-statistics and explicit rank coefficients

Using the standard concomitant representation (Yang, 1977; David and Nagaraja, 2003; Serfling and Xiao, 2007), fix the order-two kernel in (2.5), and sort all _n_ values of _Y_ increasingly. An observation with rank _q_ appears as the larger _Y_ coordinate in _q_-1 different pairs and as the smaller coordinate in _n-q_ different pairs. Its coefficient in the average of the order-two kernels therefore equals<tbc>

\(\frac{1}{\genfrac(){pt}{2}{n}{2}}\left\{\frac{q-1}{2}-\frac{n-q}{2}\right\}=\frac{2q-n-1}{n(n-1)}=w_{2,q}.\)

<tbc>For the order-three kernel (2.6), an observation of rank _q_ can appear as the smallest, middle, or largest among a selected triple. The numbers of such triples are, respectively,<tbc>

\(\genfrac(){pt}{2}{n-q}{2},(q-1)(n-q),\genfrac(){pt}{2}{q-1}{2}.\)

<tbc>Its contribution in the three positions is, respectively, 1/3,-2/3,1/3 times its measured value. Hence the coefficient is

\(w_{3,q}=\frac{\genfrac(){pt}{2}{n-q}{2}-2(q-1)(n-q)+\genfrac(){pt}{2}{q-1}{2}}{3\genfrac(){pt}{2}{n}{3}}=\frac{6q^2-6(n+1)q+(n+1)(n+2)}{n(n-1)(n-2)}.\)

This proves the concomitant representation (2.8), including the exact coefficients. The sum of the coefficients is zero for each order because the sample kernel is unchanged by adding the same constant to all measured values.

## B.3 Elementary forms and a numerical example

In elementary terms, (2.7) and (2.8) amount to the following. For each pair of observations, take the _x_ value of the pair with the larger _y_ value minus the _x_ value of the pair with the smaller _y_ value; \(\widehat{\lambda}_2^{[XY]}\) is half the average of these differences over all \(\genfrac(){pt}{2}{n}{2}\) pairs. For each triple of observations, ordered by their _y_ values, form _x_<sub>\[1\]</sub>-2_x_<sub>\[2\]</sub>+_x_<sub>\[3\]</sub>; \(\widehat{\lambda}_3^{[XY]}\) is one third of the average of these quantities over all \(\genfrac(){pt}{2}{n}{3}\) triples. Equivalently, in the probability-weighted-moment form of Hosking (1990), put

\(b_0=\frac{1}{n}\sum_{q=1}^nX_{[q:n]},b_1=\frac{1}{n}\sum_{q=1}^n\frac{q-1}{n-1}X_{[q:n]},b_2=\frac{1}{n}\sum_{q=1}^n\frac{(q-1)(q-2)}{(n-1)(n-2)}X_{[q:n]}.\) (B.2)

