BestMatch\((X\backslash R_X,\widehat{L_Y})\ge Z>f_L/2+3\beta m\).

Moreover

BestMatch\((R_X,\widehat{R_Y})=max(min(1(R_X),1(\widehat{R_Y})),min(0(R_X),0(\widehat{R_Y})))\ge f_R/2\)

since we are taking the maximum over two addends that sum to _f<sub>R</sub>_.

Finally, if we substitute the above inequalities into Equation (11) and apply Equation (10) we get that

\(Greedy(X\backslash R_X,R_X,Y)\ge(f_L+f_R)/2+3\beta m\ge LCS(X,Y)/2+3\beta m\ge(1/2+3\beta)LCS(X,Y).\)

Thus running Greedy gives us a better than 1/2 approximation in this case.

**Case 1(a)(ii) :** \(Z\le(\alpha/2+10\beta)m\)

Intuitively, in this case _Z_ is too small for us to ensure a good approximation using frequency guarantees alone. However, because _Z_ is so small, the LCS also cannot be too large. Because of this, we will be able to get a good approximation by combining a common subsequence of the (balanced) right ends of the strings with a common subsequence of the strings with the right ends removed.

More concretely, we leverage the ApproxED algorithm from Definition 7. From our previous observation we have \(f_L\le 2Z\le(\alpha+20\beta)m\). So via Equation (9) we can bound the LCS by

\(LCS(X,Y)\le f_L+LCS(R_X,\widehat{R_Y})\le(\alpha+20\beta)m+LCS(R_X,R_Y)\) (12)

where in the last step we also used the fact that \(\widehat{R_Y}\subseteq R_Y\).

We will get an approximation by returning a unary subsequence from the left parts of the strings, and using edit distance approximation on the right ends. First, we can make a call to BestMatch and get a common subsequence of length at least

BestMatch\((X\backslash R_X,Y\backslash R_Y)\ge Match(X\backslash R_X,Y\backslash R_Y,0)\ge(\alpha/2-4\beta)m\).

This last inequality above follows from combining the case 1 assumptions about the frequencies of characters in 0(_R<sub>X</sub>_) and 1(_R<sub>Y</sub>_), together with the facts that \(0(Y)\approx 1(X)=\alpha m\) and \(|R_X|=|R_Y|=\alpha m\).

Now, since _R<sub>X</sub>_ and _R<sub>Y</sub>_ are \((4\beta/\alpha)\)-balanced we can apply Lemma 10 with \(n=\alpha m\) as long as we take \(\beta\) sufficiently small in terms of \(\alpha\). Note that for fixed alphabet size and \(\rho\), the parameter \(\beta\) remains \(\Omega(1)\). This ensures that in subquadratic time we can compute a common subsequence of _R<sub>X</sub>_ and _R<sub>Y</sub>_ with length at least

\((1/2+\gamma)LCS(R_X,R_Y)\)

where \(\gamma<1\) is the constant from Lemma 10, which is larger for smaller values of \(\beta\). By the frequency assumptions on _R<sub>X</sub>_ and _R<sub>Y</sub>_, we know that

\(LCS(R_X,R_Y)\ge(\alpha/2-4\beta)m\)

