<tbc>and thus the energy \(\mathcal{E}_3(\alpha,\eta)\) is given by:

\(\mathcal{E}_3(\alpha,\eta)=\left(\frac{1}{6}+\alpha_1\right)\eta_1^2+\left(\frac{1}{6}-\alpha_1\right)\eta_2^2+\left(\alpha_1+\alpha_2\right)\left(1-\varepsilon-\eta_2\right)^2+\left(\frac{1}{3}-\alpha_1-\alpha_2\right)\left(\eta_3+\varepsilon\right)^2+\frac{1}{3}(\eta_3-\varepsilon)^2.\) (70)

Taking dual variables \(\lambda_1,\lambda_2\in\mathbb{R}\), the Lagrangian of the problem \(\mathcal{E}_3^+\) defined in Eq. (69) is given by:

\(\mathcal{L}^+(\alpha,\eta,\lambda_1,\lambda_2)=\mathcal{E}_3(\alpha,\eta)+\lambda_1(-\alpha_1-\alpha_2)+\lambda_2(\eta_1-\eta_2).\) (71)

To find solutions of the problem \(\mathcal{E}_3^+\), we study the necessary KKT system (see \[BV04, Section 5.5.3\], or \[NW06, Theorem 12.1\]). We begin with the stationarity condition, expressed at the point \((\alpha,\eta)\in[-\frac{1}{6},\frac{1}{6}]^2\times(-\frac{1}{2},\frac{1}{2})^3\):

\(0=\frac{\partial\mathcal{L}^+}{\partial\alpha_1}=\eta_1^2-\eta_2^2+\left(1-\varepsilon-\eta_2\right)^2-\left(\eta_3+\varepsilon\right)^2-\lambda_1;\)<br>
\(0=\frac{\partial\mathcal{L}^+}{\partial\alpha_2}=\left(1-\varepsilon-\eta_2\right)^2-\left(\eta_3+\varepsilon\right)^2-\lambda_1;\)<br>
\(0=\frac{\partial\mathcal{L}^+}{\partial\eta_1}=2\left(\frac{1}{6}+\alpha_1\right)\eta_1+\lambda_2;\)<br>
\(0=\frac{\partial\mathcal{L}^+}{\partial\eta_2}=2\left(\frac{1}{6}-\alpha_1\right)\eta_2-2(\alpha_1+\alpha_2)(1-\varepsilon-\eta_2)-\lambda_2;\)<br>
\(0=\frac{\partial\mathcal{L}^+}{\partial\eta_3}=2\left(\frac{1}{3}-\alpha_1-\alpha_2\right)\left(\eta_3+\varepsilon\right)+\frac{2}{3}(\eta_3-\varepsilon).\)

The remaining KKT conditions are the primal / dual feasibility conditions, which are given by:<tbc>

\(\alpha_1+\alpha_2\ge 0,\eta_1\le\eta_2,\lambda_1\ge 0,\lambda_2\ge 0,\)

<tbc>and the complementary slackness conditions:

\(\lambda_1(-\alpha_1-\alpha_2)=0,\lambda_2(\eta_1-\eta_2)=0.\)

It is easy to see that the point \((\alpha,\eta,\lambda_1,\lambda_2)=(0_{\mathbb{R}^2},0_{\mathbb{R}^3},1-2\varepsilon,0)\) is a solution of the KKT system (note that \(\varepsilon<\frac{1}{2}\)).

1
2/3
-(a1 + a2)
1/3
a1
1/6
a2
1
X1
y1
X2
y2 X3
y3
n1
n2
n3
E

Figure 16: Setup for the local minimum of \(\mathrm{W}_2^2(\mu_{\alpha,\eta},\nu)\). The support of \(\mu\) is represented with blue squares, and its weights with vertical blue lines. For the target \(\nu\), its support is red squares and its weights red lines. We consider a specific region where the points \(x_1=\eta_1\) and \(x_2=\eta_2\) stay within \((-\frac{1}{2},\frac{1}{2})\) and the weights \(a_1=\frac{1}{6}+\alpha_1\) and \(a_2=\frac{1}{6}+\alpha_2\) stay within \([0,\frac{1}{3}]\), as represented by the orange rectangle. Likewise, the point \(x_3=1+\eta_3\) must stay within \((\frac{1}{2},\frac{3}{2})\) and its weight \(a_3=\frac{2}{3}-(\alpha_1+\alpha_2)\) must stay in \([\frac{1}{3},1]\), as shown with the purple rectangle.

