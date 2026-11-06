potentially forcing \(|\tilde{y}^{(j-1)}|\neq\alpha b\).<tbc>

\(\bullet\) If \(j\notin\mathcal{I}_{\genfrac(){pt}{2}{y^{(1)},\dots,y^{(B)}}{(y^{(1)},\dots,y^{(B)})}}^\mathrm{exc}\), then let \(|\tilde{y}^{(k)}|=\alpha b\) for all \(k\in\{i+1\dots,j-1\}\) (this set is empty if _j=i_+1) and set \(\tilde{y}^{(j)}\) accordingly so that<tbc>

<tbc>\(y^{(1)}\dots y^{(j)}=\tilde{y}^{(1)}\dots\tilde{y}^{(j)},\)<tbc>

<tbc>potentially forcing \(|\tilde{y}^{(j)}|\neq\alpha b\).

We continue similarly until we have constructed all of \(\varphi_y\big(y^{(1)},\dots,y^{(B)}\big)=\big(\tilde{y}^{(1)},\dots,\tilde{y}^{(B)}\big)\).

It is clear from Definition 3.10 that the map (3.18) preserves the key inductive condition (3.19). We now confirm that it is well-defined (i.e., maps to NE<sub>std</sub>(_y_)). We let<tbc>

\(\big(y^{(i+1)},\dots,y^{(j)}\big)\)

<tbc>denote a maximal consecutive sequences of blocks processed between successive stopping points of the standardization algorithm. In the case where \(j\in\mathcal{I}_{\genfrac(){pt}{2}{y^{(1)},\dots,y^{(B)}}{(y^{(1)},\dots,y^{(B)})}}^\mathrm{exc}\), it follows from Definition 3.10 that \(|(j-1)-(i+1)+1|\le b^\epsilon\) and that for all \(k\in\{i+1,\dots,j-1\}\), it holds that<tbc>

\(|y^{(k)}|\in\big[(1-\delta)\alpha b,(1+\delta)\alpha b\big].\)

<tbc>Thus, the total amount that we shift the index of the last endpoint as we construct the mapping of strings<tbc>

\(\big(y^{(i+1)},\dots,y^{(j-2)}\big)\rightarrow\big(\tilde{y}^{(i+1)},\dots,\tilde{y}^{(j-2)}\big)\)

<tbc>is readily observed to be bounded by

\((b^\epsilon-2)\cdot\delta\alpha b\le b^\epsilon\cdot\delta\alpha b=^\text{(3.4)}\alpha b^{1/2+2\epsilon}\le^\text{(b large)}\big(\alpha\wedge(1-\alpha)\big)b.\) (3.21)

Since \(j-1\notin\mathcal{I}_{\genfrac(){pt}{2}{y^{(1)},\dots,y^{(B)}}{(y^{(1)},\dots,y^{(B)})}}^\mathrm{exc}\), we may thus define \(\tilde{y}^{(j-1)}\) in such a way (i.e., by contracting or extending _y_<sup>(_j_-1)</sup> accordingly) that \(|\tilde{y}^{(j-1)}|\in\{0,\dots,b\}\) and (3.20) holds. The analysis for the case in which \(j\notin\mathcal{I}_{\genfrac(){pt}{2}{y^{(1)},\dots,y^{(B)}}{(y^{(1)},\dots,y^{(B)})}}^\mathrm{exc}\) is effectively identical. Finally, it readily follows that the number of strings \(\tilde{y}^{(k)}\) such that \(|\tilde{y}^{(k)}|\neq\alpha b\) is at most

\(\left(\underbrace{2\gamma}_{2\cdot\big|\mathcal{I}_{\genfrac(){pt}{2}{y^{(1)},\dots,y^{(B)}}{(y^{(1)},\dots,y^{(B)})}}+\underbrace{b^{-\epsilon}}_\text{possible modification every}b^\epsilon\text{strings}\right)B=^\text{(3.4)}3\gamma B.\)

Altogether, this discussion demonstrates that

\(\varphi_y\big(y^{(1)},\dots,y^{(B)}\big)=\big(\tilde{y}^{(1)},\dots,\tilde{y}^{(B)}\big)\in\mathcal{N}\mathcal{E}_\text{std}(y),\)

and we conclude that the standardization algorithm of Definition 3.10 is indeed well-defined.

The standardization algorithm of Definition 3.10 should be thought of as an approximation algorithm in the following sense. We will use it to produce a uniform approximation-type bound of the form

\(\frac{1}{B}\sum_{i=1}^BA_\text{loc}\big(X'^{(i)},Y^{(i)}\big)\le\frac{1}{B}\sum_{i=1}^BA_\text{loc}\big(X'^{(i)},\tilde{Y}^{(i)}\big)+\frac{\beta^\star(\alpha)}{2}\le^\text{(3.6)}T_\text{std}(X',Y)+\frac{\beta^\star(\alpha)}{2},\) (3.22)

where \(\big(Y^{(1)},\dots,Y^{(B)}\big)\in\mathcal{N}\mathcal{E}_\text{ind}(Y)\), we have that

\(\varphi_Y\big(Y^{(1)},\dots,Y^{(B)}\big)=\big(\tilde{Y}^{(1)},\dots,\tilde{Y}^{(B)}\big)\in\mathcal{N}\mathcal{E}_\text{std}(Y),\)

