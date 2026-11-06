## 23:12 Improved Approximation for Longest Common Subsequence over Small Alphabets

and

\(f_R=min(1(R_X),1(\widehat{R_Y}))+min(0(R_X),0(\widehat{R_Y}))\)

which represent frequency-based upper bounds for the LCS terms from the right hand side of Equation (9). They are useful because Equation (4) together with Equation (9) implies that

\(LCS(X,Y)\le f_L+f_R.\) (10)

We also introduce the quantity

\(Z=max\left(min(1(X\backslash R_X),1(\widehat{L_Y})),min(0(X\backslash R_X),0(\widehat{L_Y}))\right)\)

which is the larger of the two addends defining _f<sub>L</sub>_, and equal to the length of the string returned by

BestMatch\((X\backslash R_X,\widehat{L_Y})\).

We further subdivide into cases based off the size of _Z_.

**Case 1(a)(i):** \(Z>(\alpha/2+10\beta)m\)

When _Z_ is large we can combine two unary subsequences to get a good enough LCS approximation. We first show that _Z_ is bigger than _f<sub>L</sub>/_2 by a constant fraction of _m_.

By definition we have

\(f_L-Z=min\left(min(1(X\backslash R_X),1(\widehat{L_Y})),min(0(X\backslash R_X),0(\widehat{L_Y}))\right)\le 1(X\backslash R_X).\)

Since _X_ has \(\alpha m\) ones and _R<sub>X</sub>_ has length \(\alpha m\) we get that

\(1(X\backslash R_X)=\alpha m-1(R_X)=\alpha m-(\alpha m-0(R_X))=0(R_X).\)

Then using the case assumptions we have

\(0(R_X)\le(\alpha/2+4\beta)m<Z-6\beta m.\)

Chaining these inequalities together and rearranging we deduce that

\(Z>f_L/2+3\beta m.\)

Now if we make a single call to the Greedy routine we obtain a string of length

\(Greedy(X\backslash R_X,R_X,Y)\ge BestMatch(X\backslash R_X,\widehat{L_Y})+BestMatch(R_X,\widehat{R_Y}).\) (11)

From our earlier discussion we have

