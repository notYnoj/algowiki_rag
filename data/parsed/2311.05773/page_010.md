1. _for any_ \(y\in X_{i+1}\)_, conditioned on y being in the inversion, we have_ \(P(x=a)\le P(x=b)\) _for a\<b, i.e., x is uniformly distributed among all the red elements in_ \(R_y=\{x\in X_i|y<x<u_{i+1}\}\) _or biased towards the outside of R<sub>y</sub>._<tbc>

_2._ _for any_ \(x\in X_i\)_, conditioned on x being in the inversion, y is either uniformly distributed in_ \(B_x=\{y\in X_{i+1}|u_i<y<x\}\)_, or biased towards the outside, i.e.,_ \(P(y=a)\ge P(y=b)\) _for a\<b._<tbc>

_3._ _Either statement (1) holds with the uniform distribution, or statement (2) holds with the uniform distribution._

_Proof._ Conditioned on one endpoint of the inversion being fixed, say the red _x_. Then there is a set _B<sub>x</sub>_ of blue elements that can form an inversion with _y_ (if not, _x_ cannot be part of an inversion). If the inversion was found by a uniformly sampled pair, each \(y\in B_x\) is chosen with the same probability, showing the statement of the lemma. If the inversion was found after sampling some of the elements, we actively choose one of the endpoints uniformly at random. If this randomly chosen element is _x_, we get (1.) with the uniform distribution. Hence, for the second part, we should assume that _y_ is the minimum (by the choice of naming in the lemma) of a set _S<sub>B</sub>_ of sampled blue elements. Observe that \(y\in S_B\cap B_x\), in fact \(y=min(S_B\cap B_x)\). Because _S<sub>B</sub>_ is the result of uniform sampling, _y_ is biased in the direction expressed in the lemma.

