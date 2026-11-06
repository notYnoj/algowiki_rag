<tbc>Proof. Fix \(\mathbf{v}\in\mathcal{L}_1^{X+Y}(\mathcal{T})\). Note that \(\mathcal{L}_1^{X+Y}(\mathcal{T})\subseteq\mathcal{L}_2^{X+Y,X-Y}(\mathcal{T})\), and thus by Proposition 3.14 we may express it as the sum of 2-part generators. We may then replace each 2-part generator with weights (1,-1,-1,1) on coordinates (_a,b,c,b+c-a_) in the _V_ <sup>_X+Y_</sup> part and weights (-1,1,1,-1) on coordinates (_s-a,s-b,s-c,s_-(_b+c-a_)) in the _V_ <sup>_X-Y_</sup> part, by a vector with weights (1,-1,-1,1,-1,1,1,-1) on coordinates (_a,b,c,b+c-a,a-s,b-s,c-s,(b+c-a_)-_s_) in the _V_ <sup>_X+Y_</sup> part. Since \(\mathbf{v}\in\mathcal{L}_1^{X+Y}(\mathcal{T})\), the total weight to each vertex \(s-a\in V^{X-Y}\) is identically 0, and thus when we replace the generators and move all weight on \(s-a\in V^{X-Y}\) to \(a-s\in V^{X+Y}\), in total we are adding 0 weight to _a-s_. Thus **v** has remained unchanged, and is now described as the sum of _Q_-gens. Hence the collection of _Q_-gens is generating for \(\mathcal{L}_1^{X+Y}(\mathcal{T})\). □

It is clear that \(\mathcal{L}_2^{X+Y,X-Y}(\mathcal{T})\) inherits the ‘zero-sum’ properties of Proposition 3.7. As well as describing a nice generating family for \(\mathcal{L}_1^{X+Y}(\mathcal{T})\), we can also obtain analogues to Propositions 3.7 and 3.8. Indeed, there is a natural recursive structure that gives motivation for the following proposition: let **e<sub>i</sub>** be the unit vector with a 1 at _i_, and 0 for every other entry. Then for a vector **v** and a shift _s_, define _f<sub>s</sub>_(**v**) by _f<sub>s</sub>(v_<sub>_s+a_</sub>)=-_v<sub>a</sub>_ for each _a_. Letting **v<sup>0</sup>**=**e<sub>a</sub>** for an arbitrary choice _a_, we define **v<sup>1</sup>**:=**v<sup>0</sup>**+_f_<sub>_s_<sub>1</sub></sub>(**v<sup>0</sup>**) and see that \(v_{s_1+a}^1=-1\), \(v_a^1=1\) and _v_<sup>1</sup> is 0 at all other entries. Any vector formed from an integer combination of these satisfies the \(\sum_iv_i=0\) condition. Defining **v<sup>2</sup>**:=**v<sup>1</sup>**+_f_<sub>_s_<sub>2</sub></sub>(**v<sup>1</sup>**), we see that **v<sup>2</sup>** has \(v_{s_1+a}^2=-1\), \(v_a^2=1\), \(v_{s_2+a}^2=-1\), and \(v_{s_1+s_2+a}^2=1\). Note that this yields all of the _SQ_-gens, since each is of the form with weights (1,-1,-1,1) on coordinates (_a,a+s_<sub>1</sub>_,a+s_<sub>2</sub>_,a+s_<sub>1</sub>+_s_<sub>2</sub>) for some free choice of _a_, _s_<sub>1</sub> and _s_<sub>2</sub>, (and, in particular, any linear combination of these vectors satisfies both \(\sum_iv_i=0\) and \(\sum_iv_i=0\)). Repeating the recursion once more, i.e. so that **v<sup>3</sup>**:=**v<sup>2</sup>**+_f_<sub>_s_<sub>3</sub></sub>(**v<sup>2</sup>**), yields all of the _Q_-gens, and naturally suggests the additional constraint that \(\sum_i^2v_i=0\) for all vectors in \(\mathcal{L}_1^{X+Y}(\mathcal{T})\).

Proposition 3.16. _Let_ \(\mathbf{v}\in\mathcal{L}_1^{X+Y}(\mathcal{T})\)_. Then_

(_i)_ \(\sum_iv_i=0\);<tbc>

(_ii)_ \(\sum_iv_i=0(modn)\)_; and_<tbc>

_(iii)_ \(\sum_{i\in V^{X+Y}}i^2v_i=0(modn)\).

_Furthermore, if n is even then_ \(2n|\sum_{i\in V^{X+Y}}i^2v_i\).

Proof. Suppose \(\mathbf{v}\in\mathcal{L}_1^{X+Y}(\mathcal{T})\). The first two zero-sum properties follow easily from the discussion above. To see the third property note that, by Proposition 3.15, **v** is the sum of an integer collection of vectors with weights (1,-1,-1,1,-1,1,1,-1) on coordinates (_a_<sub>1</sub>_,a_<sub>2</sub>_,a_<sub>3</sub>_,a_<sub>2</sub>+_a_<sub>3</sub>-_a_<sub>1</sub>_,s+a_<sub>1</sub>_,s+a_<sub>2</sub>_,s+a_<sub>3</sub>_,s+a_<sub>2</sub>+_a_<sub>3</sub>-_a_<sub>1</sub>). Manual calculation of \(\sum_i^2v_i\) for each of these _Q_-gens individually yields the result for each generator (and in particular when _n_ is even satisfy \(2n|\sum_i^2v_i\)), thus the integer sum of any collection of such generators will satisfy the equation. In particular, writing each _Q_-gen as the difference of two _SQ_-gens it can be seen that the sum of the squares of these are equal and so cancel as a _Q_-gen (modulo _n_). □

We also give the statement of the converse.

Proposition 3.17. _First suppose that n is odd. Any vector_ **v** _which only has non-zero support in V_ <sup>_X+Y_</sup> _and satisfies_

(_i)_ \(\sum v_i=0\),

