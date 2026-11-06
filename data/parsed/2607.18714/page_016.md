## 6 Ensuring ball proximity

In this section, we prove Theorem 4.1. To achieve this, we adapt two algorithms from \[Gup25\] and run them as subroutines. Let us see the first subroutine from \[Gup25\].

**Lemma 6.1** (\[Gup25\])**.** _There is an algorithm_ ENSURECLOSENESS _such that after its execution, for every pair_ (_s,t), either_ \(\mathrm{est}(s,t)\le 2|\mathrm{st}|\)_, or, for every_ \(0\le\mathrm{i}\le\mathrm{loglog}n-1\)_, either_

(_A1)_ \(|\mathrm{sa}_\mathrm{i}|\le|\mathrm{tb}_\mathrm{i}|\) _and_ \(|\mathrm{sa}_\mathrm{i}|-|\mathrm{s}\mathrm{pivot}_\mathrm{i}(s)|\le 3\)_, or_<tbc>

_(A2)_ \(|\mathrm{sa}_\mathrm{i}|\ge|\mathrm{tb}_\mathrm{i}|\) _and_ \(|\mathrm{tb}_\mathrm{i}|-|\mathrm{t}\mathrm{pivot}_\mathrm{i}(t)|\le 3\).

_Moreover,_ ENSURECLOSENESS _runs in_ \(\tilde{\mathcal{O}}(\mathrm{n}^2)\).

ENSURECLOSENESS plays a central role in \[Gup25\]. After executing ENSURECLOSENESS, either \(\mathrm{est}(s,\mathrm{t})\le 2|\mathrm{st}|\) holds or we obtain a relation between |sa<sub>i</sub>| and |s pivot<sub>i</sub>(s)| (or between |tb<sub>i</sub>| and |t pivot<sub>i</sub>(t)|). The algorithm ENSURECLOSENESS performs loglogn iterations, from i=loglogn-1 down to i=0. After the i-th iteration completes, the relation in Theorem 6.1 holds for that specific value of i. Once all iterations finish, the relation holds simultaneously for all \(0\le\mathrm{i}\le\mathrm{loglog}n-1\). In our paper, our modified nested vertex sampling starts at the intermediate set \(\mathrm{A}_\alpha\) rather than the base set A<sub>1</sub> as in \[Gup25\]. Consequently, we execute a modified version of the algorithm, which we call MODIFIEDENSURECLOSENESS, running only from i=loglogn-1 down to \(\mathrm{i}=\alpha\) and skipping the iterations below \(\alpha\).

**Lemma 6.2.** _There is an algorithm_ MODIFIEDENSURECLOSENESS _such that after its execution, for every pair_ (_s,t), either_ \(\mathrm{est}(s,\mathrm{t})\le 2|\mathrm{st}|\)_, or, for every_ \(\alpha\le\mathrm{i}\le\mathrm{loglog}n-1\)_, either_

(_A1)_ \(|\mathrm{sa}_\mathrm{i}|\le|\mathrm{tb}_\mathrm{i}|\) _and_ \(|\mathrm{sa}_\mathrm{i}|-|\mathrm{s}\mathrm{pivot}_\mathrm{i}(s)|\le 3\)_, or_<tbc>

_(A2)_ \(|\mathrm{sa}_\mathrm{i}|\ge|\mathrm{tb}_\mathrm{i}|\) _and_ \(|\mathrm{tb}_\mathrm{i}|-|\mathrm{t}\mathrm{pivot}_\mathrm{i}(t)|\le 3\).

_Moreover,_ MODIFIEDENSURECLOSENESS _runs in_ \(\tilde{\mathcal{O}}(\mathrm{n}^2)\).

The only change from Theorem 6.1 is the lower limit of the range: \(\alpha\le\mathrm{i}\) instead of \(0\le\mathrm{i}\). The algorithm MODIFIEDENSURECLOSENESS and its proof remain identical to those in \[Gup25\]. We now state the next important lemma from \[Gup25\], which crucially uses Theorem 6.1. Let us assume that est(_s,t)\>_2|st| after executing ENSURECLOSENESS. Then, \[Gup25\] show the following lemma:

**Lemma 6.3** (\[Gup25\])**.** _There is a randomised algorithm such that after its execution, for each_ \(0\le\mathrm{i}\le\mathrm{loglog}n-1\),

\(\mathrm{est}(\mathrm{u}_\mathrm{i},\mathrm{v}_\mathrm{i})\le|a_\mathrm{i}\mathrm{b}_\mathrm{i}|+18(\mathrm{loglog}n-\mathrm{i})\)

_Moreover, the algorithm runs in_ \(\tilde{\mathcal{O}}(\mathrm{n}^2)\) _time with a high probability._

The algorithm runs for loglogn iterations, from i=loglogn-1 to 0. When i=loglogn-1, it computes a good approximation between u<sub>loglogn-1</sub> and v<sub>loglogn-1</sub>. In the ith iteration, it computes a good approximation between u<sub>i</sub> and v<sub>i</sub> using the relation between u<sub>i+1</sub> and v<sub>i+1</sub> by induction, and the relations among sa<sub>i</sub>, spivot<sub>i</sub>(s), and tb<sub>i</sub>, tpivot<sub>i</sub>(t) in (A1) and (A2). As in ENSURECLOSENESS, we do not run the algorithm for loglogn iterations. Instead, we run it for \(\mathrm{loglog}n-\alpha\) iterations and apply the modified Theorem 6.2 to obtain the following.

**Lemma 6.4.** _There is a randomised algorithm such that after its execution, for each_ \(\alpha\le\mathrm{i}\le\mathrm{loglog}n-1\),

\(\mathrm{est}(\mathrm{u}_\mathrm{i},\mathrm{v}_\mathrm{i})\le|a_\mathrm{i}\mathrm{b}_\mathrm{i}|+18(\mathrm{loglog}n-\mathrm{i})\)

_Moreover, the algorithm runs in_ \(\tilde{\mathcal{O}}(\mathrm{n}^2)\) _time with a high probability._

