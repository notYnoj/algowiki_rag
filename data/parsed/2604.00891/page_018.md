Input: \((d,G=(V,E),x,y,X_\mathrm{he},Y_\mathrm{he},X_\mathrm{li},Y_\mathrm{li},X_\mathrm{di},Y_\mathrm{di},S_\pi)\) as specified in Lemma 8.<br>
res \(\leftarrow\overrightarrow{\infty}\)<br>
if \(|X_\mathrm{he}\cup X_\mathrm{li}|\le 20\sqrt{d}\) then<br>
return<br>
solve-<br>
\(\pi\)-<br>
r<br>
(<br>
_d,G,_<br>
\(2y+1,X\cup Y\)<br>
)<br>
else<br>
   Use Lemma 2 to compute a set \(\Delta\) of edges such that \(G^\Delta=G+\Delta\) is triangulated<br>
and \((\alpha_\pi d+1)\)-outerplanar<br>
   Use Corollary 1 to find a 3/4-balanced cycle separator C with at most \(2\alpha_\pi d+3\) vertices<br>
in \(G^\Delta\) for the weight functions that assigns 1/|_x_| to each vertex in \(X=X_\mathrm{he}\cup X_\mathrm{li}\).<br>
   Use Lemma 6 with input \(G^\Delta\) and C to compute a set S of separators<br>
   foreach \(C'\in\mathcal{S}\) with partition \((C'_\mathrm{he},C'_\mathrm{li},C'_\mathrm{di})\) do<br>
   Compute \(S_\pi[C'_\mathrm{in}]\) and \(S_\pi[C'_\mathrm{ex}]\) using Requirement R3<br>
   \(\mathrm{res}_1\leftarrow\text{\texttt{red-portals}}(d,C'_\mathrm{in}-\Delta,x,y+1,X_\mathrm{he}[C'_\mathrm{in}],(Y_\mathrm{he}\cup C'_\mathrm{he})[C'_\mathrm{in}],X_\mathrm{li}[C'_\mathrm{in}],(Y_\mathrm{li}\cup C'_\mathrm{li})[C'_\mathrm{in}],X_\mathrm{di}[C'_\mathrm{in}],(Y_\mathrm{di}\cup C'_\mathrm{di})[C'_\mathrm{in}],S_\pi[C'_\mathrm{in}])\)<br>
   \(\mathrm{res}_2\leftarrow\text{\texttt{red-portals}}(d,C'_\mathrm{ex}-\Delta,x,y+2,X_\mathrm{he}[C'_\mathrm{ex}],(Y_\mathrm{he}\cup C'_\mathrm{he})[C'_\mathrm{ex}],X_\mathrm{li}[C'_\mathrm{ex}],(Y_\mathrm{li}\cup C'_\mathrm{li})[C'_\mathrm{ex}],X_\mathrm{di}[C'_\mathrm{ex}],(Y_\mathrm{di}\cup C'_\mathrm{di})[C'_\mathrm{ex}],S_\pi[C'_\mathrm{ex}])\)<br>
   foreach pebble set M for \((B,d,\alpha_\pi,x)\) do<br>
   Compute \(R_\pi(d,G,B,\mathcal{M},S_\pi)\) using Requirement R2<br>
   Use Requirement R4 to compute a solution s(r) for each \(r\in R_\pi(d,G,B,\mathcal{M},S_\pi)\)<br>
based on res<sub>1</sub> and res<sub>2</sub><br>
res(r)=max(res(r),s(r))<br>
return res

• _The input to `solve-`_\(\pi\)_`-r` is a valid instance of_ \(\pi\)-Request _and_ \(x\le 200\mathrm{log}^7(d)-44\mathrm{log}(d)\).<tbc>

• _The input_ \((d,G,x,y,X_\mathrm{he},Y_\mathrm{he},X_\mathrm{li},Y_\mathrm{li},X_\mathrm{di},Y_\mathrm{di},S_\pi)\) _given to `red-portals` satisfies the following:_ \((d,G,x+2y,X_\mathrm{he}\cup Y_\mathrm{he},X_\mathrm{li}\cup Y_\mathrm{li},X_\mathrm{di}\cup Y_\mathrm{di},S_\pi)\) _is a valid instance of_ \(\pi\)-Request, \(d\ge 2^{7\alpha_\pi}\), \(x\le 200\mathrm{log}^7(d)-44\mathrm{log}(d)\)_, y\<_22log(_d),_ \(|X_\mathrm{he}\cup X_\mathrm{li}|\le(3/4)^y\cdot 50d^6\), \(|Y_\mathrm{he}|\le 40(2y)\alpha_\pi\sqrt{d}\)_, and_ \(|Y_\mathrm{li}|\le 60(2y)\alpha_\pi d\mathrm{log}(d)\).<tbc>

• _When `solve-`_\(\pi\)_`-r` with values d_<sub>1</sub> _and z_<sub>1</sub>=_x_<sub>1</sub> _or `red-portals` with values d_<sub>1</sub> _and z_<sub>1</sub>=_x_<sub>1</sub>+2_y_<sub>1</sub> _calls `solve-`_\(\pi\)_`-r` with values d_<sub>2</sub> _and z_<sub>2</sub>=_x_<sub>2</sub> _or `red-portals` with values d_<sub>2</sub> _and z_<sub>2</sub>=_x_<sub>2</sub>+2_y_<sub>2</sub> _and the results are used to combine results, then_ \(z_1\sqrt{d_1}\mathrm{log}(d_1)\le z_2\sqrt{d_2}\mathrm{log}_{d_2}\) _holds._<tbc>

• _The input to `base-case` is a valid instance of_ \(\pi\)-Request _and_ \(d\le 2^{7\alpha_\pi+2}\).

_Proof._ In the following, we show that if the invariant holds in a recursive call, then this recursive call will only invoke recursive calls for which the invariant also holds. Note that the initial call of `solve-`\(\pi\)`-r` fulfills the requirement that the input is a valid instance of \(\pi\)-Request by definition. Since `base-case` does not call any other algorithm, we only need to show that `solve-`\(\pi\)`-r` and `red-portals` maintain the invariants.

## Main Algorithm (`solve-`\(\pi\)`-r`).

We start with recursive calls made in `solve-`\(\pi\)`-r`. To this end, assume that we are in a recursive call of `solve-`\(\pi\)`-r` with input \((d,G,x,B_\mathrm{he},B_\mathrm{li},B_\mathrm{di},S_\pi)\), where \(x\le 200\mathrm{log}^7(d)-22\mathrm{log}(d)\) and \((d,G,(B_\mathrm{he},B_\mathrm{li},B_\mathrm{di}),x,S_\pi)\) corresponds to a valid instance of \(\pi\)-Request. Note that `base-case` is only called in Line 1 and only if the check in Line 1 confirms<tbc>

**Algorithm 2:** `red-portals` (maximization)

