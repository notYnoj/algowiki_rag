variables _X<sub>z</sub>_ which have values in {-1,0,-1} and are defined as follows:<tbc>

\(X_z=\left\{\begin{array}{ c c }
-1 & \text{if}y<z<x; \\
0 & \text{if}y<z\text{and}x<z,\text{or}y>z\text{and}x>z; \\
+1 & \text{if}y>z>x.
\end{array}\right.\)

<tbc>Moreover, we let _X<sub>x</sub>_ be a random variable that equals -1 if _y\<x_ and +1 if _y\>x_, and we define:<tbc>

\(\widetilde{X}_z=\left\{\begin{array}{ c c }
X_z & \text{if}z\in I_M; \\
max\{0,X_z\} & \text{if}z\in I_L\cup I_R
\end{array}\right..\)

<tbc>By Lemma 5.6, we have \(B\subseteq I=I_L\cup I_M\cup I_R\), and according to the above definitions, we have:

\(\text{score}(y)-\text{score}(x)=\sum_{z\in B\backslash\{y\}}X_z\le\sum_{z\in I_M\backslash\{y\}}\widetilde{X}_z+\sum_{z\in I_L\cup I_R}\widetilde{X}_z.\) (1)

In the rest of the proof, we will upper bound the probability that the right-hand side of (1) is non-negative. We start by considering the elements \(z\in I_M\backslash\{y\}\):

\(\bullet\) If _z=x_, then Pr(_X<sub>z</sub>_=-1)=1-_p_<sub>{_x,y_}</sub> and Pr(_X<sub>z</sub>_=1)=_p_<sub>{_x,y_}</sub>. Therefore, E\[_X<sub>z</sub>_\]=-(1-_p_<sub>{_x,y_}</sub>)+_p_<sub>{_x,y_}</sub>=2_p_<sub>{_x,y_}</sub>-1\le 2_p_-1;<tbc>

\(\bullet\) If _z\<y_, then Pr(_X<sub>z</sub>_=-1)=_p_<sub>{_z,y_}</sub>(1-_p_<sub>{_z,x_}</sub>), Pr(_X<sub>z</sub>_=1)=(1-_p_<sub>{_z,y_}</sub>)_p_<sub>{_z,x_}</sub>, and E\[_X<sub>z</sub>_\]=-_p_<sub>{_z,y_}</sub>(1-_p_<sub>{_z,x_}</sub>)+(1-_p_<sub>{_z,y_}</sub>)_p_<sub>{_z,x_}</sub>=_p_<sub>{_z,x_}</sub>-_p_<sub>{_z,y_}</sub>\le p-q;<tbc>

\(\bullet\) If _z\>x_, then Pr(_X<sub>z</sub>_=-1)=(1-_p_<sub>{_z,y_}</sub>)_p_<sub>{_z,x_}</sub>, Pr(_X<sub>z</sub>_=1)=_p_<sub>{_z,y_}</sub>(1-_p_<sub>{_z,x_}</sub>), and E\[_X<sub>z</sub>_\]=-(1-_p_<sub>{_z,y_}</sub>)_p_<sub>{_z,x_}</sub>+_p_<sub>{_z,y_}</sub>(1-_p_<sub>{_z,x_}</sub>)=_p_<sub>{_z,y_}</sub>-_p_<sub>{_z,x_}</sub>\le p-q;<tbc>

\(\bullet\) If _y\<z\<x_, then Pr(_X<sub>z</sub>_=-1)=(1-_p_<sub>{_z,y_}</sub>)(1-_p_<sub>{_z,x_}</sub>) and Pr(_X<sub>z</sub>_=1)=_p_<sub>{_z,y_}</sub>_p_<sub>{_z,x_}</sub>. Therefore, E\[_X<sub>z</sub>_\]=-(1-_p_<sub>{_z,y_}</sub>)(1-_p_<sub>{_z,x_}</sub>)+_p_<sub>{_z,y_}</sub>_p_<sub>{_z,x_}</sub>=_p_<sub>{_z,y_}</sub>+_p_<sub>{_z,x_}</sub>-1\le 2_p_-1.

Note that 2_p_-1_\<_0 and that \(p-q\ge 0\). Since the number of elements \(z\in I_M\) such that \(y<z\le x\) is at least _x-y_, we have:

\(\mathbb{E}\left[\sum_{z\in I_M\backslash\{y\}}\widetilde{X}_z\right]=\sum_{z\in I_M\backslash\{y\}z\in\{y+1,\dots,x\}}\mathbb{E}[X_z]+\sum_{z\in I_M\backslash\{y\}z\notin\{y+1,\dots,x\}}\mathbb{E}[X_z]\)<br>
\(\le(x-y)\cdot(2p-1)+(|I_M|-(x-y))\cdot(p-q)\)<br>
\(\le\rho\frac{w}{2}\cdot(2p-1)+(5w-\rho\cdot\frac{w}{2})(p-q)=\rho\frac{w}{2}(p+q-1)+5w(p-q).\)

We now consider the elements \(z\in I_L\cup I_R\). If _z\<y_, then \(\text{Pr}(X_z=1)=p_{\{z,y\}}(1-p_{\{z,x\}})\le pq\), while if _z\>x_, then \(\text{Pr}(X_z=1)=(1-p_{\{z,y\}})p_{\{z,x\}}\le pq\). Since \(\mathbb{E}[\widetilde{X}_z]=\mathbb{E}[max\{0,X_z\}]=\text{Pr}(X_z=1)\le pq\), we have:<tbc>

\(\mathbb{E}\left[\sum_{z\in I_L\cup I_R}\widetilde{X}_z\right]=\sum_{z\in I_L\cup I_R}\mathbb{E}[\widetilde{X}_z]\le 4wpq.\)

<tbc>To upper bound the probability that \(\widetilde{X}=\sum_{z\in I_M\backslash\{y\}}\widetilde{X}_z+\sum_{z\in(I_L\cup I_R)\backslash\{y\}}\widetilde{X}_z\) is non-negative, we observe that all the _X<sub>z</sub>_ are independent random variables with values in {-1,0,1} and hence the same holds for the random variables \(\widetilde{X}_z\). Moreover:

\(\mathbb{E}[\widetilde{X}]=\mathbb{E}\left[\sum_{z\in I_M\backslash\{y\}}\widetilde{X}_z\right]+\mathbb{E}\left[\sum_{z\in I_L\cup I_R}\widetilde{X}_z\right]\le\rho\cdot\frac{w}{2}(p+q-1)+5w(p-q)+4wpq\)<br>
\(=-\frac{w}{2}\left(\rho(1-p-q)-10(p-q)-8pq\right),\)

