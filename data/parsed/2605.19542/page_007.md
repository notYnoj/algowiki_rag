<tbc>Now we can conclude from above that

\(\gamma_n=\sum_{i=0}^nC_n^i\alpha_{i+1}\beta_{n-i}-\sum_{i=0}^nC_n^i\alpha_i\beta_{n+1-i}.\)

The proof of this lemma is finished. □

**Lemma 4.2.** _Let A,B,C and_ \(\alpha_i,\beta_i,\gamma_i\) _be as above. Let r,s be non- negative integers. Assume that_ \(\alpha_i=0\) _for_ \(0\le i\le r\) _and_ \(\beta_i=0\) _for_ \(0\le i\le s\)_. Then_<tbc>

\(\gamma_{r+s+1}=\big(C_{r+s+1}^r-C_{r+s+1}^s\big)\alpha_{r+1}\beta_{s+1}\)

<tbc>_and_<tbc>

\(\gamma_n=0\text{\textit{for all}}0\le n\le r+s.\)

<tbc>_Proof._ By Lemma 4.1,<tbc>

\(\gamma_{r+s+1}=\sum_{i=0}^{r+s+1}C_{r+s+1}^i\alpha_{i+1}\beta_{r+s+1-i}-\sum_{i=0}^{r+s+1}C_{r+s+1}^i\alpha_i\beta_{r+s+2-i}.\)

<tbc>If \(i\le r-1\), then \(i+1\le r\) and thus \(\alpha_{i+1}=0\). If \(i\ge r+1\), then \(r+s+1-i\le s\) and thus \(\beta_{r+s+1-i}=0\). Therefore, \(\alpha_{i+1}\beta_{r+s+1-i}=0\) for all \(i\neq r\). Then we have<tbc>

\(\sum_{i=0}^{r+s+1}C_{r+s+1}^i\alpha_{i+1}\beta_{r+s+1-i}=C_{r+s+1}^r\alpha_{r+1}\beta_{s+1}.\)

<tbc>Similarly, \(\alpha_i\beta_{r+s+2-i}=0\) for all \(i\neq r+1\). Then we have<tbc>

\(\sum_{i=0}^{r+s+1}C_{r+s+1}^i\alpha_i\beta_{r+s+2-i}=C_{r+s+1}^s\alpha_{r+1}\beta_{s+1}.\)

<tbc>We conclude from above<tbc>

\(\gamma_{r+s+1}=\big(C_{r+s+1}^r-C_{r+s+1}^s\big)\alpha_{r+1}\beta_{s+1}.\)

<tbc>We have

\(\gamma_n=\sum_{i=0}^nC_n^i\alpha_{i+1}\beta_{n-i}-\sum_{i=0}^nC_n^i\alpha_i\beta_{n+1-i}.\)

For \(n\le r+s\), we have \((i+1)+(n-i)=n+1\le r+s+1\). Then either \(i+1\le r\) or \(n-i\le s\). Thus, \(\alpha_{i+1}\beta_{n-i}=0\) for all \(0\le i\le n\). Similarly, \(\alpha_i\beta_{n+1-i}=0\) for all \(0\le i\le n\). Then we conclude that \(\gamma_n=0\) for \(n\le r+s\).

The proof of this lemma is finished. □

**Lemma 4.3.** _Suppose that_ |_A_|=1 _or_ |_B_|=1_. Then_

\(|A\dot{+}B|\ge min\{p,|A|+|B|-2\}.\)

