**Proof.** Consider \(\pi_1\) and \(\pi_2\) and suppose that \(|\mathsf{lcs}(\pi_1,\pi_2)|=x\) and \(|\mathsf{lcs}(\pi_1,\pi_3)|=y\). According to Theorem 8.1, \(\pi_2\) and \(\pi_3\) can be respectively decomposed into _x_ and _y_ substrings, such that the characters in each of these substrings appear in the reverse order as appear in \(\pi_1\). On the other hand, by the Pigeonhole principle, at least one of the substrings of \(\pi_1\) and one of the substrings of \(\pi_2\) have _m/xy_ characters in common. Since these characters appear in the same order in both of these substrings, the longest common subsequence of these two substrings is at least _m/xy_. Therefore

\(|\mathsf{lcs}(\pi_1,\pi_2)|\cdot|\mathsf{lcs}(\pi_2,\pi_3)|\cdot|\mathsf{lcs}(\pi_3,\pi_1)|\ge x\cdot y\cdot m/xy\)<br>
\(=m.\)

The second theorem we use in the proof of Lemma 8.5 is called _Turán_, which provides a lower bound on the edge size of _K_<sub>_r_+1</sub>-free graphs. In Section 4 we mentioned a general form of this theorem. By setting _r_=2 in Turán’s theorem we obtain the following Corollary.

Corollary 8.1. (of Turán’s theorem) _Any triangle-free graph on k vertices has at most k_<sup>2</sup>/4 _edges._

Now, we are ready to prove Lemma 8.5

**Proof of Lemma 8.5:** Recall that the blocks in _U_ and <o>_U_</o> constitute |_U_| block pairs, namely \((b_1,\bar{b}_1),(b_2,\bar{b}_2),\dots,(b_{|U|},\bar{b}_{|U|})\), such that for every \(1\le i\le|U|\), we have<tbc>

\(|\mathsf{lcs}(b_i,\bar{b}_i)=\Omega(n^{1/2-26\delta-4\zeta-\eta}).\)

<tbc>With this in mind, we construct a graph on the blocks of \(U'\) and \(\overline{U'}\). Let

\(d=min_{1\le i\le|U|}|\mathsf{lcs}(b_i,\bar{b}_i)|,\)

and let _G(V,E_) be a graph, where |_V_|=|_U_| and there is an edge between _v<sub>i</sub>_ and _v<sub>j</sub>_, if at least one of the following two conditions holds:

• \(|\mathsf{lcs}(b'_i,\bar{b}'_j)\ge\sqrt{3}d\).<tbc>

• \(|\mathsf{lcs}(b'_j,\bar{b}'_i)\ge\sqrt{3}d\).<tbc>

<tbc>Now, consider tree vertices \(v_i,v_j,v_k\in V\) . By definition, we know \(|\mathsf{lcs}(b'_i,\bar{b}'_i)|\ge d\). If we only consider these _d_ symbols in blocks \(b'_j\) and \(\bar{b}'_k\), by Lemma 8.6, we have<tbc>

\(|\mathsf{lcs}(b'_j,\bar{b}'_k)|\cdot|\mathsf{lcs}(b'_j,|\mathsf{lcs}(b'_i,\bar{b}'_i))|\cdot|\mathsf{lcs}(|\mathsf{lcs}(b'_i,\bar{b}'_i),\bar{b}'_k)|\ge d,\)

<tbc>which means<tbc>

\(max\left\{\begin{array}{ c }
|\mathsf{lcs}(b'_j,\bar{b}'_k)| \\
|\mathsf{lcs}(b'_j,|\mathsf{lcs}(b'_i,\bar{b}'_i))| \\
|\mathsf{lcs}(|\mathsf{lcs}(b'_i,\bar{b}'_i),\bar{b}'_k)|
\end{array}\right\}\ge\sqrt{3}d.\)

<tbc>Therefore, at least one edge exists between every triple _v<sub>i</sub>,v<sub>j</sub>_, and _v<sub>k</sub>_, and hence the complement graph of _G_ (i.e., <o>_G_</o>) is triangle-free. By Corollary 8.1, <o>_G_</o> has at most |_U_|<sup>2</sup>/4 edges, and so _G_ has at least<tbc>

\(|U|(|U|-1)/2-|U|^2/4=|U|^2/4-|U|/2\)

