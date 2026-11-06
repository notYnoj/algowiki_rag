_where_ \((k;l_1,\dots,l_n)=\frac{k!}{l_1!\times\dots\times l_n!}\).

**Remark 1.2** _Notice that the multinomial MLF can be represented as_

\(E_{(\xi_1,\xi_2,\dots,\xi_n),\gamma}(z_1,z_2,\dots,z_n)\)<br>
\(=\sum_{k=0}^\infty\sum_{l_1=0}^k\sum_{l_2=0}^{k-l_1}\dots\sum_{l_{n-1}=0}^{k-l_1-\cdots-l_{n-2}}\frac{k!}{l_1!l_2!\dots(k-l_1-l_2-\dots-l_{n-1})!}\)<br>
\(\times\frac{z_1^{k-l_1-l_2-\dots-l_{n-1}}z_2^{l_1}\dots z_n^{l_{n-1}}}{\Gamma(\gamma+\xi_1(k-l_1-l_2-\dots-l_{n-1})+\xi_2l_1+\dots+\xi_nl_{n-1})}.\)

**Remark 1.3** _The parameter of the multinomial MLF commutes, i.e.,_

\(E_{(\xi_1,\xi_2,\dots,\xi_n),\gamma}(z_1,z_2,\dots,z_n)=E_{(\xi_n,\dots,\xi_2,\xi_1),\gamma}(z_n,\dots,z_2,z_1).\) (1.7)

**Remark 1.4** _For_ \(z_1\neq 0\), \(z_2\neq 0\), \(z_3=\dots=z_n=0,n\in\mathbb{N}\) _the multinomial MLF takes the following form_

\(E_{(\xi_1,\xi_2),\gamma}(z_1,z_2)=\sum_{k=0}^\infty\sum_{l_1+l_2=kl_1\ge 0,l_2\ge 0}\frac{k!}{l_1!l_2!}\frac{z_1^{l_1}z_2^{l_2}}{\Gamma(\gamma+\xi_1l_1+\xi_2l_2)},\)<br>
\(=\sum_{k=0}^\infty\sum_{i=0}^k\frac{k!}{i!(k-i)!}\frac{z_1^iz_2^{k-i}}{\Gamma(\gamma+\xi_1i+\xi_2(k-i))}.\)

**Remark 1.5** _For_ \(z_1\neq 0\) _and z_<sub>2</sub>=_z_<sub>3</sub>=_...=z<sub>n</sub>_=0, \(n\in\mathbb{N}\) _the multinomial MLF takes the following form_

\(E_{\xi_1,\gamma}(z_1)=\sum_{k=0}^\infty\frac{z_1^k}{\Gamma(\gamma+\xi_1k)}.\)

**Lemma 1.1** _\[79\] Let_ \(0<\gamma<2\) _and_ \(0<\xi_n<\cdots<\xi_1<1\)_. Assume that the angle K satisfies_ \(\xi_1\pi/2<K<\xi_1\pi\)_, and that_ \(K\le|arg(z_1)|\le\pi\) _and_ \(-K\le z_i<0\)_, where K\>_0_, i_=2_,...,n. Then there exists a positive constant C_<sub>0</sub>_, depending only on K,_ \(\xi_i(i=1,\dots,n)\)_, and_ \(\gamma\)_, such that the multinomial MLF satisfies_

\(|E_{(\xi_1-\xi_m,\dots,\xi_1-\xi_2,\xi_1),\gamma}(z_n,\dots,z_2,z_1)|\le\frac{C_0}{1+|z_1|}.\)

**Lemma 1.2** _\[85\] For_ \(\xi_i,\gamma,\tau,\nu_i>0,i=1,2,\dots,n,n\in\mathbb{N}\) _the Laplace transform of the multinomial MLF is given by_

\(\unknown\{\tau^{\gamma-1}E_{(\xi_1,\xi_2,\dots,\xi_n),\gamma}(-\nu_1\tau^{\xi_1},\dots,-\nu_n\tau^{\xi_n})\}=\frac{s^{-\gamma}}{1+\sum_{i=1}^n\nu_is^{-\xi_i}}.\)

_If_ \(\left|\sum_{i=1}^n\nu_is^{-\xi_i}\right|<1\).

