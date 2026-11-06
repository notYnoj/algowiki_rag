Now, for every variable \(V_i\in V\) , we construct a **variable gadget** _G<sub>V<sub>i</sub></sub>_ consisting of the eight agents \(x_i^1,x_i^2,x_i^3,x_i^4,y_i^1,y_i^2,y_i^3,y_i^4\), with preferences as follows:

\(x_i^1:y_i^1c(x_i^1)y_i^2y_i^1:x_i^1x_i^4\)<br>
\(x_i^2:y_i^2c(x_i^2)y_i^3y_i^2:x_i^1x_i^2\)<br>
\(x_i^3:y_i^4c(x_i^3)y_i^3y_i^3:x_i^2x_i^3\)<br>
\(x_i^4:y_i^1c(x_i^4)y_i^4y_i^4:x_i^3x_i^4\)

where the \(c(x_i^r)\) entries will be specified later. The construction is illustrated in Figure 8. Notice that each _G<sub>V<sub>i</sub></sub>_ gadget only admits two perfect matchings:

\(M_i^1=\{\{x_i^1,y_i^1\},\{x_i^2,y_i^2\},\{x_i^3,y_i^3\},\{x_i^4,y_i^4\}\}\text{and}\)<br>
\(M_i^2=\{\{x_i^1,y_i^2\},\{x_i^2,y_i^3\},\{x_i^3,y_i^4\},\{x_i^4,y_i^1\}\},\)

which admit the blocking pairs \(\{x_i^3,y_i^4\}\) and \(\{x_i^1,y_i^1\}\), respectively, within the gadget (not counting blocking pairs that may also involve \(c(x_i^r)\) entries), respectively. Intuitively, these matchings will later correspond to _V<sub>i</sub>=T_ and _V<sub>i</sub>=F_, respectively.

For every clause \(C_j=(C_j^1\vee C_j^2\vee C_j^3)\in C\), we construct a **clause gadget** _G<sub>C<sub>j</sub></sub>_ consisting of the eight agents \(c_j^1,c_j^2,c_j^3,p_j^1,p_j^2,p_j^3,q_j,z_j\), with preferences constructed as follows:

\(c_j^1:p_j^1x(c_j^1)q_jp_j^1:c_j^1z_j\)<br>
\(c_j^2:p_j^2x(c_j^2)q_jp_j^2:c_j^2z_j\)<br>
\(c_j^3:p_j^3x(c_j^3)q_jp_j^3:c_j^3z_j\)<br>
\(z_j:p_j^1p_j^2p_j^3q_j:c_j^1c_j^2c_j^3\)

where the \(x(c_j^s)\) entries will be specified below. The construction is illustrated in Figure 9. Notice that each _G<sub>C<sub>j</sub></sub>_ gadget only admits three different perfect matchings:

\(M_j^1=\{\{c_j^1,q_j\},\{c_j^2,p_j^2\},\{c_j^3,p_j^3\},\{p_j^1,z_j\}\},\)<br>
\(M_j^2=\{\{c_j^1,p_j^1\},\{c_j^2,q_j\},\{c_j^3,p_j^3\},\{p_j^2,z_j\}\},\text{and}\)<br>
\(M_j^3=\{\{c_j^1,p_j^1\},\{c_j^2,p_j^2\},\{c_j^3,q_j\},\{p_j^3,z_j\}\},\)

which admit the blocking pairs \(\{c_j^1,p_j^1\}\), \(\{c_j^2,p_j^2\}\) and \(\{c_j^3,p_j^3\}\) within the gadget (not counting blocking pairs that may also involve \(x(c_j^s)\) entries), respectively. Intuitively, these matchings correspond to the first, second, and third literals of _C<sub>j</sub>_ being true, respectively.

