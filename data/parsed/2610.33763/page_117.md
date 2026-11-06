In this view, we begin by reporting the symbol associated with the matrix sequence \(\overline{G_{\alpha,n}}\) defined in equation (8.8).

**Proposition 8.2** _Let_ \(\alpha\in(1,2)\)_. The symbol associated with_ \(\overline{G_{\alpha,N}}\) _belongs to the Wiener class, and_

\(f_\alpha(\xi_1)=\sum_{k=-1}^\infty g_{k+1}^{(\alpha)}e^{ik\xi_1}=e^{-i\xi_1}\left(1+e^{i(\xi_1+\pi)}\right)^\alpha,\xi_1\in[-\pi,\pi].\)

**Proof:** Let us observe that \(\overline{G_{\alpha,N}}=[g_{i-j+1}^{(\alpha)}]_{i,j=1}^N\) with \(g_k^{(\alpha)}=0\) for _k\<_0, and let us define the function \(\sum_{k=-1}^\infty g_{k+1}^{(\alpha)}e^{ik\xi_1}\). When \(\alpha\in(1,2)\), it is easy to see that \(f_\alpha(\xi_1)\) lies in the Wiener class. In detail, from Proposition 8.1 we know that<tbc>

\(g_0^{(\alpha)}=1>0,g_1^{(\alpha)}=-\alpha<0,g_k^{(\alpha)}>0\forall k\ge 2,g_k^{(\alpha)}=0\forall k<0.\)

<tbc>Then

\(\sum_{k=-1}^\infty\left|g_{k+1}^{(\alpha)}\right|=\left|g_0^{(\alpha)}\right|+\left|g_1^{(\alpha)}\right|+\sum_{k=1}^\infty\left|g_{k+1}^{(\alpha)}\right|\)<br>
\(=g_0^{(\alpha)}+\left(-g_1^{(\alpha)}\right)+\sum_{k=1}^\infty g_{k+1}^{(\alpha)}\text{(since}g_0^{(\alpha)}>0,g_1^{(\alpha)}<0,g_{k+1}^{(\alpha)}>0\text{for}k\ge 1\right)\)<br>
\(=g_0^{(\alpha)}-g_1^{(\alpha)}+\sum_{k=1}^\infty g_{k+1}^{(\alpha)}.\) (8.25)

From Proposition (8.1), we have \(\sum_{k=0}^\infty g_k^{(\alpha)}=0\). Therefore,

\(\sum_{k=1}^\infty g_{k+1}^{(\alpha)}=\sum_{k=2}^\infty g_k^{(\alpha)}=\sum_{k=0}^\infty g_k^{(\alpha)}-g_0^{(\alpha)}-g_1^{(\alpha)}=-g_0^{(\alpha)}-g_1^{(\alpha)}=-1+\alpha\) (8.26)

Now, plugging (8.26) in (8.25), we find

\(\sum_{k=-1}^\infty\left|g_{k+1}^{(\alpha)}\right|=g_0^{(\alpha)}-g_1^{(\alpha)}+\left(-1+\alpha\right)=1+\alpha+\left(-1+\alpha\right)=2\alpha.\) (8.27)

Since this sum is finite, \(f_\alpha(\xi_1)\) belongs to the Wiener class for \(\alpha\in(1,2)\).<br>
To obtain an explicit formula for the symbol \(f_\alpha(\xi_1)\), let us recall the definition of \(g_k^{(\alpha)}\) given in (8.5) and rewrite \(f_\alpha(\xi_1)\) in the following manner<tbc>

\(f_\alpha(\xi_1)=\sum_{k=-1}^\infty g_{k+1}^{(\alpha)}e^{ik\xi_1}=\sum_{k=0}^\infty g_k^{(\alpha)}e^{i(k-1)\xi_1}=\sum_{k=0}^\infty\left(-1\right)^k\genfrac(){pt}{2}{\alpha}{k}e^{i(k-1)\xi_1}.\)

<tbc>We now write (-1)_<sup>k</sup>_ as \(e^{ik\pi}\) so that<tbc>

\(f_\alpha(\xi_1)=\sum_{k=0}^\infty\genfrac(){pt}{2}{\alpha}{k}e^{i(k-1)\xi_1}e^{ik\pi}=e^{-i\xi_1}\sum_{k=0}^\infty\genfrac(){pt}{2}{\alpha}{k}e^{ik(\xi_1+\pi)}.\)

