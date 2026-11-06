<tbc>Note, in particular, that if _a_=0 and _b_=1, then we are able to write any vector (0,1_,x,_1+_x_), where _x\<n_ as the sum of _O_(log(_n_)) _SQ_-gens each of the form (0,1,2_<sup>i</sup>,_1+2_<sup>i</sup>_), where 2_<sup>i</sup>\<n/_2. Using Proposition 4.17, we can also prove the following.

Proposition 4.18. _Let_ \(\mathbf{v}=(a,a+b,a+c,a+b+c)\) _be an SQ-gen written so that_ \(a=a^\circ\le a+b=(a+b)^\circ\le(a+c)^\circ=a+c\)_. Then we can write_ **v** _as the sum of O_(log<sup>2</sup>(_n_)) _SQ-gens, where each is of the form_ \((a',a'+2^i,a'+2^j,a'+2^i+2^j)\) _for some_ \(a'<n\)_, and_ \(2^i,2^j<\mathrm{min}\{n-a',n/2\}\).

Proof. By Proposition 4.17, we can write **v** as the sum of _O_(log(_n_)) _SQ_- gens, where each is of the form (_s,s+b,s_+2_<sup>j</sup>,s+b_+2_<sup>j</sup>_), where _s\<n_ and 2_<sup>j</sup>\<_min{_n-s,n/_2}. By applying Proposition 4.17 to each of these _O_(log(_n_)) _SQ_-gens, it is clear that we can write (_s,s+b,s_+2_<sup>j</sup>,s+b_+2_<sup>j</sup>_) as the sum of _O_(log(_n_)) _SQ_-gens where each is of the form \((s',s'+2^i,s'+2^j,s'+2^i+s^j)\), where \(s'<n\), and \(2^i<\mathrm{min}\{n-s',n/2\}\). That is, we have expressed **v** as the sum of _O_(log<sup>2</sup>(_n_)) _SQ_-gens of the form \((a',a'+2^i,a'+2^j,a'+2^i+2^j)\) for some \(a'<n\), and \(2^i,2^j<\mathrm{min}\{n-a',n/2\}\), as required. □

Proposition 4.19. _Suppose that_ \(\mathbf{v}\in\mathcal{L}_1^{X+Y}(\mathcal{T})\)_, that_ **v** _can be written as the sum of_ \(z=O(n^{1-\alpha_3})SQ\)_-gens of the form_ (0,1,2_<sup>i</sup>,_1+2_<sup>i</sup>_) _for some_ 2_<sup>i</sup>\<n/_2 _and_ \(0<\alpha_3<1/2\)_, and that_ \(\sum i^2v_i\neq 0\)_. Then we can add Q-gens to_ **v** _in such a way that_ \(\sum i^2v_i=0\)_, and we add at most_ \(O(n^{1-\alpha_3})\) _vectors to the SQ-gens decomposition of_ **v**_, each of the form_ (0,1,2,3) _or_ (0,1_,n_-2_,n_-1)_. Furthermore, we can do this in such a way that we have added_ \(O(n^{1-\alpha_3})\) _edges to_ \(\Phi\).

Proof. We start by observing that any _SQ_-gen of the form (0,1,2_<sup>i</sup>,_1+2_<sup>i</sup>_), where 2_<sup>i</sup>\<n/_2, adds \(\pm 2^{i+1}\) to \(\sum i^2v_i\), where 2<sup>_i_+1</sup>_\<n_. Thus \(|\sum i^2v_i|\le nz=O(n^{2-\alpha_3})\) and, furthermore, \(\sum i^2v_i\) is even. Without loss of generality assume \(\sum_i^2v_i>0\) and write \(\sum i^2v_i=:a'=an\), where \(a\in\mathbb{Z}\), \(a=O(n^{1-\alpha_3})\), and _a_ is even since either _n_ is odd, or when _n_ is even we have that \(2n|\sum i^2v_i\). Then we may add _a/_2 _Q_-gens of the form (_n_-2_,n_-1,0,1,0,1,2,3) to **v**. Since each of these adds -2_n_ to \(\sum i^2v_i\), this reduces \(\sum i^2v_i\) to 0, and adds _a/_2 vectors of the form (0,1,2,3) and _a/_2 vectors of the form (0,1_,n_-2_,n_-1) to the _SQ_-gens decomposition of **v**. That is, in total we have added \(O(n^{1-\alpha_3})\) vectors to the _SQ_-gens decomposition of **v**, and \(O(n^{1-\alpha_3})\) edges to \(\Phi\) and \(\sum i^2v_i=0\), as required. □

We now turn to the proof of Lemma 4.14:

Proof of Lemma 4.14. Rather than considering \(\mathbf{v}\in\mathcal{L}_1^{X+Y}(\mathcal{T})\), we consider **v** such that

(i) **v**\\**v**<sup>**X+Y**</sup>=**0**,<tbc>

(ii) \(\sum v_i=0\),<tbc>

(iii) \(\sum iv_i=0(\mathrm{mod}n)\),<tbc>

(iv) \(\sum i^2v_i=0(\mathrm{mod}n)\), or<tbc>

(v) \(2n|\sum_{i\in V^{X+Y}}i^2v_i\) when _n_ is even.

Since every \(\mathbf{v}\in\mathcal{L}_1^{X+Y}(\mathcal{T})\) satisfies the above properties (by Proposition 3.16), it follows that if we can show that any such vector also satisfying \(|\mathbf{v}|=:t=O(n^{1-\alpha_1})\) can be reduced to **0** adding only \(O(n^{1-\alpha_2})\) edges to \(\Phi\) for some \(0<\alpha_2<\alpha_1\), then every \(\mathbf{v}\in\mathcal{L}_1^{X+Y}(\mathcal{T})\) satisfying \(|\mathbf{v}|=:t=O(n^{1-\alpha_1})\) can be reduced to **0** in this way, satisfying the claims of the lemma. Suppose \(|\mathbf{v}|=:t=O(n^{1-\alpha_1})\). By Proposition

