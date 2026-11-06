where<tbc>

\(\psi_{j,k}=\left\langle\psi(x,y),Y_{j,k}(x,y)\right\rangle:=\int_0^1\int_0^1\psi(x,y)Y_{j,k}(x,y)dxdy.\)

<tbc>The functions **W**_<sub>j,k</sub>(t_) and **Z**_<sub>j,k</sub>(t_) are defined as follows<tbc>

\(\mathbf{W}_{j,k}(t)=1-\lambda_{j,k}\int_0^t\mathbf{V}_{j,k}(\tau)d\tau\text{and}\mathbf{Z}_{j,k}(t)=\int_0^t\mathbf{V}_{j,k}(\tau)d\tau,\) (5.27)

<tbc>where

\(\mathbf{V}_{j,k}(t)=\mathcal{L}^{-1}\left(\frac{1}{s\widehat{\varrho}(s)+\lambda_{j,k}}\right),\) (5.28)

and **V**_<sub>j,k</sub>(t_) is the impulse-response function. From Lemma 4.1 in \[13\], we establish that **V**_<sub>j,k</sub>(t_) is a completely monotone function, meaning that its Laplace transform \(\widehat{\mathbf{V}}_{j,k}(s)\) is a Stieltjes function.<br>
In the Laplace domain, the representations of **W**_<sub>j,k</sub>(t_) and **Z**_<sub>j,k</sub>(t_) are given as follows

\(\widehat{\mathbf{W}}_{j,k}(s)=\frac{1}{s}-\frac{\lambda_{j,k}}{s(s\widehat{\varrho}(s)+\lambda_{j,k})},\widehat{\mathbf{Z}}_{j,k}(s)=\frac{1}{s(s\widehat{\varrho}(s)+\lambda_{j,k})}.\big\}\) (5.29)

The additional condition (5.13) provides the following expression for _f<sub>j,k</sub>_<tbc>

\(f_{j,k}=\frac{1}{\mathbf{Z}_{j,k}(T)}\left(g_{j,k}-\psi_{j,k}\mathbf{W}_{j,k}(T)\right),\) (5.30)

<tbc>where \(g_{j,k}=\left\langle g(x,y),Y_{j,k}(x,y)\right\rangle\).<br>
By plugging the value of _f<sub>j,k</sub>_ in Eq. (5.26), we obtain<tbc>

\(U_{j,k}(t)=\psi_{j,k}\mathbf{W}_{j,k}(t)+\frac{\mathbf{Z}_{j,k}(t)}{\mathbf{Z}_{j,k}(T)}\big(g_{j,k}-\psi_{j,k}\mathbf{W}_{j,k}(T)\big).\) (5.31)

<tbc>Now, we examine specific cases of Eqs. (5.26) and (5.30) based on the behavior of \(\varrho(t)\).<br>
To analyze the Laplace transform of the power-law memory kernel, given by \(\widehat{\varrho}(s)=\sum_{\xi=1}^n\frac{P_\xi}{(s+p)^{1-\beta_\xi}}\) and apply it in Eq. (5.29), we obtain the following estimates<tbc>

\(\mathbf{W}_{j,k}(t)=\frac{1}{P_1}-\frac{\lambda_{j,k}}{D_1}\int_0^te^{-p\tau}\tau^{\beta_1-1}E_{\bar{\beta},\beta_1}(\cdots\lambda\tau\cdots)d\tau\left.\begin{array}{ c }
=\frac{1}{P_1}e^{-pt}E_{\bar{\beta},1}(\cdots\lambda\mathbf{t}\cdots), \\
\mathbf{Z}_{j,k}(t)=\frac{1}{P_1}\int_0^te^{-p\tau}\tau^{\beta_1-1}E_{\bar{\beta},\beta_1}(\cdots\lambda\tau\cdots)d\tau \\
=\frac{1}{P_1}e^{-pt}t^{\beta_1}E_{\bar{\beta},\beta_1+1}(\cdots\lambda\mathbf{t}\cdots),
\end{array}\right\},\) (5.32)

<tbc>where \(E_{\bar{\beta},\beta_1}(\cdot)\) denotes the multinomial (generalized) Mittag–Leffler function, with parameters<tbc>

\(\bar{\beta}=(\beta_1-\beta_n,\dots,\beta_1-\beta_2,\beta_1),\)

