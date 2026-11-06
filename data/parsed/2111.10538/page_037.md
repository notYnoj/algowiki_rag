**Definition 4.5** (Window construction for arbitrary \(\lambda\))**.**

\(W_A,W_B^0:=\big\{B^{(\mathrm{left},\mathrm{len})}\big|\mathrm{left}=y\cdot d,\forall y\in\{0,1,\cdots,t_0-1\}\big\}\)

\(W_B^i:=\big\{B^{(\mathrm{left},\mathrm{len})}\big|\mathrm{left}=y\cdot d_i,\mathrm{len}=d_i/2+x\cdot d,\forall x\in\{1,\cdots,d_i/(2d)\}\forall y\in\{0,1,\cdots,t_i-1\}\big\}\)

where we use _B_<sup>(left,len)</sup> to denote a (contiguous) substring of string _B_ that starts at left and has length len. Finally _W<sub>B</sub>_ is \(\cup_{i\in\{0,1,\cdots,f\}}W_B^i\).

In other words, the window construction in Definition 4.5 considers all the substrings that start at any multiple of \(d\cdot 2^i\) and whose length is a multiple of _d_, and at most \(d\cdot 2^i-1\).

**Algorithm 5** Window construction algorithm for arbitrary \(\lambda\)

procedure CubicWindows\((A,B,n,d,\epsilon_0)\triangleright\) Generate _W<sub>A</sub>_ and \(W_B^0\):<br>
   \(W_A,W_B^0\leftarrow\emptyset\)<br>
   \(t\leftarrow n/d\)<br>
   for \(y=0\rightarrow t-1\) do<br>
   \(\mathrm{left}\leftarrow y\cdot d\)<br>
   \(W_A\leftarrow W_A\cup\big\{A^{(\mathrm{left},d)}\big\}\)<br>
   \(W_B^0\leftarrow W_B^0\cup\big\{B^{(\mathrm{left},d)}\big\}\)<br>
   end for<br>
   \(f\leftarrow\mathrm{log}(1/\epsilon_0)\triangleright\) Generate _W<sub>B</sub>_:<br>
   \(W_B\leftarrow W_B^0\triangleright d\cdot 2^f=d/\epsilon_0\)<br>
   for \(i=1\rightarrow f\) do<br>
   \(W_B^i\leftarrow\emptyset\)<br>
   \(d_i\leftarrow d\cdot 2^i\), \(t_i\leftarrow n/d_i\)<br>
   for \(x=1\rightarrow d_i/(2d)\) do<br>
   for \(y=0\rightarrow t_i-1\) do<br>
   \(\mathrm{left}\leftarrow y\cdot d_i\)<br>
   \(\mathrm{len}\leftarrow d_i/2+x\cdot d\)<br>
   \(W_B^i\leftarrow W_B^i\cup\big\{B^{(\mathrm{left},\mathrm{len})}\big\}\)<br>
   end for<br>
   end for<br>
   \(W_B\leftarrow W_B\cup W_B^i\)<br>
   end for<br>
   return W<sub>A</sub>,W<sub>B</sub>,f<br>
end procedure

**Fact 4.6** (Parameters for arbitrary \(\lambda\) (Theorem 2.1))**.**

_Let_ \(\epsilon>0\) _be a small constant and_ \(\lambda\) _is the relative length of the true LCS between A and B. In order to make sure the loss in the approximation is small, we use_<tbc>

\(\epsilon_0:=\epsilon\lambda.\)

