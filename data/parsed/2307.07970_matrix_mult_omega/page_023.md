4. **Compatibility zero-out II: unique triple.** After the compatibility zero-out I, every level-1 block is compatible with at least 1 level-\(\ell\) triple and we want every level-1 block to be compatible with _exactly one_ level-\(\ell\) triple. So in this step, we zero out level-1 _Z_-blocks that are compatible with more than one level-\(\ell\) triples. Note that the level-1 blocks zeroed out in this step will become holes.<tbc>

5. **Usefulness zero-out.** Now that each remaining level-1 _Z_-block \(Z_\hat{K}\) is contained in exactly one level-\(\ell\) triple _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_, we can define the notion of whether a level-1 block is _useful_ for the level-\(\ell\) triple containing it as whether it is consistent with the complete split distributions \(\{\beta_{Z,i,j,k}\}_{i+j+k=2^\ell}\). Note that we can only do this now because previously we do not have the property that every level-1 _Z_-block is in a unique level-\(\ell\) triple. In this step we zero out the level-1 blocks that are not useful for the level-\(\ell\) triple containing it.<tbc>

6. **Fixing holes.** Now we have obtained level-1-independent level-\(\ell\) interface tensors with holes. We use the following result which will be proved in Section 7 to fix the holes.<tbc>

<tbc>**Corollary 4.2** (Fixing holes in interface tensors)**.** _Let T be a level-_\(\ell\) _interface tensor with parameter list_<tbc>

<tbc>\(\{(n_t,i_t,j_t,k_t,\beta_{X,t},\beta_{Y,t},\beta_{Z,t})\}_{t\in[s]}.\)<tbc>

<tbc>_Let_ \(N=2^{\ell-1}\cdot\sum_{t\in[s]}n_t\)_. Suppose T_<sub>1</sub>_,...,T<sub>r</sub> are broken copies of T where_ \(\le\frac{1}{8N}\) _fraction of level-1 X-, Y - and Z-blocks are holes. If_ \(r\ge 2^{C_1N/logN}\) _for some large enough constant C_<sub>1</sub>_\>_0_, the direct sum_ \(\oplus_{i=1}^rT_i\) _can degenerate into an unbroken copy of T._

## 5 Global Stage

In the global stage, we take as input the tensor \(\mathrm{CW}_q^{\otimes N}\) for \(N=n\cdot 2^{\ell^*}\) and output independent copies of a level-\(\ell^*\) interface tensor, where the output will be a degeneration of the input. For the rest of this section, we will use \(\ell\) to denote \(\ell^*\) for convenience.

Given \(\alpha\), which is a distribution over \(\{(i,j,k)\in\mathbb{Z}_{\ge 0}^3|i+j+k=2^\ell\}\), and \(\beta_{X,i,j,k},\beta_{Y,i,j,k},\beta_{Z,i,j,k}\), which are level-\(\ell\) complete split distributions, we define the following quantities:

• \(\alpha_X\) is the marginal distribution of \(\alpha\) on the _X_-dimension, i.e., \(\alpha_X(i)=\sum_{j,k}\alpha(i,j,k)\) for any _i_. We also similarly define \(\alpha_Y\) and \(\alpha_Z\).<tbc>

• _D_ is the set of distributions whose marginal distributions on the three dimensions are \(\alpha_X,\alpha_Y,\alpha_Z\) respectively, and let the penalty term \(P_\alpha:=\mathrm{max}_{\alpha^\prime\in D}H(\alpha')-H(\alpha)\ge 0\).<tbc>

• For every _k_, \(\alpha(+,+,k):=\sum_{i>0,j>0}\alpha(i,j,k)\); for every _j_, \(\alpha(+,j,+):=\sum_{i>0,k>0}\alpha(i,j,k)\); and for every _i_, \(\alpha(i,+,+):=\sum_{j>0,k>0}\alpha(i,j,k)\).<tbc>

• For every _k_, \(\overline{\beta_{Z,+,+,k}}:=\frac{1}{\alpha(+,+,k)}\sum_{i>0,j>0}\alpha(i,j,k)\cdot\beta_{Z,i,j,k}\), and \(\overline{\beta_{Y,+,j,+}}\) and \(\overline{\beta_{X,i,+,+}}\) are defined similarly.<tbc>

• \(\overline{\beta_{X,*,*,*}}:=\sum_{i,j,k}\alpha(i,j,k)\cdot\beta_{X,i,j,k}\) and \(\overline{\beta_{Y,*,*,*}}\) and \(\overline{\beta_{Z,*,*,*}}\) are defined similarly.<tbc>

• \(\lambda_Z:=\sum_{i,j,k:i=0\text{or}j=0}\alpha(i,j,k)\cdot H(\beta_{Z,i,j,k})+\sum_k\alpha(+,+,k)\cdot H(\overline{\beta_{Z,+,+,k}})\), and \(\lambda_X\) and \(\lambda_Y\) are defined similarly.<tbc>

