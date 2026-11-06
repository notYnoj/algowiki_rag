Hence, \(\alpha_\pi^7(\frac{7}{4})^6\le(2^{\alpha_\pi-1})^7\cdot 32=2^{7\alpha_\pi-7+5}\le d\). Combined with Lemmas 6 and 7, this implies that

\(|B'_\mathrm{li}|\le|B_\mathrm{li}\cup C'_\mathrm{li}|\le 60\alpha_\pixd\mathrm{log}(d)+60\alpha_\pi d\mathrm{log}(\alpha_\pi d)\)<br>
\(\le 60(x+1)\alpha_\pi d\mathrm{log}(\alpha_\pi d)\)<br>
\(\le 30(2x+2)\frac{7}{4}\alpha_\pi\frac{4d}{7}\mathrm{log}(\frac{7\alpha_\pi}{4}\frac{4d}{7})\)<br>
\(\le 30(2x+2)\frac{7}{4}\alpha_\pi\frac{4d}{7}(\mathrm{log}(\frac{4d}{7})^{8/7})\)<br>
\(\le 30x'\frac{7\cdot 8}{4\cdot 7}d'\mathrm{log}(d')\)<br>
\(\le 60x'd'\mathrm{log}(d').\)

To show that the third invariant is also maintained in this case, note that \(\frac{4d}{7}\ge d^{3/4}\) for all _d\>_10. Hence, we have

\(x'\sqrt{d'}\mathrm{log}(d')\ge(2x+2)\sqrt{\frac{4d}{7}}\mathrm{log}(\frac{4d}{7})\)<br>
\(\ge 2x\sqrt{\frac{4}{7}}\sqrt{d}\mathrm{log}(d^{3/4})\)<br>
\(\ge x\sqrt{d}\mathrm{log}(d)(2\sqrt{\frac{4}{7}}\frac{3}{4})\)<br>
\(\ge x\sqrt{d}\mathrm{log}(d).\)

## Reduce Portals (red-portals).

We now consider a recursive call of `red-portals` with input \((d,G,x,y,X_\mathrm{he},Y_\mathrm{he},X_\mathrm{li},Y_\mathrm{li},X_\mathrm{di},Y_\mathrm{di},S_\pi)\) which satisfies our invariant and show that the input to each call of `solve-\(\pi\)-r` and `red-portals` also satisfies the respective invariants. Observe that `solve-\(\pi\)-r` is only called in Line 2 and with input \((d,G,y+1,X_\mathrm{he}\cup Y_\mathrm{he},X_\mathrm{li}\cup Y_\mathrm{li},X_\mathrm{di}\cup Y_\mathrm{di},S_\pi)\), which is by assumption a valid instance of \(\pi\)-Request since \(x\ge 1\) and \(|X_\mathrm{he}\cup X_\mathrm{li}|\le 20\sqrt{d}\). Moreover, the result is never used to combine solutions using Requirement R4, so the third invariant is not applicable here.

We now consider the input \((d',G',x',y',X'_\mathrm{he},Y'_\mathrm{he},X'_\mathrm{li},Y'_\mathrm{li},X'_\mathrm{di},Y'_\mathrm{di},S'_\pi)\) given to `red-portals` in Line 2. We need to show that

1. \(G'\) is a \(\alpha_\pi d'\)-outerplanar graph,<tbc>

2. \(1\le x'\le 200\mathrm{log}^7(d')-22\mathrm{log}(d')\),<tbc>

3. \(y'<22\mathrm{log}(d')\),<tbc>

4. \(|X'_\mathrm{he}|\le 40x'\alpha_\pi\sqrt{d'}\),<tbc>

5. \(|Y'_\mathrm{he}|\le 40(2y')\alpha_\pi\sqrt{d'}\),<tbc>

6. \(|X'_\mathrm{li}|\le 60x'\alpha_\pi d'\mathrm{log}(d')\),<tbc>

7. \(|Y'_\mathrm{li}|\le 60(2y')\alpha_\pi d'\mathrm{log}(d')\),<tbc>

8. \(d'\ge 2^{7\alpha_\pi}\),<tbc>

9. \(|X'_\mathrm{he}\cup X_\mathrm{li}|\le(^{3/4})^{y^\prime}\cdot 50d'^6\), and<tbc>

10. \((x+2y)\sqrt{d}\mathrm{log}(d)\le(x'+2y')\sqrt{d'}\mathrm{log}(d')\).

Note that points 1,2,4,6,8, and 10 hold as \(d'=d,x'=x,y'=y+1,X'_\mathrm{he}\subseteq X_\mathrm{he},X'_\mathrm{li}\subseteq X_\mathrm{li}\), and \(G'\) is a subgraph of _G_. For point 9, note that \(|X'_\mathrm{he}\cup X'_\mathrm{li}|\le 3/4|X_\mathrm{he}\cup X_\mathrm{li}|\) as \(C'\) is <sup>3/4</sup>-balanced with respect to the weight function that assign weight \(1/|X_\mathrm{he}\cup X_\mathrm{li}|\) to each vertex in \(X_\mathrm{he}\cup X_\mathrm{li}\) and zero to all other vertices. Hence,<tbc>

\(|X'_\mathrm{he}\cup X'_\mathrm{li}|\le(^{3/4})|X_\mathrm{he}\cup X_\mathrm{li}|\le^{3/4}\cdot(^{3/4})^y\cdot 50d^6=(^{3/4})^{y+1}\cdot 50d^6=(^{3/4})^{y^\prime}\cdot 50d'^6.\)

