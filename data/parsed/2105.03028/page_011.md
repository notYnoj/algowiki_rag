Note that by Equation (4) the LCS of the input strings

\(LCS(X,Y)\le(2\alpha+\delta)m\) (7)

cannot be too large, because the LCS contain at most \(\alpha m\) 1s from _X_ and \(\approx\alpha m\) 0s from _Y_ . Let _R<sub>X</sub>_ and _R<sub>Y</sub>_ denote the substrings of _X_ and _Y_ consisting of their rightmost \(\alpha m\) characters respectively. Similarly define _L<sub>X</sub>_ and _L<sub>Y</sub>_ as the substrings of _X_ and _Y_ consisting of the leftmost \(\alpha m\) characters. Set \(M_X=X\backslash(L_X\cup R_X)\) and \(M_Y=Y\backslash(L_Y\cup R_Y)\) to be the middle substrings of _X_ and _Y_ that remain when these left and right ends are chopped off.

We now follow the casework of [21], explaining at each step why the arguments still hold in our more general setting. These cases are based off the frequencies of 0s and 1s in the left and right ends of the inputs, and consider separately the situation where these substrings are pseudorandom (balanced) or structured (imbalanced). In the former case we can appeal to edit distance as in the proof of Lemma 10, and in the latter situation we can exploit the imbalance in the strings to use the simpler unary algorithms described in definitions 15, 16, and 17. Intuitively, we succeed in using edit distance approximation arguments (and overcome the barrier described the end of Section 2) in this particular case because even though _X_ and _Y_ may have different size, we identify right and left substrings which all have equal length and only employ edit distance approximation around these areas.

Recall that we assumed that \(\alpha<1/2-\rho\) for some constant \(\rho\). Take a parameter \(\beta<\rho/20\) to represent deviation from the balanced case. By choosing \(\delta\) sufficiently small in terms of \(\beta\) we may additionally assume that

\(1(X),0(Y)<(1/2-10\beta)m\) (8)

since in the hypothesis of the lemma we supposed that \(1(X)<(1/2-\rho)m\) and that 0(_Y_)≈1(_X_). Finally, as one last piece of notation, we write |_A_| to denote length of an arbitrary string _A_. We now begin the casework, maintaining consistency with [21].

## Case 1(a): \(1(R_Y),0(R_X)\in[(\alpha/2-4\beta)m,(\alpha/2+4\beta)m]\)

In this case both right ends of the strings are balanced. We will give a good approximation for the LCS by splitting these strings at the right ends and using the aforementioned algorithms.

Consider an optimal alignment between _X_ and _Y_ (i.e. a maximum partial matching of identical characters in _X_ and _Y_ , corresponding to the LCS of _X_ and _Y_ ). Let \(\widehat{R_Y}\) be the minimal suffix (from the right end) of the string _Y_ with the property that every character from _R<sub>X</sub>_ which is matched in the alignment is paired up with some character in \(\widehat{R_Y}\).

Without loss of generality, we may assume that \(\widehat{R_Y}\) is a substring of _R<sub>Y</sub>_. This is because if \(\widehat{R_Y}\) was not contained in _R<sub>Y</sub>_, we could define an analogous substring of \(\widehat{R_X}\) of _X_ satisfying \(\widehat{R_X}\subseteq R_X\) and then use a symmetric argument to get the desired approximation. Let \(\widehat{L_Y}=Y\backslash\widehat{R_Y}\) be the left substring of _Y_ that remains after chopping of \(\widehat{R_Y}\).

Optimality of the alignment implies that

\(LCS(X,Y)=LCS(X\backslash R_X,\widehat{L_Y})+LCS(R_X,\widehat{R_Y}).\) (9)

Define the quantities

\(f_L=min(1(X\backslash R_X),1(\widehat{L_Y}))+min(0(X\backslash R_X),0(\widehat{L_Y}))\)

