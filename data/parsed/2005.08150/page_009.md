<tbc>For each vertex \(u\in V_i\), where \(i\in[k]\), we have the following preferences:

\(u_1:\langle u_2,p_{\lceil\ell/2\rceil}^i\rangle\text{where for some}\ell\in[n]\text{,}u\text{is the}\ell^{th}\text{vertex in}V_i\text{.}u_{2h+1}:\langle u_{2h},e,u_{2h+2}\rangle\text{where}e\text{is the}h^{th}\text{element of}E_u\text{,}h\in[r]u_{2h}:\langle u_{2h-1},u_{2h+1}\rangle\text{where}h\in[r]u_{2r+2}:\langle u_{2r+1},\tilde{p}_{\lceil\ell/2\rceil}^i\rangle\text{where for some}\ell\in[n]\text{,}u\text{is the}\ell^{th}\text{vertex in}V_i\)

For the special vertices of the _i<sup>th</sup>vertex gadget_, we have the following preferences:

\(p_\ell^i:\langle u_1,v_1,a_{1,\ell}^i\rangle\text{where for some}\ell\in[n/2]\text{,}u\text{and}v\text{are the}2\ell-1^{st}\text{and}2\ell^{th}\text{vertices of}V_i\text{, respectively.}\tilde{p}_\ell^i:\langle u_{2r+2},v_{2r+2},\tilde{a}_{1,\ell}^i\rangle\text{where for some}\ell\in[n/2]\text{,}u\text{and}v\text{are the}2\ell-1^{st}\text{and}2\ell^{th}\text{vertices of}V_i\text{, respectively.}a_{1\ell}^i:\langle p_\ell^i,b_{1,\lceil\ell/2\rceil}^i\rangle\text{where}\ell\in[n/2]\tilde{a}_{1,\ell}^i:\langle\tilde{p}_\ell^i,\tilde{b}_{1,\lceil\ell/2\rceil}^i\rangle\text{where}\ell\in[n/2]a_{j,\ell}^i:\langle b_{j-1,\ell}^i,b_{j,\lceil\ell/2\rceil}^i\rangle\text{where}j\in[log_2(n/2)]\backslash\{1\text{and}\ell\in[n/2^j]b_{j,\ell}^i:\langle a_{j,2\ell-1}^i,a_{j,2\ell}^i,a_{j+1,\ell}^i\rangle\text{where}j\in[log_2(n/2)]\backslash\{1\text{and}\ell\in[n/2^j]b_{j,\ell}^i:\langle\tilde{a}_{j(2\ell-1)}^i,\tilde{a}_{j,2\ell}^i,\tilde{a}_{j+1,\ell}^i\rangle\text{where}j\in[log_2(n/2)-1]\text{and}\ell\in[n/2^{j+1}]b_{j,1}^i:\langle a_{j,1}^i,a_{j,2}^i\rangle\text{where}j=log_2(n/2)\tilde{b}_{j,1}^i:\langle\tilde{a}_{j,1}^i,\tilde{a}_{j,2}^i\rangle\text{where}j=log_2(n/2)\)

For each edge \(e\in E_{ij}\), \(1\le i<j\le k\), we have the following preferences:

\(e:\langle\tilde{e},u_{2h+1},v_{2h^\prime+1},q_{\lceil\ell/2\rceil}^{ij}\rangle\text{where for some}\ell\in[m]\text{, edge}e=uv=E_{ij}(\ell)\text{and for some}h,h'\in[r]\text{,}e=E_u(h)\text{and}e=E_v(h')\text{.}\tilde{e}:\langle e,\tilde{q}_{\lceil\ell/2\rceil}^{ij}\rangle\text{where for some}\ell\in[m]\text{, edge}e=uv\text{is the}\ell^{th}\text{element of}E_{ij}\)

For the special vertices of the _ij<sup>th</sup>_ edge gadget, we have the following preferences:

\(q_\ell^{ij}:\langle e,e',c_{1,\ell}^{ij}\rangle\text{where for some}\ell\in[m/2]\text{, edges}e\text{and}e'\text{are the}2\ell-1^{st}\text{and}2\ell^{th}\text{elements of}E_{ij}\text{, respectively.}\tilde{q}_\ell^{ij}:\langle\tilde{e},\tilde{e'},\tilde{c}_{1,\ell}^{ij}\rangle\text{where for some}\ell\in[m/2]\text{, edges}e\text{and}e'\text{are the}2\ell-1^{st}\text{and}2\ell^{th}\text{elements of}E_{ij}\text{, respectively.}c_{1,\ell}^{ij}:\langle q_\ell^{ij},d_{1,\lceil\ell/2\rceil}^{ij}\rangle\text{where}\ell\in[m/2]\tilde{c}_{1,\ell}^{ij}:\langle\tilde{q}_\ell^{ij},\tilde{d}_{1,\lceil\ell/2\rceil}^{ij}\rangle\text{where}\ell\in[m/2]c_{h,\ell}^{ij}:\langle d_{h-1,\ell}^{ij},d_{h,\lceil\ell/2\rceil}^{ij}\rangle\text{where}h\in[log_2(m/2)]\backslash\{1\},\ell\in[m/2^h]\tilde{c}_{h,\ell}^{ij}:\langle\tilde{d}_{h-1,\ell}^{ij},\tilde{d}_{h,\lceil\ell/2\rceil}^{ij}\rangle\text{where}h\in[log_2(m/2)]\backslash\{1\}\text{and}\ell\in[m/2^h]d_{h,\ell}^{ij}:\langle c_{h,2\ell-1}^{ij},c_{h,2\ell}^{ij},c_{h+1,\ell}^{ij}\rangle\text{where}h\in[log_2(m/2)-1]\text{and}\ell\in[m/2^{h+1}]\tilde{d}_{h,\ell}^{ij}:\langle\tilde{c}_{h,2\ell-1}^{ij},\tilde{c}_{h,2\ell}^{ij},\tilde{c}_{h+1,\ell}^{ij}\rangle\text{where}h\in[log_2(m/2)-1]\text{and}\ell\in[m/2^{h+1}]d_{h,1}^{ij}:\langle c_{h,1}^{ij},c_{h,2}^{ij}\rangle\text{where}h=log_2(m/2)\tilde{d}_{h,1}^{ij}:\langle\tilde{c}_{h,1}^{ij},\tilde{c}_{h,2}^{ij}\rangle\text{where}h=log_2(m/2)\)

\(B=\{b_{j,\ell}^i:i\in[k],j\in[log_2(n/2)],\ell\in[\gamma_j]\}\)<br>
\(\tilde{B}=\{\tilde{b}_{j,\ell}^i:i\in[k],j\in[log_2(n/2)],\ell\in[\gamma_j]\}\)

** 1.** Preference lists in the proof of Theorem 1; notation \(\langle\cdot,\cdot\rangle\) denotes the order of preference over neighbors.

