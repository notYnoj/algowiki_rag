<tbc>where

\(T_{I,J,K}=T_{I_1,J_1,K_1}\otimes T_{I_2,J_2,K_2}\otimes\cdots\otimes T_{I_n,J_n,K_n}.\)

We will refer to these three sets of variables as _X_-variables, _Y_ -variables and _Z_-variables respectively. Because each _T<sub>i,j,k</sub>_ is a matrix multiplication tensor and the tensor products of several _T<sub>i,j,k</sub>_’s will still be matrix multiplication tensors, _T<sub>I,J,K</sub>_ is a matrix multiplication tensor for any \(I\in[s_X]^n,J\in[s_Y]^n,K\in[s_Z]^n\). For any \(I\in[s_X]^n\), let _X<sub>I</sub>_ denote \(X_{I_1}\times X_{I_2}\times\cdots\times X_{I_n}\), which is a subset of _X<sup>n</sup>_. Similarly we define _Y<sub>J</sub>_ and _Z<sub>K</sub>_. It is not difficult to see that _T<sub>I,J,K</sub>_ is exactly the subtensor of \(T^{\otimes n}\) when restricted to _X<sub>I</sub>,Y<sub>J</sub>,Z<sub>K</sub>_. We call such subsets _X<sub>I</sub>,Y<sub>J</sub>,Z<sub>K</sub> variable blocks_.

The goal of the laser method is to select some of the variable blocks _X<sub>I</sub>,Y<sub>J</sub>_ or _Z<sub>K</sub>_ and zero out all of the variables in these blocks, i.e. "zero out the blocks", so that the remaining tensor is a direct sum of _T<sub>I,J,K</sub>_’s.

The laser method specifies a distribution \(\alpha\) over triples (_i,j,k_) where \(i\in[s_X],j\in[s_Y],k\in[s_Z]\), so that for each _T<sub>I,J,K</sub>_ that we want to keep in the direct sum, we require that

\(\big|\{t\in[n]|(I_t,J_t,K_t)=(i,j,k)\}\big|=\alpha(i,j,k)\cdot n.\) (1)

If a subtensor _T<sub>I,J,K</sub>_ satisfies (1), we say that it is _consistent_ with the distribution \(\alpha\).

The distribution \(\alpha\) induces the marginal distributions \(\alpha_X,\alpha_Y,\alpha_Z\) on the _X_-, _Y_ -, _Z_-variables over the indices \[_s<sub>X</sub>_\],\[_s<sub>Y</sub>_\],\[_s<sub>Z</sub>_\] respectively as follows. Let \(\alpha_X\), \(\alpha_Y\), \(\alpha_Z\) be the marginal distributions of \(\alpha\) on the three dimensions respectively, i.e.,

\(\alpha_X(i)=\sum_{j\in[s_Y],k\in[s_Z]}\alpha(i,j,k)\forall i\in[s_X],\)<br>
\(\alpha_Y(j)=\sum_{i\in[s_X],k\in[s_Z]}\alpha(i,j,k)\forall j\in[s_Y],\)<br>
\(\alpha_Z(k)=\sum_{i\in[s_X],j\in[s_Y]}\alpha(i,j,k)\forall k\in[s_Z].\)

In the laser method, we zero out all _X_-variable blocks _X<sub>I</sub>_ that are not consistent with \(\alpha_X\) (_X<sub>I</sub>_ is consistent with \(\alpha_X\) if \(|\{t\in[n]:I_t=i\}|=\alpha_X(i)\cdot n\) for every \(i\in[s_X]\)). We similarly zero out all _Y_ -variable blocks _Y<sub>J</sub>_ that are not consistent with \(\alpha_Y\) and _Z_-variable blocks _Z<sub>K</sub>_ that are not consistent with \(\alpha_Z\).

At this stage, a subtensor _T<sub>I,J,K</sub>_ remains if _X<sub>I</sub>,Y<sub>J</sub>_ and _Z<sub>K</sub>_ all remain. Thus, all remaining _T<sub>I,J,K</sub>_’s are consistent with some distribution \(\alpha'\) that induces the same marginal distributions \(\alpha_X,\alpha_Y,\alpha_Z\), though \(\alpha'\) might be different from \(\alpha\). The final stages of the laser method aim to keep a collection of independent subtensors _T<sub>I,J,K</sub>_ and zero out the subtensors _T<sub>I,J,K</sub>_ that are consistent with a distribution \(\alpha'\neq\alpha\), using techniques such as hashing and greedy procedures. Eventually, the laser method obtains multiple independent copies of the tensor isomorphic to:

\(\mathcal{T}:=\otimes_{i,j,k}T_{i,j,k}^{\otimes\alpha(i,j,k)\cdot n}.\)

## The Coppersmith-Winograd tensor CW_<sub>q</sub>_.

Prior works \[CW90, DS13, Vas12, LG14, AV21, DWZ23\] that obtained the best bounds on \(\omega\) used the Coppersmith-Winograd tensor CW_<sub>q</sub>_ and its powers as the starting tensor _T_ in the laser method. The Coppersmith-Winograd tensor CW_<sub>q</sub>_ for a nonnegative integer _q_ is defined as<tbc>

\(\mathrm{CW}_q:=x_0y_0z_{q+1}+x_0y_{q+1}z_0+x_{q+1}y_0z_0+\sum_{i=1}^q(x_0y_iz_i+x_iy_0z_i+x_iy_iz_0).\)

