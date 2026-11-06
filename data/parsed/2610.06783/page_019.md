## 2.3.2 Unraveling the recursion computation

In this subsection, we carefully work out which two numbers are multiplied at the leaf \(\tau\), and what is returned by Full(_a,b_). For a leaf \(\tau\) let<tbc>

\(\Phi_\tau(a):=\sum_ua[u]\prod_{\ell=1}^L\varphi_{\tau_\ell}(u_\ell),\Psi_\tau(b):=\sum_vb[v]\prod_{\ell=1}^L\psi_{\tau_\ell}(v_\ell),\)

<tbc>where the sums are over all left strings _u_ and all right strings _v_ of length _L_. We extend the relation "contributes to" of Section 2.2 from terms to vertices: a vertex \(\tau_1\cdots\tau_k\) **_contributes to_** an output string _w_ if \(\tau_\ell\) contributes to \(w_\ell\) at every level \(\ell\le k\). Thus the leaf \(\tau\) contributes to _w_ if \(\tau_\ell=P_{ij}\) at every level \(\ell\) where \(w_\ell=z_{ij}\) (but \(\tau_\ell\) may be arbitrary at the levels where \(w_\ell=z_0\)). Let Mult(_a,b_) be the array on the output strings of length _L_ given by

\(\mathrm{Mult}(a,b)[w]:=\sum_{\tau\text{contributing to}w}\Phi_\tau(a)\Psi_\tau(b).\) (2)

**Lemma 7.** _At the leaf_ \(\tau\), Full(_a,b_) _multiplies_ \(\Phi_\tau(a)\) _by_ \(\Psi_\tau(b)\)_, and it returns_ Mult(_a,b)._

_Proof._ By induction on _L_ (see Figure 3). For _L_=0, the only leaf is the empty string \(\tau\), and \(\Phi_\tau(a)=a\) and \(\Psi_\tau(b)=b\), as the products over the levels are empty, so step (1) multiplies them and returns _ab_=Mult(_a,b_). For \(L\ge 1\), step (2) is the encoding: since \(a_s[u']=a[su']\), for every leaf \(\lambda\tau'\) we have<tbc>

\(\Phi_{\lambda\tau^\prime}(a)=\sum_s\varphi_\lambda(s)\Phi_{\tau^\prime}(a_s)=\Phi_{\tau^\prime}(A_\lambda),\)

the array a, cut into its seven slices a according to the variable s at level 1
ax1
ax2
ax3
ap11
ap12
ap21
ap22
step (2): encode
AP11
AP12
AP13
AP21
AP22
AP23
AP31
AP32
AP33
APo
step (3): recurse
CP11
CP12
CP13
CP21
CP22
CP23
CP31
CP32
CP33
CPo
step (4): decode
Cz11
Cz12
Cz13
Cz21
Cz22
Cz23
Cz31
Cz32
Cz33
Czo
the array c, cut into its ten slices cz according to the output variable z at level 1

Figure 3: One level of the recursion, the analog of one step of Strassen’s algorithm. In step (2), each of the ten terms \(\lambda\) combines at most three of the seven slices _a<sub>s</sub>_ into \(A_\lambda=\sum_s\varphi_\lambda(s)a_s\) (solid lines: +, dashed: -). For instance, _A_<sub>_P_<sub>31</sub></sub>=_a_<sub>_x_<sub>3</sub></sub>-_a_<sub>_p_<sub>11</sub></sub>-_a_<sub>_p_<sub>21</sub></sub> and _A_<sub>_P_<sub>0</sub></sub>=-_a_<sub>_x_<sub>1</sub></sub>-_a_<sub>_x_<sub>2</sub></sub>-_a_<sub>_x_<sub>3</sub></sub>. The same is done to _b_ with the forms \(\psi_\lambda\). In step (3), the ten pairs are multiplied by recursive calls, \(C_\lambda=\mathrm{Full}(A_\lambda,B_\lambda)\). In step (4), the slice _c<sub>z<sub>ij</sub></sub>_ of the output is _C<sub>P<sub>ij</sub></sub>_, and the slice _c_<sub>_z_<sub>0</sub></sub> is the sum of all ten, because every term contributes to _z_<sub>0</sub>.

