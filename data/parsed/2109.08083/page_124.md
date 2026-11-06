<tbc>It follows that

\(p_v^i\le\frac{4(1\pm\frac{2.1c_{H_i}}{\delta_{H_i}})max\{c_{H_i},log(n)t_i^{-\epsilon_1}\}|E_{H_i}(v,I_{t_i}\backslash I_{t_{i+1}},*,*)|}{(1\pm(\frac{3.1c_{H_i}}{\delta_{H_i}}+log^{3l_3+7}(n)t_i^{-\epsilon_1}))\delta_{H_i}^3|E_{H_i}(v,I_{t_{i+1}})|}\)<br>
\(\le\frac{4.1max\{c_{H_i},log(n)t_i^{-\epsilon_1}\}|E_{H_i}(v,I_{t_i}\backslash I_{t_{i+1}},*,*)|}{\delta_{H_i}^3|E_{H_i}(v,I_{t_{i+1}})|},\)

since by Proposition 6.31, \(\left(\frac{3.1c_{H_i}}{\delta_{H_i}}+log^{3l_3+7}(n)t_i^{-\epsilon_1}\right)\le\frac{4log^{l_4+l_3+2}(n)}{c_1t_i^{\epsilon_1}}\) .

That<tbc>

\(p_e^i\le max_{v\in e}\frac{16.1max\{c_{H_i},log(n)t_i^{-\epsilon_1}\}|E_{H_i}(v,I_{t_i}\backslash I_{t_{i+1}},*,*)|}{\delta_{H_i}^3|E_{H_i}(v,I_{t_{i+1}})|}\)

<tbc>for every \(e\in H_{i.1}[I_{t_{i+1}}]\) follows from the bound on \(p_v^i\) and Proposition 6.42. Finally, by the upper bound on \(p_e^i\) given by Corollary 6.43 we have that

\(1\le\frac{1}{1-p_e^i}=1+\frac{p_e^i}{1-p_e^i}\le 1+1.1p_e^i\)

as required. □

We introduce the following notation so that subsequent equations become less cumbersome. Let<tbc>

\(E_{out}^i:=max_{v\in V(H_i[I_{t_{i+1}}])}|E_{H_i}(v,I_{t_i}\backslash I_{t_{i+1}},*,*)|\)

<tbc>and<tbc>

\(E_{in}^i:=min_{v\in V(H_i[I_{t_{i+1}}])}|E_{H_i}(v,I_{t_{i+1}})|,\)

<tbc>and define

\(m_i:=\frac{max\{c_{H_i},log(n)t_i^{-\epsilon_1}\}E_{out}^i}{\delta_{H_i}^3E_{in}^i}.\)

We also suppose that _H_<sub>_i_+1</sub> has depth \(j'\). (Note that given _H<sub>i</sub>_ has depth _j_, that \(j'\in\{j,j+1\}.\))

In the following lemma, some properties follow immediately from the strategy or afore mentioned results, but we list all the properties here to account for all properties we care to understand for permissibility of (_H_<sub>_i_+1</sub>_,w_<sub>_i_+1</sub>).

Lemma 6.52. (_H_<sub>_i_+1</sub>_,w_<sub>_i_+1</sub>) _has the following properties:_

(_i)_ \(H_{i+1}\subseteq H_{1*}[I_{t_{i+1}}]\),<tbc>

(_a)_ _if_ \(v\in V(H_{i+1})\) _is i-reachable then_<tbc>

<tbc>\(d_{w_{i+1},H_{i+1}}(v)\ge 1-\left(\frac{c_{H_i,v}}{\delta_{H_i,v}}+2.2log^{3l_3+7}(n)t_i^{-\epsilon_1}\right),\)<tbc>

<tbc>_and in particular,_ \(c_{H_{i+1},v}\le\frac{c_{H_i,v}}{\delta_{H_i,v}}+2.2log^{3l_3+7}(n)t_i^{-\epsilon_1}.\)<tbc>

(_b)_ _If_ \(v\in V(H_{i+1})\) _is not i-reachable then_<tbc>

<tbc>\(d_{w_{i+1},H_{i+1}}(v)=d_{w_{1*},H_{1*}}(v)\ge 1-t_1^{-\epsilon_1},\)<tbc>

<tbc>_and_ \(c_{H_{i+1},v}\le t_1^{-\epsilon_1}.\)

