\(\text{est}(\text{pivot}_\alpha(s),t)\le\text{est}(\text{pivot}_\alpha(s),v_\alpha)+|(v_\alpha,b_\alpha)|+|b_\alpha t|\)<br>
Using Equation (2), we get:<tbc>

\(\le(|sb_\alpha|+|s\text{pivot}_\alpha(s)|+18(loglogn-\alpha)+1)+1+|b_\alpha t|\)<br>
\(=|st|+|s\text{pivot}_\alpha(s)|+18(loglogn-\alpha)+2\) \(\text{(3)}\)

By symmetry, we also get \(\text{est}(\text{pivot}_\alpha(t),s)\le|st|+|t\text{pivot}_\alpha(t)|+18(loglogn-\alpha)+2\).<tbc>

3. Part 3: Estimate the distance between _s_ and t<tbc>

<tbc>In the third part of our algorithm, we estimate the distance between _s_ and t via \(\text{pivot}_\alpha(s)\) in TRIANGULATE(_s_). Thus, we get:<tbc>

\(\text{est}(s,t)\le\text{est}(s,\text{pivot}_\alpha(s))+\text{est}(\text{pivot}_\alpha(s),t)\)

Using Theorem 3.4, we have calculated the distance between _s_ and \(\text{pivot}_\alpha(s)\). Thus, \(\text{est}(s,\text{pivot}_\alpha(s))=|s\text{pivot}_\alpha(s)|\). Also, using Equation (3), we get:<tbc>

\(\le|s\text{pivot}_\alpha(s)|+(|st|+|s\text{pivot}_\alpha(s)|+18(loglogn-\alpha)+2)\)<br>
\(=|st|+2|s\text{pivot}_\alpha(s)|+18(loglogn-\alpha)+2\) \(\text{(4)}\)

By symmetry, we also get \(\text{est}(s,t)\le|st|+2|t\text{pivot}_\alpha(t)|+18(loglogn-\alpha)+2\).

## 6.3 Proof of Theorem 4.1

We now summarize the results of this section. We run the three algorithms in sequence: first MODIFIEDENSURECLOSENESS (Theorem 6.2), then algorithm in Theorem 6.4, and finally ENSUREBALLPROXIMITY. Each runs in time \(\tilde{\mathcal{O}}(n^2)\), so the total running time is \(\tilde{\mathcal{O}}(n^2)\).

After MODIFIEDENSURECLOSENESS terminates, for every pair (_s,t_) either \(\text{est}(s,t)\le 2|st|\) holds, in which case we are done, or the conditions of Theorem 6.2 hold. Henceforth, in this section we assume the latter, i.e., est(_s,t)\>_2|_st_|. The conditions of Theorem 6.2 are then used as input by Theorem 6.4, whose output is in turn used by ENSUREBALLPROXIMITY to obtain Equation (4). We now show the guarantees given by ENSUREBALLPROXIMITY. Substituting \(\alpha=loglogn-4\) in Equation (4), we obtain:<tbc>

\(\text{est}(s,t)\le|st|+2|s\text{pivot}_{loglogn-4}(s)|+74\)

<tbc>Suppose \(|s\text{pivot}_{loglogn-4}(s)|\le\lfloor|st|/2\rfloor-37\). Then:

\(\text{est}(s,t)\le|st|+2|s\text{pivot}_{loglogn-4}(s)|+74\)<br>
\(\le|st|+2(\lfloor|st|/2\rfloor-37)+74\)<br>
\(\le 2|st|\)

Thus, if \(|s\text{pivot}_{loglogn-4}(s)|\le\lfloor|st|/2\rfloor-37\), then we already obtain a 2 approximation of the st path. Using a symmetrical argument, if \(|t\text{pivot}_{loglogn-4}(t)|\le\lfloor|st|/2\rfloor-37\), we again obtain a 2 approximation of the st path. Thus, we have proven Theorem 4.1 with \(c'=37\).

