### E.3 Proof of Proposition 7.0.2

Consider a set \(R_{\alpha,c}:=\{(a,b)\in[m]^2|a,b\ge\alpha m,a+b\le m,|a-b|\le c\sqrt{m}\}\). Let _S_ denote the above-mentioned sum in the problem. We can rewrite it as follows

\(S=\sum_{t_1=\alpha m}^m\sum_{t_2=\alpha m}^{m-t_1}\genfrac(){pt}{2}{m}{t_1}\genfrac(){pt}{2}{m-t_1}{t_2}2^{m-(t_1+t_2)}\)<br>
\(=\sum_{(t_1,t_2)\in R_{\alpha,c}}\frac{m!}{t_1!t_2!t_3!}1^{t_1}\cdot 1^{t_2}\cdot 2^{t_3}\)<br>
\(=4^m\cdot\sum_{(t_1,t_2)\in R_{\alpha,c}}\frac{m!}{t_1!t_2!t_3!}\genfrac(){pt}{2}{1}{4}^{t_1}\cdot\genfrac(){pt}{2}{1}{4}^{t_2}\cdot\genfrac(){pt}{2}{1}{2}^{t_3}.\)

Let _X_<sub>1</sub>_,X_<sub>2</sub>, and _X_<sub>3</sub> be three random variables that follows multinomial distribution with _m_ repetitions and probabilities 1/4, 1/4, and 1/2 respectively. Then, using the p.m.f. of the multinomial distribution in the above equation, we have the following<tbc>

\(S=4^m\cdot\mathbb{P}\left((X_1,X_2)\in R_{\alpha,c}\right).\)

<tbc>Since, E(_X_<sub>1</sub>)=E(_X_<sub>2</sub>)=_m/_4, Var(_X_<sub>1</sub>)=Var(_X_<sub>2</sub>)=3_m/_16 and \(\alpha<1/4\), using Chebyshev inequality, we get<tbc>

\(\mathbb{P}\left(X_1<\alpha m,X_2<\alpha m\right)=\mathcal{O}\left(\frac{1}{m}\right).\)

<tbc>Now, let _D=X_<sub>1</sub>-_X_<sub>2</sub>, then we have E(_D_)=0 and Var(_D_)=3_m/_16. Then, again by using Chebyshev inequality, we have

\(\mathbb{P}(|D|>c\sqrt{m})\le\frac{1}{2c^2}.\)

Then, using the union bound, we get the desired result.

## References

