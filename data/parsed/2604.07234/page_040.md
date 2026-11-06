<tbc>A direct computation gives<tbc>

\(x\partial_xlogZ(x,y)=\frac{1-x-xy}{D(x,y)},y\partial_ylogZ(x,y)=\frac{1-2x-xy+x^2(1-y)}{D(x,y)}.\)

<tbc>Therefore the moment constraints are equivalent to<tbc>

(4.37) \(\frac{1-x-xy}{D(x,y)}=\frac{1}{\alpha\rho},\)

<tbc>and

(4.38) \(\frac{1-2x-xy+x^2(1-y)}{D(x,y)}=\frac{1}{\rho}.\)

Solving (4.37)-(4.38) yields

(4.39) \(x(\rho)=\frac{(1-\alpha)(2-2\alpha+\alpha\rho)}{2-\alpha\rho},\)

and

(4.40) \(y(\rho)=\frac{\alpha^2(2-\rho)(1-\rho)}{(1-\alpha)(2-2\alpha+\alpha\rho)}.\)

Substituting (4.39)-(4.40) into the closed form for _Z_ gives<tbc>

(4.41) \(Z(x(\rho),y(\rho))=\frac{\alpha(1-\rho)\sqrt{2-\rho}}{\sqrt{\rho}\sqrt{(2-\alpha\rho)(2-2\alpha+\alpha\rho)}}.\)

<tbc>In particular,<tbc>

\(Z(x(\rho),y(\rho))\longrightarrow\infty\text{as}\rho\downarrow 0,\)

<tbc>and<tbc>

\(Z(x(\rho),y(\rho))\longrightarrow 0\text{as}\rho\uparrow 1.\)

<tbc>Moreover, \(Z(x(\rho),y(\rho))=1\) is equivalent, after squaring (4.41), to

(4.42) \(2\alpha^2\rho^2+(4\alpha-5\alpha^2-4)\rho+2\alpha^2=0.\)

The polynomial on the left-hand side of (4.42) has value \(2\alpha^2>0\) at \(\rho=0\) and value<tbc>

\(2\alpha^2+(4\alpha-5\alpha^2-4)+2\alpha^2=4\alpha-\alpha^2-4=-(2-\alpha)^2<0\)

<tbc>at \(\rho=1\). Hence it has at least one root in (0,1). Since its constant term equals its leading coefficient, the product of its roots is 1, so it can have at most one root in (0,1). Therefore there is a unique \(\rho^*\in(0,1)\) such that<tbc>

\(Z(x(\rho^*),y(\rho^*))=1.\)

<tbc>Because \(Z(x(\rho),y(\rho))\) is continuous, the uniqueness of \(\rho^*\) and the above boundary limits imply<tbc>

\(Z(x(\rho),y(\rho))>1\text{for}0<\rho<\rho^*,Z(x(\rho),y(\rho))<1\text{for}\rho^*<\rho<1.\)

<tbc>By (4.36), it follows that

\(g'(\rho)>0\text{for}0<\rho<\rho^*,g'(\rho)<0\text{for}\rho^*<\rho<1.\)

Thus _g_ is strictly increasing on \((0,\rho^*)\) and strictly decreasing on \((\rho^*,1)\), so _g_ attains its maximum uniquely at \(\rho^*\in(0,1)\).

Finally, setting \((x^*,y^*):=(x(\rho^*),y(\rho^*))\), we have proved (4.33). Plugging this into (4.35) gives

\(\mathsf{R}(\alpha)=g(\rho^*)=-logx^*-\alpha logy^*,\)

which is (4.34). □

