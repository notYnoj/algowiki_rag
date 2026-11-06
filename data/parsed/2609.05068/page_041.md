where \(\delta=\frac{1}{n+2m}=\frac{3}{5n}\). Consequently, at least one path must carry a load strictly greater than \(1+\delta\). We show that the delay of such a path is strictly greater than _d_<sub>2</sub>=2, which contradicts the feasibility of the flow.

• **Case 1.** Assume that the load through a path \(\{s\rightarrow u_i\rightarrow t\}_{i\in I}\) exceeds \(1+\delta\). The delay is:<tbc>

<tbc>\(d_{s\rightarrow u_i\rightarrow t}\ge\frac{1}{c_{(s,u_i)}-(1+\delta)}+\frac{1}{c_{(u_i,t)}-(1+\delta)}=\frac{1}{mw_i+(m-1)W+1-\delta}+\frac{1}{1-\delta}.\)<tbc>

<tbc>Using \(w_i\le\frac{W}{m}\), we have \(mw_i+(m-1)W\le W+mW-W=mW=\frac{n/3}{(2n)^2}=\frac{1}{12n}\). Thus, because \(\frac{1}{1-e}\ge 1+e\) for _e\<_1:<tbc>

<tbc>\(d_{s\rightarrow u_i\rightarrow t}\ge\frac{1}{1+\frac{1}{12n}-\frac{3}{5n}}+\frac{1}{1-\frac{3}{5n}}\ge(1-\frac{1}{12n}+\frac{3}{5n})+(1+\frac{3}{5n})=2+2\frac{3}{5n}-\frac{1}{12n}>2\)<tbc>

<tbc>ensuring that commodity _k_<sub>2</sub> cannot satisfy its delay if a load \(1+\delta\) crosses path \(s\rightarrow u_i\rightarrow t\).<tbc>

• **Case 2.** Assume that the load through a path \(\{s\rightarrow v_j\rightarrow t\}_{j\in I}\) exceeds \(1+\delta\). The delay is:<tbc>

<tbc>\(d_{s\rightarrow v_j\rightarrow t}\ge\frac{1}{c_{(s,v_j)}-(1+\delta)}+\frac{1}{c_{(v_j,t)}-(1+\delta)}=\frac{1}{1-\delta}+\frac{1}{\frac{W}{m}+1-\delta}.\)<tbc>

<tbc>Using the same reasoning as above, we get:<tbc>

<tbc>\(d_{s\rightarrow v_j\rightarrow t}\ge\frac{1}{1-\frac{3}{5n}}+\frac{1}{1+\frac{3}{4n^3}-\frac{3}{5n}}\ge(1+\frac{3}{5n})+(1-\frac{3}{4n^3}+\frac{3}{5n})=1+2\frac{3}{5n}-\frac{3}{4n^3}>2\)<tbc>

<tbc>ensuring that commodity _k_<sub>2</sub> cannot satisfy its delay if a load \(1+\delta\) crosses path \(s\rightarrow v_j\rightarrow t\).<tbc>

• **Case 3.** Assume that the load through a path \(\{s\rightarrow v_j^N\rightarrow t\}_{j\in I}\) exceeds \(1+\delta\). The delay is:<tbc>

<tbc>\(d_{s\rightarrow v_j^N\rightarrow t}\ge\frac{1}{c_{(s,v_j^N)}-(1+\delta)}+\frac{1}{c_{(v_j^N,t)}-(1+\delta)}=\frac{1}{1-\delta}+\frac{1}{W\frac{(n+1)(n-3)}{n}+1-\delta}.\)<tbc>

