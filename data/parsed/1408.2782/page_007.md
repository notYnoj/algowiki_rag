_Proof._ Suppose a woman _w_ receives proposals in the first iteration of the loop in **QuantileMatch**. If she is matched with one of these suitors when **ProposalRound** terminates, she rejects all other men and receives no further proposals during the current **QuantileMatch**. On the other hand, if she is not matched with one of these suitors after the first round, then by the maximality of the matching found in Step 3 of **ProposalRound**, all of the suitors in her best quantile receiving proposals are matched with other women. Thus, in the next iteration, she only receives proposals from men in strictly worse quantiles than she accepted in the first. Similarly, in each iteration of the loop, her best quantile receiving proposals (if any) is strictly worse than the previous iteration. Therefore, after _k_ iterations, no woman will receive proposals, hence each man _m_ must have \(A^m=\varnothing\).

### 3.4 The ASM algorithm

In this section, we describe the main algorithm **ASM** (Algorithm 3). The idea of **ASM** is to iterate **QuantileMatch** until a large fraction men with high degree are either matched or have been rejected by all acceptable partners. We call such men **_good_**. By iterating **QuantileMatch** a constant number of times, we can ensure that the fraction of good men is close to 1. In order to bound the number of blocking pairs from men which are **_bad_** (not good), we must ensure that bad men comprise only a small fraction of players with relatively high degree. To this end, we only allow men who are potentially involved in many blocking pairs (that is, with |_Q_| relatively large) to participate in later calls to **QuantileMatch**.

**Algorithm 3** \(\text{\textbf{ASM}}(P,\varepsilon,n)\)

\(k\leftarrow\left\lceil 8\varepsilon^{-1}\right\rceil,\delta\leftarrow\varepsilon/8\)

**for all** \(i\le k\) **do**

\(Q_i\leftarrow\{v|q(v)=i\}\)

**end for**

\(Q\leftarrow\bigcup_iQ_i,p\leftarrow\varnothing\)

**for** \(i\leftarrow 0\) to log_n_ **do**

**if** \(|Q|\ge 2^i\) **then**

**for** \(j\leftarrow 1\) to \(2\delta^{-1}k\) **do**

**QuantileMatch**(_Q,k_)

**end for**

**end if**

**end for**

## 4 Performance guarantees

Here we analyze the performance of **ASM** and its subroutines. The run-time guarantee (Theorem 4.7) is a simple consequence of the description of **ASM** and its subroutines. To prove the approximation guarantee (Theorem 4.1), we consider blocking edges from two sets of men separately. We call a man _m **good**_ if when **ASM** terminates, he is either matched or has been rejected by all of his acceptable partners. A man who is not good is **_bad_**. We denote the sets of good and bad men by _G_ and _B_, respectively.

**Theorem 4.1** (Approximation guarantee)**.** The matching _M_ output by **ASM** induces at most \(\varepsilon|E|\) blocking pairs with respect to P. Thus _M_ is \((1-\varepsilon)\)-stable.

### 4.1 Bounding blocking pairs from good players

We bound the number of blocking pairs from good men in two steps. First we show that the good men are not involved in any (2_/k_)-blocking pairs (see Definition 2.3). Next, we show that<tbc>

