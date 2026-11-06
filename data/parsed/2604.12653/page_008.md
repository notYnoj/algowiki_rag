\(log(1+|a(x_i)-a(x_{i-1})|)\le log(1+t_i-a(x_i))+log(1+t_{i-1}-a(x_{i-1}))+log(1+t_i-t_{i-1})\)<br>
\(\le log(1+t_i-a(x_i))+log(1+t_{i-1}-a(x_{i-1}))+t_i-t_{i-1}\)

In the unified bound (Definition 1), we will use _y=x_<sub>_i_-1</sub> for _x=x<sub>i</sub>_. By the unified bound, the total cost to execute _S_ is

\(t+1+\sum_{i=2}^k\big(1+log(b(x_i)-b(x_{i-1}))+log|a(x_i)-a(x_{i-1})|\big)\)<br>
\(\le t+1+k+\sum_{i=2}^k(t_i-t_{i-1})+\sum_{i=2}^k\big(log(1+t_i-a(x_i))+log(1+t_{i-1}-a(x_{i-1}))\big)\)<br>
\(\le t+1+k+2\sum_{i=1}^klog(1+t_i-a(x_i))+t,\)

which is the total time to execute _S_ as claimed by Lemma 8.

## 3 Analyzing `UniTopSort`

In this section, we show:

**Theorem 4.** _**UniTopSort** has O(n+m_) _preprocessing time and O_(log_e(G_)+_n_) _sorting time._

The only preprocessing step in `UniTopSort` is computing a topological ordering of _G_. This takes _O(n+m_) time using a textbook algorithm. In the sorting phase of `UniTopSort`, every item in _X_ gets inserted and extracted exactly once. We assign every \(x\in X\) two numbers \(a(x),b(x)\in[1,n]\) as in Definition 1. Then, we associate to every item _x_ the open interval \((\ell(x),r(x))\subseteq[0,2n]\), where _r(x_)=_a(x_)+_b(x_) and \(\ell(x)=max\big(0,max_{y:a(y)<a(x)\wedge b(y)<b(x)}(a(y)+b(y))\big)\).

**Lemma 9.** _The_ \(x\leftarrow\text{extractMin}()\) _operation has an amortized running time of_ \(O(1+log(r(x)-\ell(x)))\).

_Proof._ Intuitively, this follows from the fact that the definition of \(\ell(x)\) takes the maximum over a smaller set compared to the unified bound. Formally, let \(y_0=argmax_{y:a(y)<a(x)\wedge b(y)<b(x)}(a(y)+b(y))\). Suppose first that _y_<sub>0</sub> does not exist (i.e. because there are no valid items _y_). Then \(\ell(x)=0\). If _x_ is the very first item extracted, then by the unified bound, the extractMin operation takes _O_(1) time. Otherwise, let _y_ be an arbitrary item extracted before _x_. By the unified bound, the extractMin operation that returns _x_ takes _O_(log|_a(x_)-_a(y_)|+log|_b(x_)-_b(y_)|) time. Since<tbc>

\(log|a(x)-a(y)|+log|b(x)-b(y)|\le loga(x)+logb(x)\le 2log(a(x)+b(x))=2log(r(x)-\ell(x)).\)

<tbc>This shows the lemma. Suppose now that _y_<sub>0</sub> exists. Then \(\ell(x)=a(y_0)+b(y_0)\), and also _a(y_<sub>0</sub>)_\<a(x_) and _b(y_<sub>0</sub>)_\<b(x_). In the unified bound (Definition 1), we could pick _y=y_<sub>0</sub>, hence the extractMin operation that returns _x_ takes _O_(log(_a(x_)-_a(y_))+log(_b(x_)-_b(y_))) amortized time. Since

\(log|a(x)-a(y)|+log|b(x)-b(y)|\le 2log(a(x)+b(x)-a(y)-b(y))=2log(r(x)-\ell(x)),\)

this shows the lemma.

