## 23:14 Improved Approximation for Longest Common Subsequence over Small Alphabets

so in fact the subsequence of _R<sub>X</sub>_ and _R<sub>Y</sub>_ returned by Lemma 10 has length at least

\((1/2+\gamma)\mathrm{LCS}(R_X,R_Y)\ge\mathrm{LCS}(R_X,R_Y)/2+\gamma(\alpha/2-4\beta)m.\)

Now if we combine these two subsequences together, we get a common subsequence of _X_ and _Y_ of length at least

\(\mathrm{LCS}(R_X,R_Y)/2+(\alpha/2-4\beta)m+\gamma(\alpha/2-4\beta)m\)

which can be written in the form

\(((\alpha+20\beta)m+\mathrm{LCS}(R_X,R_Y))/2+(\gamma\alpha/2-14\beta-4\gamma\beta)m.\)

By applying Equation (12) and the fact that \(\gamma<1\) we see that this is at least

\(\mathrm{LCS}(X,Y)/2+(\gamma\alpha/2-18\beta)m.\)

Finally, by picking \(\beta\) small enough this expression is at least

\(\mathrm{LCS}(X,Y)/2+(\gamma\alpha/3)m\ge(1/2+\gamma/6)\mathrm{LCS}(X,Y)\)

where in the last step we have used Equation (4) together with \(1(X)=\alpha m\) and \(0(Y)\approx\alpha m\). This proves that we can attain a better than 1/2 approximation for the LCS as claimed.

## Case 1(b): \(1(R_Y)<(\alpha/2-4\beta)m\) and \(0(R_X)\le(\alpha/2+2\beta)m\)

In this case the right ends of _X_ and _Y_ each do not contain too much their respective strings’ most common characters. We show that this implies the LCS of both strings must be so small that simply returning a unary string yields a better than 1/2 approximation.

As in case 1(a), consider an optimal alignment between _X_ and _Y_ . Now define the substring \(\widehat{R_Y}\) to be the minimal suffix of _Y_ which contains all characters of _Y_ that _R<sub>X</sub>_ is aligned to. Let \(\widehat{L_Y}=Y\backslash\widehat{R_Y}\) be what remains of _Y_ after _R<sub>Y</sub>_ is removed. Since the alignment is optimal, Equation (9) holds.

We now subdivide into further case based off how the right ends of strings are aligned.

**Case 1(b)(i): every character of** _R<sub>X</sub>_ **is matched to some character of** _R<sub>Y</sub>_ **in the alignment.**

In this case \(\widehat{R_Y}\) is a substring of _R<sub>Y</sub>_. From Equation (4) and the case assumptions we get that

\(\mathrm{LCS}(X\backslash R_X,\widehat{L_Y})\le 1(X\backslash R_X)+0(\widehat{L_Y})\le(\alpha/2+2\beta)m+0(\widehat{L_Y})\)

and

\(\mathrm{LCS}(R_X,\widehat{R_Y})\le 1(\widehat{R_Y})+0(\widehat{R_Y})\le(\alpha/2-4\beta)m+0(\widehat{R_Y}).\)

Note that in this second inequality we are using the inequality \(1(\widehat{R_Y})\le 1(R_Y)\) which follows from the earlier observation that \(\widehat{R_Y}\subseteq R_Y\). By adding these inequalities together and substituting the result into Equation (9) we deduce that

