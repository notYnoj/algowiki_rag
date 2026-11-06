<tbc>Theorem 1.7 is at the heart of our counting and sampling algorithms from Theorem 1.2. Intuitively, it states that given a solution _Y_ sampled from \(\mu_{\Phi\backslash c_0}\) (which may violate _c_<sub>0</sub>), we can flip the value of at most _O_(log_n_) variables with high probability to obtain a truth assignment _X_ in such a way that _X_ is a solution to \(\Phi\) and is distributed uniformly at random as \(\mu_\Phi\). We establish Theorem 1.7 by constructing a recursive coupling procedure and showing it terminates with high probability within _O_(log_n_) iterations. We then apply an LP-based algorithm introduced by Moitra \[Moi19\] which provides fast counting and sampling algorithms; this is also the strategy in \[WY24\].

The coupling result in Theorem 1.7 can be understood as a way to describe the _decay of correlation_ phenomenon. In particular, it is similar to various other notions of correlation decay such as disagreement percolation for showing Gibbs uniqueness \[vdBS94\], recursive coupling for proving strong spatial mixing \[GMP05\], and especially coupling independence for showing spectral independence \[CZ23, CGG<sup>+</sup>24\]. For random CSPs like _k_-SAT, the Wasserstein distance between the original formula and the formula obtained after the removal of a single clause is reminiscent of the cavity method. However, establishing Theorem 1.7 for random _k_-SAT is quite different from those previous works on distinct models. Firstly, the _k_-SAT instance is based on hypergraphs while previous rigorous approaches for correlation decay mostly consider models defined on graphs. Secondly, the hypergraph associated with a random _k_-SAT formula contains a large maximum degree, making the analysis significantly more challenging. Finally, Theorem 1.7 considers the removal of a constraint, while previous approaches often consider flipping the value of a variable.

Before discussing our proof approach for Theorem 1.7 in Section 1.3, we first mention a few direct yet important implications of Theorem 1.7 for random _k_-SAT at the considered densities.

Many empirical studies in statistical physics use heuristics to predict the solution space geometry of random _k_-SAT, with the (predicted) phase transitions illustrated in Figure 1. Extensive research from both computer science and statistical physics has been dedicated to understanding these phases and their corresponding thresholds \[MMZ05, DMMZ05, ART06, CP12, ZK16, BS20\]. Notably, the satisfiability threshold \(\alpha_\mathrm{sat}\) has been precisely determined by \[DSS22\] for sufficiently large _k_. Other important thresholds, such as the clustering threshold \(\alpha_\mathrm{clust}\) (also referred to as the dynamic phase transition threshold in \[KMRT<sup>+</sup>07\]), where the solution space of a _k_-SAT fragments into an exponential number of clusters, and the condensation threshold \(\alpha_\mathrm{cond}\), beyond which the solution space is dominated by a few large clusters, have been extensively studied but are not yet fully characterized.

One of the key tools for statistical physicists in understanding and describing the solution space geometry of random _k_-SAT are the notions of _replica symmetry_ and _replica symmetry breaking_ \[MRTS08\], first introduced by Parisi \[Par79\]. Informally, "replica symmetry" refers to the idea that two uniformly chosen variables are nearly independent, while "replica symmetry breaking" corresponds to the existence of extensive long-range correlations. Following \[KMRT<sup>+</sup>07\], we present the formal definition below.

**Definition 1.8** (replica symmetry)**.** Given \(k,\alpha\), we say that a random _k_-SAT model with density \(\alpha\) is _replica symmetric_ if, for \(\Phi=(V,C)\sim\Phi(k,n,\lfloor\alpha n\rfloor)\), a uniform satisfying assignment \(\sigma\sim\mu_\Phi\), and two variables \(v_1,v_2\in V\) chosen uniformly at random, the following holds:<tbc>

\(\mathrm{lim}_{n\rightarrow\infty}|\mathbf{Pr}\left[\sigma(v_1)=\sigma(v_2)=\mathsf{True}\right]-\mathbf{Pr}\left[\sigma(v_1)=\mathsf{True}\right]\mathbf{Pr}\left[\sigma(v_2)=\mathsf{True}\right]|=0.\)

auniq
acust
acond
sat
uniqueness
extremality
clustering
condensation
unsat
constraint level a

Figure 1. The heuristic diagram in \[DSS22\] depicts phase transitions in the geometry of the

solution space of a random _k_-SAT instance as the density \(\alpha\) increases from left to right.

