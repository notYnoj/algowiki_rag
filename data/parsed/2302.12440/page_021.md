On the other hand,

\(I(X;Q^m,Y^m)=\sum_{i\ge 1}\mathbb{P}[m\ge i]I(X;Q_i,Y_i|Q^{i-1},Y^{i-1},m\ge i)\text{(chain rule of mutual information)}\)<br>
\(=\sum_{i\ge 1}\mathbb{P}[m\ge i]I(X;Y_i|Q_i,Q^{i-1},Y^{i-1},m\ge i)\)<br>
\((Q_i\text{and}X\text{are independent conditioned on}(Q^{i-1},Y^{i-1}))\)<br>
\(\le\sum_{i\ge 1}\mathbb{P}[m\ge i]I(X,Q_i,Q^{i-1},Y^{i-1};Y_i|m\ge i)\text{(chain rule)}\)<br>
\(=\sum_{i\ge 1}\mathbb{P}[m\ge i]I(X,Q_i;Y_i|m\ge i)\)<br>
\(((Q^{i-1},Y^{i-1})\text{and}Y_i\text{are independent conditioned on}(X,Q_i))\)<br>
\(=\sum_{i\ge 1}\mathbb{P}[m\ge i]\left(H(Y_i|m\ge i)-H(Y_i|X,Q_i,m\ge i)\right)\text{(2)}\)

Let \(q_i=\mathbb{P}[Y_i=*|m\ge i]\). Because the algorithm makes at most _n-n/k_ queries between elements in the same group, we have

\(\sum_{i\ge 1}\mathbb{P}[m\ge i]q_i\le n-n/k.\)

We have

\(H(Y_i|m\ge i)\le h\left(q_i,\frac{1-q_i}{2},\frac{1-q_i}{2}\right)\)

and

\(H(Y_i|X,Q_i,m\ge i)=0\cdot q_i+h(p)(1-q_i).\)

Note that \(H(Y_i|m\ge i)\le\mathrm{log}3\) trivially, so by Equation (2), \(I(X;Q^m,Y^m)\le\mathrm{log}3\cdot\sum_{i\ge 1}\mathbb{P}[m\ge i]=\mathrm{log}3\cdot\mathbb{E}[m]\). Combining with Equation (1), we have \(\mathbb{E}[m]=\Omega(n\mathrm{log}n)\).

Note that \(g(x):=h(x,\frac{1-x}{2},\frac{1-x}{2})\) is concave in _x_, so

\(\sum_{i\ge 1}\mathbb{P}[m\ge i]H(Y_i|m\ge i)\le\left(\sum_{i\ge 1}\mathbb{P}[m\ge i]\right)g\left(\frac{\sum_{i\ge 1}\mathbb{P}[m\ge i]q_i}{\sum_{i\ge 1}\mathbb{P}[m\ge i]}\right)\text{(Jensen’s inequality)}\)<br>
\(\le\mathbb{E}[m]\cdot g\left(\mathrm{min}\left\{\frac{1}{3},\frac{n-n/k}{\mathbb{E}[m]}\right\}\right)\)<br>
\((g\text{is increasing on}[0,\frac{1}{3}]\text{and is maximized at}\frac{1}{3})\)<br>
\(=(1+o(1))\mathbb{E}[m].\text{(}n=o(\mathbb{E}[m])\text{)}\)

