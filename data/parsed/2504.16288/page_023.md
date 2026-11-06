_O_(|_w_|+_m_). Further, they match our upper bounds. The section is structured in two parts. We first show lower bounds for the infix, prefix, extension and left-extension relations: Theorem 7.1 covers the matching problem and its min- and max-variants, and Theorems 7.2 and 7.4 cover lower bounds for the universal-variant with the infix and prefix relations; note that the universal-variant for extension and left-extension was shown earlier to be PSPACE-complete (Theorem 6.1). Second, we show lower bounds for the min- and max-variants of the sub- and supersequence relations; the case of the universal-variant was covered by Theorem 6.1, too.

## 7.1 Infix, Prefix, Extension and Left-Extension Relations

We first observe that SETH-based lower bounds for the \(\unknown_\text{in}^-\), \(\unknown_\text{pre}^-\), \(\unknown_\text{ext}^-\) and \(\unknown_\text{lext}\)-matching problems can be obtained by minor adaptations of the original construction from \[BI16\]. Moreover, since the min- and max-variants also solve the non-quantitative variants of the matching problem, we can conclude that these lower bounds also hold for the quantitative variants:

**Theorem 7.1.** _If the matching problem for the infix, prefix, extension and left-extension relation can be solved in time_ \(O((|w|m)^{1-\epsilon})\) _for some_ \(\epsilon>0\)_, then SETH fails. The same holds for the min- and max-variants, even if we operate on an alphabet of constant size, and even if we only require the length of the answer strings._

_Proof._ Let us first recall that if \(w\in\mathsf{L}(M)\) for a given string _w_ and \(\varepsilon\)NFA _M_ can be decided in time \(O((|w|\cdot|M|)^{1-\epsilon})\) for some \(\epsilon>0\), then SETH fails (see \[BI16\]); this result even holds on an alphabet of constant size.

Let _w_ be an input string and _M_ an \(\varepsilon\)NFA. In time _O_(|_M_|) we can construct an \(\varepsilon\)NFA \(M'\) with \(\mathsf{L}(M')=\{\#\}\cdot\mathsf{L}(M)\cdot\{\#\}\), where # is a fresh symbol (i.e., not used on any transition of _M_). Note that \(w\in\mathsf{L}(M)\) if and only if \(\#w\#\in\mathsf{L}(M')\). Moreover, the only infix, prefix, left-extension or extension of #_w_# that could possibly be accepted by \(M'\) is the string #_w_# itself. Indeed, if \(M'\) accepts a proper infix or prefix, then it would accept a string that does not start or end with #, and if \(M'\) accepts a proper left-extension (or extension), then _M_ would accept a string that contains an occurrence of #. Hence, the following statements are equivalent:

• _M_ accepts _w_.<tbc>

• \(M'\) accepts #_w_#.<tbc>

• \(M'\) accepts an infix of #_w_#.<tbc>

• \(M'\) accepts a prefix of #_w_#.<tbc>

• \(M'\) accepts a left-extension of #_w_#.<tbc>

• \(M'\) accepts an extension of #_w_#.

If we could solve the matching problem for the infix, prefix, extension and left-extension relation on the instance \(M'\) and #_w_# in time \(O((|\#w\#|\cdot|M'|)^{1-\epsilon})\) for some \(\epsilon>0\), then we would have decided whether \(w\in\mathsf{L}(M)\) in time \(O((|w|\cdot|M|)^{1-\epsilon})\).

This shows that if the matching problem for the infix, prefix, extension and left-extension relation can be solved in time \(O((|w|\cdot|M|)^{1-\epsilon})\) for some \(\epsilon>0\), then SETH fails.

Obviously, each of the min- or max-variant of the matching problem for the infix, prefix, extension and left-extension relation implicitly also solves the matching problem for the infix, prefix, extension and left-extension relation: this is true even if the min- and max-variants are only required to compute the length of their answers (and not the strings themselves). Thus, the lower bounds carry over to the quantitative variants as well.

Further, we can show that the _O_(|_w|m_) upper bound for the universal variant of the matching problem for the prefix relation is also optimal under SETH:

