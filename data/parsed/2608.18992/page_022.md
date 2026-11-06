probability at least \(1-\frac{1}{2c}\) by Markov’s inequality. Let E denote the event \(M\le\bar{M}\) and let **1**<sub>E</sub> be the indicator random variable for this event. By Fact 2.1,

\(\mathbf{I}\big[\hat{\Pi}:Z\big|S_{VA}\big]\le\mathbf{I}\big[\hat{\Pi}:\mathbf{1}_\mathcal{E},Z\big|S_{VA}\big]\)<br> \(\text{(by Fact 2.2)}=\mathbf{I}\big[\hat{\Pi}:Z\big|S_{VA},\mathbf{1}_\mathcal{E}\big]+\mathbf{I}\big[\hat{\Pi}:\mathbf{1}_\mathcal{E}\big|S_{VA}\big]\)<br> \(\text{(by Fact 2.5)}\le\mathbf{I}\big[\hat{\Pi}:Z\big|S_{VA},\mathbf{1}_\mathcal{E}\big]+1\)<br> \(\text{(since}\neg\mathcal{E}\text{is}\{M>\bar{M}\}\big)=\mathbf{Pr}[\mathbf{1}_\mathcal{E}=1]\mathbf{I}\big[\hat{\Pi}:Z\big|S_{VA},\mathcal{E}\big]+\mathbf{Pr}[\mathbf{1}_\mathcal{E}=0]\mathbf{I}\big[\hat{\Pi}:Z\big|S_{VA},M>\bar{M}\big]+1\)<br> \(\le\mathbf{I}\big[\hat{\Pi}:Z\big|S_{VA},\mathcal{E}\big]+\frac{1}{2c}\mathbf{H}\big[Z\big|M>\bar{M}\big]+1\)<br> \(\le\mathbf{I}\big[\hat{\Pi}:Z\big|S_{VA},\mathcal{E}\big]+\frac{1}{2c}log_2\big(|\text{supp}(Z|M>\bar{M})|\big)+1,\)<br> \(\le\mathbf{I}\big[\hat{\Pi}:Z\big|S_{VA},\mathcal{E}\big]+\frac{1}{2c}log_2(|\text{supp}(Z)|)+1,\)

where, in the final inequality, we have used the fact that conditioning on an event cannot increase the support of a random variable.<sup>4</sup> Applying the upper bound on |supp(_Z_)| guaranteed by the premise in (i), we obtain

\(\mathbf{I}\big[\hat{\Pi}:Z\big|S_{VA}\big]\le\mathbf{I}\big[\hat{\Pi}:Z\big|S_{VA},\mathcal{E}\big]+\frac{L}{2}+1.\) (20)

To see why (20) also holds for algorithms satisfying only (ii) and not the bound on the support in (i), observe that the event \(M\le\beta\cdot d_U\le\bar{M}\) holds with probability 1 for algorithms that guarantee a worst case upper bound on the number of awake rounds.

For any \(j\ge M+1\), we define \(R_j=\infty\) and \(\hat{\Pi}_j=\langle\rangle\) (i.e., the empty message), which in particular implies that \(\mathbf{H}\big[R_j,\hat{\Pi}_j\big]=0\). Next, we derive an upper bound on the term

<sup>4</sup> To see that \(|\text{supp}(Z|\mathcal{E})|\le|\text{supp}(Z)|\), for any event E, it suffices to observe that \(\forall z:\mathbf{Pr}[Z=z|\mathcal{E}]=\frac{\mathbf{Pr}[Z=z\wedge\mathcal{E}]}{\mathbf{Pr}[\mathcal{E}]}\le\frac{\mathbf{Pr}[Z=z]}{\mathbf{Pr}[\mathcal{E}]}\) . Note that conditioning on E may increase the entropy of _Z_ nevertheless.

\begin{tabular}{cc}
Variable & Description \\ _αU_ & total number of awake rounds summed over the nodes in _U_ \\ _β_ & assumed upper bound on _αU_ \\ _dU_ & maximum number of neighbors in _∂U_ of any node in _U_ \\ _e(U,∂U_) & the number of edges across the cut \\ E, **1**<sub>E</sub> & event E occurs if \(M\le\bar{M}\); **1**<sub>E</sub> is its indicator random variable \\ _L_ & amount of information that the nodes in _U_ need to learn about \(\hat{\Pi}\) \\ _₹ M_ & upper bound on _M_ \\ _M_ & actual length of the extended transcript \(\hat{\Pi}\) \\ \(\hat{\Pi}\) & extended transcript (see Def. 12) \\ _ΠU_ & transcript of messages sent from _∂U_ to _U_ \\ _(Ri,\(\hat{\Pi}_i\))_ & message \(\hat{\Pi}_i\) was sent in round _Ri_ \\ _SVA_ & initial knowledge of the nodes in _VA_ \\ _U_ & nodes in _VA_ that have an edge to _VB_ \\ _∂U_ & nodes in _VB_ that have an edge to _VA_ \\ _(VA,VB_) & vertex cut that we are focusing on \\ _Z_ & function of the graph about which the nodes in _U_ need to learn something \\ \end{tabular}

**Figure 3** List of variables and parameters used in the proof of Lemma 1.

