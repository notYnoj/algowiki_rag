_Proof._ Let _y=kx_. It is enough to argue that \(\mathrm{sin}(y)\ge y-\frac{y^3}{\pi^2}\) in the range \(y\in[0,\pi]\).

Let \(f(y)=\mathrm{sin}(y)-y+\frac{y^3}{\pi^2}\). Notice that \(f(0)=f(\pi)=0\) and \(f'(\pi)>0\). We will argue that there is a unique point \(y^*\in(0,\pi)\) such that \(f'(y^*)=0\), which will ensure that \(f(y)\le 0\) for all \(y\in[0,\pi]\).

We can calculate that

\(f'(y)=\mathrm{cos}(y)-1+\frac{3y^2}{\pi^2}\)<br>
\(=\frac{3y^2}{\pi^2}-2\mathrm{sin}^2\left(\frac{y}{2}\right).\)

So \(f'(y)=0\) if and only if \(\mathrm{sin}(y/2)=\pm(\sqrt{6}/\pi)\cdot(y/2)\), which is satisfied by one unique point \(y^*\in(0,\pi)\).

**Claim 63.** _For positive integers k, and_ \(x\in(0,\pi/2k]\),

\(\mathrm{cot}(kx)\le\frac{1}{kx}.\)

_Proof._ Let _y=kx_. We will prove that \(\mathrm{cot}(y)\le\frac{1}{y}\) for all \(y\in(0,\pi/2]\). It is enough to prove that \(y\mathrm{cos}(y)\le\mathrm{sin}(y)\) for all \(y\in[0,\pi/2]\).

The latter inequality follows because both sides are zero when _y_=0, and the derivative of the left hand side is bounded above by the derivative of the right hand side when \(y\in[0,\pi/2]\):

\(\mathrm{cos}(y)-y\mathrm{sin}(y)\le\mathrm{cos}(y).\)

Now we finish the proof of Claim 61.

_Proof._ Notice that<tbc>

\(\frac{\mathrm{sin}((b+k)x)}{\mathrm{sin}(kx)}=\frac{\mathrm{sin}(kx)\mathrm{cos}(bx)+\mathrm{sin}(bx)\mathrm{cos}(kx)}{\mathrm{sin}(kx)}\)

y
X
T

y
X
T/2

(a) Claim 62

(b) Claim 63

Figure 13: Plots of Trigonometric Bounds.

Trigonometric functions are dotted, upper bounds are dashed.

