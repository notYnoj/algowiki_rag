### A Generating neighborhoods

**Algorithm 1. GenerateNeighborhood**(_T,d_)

**for** (_i_=1..|_T_|) **do** _r<sub>i</sub>_:=_d_;

**GenerateNeighborhood**(_T,r,_1)

**GenerateNeighborhood**(_T,r,p_)

**if** \((p\le l)\) **then**

**if** (**not** prune(_T,r_)) **then**

**for** \(\alpha\in\Sigma\) **do**

\(x_p:=\alpha\)

**for** (_i_=1..|_T_|) **do**

\(T'_i:=T_i[2..|S_i|]\)

\(r'_i:=r_i\);

**if** \((T_i[0]\neq\alpha)\) **then** \(r'_i:=r'_i-1\);

**end for**

**GenerateNeighborhood**\((T',r',p+1)\)

**end for**

**end if**

**else**

report _l_-mer _x_

**end if**

### B PMS8 pseudocode

**Algorithm 2. PMS8**(_T,d_)

**for** (_i_=1.._n_) **do** \(R_i=\{u|u\in S_i\}\)

_stack_={}

**GenerateMotifs**(1_,stack,R_)

**GenerateMotifs**(_p,stack,R_)

**for** \((u\in R_p)\) **do**

stack.push(_u_)

\(R':=\)filter(_R,_ stack)

**if** \((R'.\)size _\>_0) **then**

**if** (ThresholdCondition) **then**

_N_:=**GenerateNeighborhood**(stack,_d_)

**for** \((m\in N)\) **do**

**if** \((\text{isMotif}(m,R'))\) **then** output _m_;

**else**

**GenerateMotifs**\((p+1,R')\)

stack.pop()

**end for**

