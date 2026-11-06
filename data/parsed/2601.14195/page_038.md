We define<tbc>

\(M(n)=9216n^2+229n,\text{and}\)<br>
\(k(n)=\left\lceil\frac{1}{3}(n+8\varepsilon-8)\right\rceil.\)

<tbc>Clearly \(M(n)\in\mathbb{N}\) because _n_ is a positive integer, so we can take _M(n_) out of the ceiling in _C(n_) and simply state<tbc>

\(C(n)=M(n)+k(n).\)

<tbc>Notice that, for \(n\ge 1\) and \(0<\varepsilon<1\), we have that<tbc>

\(-2\le k(n)\le\left\lceil\frac{n}{3}\right\rceil.\)

<tbc>Also, observe that<tbc>

\((96n+1)^2=9216n^2+192n+1,\text{and}\)<br>
\((96n+2)^2=9216n^2+384n+4.\)

<tbc>Hence, as \(n\ge 1\),<tbc>

\((96n+1)^2<C(n)<(96n+2)^2,\text{and}\)<br>
\(\left\lfloor\sqrt{C(n)}\right\rfloor=96n+1.\)

<tbc>Thus, finally,

\(|A_r|=C(n)-\frac{56}{3}n-96n\left\lfloor\sqrt{C(n)}\right\rfloor-96n\)<br>
\(=M(n)+k(n)-\frac{56}{3}n-96n(96n+1)-96n\)<br>
\(=9216n^2+229n+k(n)-\frac{56}{3}n-9216n^2-96n-96n\)<br>
\(=\frac{55}{3}n+k(n)\)<br>
\(>18n-2,\text{by}k(n)\ge-2\)<br>
\(>0,\text{by}n\ge 1.\)

For each variable \(V_i\in V\) , we construct the variable gadget _G<sub>V<sub>i</sub></sub>_ as in the proof of Theorem 4.4, and, for each clause \(C_j\in C\), we construct the clause gadget _G<sub>C<sub>j</sub></sub>_ as in the proof of Theorem 4.4.

Now, furthermore, for each \(x_i^r\) agent in each variable gadget _G<sub>V<sub>i</sub></sub>_, we construct \(\gamma_*\) many **connector gadgets** \(G_{T_{i,\gamma}^r}\) (where \(1\le\gamma\le\gamma_*\)) consisting of the twelve agents \(t_{i,\gamma}^{r,1},t_{i,\gamma}^{r,2},\dots,t_{i,\gamma}^{r,12}\), with preferences as follows:

\(t_{i,\gamma}^{r,1}:t_{i,\gamma}^{r,2}c(t_{i,\gamma}^{r,1})t_{i,\gamma}^{r,12}t_{i,\gamma}^{r,7}:t_{i,\gamma}^{r,6}x_{i,\gamma}^rt_{i,\gamma}^{r,8}\)<br>
\(t_{i,\gamma}^{r,2}:t_{i,\gamma}^{r,3}t_{i,\gamma}^{r,1}t_{i,\gamma}^{r,8}:t_{i,\gamma}^{r,7}t_{i,\gamma}^{r,9}\)<br>
\(t_{i,\gamma}^{r,3}:t_{i,\gamma}^{r,4}t_{i,\gamma}^{r,2}t_{i,\gamma}^{r,9}:t_{i,\gamma}^{r,8}t_{i,\gamma}^{r,10}\)<br>
\(t_{i,\gamma}^{r,4}:t_{i,\gamma}^{r,5}t_{i,\gamma}^{r,3}t_{i,\gamma}^{r,10}:t_{i,\gamma}^{r,9}t_{i,\gamma}^{r,11}\)<br>
\(t_{i,\gamma}^{r,5}:t_{i,\gamma}^{r,6}t_{i,\gamma}^{r,4}t_{i,\gamma}^{r,11}:t_{i,\gamma}^{r,10}t_{i,\gamma}^{r,12}\)<br>
\(t_{i,\gamma}^{r,6}:t_{i,\gamma}^{r,5}t_{i,\gamma}^{r,7}t_{i,\gamma}^{r,12}:t_{i,\gamma}^{r,11}t_{i,\gamma}^{r,1}\)

