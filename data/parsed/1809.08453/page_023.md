input :<br>
set IN<sub>v</sub> and `OUT`<sub>v</sub> of mandatory and forbidden rotations, index k of the next triple, set \(\mathcal{A}_\unknown\)<br>
output: T<sub>W</sub>(v)<br>
Compute `x`<sub>IN<sub>v</sub></sub> and `x`<sub>P\\`OUT`<sub>v</sub></sub><br>
\(T\leftarrow\emptyset\); \(R\leftarrow\mathsf{IN}_\unknown\); \(i\leftarrow 0\); \(\mathbf{x}_i\leftarrow\mathbf{x}_R\)<br>
\(W_i\leftarrow\{w\in\mathcal{A}_\unknown\cap\mathcal{W}:d(w,\mathbf{x}_i)=d_k^\unknown(\mathbf{x}_i)\}\)<br>
Flag \(\leftarrow\) False<br>
while \(W_i\neq\emptyset\) do<br>
   for \(w\in W_i\)<br>
   let m be the match of w in x<sub>i</sub><br>
   \(T\leftarrow T\cup\{(d(w,m),w,m)\}\)<br>
   if \((m,w)\in\mathbf{x}_{P\backslash\mathsf{OUT}_\unknown}\) then Flag \(\leftarrow\) True<br>
   else \(R\leftarrow R\cup\rho_\mathsf{break}(m,w)\cup\mathsf{Anc}(\rho_\mathsf{break}(m,w))\)<br>
   if Flag then return T<br>
   \(i\leftarrow i+1\); \(\mathbf{x}_i\leftarrow\mathbf{x}_R\)<br>
   \(W_i\leftarrow\{w\in\mathcal{A}_\unknown\cap\mathcal{W}:d(w,\mathbf{x}_i)=d_k^\unknown(\mathbf{x}_i)\}\)<br>
return T

input :<br>
set IN<sub>v</sub> and `OUT`<sub>v</sub> of mandatory and forbidden rotations, index k of the next triple, set \(\mathcal{A}_\unknown\)<br>
output: T<sub>M</sub>(v)<br>
Compute `x`<sub>IN<sub>v</sub></sub> and `x`<sub>P\\`OUT`<sub>v</sub></sub><br>
\(T\leftarrow\emptyset\); \(R\leftarrow P\backslash\mathsf{OUT}_\unknown\); \(i\leftarrow 0\); \(\mathbf{x}_i\leftarrow\mathbf{x}_R\)<br>
   \(M_i\leftarrow\{m\in\mathcal{A}_\unknown\cap\mathcal{M}:d(m,\mathbf{x}_i)=d_k^\unknown(\mathbf{x}_i)\}\)<br>
Flag \(\leftarrow\) False<br>
while \(M_i\neq\emptyset\) do<br>
   for \(m\in M_i\)<br>
   let w be the match of m in x<sub>i</sub><br>
   \(T\leftarrow T\cup\{(d(m,w),m,w)\}\)<br>
   if \((m,w)\in\mathbf{x}_{\mathsf{IN}_\unknown}\) then Flag \(\leftarrow\) True<br>
   else \(R\leftarrow R\backslash(\rho_\mathsf{get}(m,w)\cup\mathsf{Des}(\rho_\mathsf{get}(m,w)))\)<br>
   if Flag then return T<br>
   \(i\leftarrow i+1\); \(\mathbf{x}_i\leftarrow\mathbf{x}_R\)<br>
   \(M_i\leftarrow\{m\in\mathcal{A}_\unknown\cap\mathcal{M}:d(m,\mathbf{x}_i)=d_k^\unknown(\mathbf{x}_i)\}\)<br>
return T

### 6 Conclusion

In this paper, we have shown that the minimization of a Generalized Gini Index (GGI) of the dissatisfactions of men and women in a stable marriage problem is an NP-hard problem. Then, we have proposed a polynomial time 2-approximation algorithm for the problem, based on a rounding of the optimal solution to the linear programming relaxation of the problem. Lastly, we have shown that minimizing a GGI of the dissatisfactions of men and women in a stable marriage is in the class XP with respect to the number of strictly positive weights in the GGI operator.

For future works, following Aziz and Klaus \[2017\], it could be worth investigating the randomized version of the GGI stable marriage problem. By _randomized_, we mean that we consider mixed stable marriages, and not only deterministic stable marriages. A mixed stable marriage is a probability distribution over stable marriages. This enlargement of the

**Algorithm 3:** NextWomen

**Algorithm 4:** NextMen

