**Algorithm 3** Computation of est for LCS

function ComputeLCS(l,y<sub>l</sub>,r,y<sub>r</sub>,s)

• **requirement 1:** \(\langle l,y_l\rangle\) and \(\langle r,y_r\rangle\) are both vertices in the sparsified grid graph

• **requirement 2:** \(\langle r,y_r\rangle\) is reachable from \(\langle l,y_l\rangle\)

• **requirement 3:** \(s\in[S]\cup\{0\}\)

• **requirement 4:** (l,r] is a scale-s interval

• **returns:** an estimate est\[l,y<sub>l</sub>,r,y<sub>r</sub>\] for the longest \(\langle l,y_l\rangle\)-\(\langle r,y_r\rangle\) path

2: **if** s=0 **then return** ew\[l,y<sub>l</sub>,r,y<sub>r</sub>\]

3: **else if** \(s\notin\widetilde{S}\) **then**

4: \(V\leftarrow\emptyset\triangleright\) Initialize vertices for Scale-(s-1) Sparsified Grid Graph

5: \(E\leftarrow\emptyset\triangleright\) Initialize edges for Scale-(s-1) Sparsified Grid Graph

6: **for** \(x\in\) multiples of I<sub>s-1</sub> in (l,r] **do**

7: **for** \(y\in\) multiples of \(I_{s-1}/\phi_y\) in \[0,n\] **do**

8: add \(\langle x,y\rangle\) to V

9: **if** \(x+I_{s-1}\le r\) **then**

10: **for** \(y'\in\) multiples of \(I_{s-1}/\phi_y\) in \[0,n\] **do**

11: **if** \(|y'-y|\le I_{s-1}\) **then**

12: **if** \(\mathrm{est}[x,y,x+I_{s-1},y']=\perp\) **then** \(\triangleright\) Estimate not yet computed

13: \(\mathrm{est}[x,y,x+I_{s-1},y']\leftarrow\mathrm{ComputeEstimatLCS}\left(x,y,x+I_{s-1},y',s-1\right)\triangleright\) Compute estimate for sub-interval

14: add an edge from \(\langle x,y\rangle\) to \(\langle x+I_{s-1},y'\rangle\) with weight \(\mathrm{est}[x,y,x+I_{s-1},y']\)

to E

15: \(G\leftarrow\langle V,E\rangle\triangleright\) Create the Scale-(s-1) Sparsified Grid Graph

16: **return** length of longest \(\langle l,y_l\rangle\)-\(\langle r,y_r\rangle\) path in G via standard techniques for acyclic graphs

17: **else**

18: \(\overline{y_i}\leftarrow(I_{s-1}/\phi_y)\cdot\left\lfloor\frac{y_l+i\cdot\frac{y_r-y_l}{M}}{I_{s-1}/\phi_y}\right\rfloor\) for \(1\le i\le M\)

19: \(m_i\leftarrow l+i\cdot\frac{r-l}{M}\) for \(1\le i\le M\)

20: **for** \(i\in[1,M]\) **do**

21: **if** \(\eta_{l,r,i}=1\) **then** \(\triangleright i\)-th sub-interval is in sample

22: **if** \(\mathrm{est}[m_{i-1},\overline{y_{i-1}},m_i,\overline{y_i}]=\perp\) **then** \(\triangleright\) Estimate not yet computed

23: \(\mathrm{est}[m_{i-1},\overline{y_{i-1}},m_i,\overline{y_i}]\leftarrow\mathrm{ComputeEstimatLCS}\left(m_{i-1},\overline{y_{i-1}},m_i,\overline{y_i},s-1\right)\triangleright\)

Compute estimate for sub-interval

24: **return** ESTSUM \(\left((\mathrm{est}[m_{i-1},\overline{y_i},m_i,\overline{y_i}])_{\eta_{l,r,i}=i|i\in[M]}\right)\)

