It is not hard to check that \(\langle a,b,c\rangle\otimes\langle d,e,f\rangle=\langle ad,be,cf\rangle\). For a tensor _T_, let _R(T_) denote the tensor rank of _T_ and the matrix multiplication exponent \(\omega\) is defined as<tbc>

\(\omega:=\mathrm{inf}_{q\in\mathbb{N},q\ge 2}\mathrm{log}_qR(\langle q,q,q\rangle).\)

<tbc>It is hard to directly bound the tensor rank of \(\langle q,q,q\rangle\) in general, so current approaches to bounding \(\omega\) utilize Schönhage’s asymptotic sum inequality \[Sch81\], which states that if one can bound the asymptotic rank of a direct sum of matrix multiplication tensors, where the asymptotic rank \(\widetilde{R}(T)\) of a tensor _T_ is defined as

\(\widetilde{R}(T):=\mathrm{lim}_{n\rightarrow\infty} R(T^{\otimes n})^{1/n},\)

then one can get a bound on \(\omega\). More specifically, we recall the asymptotic sum inequality as follows.

**Theorem 2.1** (Asymptotic Sum Inequality \[Sch81\])**.** _For positive integers r\>m and a<sub>i</sub>,b<sub>i</sub>,c<sub>i</sub> for_ \(i\in[m]\)_, if_<tbc>

\(\widetilde{R}\left(\oplus_{i=1}^m\langle a_i,b_i,c_i\rangle\right)\le r,\)

<tbc>_then_ \(\omega\le 3\tau\) _where_ \(\tau\in[2/3,1]\) _is the solution to the equation_

\(\sum_{i=1}^m(a_i\cdot b_i\cdot c_i)^\tau=r.\)

Schönhage’s asymptotic sum inequality gave rise to the following approach to bounding \(\omega\): start with a tensor _T_ whose asymptotic rank \(\widetilde{R}(T)\) is easy to bound. Consider \(T^{\otimes n}\) for some _n_ sufficiently large and we want to transform \(T^{\otimes n}\) into a direct sum of matrix multiplication tensors whose asymptotic rank is upper bounded by the asymptotic rank of \(\widetilde{R}(T^{\otimes n})=\widetilde{R}(T)^n\). The common ways of doing such transformation is via zeroing-out, i.e., setting some variables in \(T^{\otimes n}\) to zero, or the more general degeneration, whose definition is deferred to Section 3. Then we can apply the asymptotic sum inequality to get a bound on \(\omega\). Observe that if \(T^{\otimes n}\) can be degenerated into \(\oplus_{i=1}^m\langle a_i,b_i,c_i\rangle\), then for a fixed \(\tau\), we want to maximize the value of \(\sum_{i=1}^m(a_i\cdot b_i\cdot c_i)^\tau\). This gives a notion of the "matrix multiplication value" of a tensor _T_ that we want to maximize. Then notice that a lower bound on the value of \(T^{\otimes n}\) would directly imply an upper bound on \(\omega\) via the asymptotic sum inequality. It still remains unknown how to get the best possible bound on \(\omega\) via a tensor power \(T^{\otimes n}\), but the laser method provides one way to give a nontrivial bound.

## Laser method.

Let _T_ be a tensor over three sets of variables _X,Y,Z_. For positive integers _s<sub>X</sub>,s<sub>Y</sub>,s<sub>Z</sub>_, let \(X=\sqcup_{i\in[s_X]}X_i,Y=\sqcup_{j\in[s_Y]}Y_j\) and \(Z=\sqcup_{k\in[s_Z]}Z_k\) be partitions of the _X_-, _Y_ -, _Z_-variable sets into _s<sub>X</sub>,s<sub>Y</sub>,s<sub>Z</sub>_ parts respectively. Then _T_ can be written as a sum of subtensors \(\sum_{i,j,k}T_{i,j,k}\), where _T<sub>i,j,k</sub>_ denotes the subtensor of _T_ restricted to variables _X<sub>i</sub>,Y<sub>j</sub>,Z<sub>k</sub>_.

Suppose for now that each subtensor _T<sub>i,j,k</sub>_ is a matrix multiplication tensor. If _T_ is a direct sum of matrix multiplication tensors, then we can apply Schönhage’s asymptotic sum inequality \[Sch81\] to obtain a bound on \(\omega\). However, _T_ is a sum of _T<sub>i,j,k</sub>_, not necessarily a direct sum.

The laser method \[Str86\] is devised to overcome this issue. First, we take the _n_-th tensor power of _T_ for some large _n_, which is a tensor over variables _X<sup>n</sup>,Y<sup>n</sup>,Z<sup>n</sup>_:<tbc>

\(T^{\otimes n}=\sum_{I\in[s_X]^n}\sum_{J\in[s_Y]^n}\sum_{K\in[s_Z]^n}T_{I,J,K},\)

