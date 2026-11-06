that _G_ has at most \(d\le 2^{7\alpha_\pi}\). It is called with the same input \((d,G,x,B_\mathrm{he},B_\mathrm{li},B_\mathrm{di},S_\pi)\), which is a valid instance of \(\pi\)-Request by assumption. Hence, all requirements are met in this case.

We next analyze the case where `solve-\(\pi\)-r` calls `red-portals`. Note that the only recursive call to `red-portals` is in Line 1 with input \((d,G,x,0,B_\mathrm{he},\emptyset,B_\mathrm{li},\emptyset,B_\mathrm{di},\emptyset,S_\pi)\). In this case, all invariants of `red-portals` except \(d\ge 2^{7\alpha_\pi}\) and \(|B_\mathrm{he}\cup B_\mathrm{li}|\le(3/4)^0\cdot 50d^6\) hold by the assumption that \((d,G,(B_\mathrm{he},B_\mathrm{li},B_\mathrm{di}),x,S_\pi)\) is a valid instance of \(\pi\)-Request. Note that since we passed Line 1, we may assume that \(d\ge 2^{7\alpha_\pi}\). Since (_B,x_) is almost measured for _k_ and \(\alpha_\pi\), we have that \(x\le 200\mathrm{log}^7(d)\) and therefore \(|B_\mathrm{he}|\le 200\mathrm{log}^7(d)\cdot 40\alpha_\pi\sqrt{d}=8000\alpha_\pi\sqrt{d}\mathrm{log}^7(d)\) and \(|B_\mathrm{li}|\le 200\mathrm{log}^7(d)\cdot 60\alpha_\pi d\mathrm{log}(d)=12000\alpha_\pi d\mathrm{log}^8d\). These are at most \(20000\alpha_\pi d\mathrm{log}^7d\) vertices combined, which is upper bounded by 31_d_<sup>6</sup> by Lemma 7 as \(d>2^{7\alpha_\pi}\ge 100\). The third invariant also clearly holds here as _z_<sub>1</sub>=_x\<x_+1=_x_<sub>2</sub> and _d_<sub>1</sub>=_d=d_<sub>2</sub>.

Let next \(I'=(d',G',x',B'_\mathrm{he},B'_\mathrm{li},B'_\mathrm{di},S'_\pi)\) be the input to a recursive call of `solve-\(\pi\)-r` in Line 1 or 12. Recall that \(I'\) is a valid instance of \(\pi\)-Request if

1. \(G'\) is a \(\alpha_\pi d'\)-outerplanar graph,<tbc>

3. \(|B'_\mathrm{he}|\le 40x\alpha_\pi\sqrt{d}\), and<tbc>

2. \(1\le x'\le\mathrm{max}(200\mathrm{log}^7(d')-44\mathrm{log}(d),1)\),<tbc>

4. \(|B'_\mathrm{li}|\le 60x\alpha_\pi d\mathrm{log}(d)\).

Since \(d'=d\) and \(G'\) is a subgraph of _G_, the first point trivially holds. Note that since we reached past Line 1, it holds that \(1\le x'=x+1\le 40\mathrm{log}^7(d)+1\le 200\mathrm{log}^7(d)-22\mathrm{log}(d)\). As we only potentially removed vertices from _B_<sub>he</sub>, the third point also holds trivially. Finally, since we only added \(2\alpha_\pi d+3\) vertices to _B_<sub>li</sub>, we have that \(|B'_\mathrm{li}|=|B_\mathrm{li}\cup C_\mathrm{he}|\le|B_\mathrm{li}|+|C_\mathrm{li}|\le 40x\alpha_\pi d\mathrm{log}(d)+2\alpha_\pi d+3\le 40(x+1)\alpha_\pi d\mathrm{log}(d)\), which shows the fourth condition. The third invariant again trivially holds as _z_<sub>1</sub>_\<z_<sub>2</sub> and _d_<sub>1</sub>=_d_<sub>2</sub>.

Let now \(I'=(d',G',x',B'_\mathrm{he},B'_\mathrm{li},B'_\mathrm{di},S'_\pi)\) be the input to a recursive call in Line 1 or 24. Note that the application of Lemma 1 in Line 1 ensures that \(C'_\mathrm{in}-A_\mathrm{in}\) and \(C'_\mathrm{ex}-A_\mathrm{ex}\) are \(d'\alpha_\pi\)-outerplanar graphs. Moreover, since we passed Line 1, we have \(x\le 40\mathrm{log}^7(d)\) implying

\(1\le x'=2x+2\le 2\cdot 40\mathrm{log}^7(d)+2\)<br>
\(\le 80\mathrm{log}^7((7/4)d')+2\)<br>
\(=80(\mathrm{log}(d')+\mathrm{log}(7/4))^7+2\)<br>
\(<80(\mathrm{log}(d')+1)^7+2\)<br>
\(=80(\mathrm{log}^7(d')+7\mathrm{log}^6(d')+21\mathrm{log}^5(d')+35\mathrm{log}^4(d')+35\mathrm{log}^3(d')+21\mathrm{log}^2(d')+7\mathrm{log}(d')+1)+2\)<br>
\(\le 80\mathrm{log}^7(d')(1+7/7+21/7^2+35/7^3+35/7^4+21/7^5+7/7^6+3/7^7)\)<br>
\(\le 80\cdot 2.45\mathrm{log}^7(d')\le 200\mathrm{log}^7(d')-44\mathrm{log}(d'),\)

where the third and second from last inequality hold as \(\mathrm{log}(d)\ge 7\) as \(d\ge 2^{7\alpha_\pi}\ge 2^7\). Moreover, Lemmas 6 and 7 yield

\(|B'_\mathrm{he}|\le|B_\mathrm{he}\cup C'_\mathrm{he}|\le 40\alpha_\pi x\sqrt{d}+40\sqrt{\alpha_\pi d}\le 40(x+1)\alpha_\pi\sqrt{d}\)<br>
\(\le 40(2x+2)\alpha_\pi\sqrt{\frac{d}{4}}\le 40x'\alpha_\pi\sqrt{\frac{4d}{7}}\)<br>
\(\le 40x'\alpha_\pi\sqrt{d'}\)

We will next show that \(\frac{7\alpha_\pi}{4}\le(\frac{4d}{7})^\frac{1}{7}\) or equivalently \(d\ge\alpha_\pi^7(\frac{7}{4})^6\). Note that when \(\alpha_\pi=1\), then \(d\ge 2^7\ge 32\ge\frac{7^6}{4}=\frac{7^6}{4}\alpha_\pi^7\). For all positive integers \(\alpha_\pi\ge 2\), it holds that \(\alpha_\pi\le 2^{\alpha_\pi-1}\).

