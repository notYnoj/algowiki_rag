_Proof._ Since the encoding function is an instantiation of the exponential mechanism, we know from Lemma 11 that the instantiation \(\mathsf{PriCoor}((\sigma,\pi),q,\varepsilon,D)\) satisfies \((\varepsilon,0)\)-joint differential privacy.

Since the coordination protocol guarantees an approximation ratio of \(\rho\), there exists some message \(r^\bullet\) in the set R such that<tbc>

\(\mathbb{E}_\pi\left[S(D,(\pi(r^\bullet,D^{(i)}))_{i\in[n]})\right]=q'(D,r^\bullet)\ge\frac{\mathsf{OPT}(D)}{\rho}.\)

<tbc>Note that \(\Delta(q')\le 1\) by our assumption on _f_. Then the utility guarantee of the exponential mechanism gives<tbc>

\(\mathbb{E}_\pi\left[S(D,(\pi(\sigma'(r,D),D^{(i)})))_{i\in[n]})\right]=q'(D,\pi(\sigma'(r,D)))\ge max_{r\in\mathcal{R}}q'(D,r)-\frac{2(\mathrm{log}(|\mathcal{R}|-\mathrm{log}(1/\beta)))}{\varepsilon}\)

<tbc>Also, observe that \(\mathrm{max}_{r\in\mathcal{R}}q'(D,r)\ge\mathsf{OPT}(D)/\rho\) and \(\mathrm{log}(|\mathcal{R}|)\le\ell\), so we also have

\(\mathbb{E}_\sigma\left[S(D,(\pi(\sigma'(r,D),D^{(i)})))_{i\in[n]})\right]\ge\mathsf{OPT}(D)/\rho-\frac{2(\ell-\mathrm{log}(1/\beta)))}{\varepsilon}\)

which recovers our stated bound.

## 5.3 Efficiency in Games with Dynamic Population

Now we briefly discuss a connection between coordination complexity and the efficiency in games with dynamic population, which leverages the connection to joint differential privacy discovered by \[LST15\]. We briefly introduce the model in \[LST15\], but the discussion will necessarily be lacking in detail - see \[LST15\] for a formal treatment.

Let _G_ be an _n_-player normal form _stage game_. We consider this game played repeatedly with a changing population of players over _T_ rounds. Each player _i_ has an action set A_<sub>i</sub>_, type _D_<sup>(_i_)</sup>, and a utility function _u(D_<sup>(_i_)</sup>_,a_)=_u<sub>i</sub>(a_). For concreteness, we can think about allocation games defined by auction rules _M_, which take as input an action profile and output an allocation _X<sub>i</sub>(a_) and a payment _P<sub>i</sub>(a_) for each player. Players have quasi-linear utility _u<sub>i</sub>(a_)=_v(D_<sup>(_i_)</sup>_,X<sub>i</sub>(a_))-_P<sub>i</sub>(a_)=_v<sub>i</sub>(X<sub>i</sub>(a_))-_P<sub>i</sub>(a_), where \(v_i:\mathcal{A}^n\rightarrow[0,1]\) denotes the valuation of player _i_ over the allocation. In these games, a natural objective function is social welfare: \(S(D,a)=\sum_{i=1}^nv_i(X_i(a))\). We write \(\mathsf{OPT}(D)=\mathrm{max}_{a\in\mathcal{A}^n}S(D,a)\) to denote the optimal welfare with respect to an instance _D_.

In the model of \[LST15\], after each round, every player independently exits with some probability _p_. Whenever a player leaves the game, she is replaced a new player, whose type is chosen adversarially. We will write _D<sup>t</sup>_ to denote the game instance, and _a<sup>t</sup>_ to denote the action profile played at round _t_. Lastly, we also assume that each player in the game is a _no-regret learner_ and plays some _adaptive learning algorithm_.<sup>5</sup>

The main result of \[LST15\] is that the existence of jointly differentially private algorithms that find action profiles approximately optimizing the welfare in a game implies that when the dynamically changing game is played by no-regret players, their average welfare is high.

**Theorem 6** (Corollary 5.2 of \[LST15\])**.** _Consider a mechanism with dynamic population_ (_M,T,p), such that the stage mechanism M is allocation based_ \((\lambda,\mu)\)_-smooth and_ \(T\ge 1/p\)_. Assume that there exists an_ \((\varepsilon,\delta)\)_-joint differentially private allocation algorithm_ \(X^\bullet:\mathcal{X}^n\rightarrow\mathcal{A}^n\) _such that for any input instance_ \(D\in\mathcal{X}^n\) _it computes a feasible outcome that is_ \(\rho\)_-approximately optimal_

\(\mathbb{E}[S(D,X^\bullet(D)]\ge\mathsf{OPT}(D)/\rho.\)

<sup>5</sup>For more details of adaptive learning algorithms and adaptive regret, see \[HS07\].

