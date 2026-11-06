where

\(R'_s=\left\{(u'_1,u'_2):\forall j\in s,a_j<u'_j<b_j\forall j\notin s,b_j<u'_j<1\right\}\)

This defines the region \(R'_s\) to be the one where the coordinates with indices in \(s\in S\) lie within their boundaries, and the other coordinates exceed them. We can see that this division of the square forms a nonoverlapping cover of \(C'\), i.e. \(\cap_{s\in S}R'_s=\emptyset\) and \(\bigcup_{s\in S}R'_s=C'\). In order to map into these sets without disrupting the probability distribution, we need to know the relative volumes of these regions. We see that for region \(R'_s\), its volume is \(V_{R_s^\prime}=\prod_{j\in s}(b_j-a_j)\prod_{k\notin s}(1-b_k)\). Furthermore, the volume of the region we cut out of the unit square to create the region \(C'\) is \(V_\mathrm{out}=\prod_{j=1}^2(1-b_j)\), so we know that the total volume of region \(C'\) is \(V_{C^\prime}=1-V_\mathrm{out}\). Thus, the fraction of the total volume which is occupied by \(R'_s\) is \(f_s=\frac{V_{R_s^\prime}}{V_{C^\prime}}\) . Because we are working with a uniform distribution, we need this fraction to be the probability that our final uniform sample came from region \(R'_s\).

We want to start with a uniform draw over an unrestricted unit square which we will call _C_. Call the coordinates of this sample (_u_<sub>1</sub>_,u_<sub>2</sub>), where \(\forall i\in\{1,2\},0<u_i<1\). We need to find a mapping from _C_ to \(C'\) which preserves the relative probabilities of falling into the regions \(R'_s\). To do this, we can cut along coordinate _u_<sub>2</sub> to create three regions _R<sub>s</sub>_ with volumes _f<sub>s</sub>_ in our new space so that we can map region _R<sub>s</sub>_ into \(R'_s\) and preserve this probability. Thus, in our unrestricted space, we can define:<tbc>

\(R_s=\{(u_1,u_2):0<u_1<1;\sum_{j=1}^{s-1}f_j<u_2<\sum_{j=1}^sf_j\}\)

<tbc>so that the total volume of _R<sub>s</sub>_ is _f<sub>s</sub>_. Once we have this division, it is easy to create the mapping from _R<sub>s</sub>_ to \(R'_s\): \(g_s(u_j)=u'_j\) where

\(g_s(u_j)=\left\{(b_j-a_j)u_j+a_j\text{if}j\in s,j=1\frac{b_j-a_j}{f_s}(u_j-\sum_{l=1}^{s-1}f_l)+a_j\text{if}j\in s,j=2(1-b_j)u_j+b_j\text{if}j\notin s,j=1\frac{1-b_j}{f_s}(u_j-\sum_{l=1}^{s-1}f_l)+b_j\text{if}j\notin s,j=2\right.\)

where the function _g<sub>s</sub>(u<sub>j</sub>_) indicates that this _g<sub>s</sub>_ is only to be used to map between points in _R<sub>s</sub>_ and \(R'_s\), where \((u_1,u_2)\in R_s\) if \(\sum_{j=1}^{s-1}f_j<u_2<\sum_{j=1}^sf_j\). Define the final mapping to be _g(u_<sub>1</sub>_,u_<sub>2</sub>)=(_g<sub>s</sub>(u_<sub>1</sub>)_,g<sub>s</sub>(u_<sub>2</sub>)) when \((u_1,u_2)\in R_s\).

