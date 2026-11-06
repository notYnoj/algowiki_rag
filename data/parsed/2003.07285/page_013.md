<tbc>By the precondition of Algorithm 1, we know that the solution size is at most \(n^{1-\delta}\). Thus, in order to find a \(n^{(1-\delta)/2}\) approximation solution for lcs(_s,<o>s</o>_), it suffices to find the longest common subsequence of _s_<sup>∗</sup> and <o>_s_</o> up to a size at most<tbc>

\(n^{1-\delta}\cdot n^{(1-\delta)/2}=n^{(1-\delta)/2}.\)

<tbc>Therefore, using a dynamic program based on  (4.1), we can find a solution in time

\(|s^*|n^{(1-\delta)/2}\mathrm{log}n=n^{(1+\delta)/2}n^{(1-\delta)/2}\mathrm{log}n\)<br>
\(=\tilde{O}(n).\) (6.3)

