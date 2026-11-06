**Case 4:** \(0(L_X),0(R_X)\le(\alpha/2+\beta)m\) **and** \(1(L_Y),1(R_Y)>(\alpha/2+2\beta)m\)

This case is symmetric to case 3 and similar reasoning handles it.

**Case 5:** \(0(L_X),1(R_Y)>(\alpha/2+\beta)m\)

In this case, the ends of the strings have unusually large instances of either 0 or 1. This will enable us to combine two calls to Match to get the desired approximation.

We can check that the right end of _Y_ does not have many 0s

\(0(R_Y)=|R_Y|-1(R_Y)<\alpha m-(\alpha/2+\beta)m=(\alpha/2-\beta)m.\)

It follows that the remainder of the string \(Y\backslash R_Y=L_Y\cup M_Y\) has many zeros

\(0(Y\backslash R_Y)=0(Y)-0(R_Y)\approx\alpha m-0(R_Y)>(\alpha/2+\beta)m.\)

Similar reasoning shows that

\(1(L_X)=\alpha m-0(L_X)<(\alpha/2-\beta)m\)

so that the remaining portion of _X_ has many ones

\(1(X\backslash L_X)=1(X)-1(L_X)=\alpha m-1(L_X)>(\alpha/2+\beta)m.\)

It follows that

\(Match(L_X,Y\backslash R_Y,0)+Match(X\backslash L_X,R_Y,1)>(\alpha+2\beta)m\)

yields a better than 1/2 approximation since by Equation (7) the LCS is at most \(\approx 2\alpha m\).

**Case 6:** \(1(L_Y),0(R_X)>(\alpha/2+\beta)m\)

This is symmetric to case 5 and a similar argument proves the result holds in this situation.

By inspection or by referring to  1 of [21], we can verify that these cases handle all possible input strings satisfying the conditions of the lemma. Since in every case we obtain a better than 1/2 approximation for the LCS in subquadratic time, we have proven the claim.

## 5 Open Problems

Theorem 2 of our work shows how to obtain better than \(1/|\Sigma|\) approximations for the longest common subsequence of _equal-length strings_ over an alphabet \(\Sigma\). It remains an open problem to get such approximations in the setting where the input strings have different length (and by Corollary 5, to solve this problem it suffices to obtain an improvement in the setting of binary alphabets, where \(|\Sigma|=2\)).

Additionally, although our algorithm beats the longstanding trivial approximation ratio for LCS, it does so only by a modest amount. It would be interesting to get better approximation ratios, both in terms of their concrete value for small \(|\Sigma|\) and in terms of their growth as a function of the alphabet size.

