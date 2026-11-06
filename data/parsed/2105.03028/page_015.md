\(LCS(X,Y)\le(\alpha-2\beta)m+\left(0(\widehat{L_Y})+0(\widehat{R_Y})\right)\le(\alpha-2\beta)m+\alpha m=(2\alpha-2\beta)m\)

where we have used the fact that 0 occurs in \(Y\approx\alpha m\) times. **Case 1(b)(ii): some character of** _R<sub>X</sub>_ **is matched outside** _R<sub>Y</sub>_ **in the alignment.** In this case _R<sub>Y</sub>_ is a substring of \(\widehat{R_Y}\). Using Equation (4) again we find that

\(LCS(X\backslash R_X,\widehat{L_Y})\le 1(X\backslash R_X)+0(\widehat{L_Y})\) (13)

From \(0(R_X)\le(\alpha/2+2\beta)m\) we know that \(1(R_X)\ge(\alpha/2-2\beta)m\) since _R<sub>X</sub>_ has length \(\alpha m\). It follows that

\(1(X\backslash R_X)=1(X)-1(R_X)\le(\alpha/2+2\beta)m\)

since \(1(X)=\alpha m\).

Similarly, since \(1(R_Y)<(\alpha/2-4\beta)m\) and _R<sub>Y</sub>_ has length \(\alpha m\) we know that \(0(R_Y)>(\alpha/2+4\beta)m\). Since \(R_Y\subseteq\widehat{R_Y}\) it must be the case that \(0(\widehat{R_Y})>(\alpha/2+4\beta)m\) which means that

\(0(\widehat{L_Y})=0(Y)-0(\widehat{R_Y})\approx\alpha m-0(\widehat{R_Y})<(\alpha/2-4\beta)m.\)

Adding these two inequalities and substituting into Equation (13) proves that

\(LCS(X\backslash R_X,\widehat{L_Y})\le(\alpha-2\beta)m.\)

Then applying Equation (9) and using the fact that _R<sub>X</sub>_ has length \(\alpha m\) proves that

\(LCS(X,Y)=LCS(X\backslash R_X,\widehat{L_Y})+LCS(R_X,\widehat{R_Y})\le(\alpha-2\beta)m+\alpha m=(2\alpha-2\beta)m.\)

Thus in both this subcase and the previous one, the LCS is at most \((2\alpha-2\beta)m\). Hence, returning the string of \(\approx\alpha m\) zeros obtained by calling Match(_X,Y,_0) gives a better than 1/2 approximation as desired.

**Case 1(c):** \(1(R_Y)\le(\alpha/2+2\beta)m\) **and** \(0(R_X)<(\alpha/2-4\beta)m\)

This case is symmetric to case 1(b) and similar reasoning handles it.

**Case 2:** \(1(L_Y),0(L_X)\le(\alpha/2+2\beta)m\)

Combining cases 1(a), 1(b), and 1(c) resolves the situation where

\(1(R_Y),0(R_X)\le\alpha/2+2\beta.\)

Consequently, case 2 is symmetric to case 1. In particular, we can flip the strings (by replacing _X_ with the string \(X'\) which consists of the symbols of _X_ read in reverse from right to left, and replacing _Y_ with its analogous reverse string \(Y'\)) and apply the arguments from case 1 to handle this case.

