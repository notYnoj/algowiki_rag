Using<tbc>

\(\frac{1}{g_L(t)}=\alpha_Lmax\{\sigma,t\},\)

<tbc>we obtain<tbc>

\(\mathbb{E}[Z^2|W=w]=2\alpha_L\int_0^umax\{\sigma,t\}dt.\)

<tbc>If \(u\le\sigma\), then<tbc>

\(\mathbb{E}[Z^2|W=w]=2\alpha_L\sigma u\le\alpha_L(\sigma^2+u^2),\)

<tbc>by the inequality \(2ab\le a^2+b^2\).<br>
If \(u\ge\sigma\), then<tbc>

\(\mathbb{E}[Z^2|W=w]=2\alpha_L\left(\int_0^\sigma\sigma dt+\int_\sigma^utdt\right)\)<br>
\(=2\alpha_L\left(\sigma^2+\frac{u^2-\sigma^2}{2}\right)=\alpha_L(\sigma^2+u^2).\)

<tbc>Thus, in all cases,<tbc>

\(\mathbb{E}[Z^2|W=w]\le\alpha_L\big(\sigma^2+(|w|\wedge L)^2\big)=\alpha_L\big(\sigma^2+([|w|]_L)^2\big).\)

<tbc>Taking expectations gives<tbc>

\(\mathbb{E}[Z^2]\le\alpha_L\big(\sigma^2+\mathbb{E}\big[([|W|]_L)^2\big]\big).\)

<tbc>Since \(([|W|]_L)^2\le W^2\) and \(\mathbb{E}[W^2]\le 2\sigma^2\), we conclude that<tbc>

\(\mathbb{E}[Z^2]\le\alpha_L(\sigma^2+2\sigma^2)=3\alpha_L\sigma^2.\)

<tbc>Therefore

\(Var(Z)\le\mathbb{E}[Z^2]\le 3\alpha_L\sigma^2.\)

_Proof of (iii)._ Since \(Y\in\{0,1\}\),

\(|Z|=\left|\frac{2S}{g_L(T)}Y\right|\le\frac{2}{g_L(T)}=2\alpha_Lmax\{\sigma,T\}\le 2\alpha_LL,\)

because \(T\in[0,L]\).

## B.3 Proof of Lemma 4 (Clipping bias)

_Proof._ For every real _w_,<tbc>

\(|w-[w]_L|=(|w|-L)_+.\)

<tbc>Also, for every \(x\ge 0\),<tbc>

\((x-L)_+\le\frac{x^2}{4L}.\)

<tbc>Indeed, the inequality is trivial when \(x\le L\). If _x\>L_, then<tbc>

\(x-L\le\frac{x^2}{4L}\Longleftrightarrow 0\le(x-2L)^2.\)

<tbc>Applying this with _x_=|_W_|, we get<tbc>

\(|W-[W]_L|=(|W|-L)_+\le\frac{W^2}{4L}.\)

<tbc>Therefore

\(\big|\mathbb{E}[W]-\mathbb{E}[[W]_L]\big|=\big|\mathbb{E}[W-[W]_L]\big|\le\mathbb{E}\big[|W-[W]_L|\big]\le\frac{\mathbb{E}[W^2]}{4L}\le\frac{\sigma^2}{2L},\)

since \(\mathbb{E}[W^2]\le 2\sigma^2\).

