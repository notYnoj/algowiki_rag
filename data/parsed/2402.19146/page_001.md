# Subsequence Matching and LCS under Cartesian-Tree Equivalence

**Abstract**

Two strings of the same length are said to _Cartesian-tree match_ (_CT-match_) if their Cartesian-trees are isomorphic [Park et al., TCS 2020]. Cartesian-tree matching is a natural model that allows for capturing similarities of numerical sequences. Oizumi et al. [CPM 2022] showed that subsequence pattern matching under CT-matching model (_CT-MSeq_) can be solved in _O(nm_loglog_n_) time, where **_n_** and **_m_** are text and pattern lengths, respectively. This current article follows this line of research, and gives the following new results:

(1) An _O(nm_)-time CT-MSeq algorithm for binary alphabets.<br> (2) An _O_((_nm_)<sup>1-\(\epsilon\)</sup>)-time conditional lower bound for the CT-MSeq problem on alphabets of size 4, for any constant \(\epsilon>0\), under the Orthogonal Vector Hypothesis (OVH).<br> Further, we introduce the new problem of _longest common subsequence under CT-matching_ (_CT-LCS_) for two given strings **_S_** and **_T_** of length **_n_**, and present the following results:

Taketo Tsujimoto<sup>1</sup>, Yuki Yonemoto<sup>1∗</sup>, Hiroki Shibata<sup>2</sup>,<br> Takuya Mieno<sup>3</sup>, Yuto Nakashima<sup>4</sup>, Shunsuke Inenaga<sup>4</sup>

<sup>1</sup>Department of Information Science and Technology, Kyushu University, Japan.

<sup>2</sup>Joint Graduate School of Mathematics for Innovation, Kyushu University, Japan.

<sup>3</sup>Department of Computer and Network Engineering, University of Electro-Communications, Japan.

<sup>4</sup>Department of Informatics, Kyushu University, Japan.

\*Corresponding author(s). E-mail(s): yonemoto.yuuki.240@s.kyushu-u.ac.jp; Contributing authors: tsujimoto.taketo.852@s.kyushu-u.ac.jp; Shibata.hiroki.753@s.kyushu-u.ac.jp; tmieno@uec.ac.jp; nakashima.yuto.003@m.kyushu-u.ac.jp; inenaga.shunsuke.380@m.kyushu-u.ac.jp;

