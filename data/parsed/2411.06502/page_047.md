Proof. We rewrite the indices for the output of the \((s,s',q,q')\)-DISED instance as (see Figure 12)

\(\{(x,x',y,y'):(x,x')\in B_1^+(s,s',q,q'),(y,y')\in B_r^+(s,s',q,q')\}=\)<br> \(\{(x,x',y,y'):(x,x')\in B_1^+(s,s',r,q'),(y,y')\in B_r^+(s,s',r,q')\}\) (19) \(\cup\{(x,x',y,y'):(x,x')\in B_1^+(s,s',r,q'),(y,y')\in[\mathrm{r}(q)..\mathrm{r}(r)]\times\mathrm{r}(s')\}\) (20) \(\cup\{(x,x',y,y'):(x,x')\in[\mathrm{I}(r)..\mathrm{I}(q)]\times\mathrm{I}(s'),(y,y')\in B_r^+(s,s',r,q')\}\) (21) \(\cup\{(x,x',y,y'):(x,x')\in[\mathrm{I}(r)..\mathrm{I}(q)]\times\mathrm{I}(s'),(y,y')\in[\mathrm{r}(q)..\mathrm{r}(r)]\times\mathrm{r}(s')\}.\) (22)

Now, we describe how to compute \(\mathrm{sim}(F[x..y),F[x'..y'))\) for the index sets (19), (20), (21), and (22).

For (19), note that (19) is the output of the \((s,s',r,q')\)-DISED instance.

For (20), observe that for such ranges of _x_ and _y_, we can write

\(F[x..y)=F[x..\mathrm{I}(r))+F[\mathrm{I}(r)..y).\)

From Proposition 3.7 follows that \(\mathrm{I}(r)\times[\mathrm{I}(s')..\mathrm{r}(s')]\) is an anchor set for \(\mathrm{sim}(F[x..y),F[x'..y'))\).

Next, we show how to compute \(\mathrm{sim}(F[x..y),F[x'..y'))\) in two cases that cover all possible scenarios.

(1) In the first case there is an anchor \((z,z')\in\mathrm{I}(r)\times[\mathrm{I}(s')..\mathrm{I}(q')]\). Then we can compute directly

\(\mathrm{sim}(F[x..y),F'[x'..y'))=\mathrm{max}_{z^\prime\in[\mathrm{I}(s^\prime)..\mathrm{I}(q^\prime)]:x^\prime\le z^\prime}\big\{\mathrm{sim}(F[x..\mathrm{I}(r),F'[x'..z'))\)<br> \(+\mathrm{sim}(F[\mathrm{I}(r)..y),F'[z'..y'))\big\},\)

where the first summand can be obtained from Main Theorem 4 and Theorem 4.1 on \(F[\mathrm{I}(s)..\mathrm{I}(r))\) and \(F'[\mathrm{I}(s')..\mathrm{I}(q'))\) and the second from the output from the \((r,s',q,q')\)-DISED instance.

(2) In the second case there is an anchor \((z,z')\in\mathrm{I}(r)\times[\mathrm{I}(q')..\mathrm{r}(s')]\). We further distinguish two subcases:

(a) In the first subcase suppose that \(z'\ge\mathrm{r}(q')\) and that the first case of Proposition 3.12 applied on \(\mathrm{sub}(s')\), \(F[\mathrm{I}(s)..\mathrm{I}(r))\), \(\mathrm{sub}(s')\) and \(q'\) holds. That is, \(z'\ge\mathrm{r}(q')\) and there is \(t'\in S\) such that \(s'\le t'<q'\) and \(\mathrm{sim}(F[x..z),F[x'..z'))\) aligns \(\mathrm{sub}(t')\) to a subtree of \(F[\mathrm{I}(s)..\mathrm{I}(r))\). Note, whenever \(z'\ge\mathrm{r}(q')\), then \(\mathrm{sub}(q')\subseteq F'[x'..z')\subseteq\mathrm{sub}(s')\). We derive that

\(\mathrm{sim}(F[x..z),F'[x'..z'))=\mathrm{sim}_{q^\prime}(F[x..z),F[x'..z')),\)

where \(\mathrm{sim}_{q^\prime}\) can be obtained from Lemma 4.10 on \(\mathrm{sub}(s'),F[\mathrm{I}(s)..\mathrm{I}(r)),S'\) and \(q'\in S'\). We may therefore write

\(\mathrm{sim}(F[x..y),F'[x'..y'))=\mathrm{max}_{(z,z^\prime)\in\mathrm{I}(r)\times[\mathrm{r}(q^\prime)..\mathrm{r}(s^\prime)]}\big\{\mathrm{sim}_{q^\prime}(F[x..z),F'[x..z'))\)<br> \(+\mathrm{sim}(F[z..y),F'[z'..y'))\big\}.\)

In this last expression, we can obtain the first summand, as mentioned before, from Lemma 4.10 on \(\mathrm{sub}(s'),F[\mathrm{I}(s)..\mathrm{I}(r)),S'\) and \(q'\in S'\), and the second summand from Lemma 5.7(12).

(b) In the second subcase, we have that either \(z'<\mathrm{r}(q')\), or \(z'\ge\mathrm{r}(q')\) and \(\mathrm{sim}(F[x..z),F[x'..z'))=\mathrm{sim}(F[x..z),F'[x'..\mathrm{I}(q'))+F'[\mathrm{I}(q')..z'))\). Therefore, for either of the two possible subcases, we can write \(\mathrm{sim}(F[x..z),F[x'..z'))=\mathrm{sim}(F[x..z),F'[x'..\mathrm{I}(q'))+F'[\mathrm{I}(q')..z'))\). By Propo sition 3.7, we have that \([\mathrm{I}(s)..\mathrm{I}(r)]\times\mathrm{I}(q')\) is a anchor set for \(\mathrm{sim}(F[x..z),F'[x'..z'))\). By Propo sition 3.8(ii), we get that \([\mathrm{I}(s)..\mathrm{I}(r)]\times\mathrm{I}(q')\) is also an anchor set for \(\mathrm{sim}(F[x..y),F'[x'..y'))\).

