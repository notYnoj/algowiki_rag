Observe that \(\beta\le 1\) by (2). By (1), (6), and (8), we have

\(Pr\big(\big|\frac{Y}{N}-p\big|\ge\beta p\big)=Pr\big(|Y-pk|\ge\beta pk\big)\le 2exp\big(-\frac{\beta^2pk}{3}\big)=2exp\big(-\frac{\beta^2|M_j|N}{3|R|}\big)\le 2exp\big(-\frac{\beta^2N}{6(\Delta+1)}\big)\le\frac{\delta}{3}.\)

Next we show that, with probability at least \(1-\delta\), the estimate \(\hat{m}\) approximates \(|M_\infty|\) with the claimed accuracy. Observe first that \(|ac-bd|\le a|c-d|+d|a-b|\) for \(a,b,c,d\ge 0\). Thus, with probability at least \(1-\delta\), both no failure occurs and

\(\big|\hat{m}-|M_j|\big|=n\big|\frac{X}{N}\cdot\frac{Y}{N}-\frac{|R|}{n}\cdot\frac{|M_j|}{|R|}\big|\le n\big(\frac{X}{N}\cdot\big|\frac{Y}{N}-\frac{|M_j|}{|R|}\big|+\frac{|M_j|}{|R|}\cdot\big|\frac{X}{N}-\frac{|R|}{n}\big|\big)\le n\big(\frac{X}{N}\cdot\gamma\cdot\frac{|M_j|}{|R|}+\frac{|M_j|}{|R|}\cdot\gamma\cdot\frac{|R|}{n}\big)\le 2\gamma n=2\gamma\big(|R|+|B|\big)\le 4\Delta\gamma|M_\infty|=\frac{\epsilon}{2}\cdot|M_\infty|\text{(9)}\)

where the last inequality follows by (4) and (5). Thus, with probability at least \(1-\delta\), we have

\(\big|\hat{m}-|M_\infty|\big|\le\big|\hat{m}-|M_j|\big|+\big||M_j|-|M_\infty|\big|\le\frac{\epsilon}{2}\cdot|M_\infty|+\frac{\epsilon}{2}\cdot|M_\infty|=\epsilon|M_\infty|\)

where the last inequality follows by (3) and (9).

It remains to derive an upper bound for the number of oracle queries we make to compute the estimate. First, we make _N_ queries to determine _X_. Second, we make \(2(\Delta+1)N\) queries to obtain _N_ red nodes (or declare failure). Third, for each of the _N_ red nodes, we execute the algorithm in Section 4 for _j_ rounds to determine whether the node is matched in _M<sub>j</sub>_. Each round of the algorithm propagates information (messages) for at most two hops in G, which implies that we can decide whether any given \(r\in R\) is matched in _M<sub>j</sub>_ if we know the preferences of all nodes within distance 2_j_ from _r_ in G. There are at most<tbc>

\(1+\Delta\sum_{i=0}^{2j-1}(\Delta-1)^i=1+\frac{\Delta}{\Delta-2}\big((\Delta-1)^{2j}-1\big)<3(\Delta-1)^{2j}\)

