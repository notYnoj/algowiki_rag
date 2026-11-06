**Algorithm 4** Window construction algorithm for constant \(\lambda\)

procedure QuadraticWindows\((A,B,n,d,\epsilon_0)\)<br>
   \(\triangleright\) Generate W<sub>A</sub>:<br>
   \(W_A\leftarrow\emptyset\)<br>
   \(t\leftarrow n/d\)<br>
   for \(y=0\rightarrow t-1\) do<br>
   left \(\leftarrow y\cdot d\)<br>
   \(W_A\leftarrow W_A\cup\left\{A^{(left,d)}\right\}\)<br>
   end for<br>
   \(\triangleright\) Generate W<sub>B</sub>:<br>
   \(f\leftarrow\left\lceil log_{1+\epsilon_0}(1/\epsilon_0)\right\rceil+1\triangleright d\cdot(1+\epsilon_0)^f=\Theta(d/\epsilon_0)\)<br>
   \(W_B\leftarrow\emptyset\)<br>
   for \(i=-f\rightarrow f\) do<br>
   \(W_B^i\leftarrow\emptyset\)<br>
   \(d_i\leftarrow d(1+\epsilon_0)^i\), \(t_i\leftarrow n/d_i\), \(g_i\leftarrow\epsilon_0d_i\triangleright d_i\) is the length, g<sub>i</sub> is the shift<br>
   for \(x=0\rightarrow d_i/g_i-1\) do<br>
   for \(y=0\rightarrow t_i-1\) do<br>
   left \(\leftarrow x\cdot g_i+y\cdot d_i\)<br>
   len \(\leftarrow d_i\)<br>
   \(W_B^i\leftarrow W_B^i\cup\left\{B^{(left,len)}\right\}\)<br>
   end for<br>
   end for<br>
   \(W_B\leftarrow W_B\cup W_B^i\)<br>
   end for<br>
   return W<sub>A</sub>,W<sub>B</sub>,f<br>
end procedure

