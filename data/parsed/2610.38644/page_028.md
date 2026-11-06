## B.2 Completion of the square

Define the midpoint and separation coordinates

\(m=\frac{x+y}{2},d=x-y.\) (68)

We first rewrite the quadratic form in the exponent:

\((x-c)^2+(y-c)^2=x^2+y^2-2c(x+y)+2c^2.\) (69)

Using

\(x^2+y^2=\frac{(x-y)^2}{2}+\frac{(x+y)^2}{2},\) (70)

and

\(2(c-m)^2=2c^2-2c(x+y)+\frac{(x+y)^2}{2},\) (71)

we obtain

\((x-c)^2+(y-c)^2=2(c-m)^2+\frac{(x-y)^2}{2}.\) (72)

Substituting eq. 72 into eq. 67 gives

\(k_{[a,b]}(x,y)=\frac{1}{b-a}\int_a^b\mathrm{exp}\left(-\frac{(x-y)^2}{4\sigma^2}\right)\mathrm{exp}\left(-\frac{(c-m)^2}{\sigma^2}\right)dc\)<br>
\(=\frac{\mathrm{exp}\left(-\frac{d^2}{4\sigma^2}\right)}{b-a}\int_a^b\mathrm{exp}\left(-\frac{(c-m)^2}{\sigma^2}\right)dc.\) (73)

Thus, the kernel separates into a Gaussian factor depending on the relative distance _d=x-y_ and a finite-support correction depending on the midpoint _m_=(_x+y)/_2.

## B.3 Evaluation using the error function

Introduce the change of variables

\(z=\frac{c-m}{\sigma},dc=\sigma dz.\) (74)

The limits become

\(z_a=\frac{a-m}{\sigma},z_b=\frac{b-m}{\sigma}.\) (75)

Therefore,

\(\int_a^b\mathrm{exp}\left(-\frac{(c-m)^2}{\sigma^2}\right)dc=\sigma\int_{z_a}^{z_b}e^{-z^2}dz.\) (76)

Using the error function

\(\mathrm{erf}(z)=\frac{2}{\sqrt{\pi}}\int_0^ze^{-t^2}dt,\) (77)

we have

\(\int_{z_a}^{z_b}e^{-z^2}dz=\frac{\sqrt{\pi}}{2}\left[\mathrm{erf}(z_b)-\mathrm{erf}(z_a)\right].\) (78)

Hence,

\(\int_a^b\mathrm{exp}\left(-\frac{(c-m)^2}{\sigma^2}\right)dc=\frac{\sqrt{\pi}\sigma}{2}\left[\mathrm{erf}\left(\frac{b-m}{\sigma}\right)-\mathrm{erf}\left(\frac{a-m}{\sigma}\right)\right].\) (79)

Substitution into eq. 73 yields the closed form

\(\boxed{k_{[a,b]}(x,y)=\frac{\sqrt{\pi}\sigma}{2(b-a)}\mathrm{exp}\left(-\frac{(x-y)^2}{4\sigma^2}\right)}\)<br>
\(\times\left[\mathrm{erf}\left(\frac{b-\frac{x+y}{2}}{\sigma}\right)-\mathrm{erf}\left(\frac{a-\frac{x+y}{2}}{\sigma}\right)\right].\) (80)

Equation eq. 80 is the bounded continuum-feature Gaussian kernel used in this work.

