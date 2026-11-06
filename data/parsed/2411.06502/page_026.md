**Proof.** First, we want to argue that it is sufficient to demonstrate the following simplified version of the lemma: In time O(_m_) we can find **F**<sub>1</sub>_,...,_**F**_<sub>d</sub>_, all of size at most \(\Delta\), such that \(d=\mathcal{O}(m/\Delta)\) and such that, given the output of the \((w,F_i,F')\)-BBD instance for all \(i\in[1..d]\), we can solve the \((w,F,F')\)-BBD instance in time \(\mathcal{O}(m/\Delta\cdot T_\text{MUL}(m))\). This simplification is sufficient to prove the lemma, as we can apply this lemma to each \((w,F_i,F')\)-BBD instance for \(i\in[1..d]\), this time decomposing \(F'\) (BBD is symmetrical w.r.t. swapping the role of **F** and \(F'\)).

To prove the simplified version of the lemma, we utilize Algorithm 1 (an adaptation of Algorithm 2 from \[Mao22\]) on the \((w,F,F')\)-BBD instance. Algorithm 1 applies recursively Mao’s transitions with the same parameter \(\Delta\) on forests \(H\subseteq F\), until it is left with forests of size at most \(\Delta\). Algorithm 1 assumes that for **H** of size at most \(\Delta\) the output of the \((w,H,F')\)-BBD instance can be retrieved directly (this assumption is equivalent to putting such instances among **F**<sub>1</sub>_,...,_**F**_<sub>d</sub>_).

The correctness of Algorithm 1 follows directly from Lemma 4.6 and Lemma 4.7.

What remains to be demonstrated is a bound on _d_ and on the running time. For that purpose, notice that _d=_O(_t_<sub>I</sub>+_t_<sub>II</sub>) and the running time is bounded by \(\mathcal{O}((t_\mathrm{I}+t_\mathrm{II})\cdot T_\text{MUL}(m))\), where _t_<sub>I</sub>_,t_<sub>II</sub> is the number

**Algorithm 1** Adaptation of Algorithm 2 from \[Mao22\].

**Input:** a forest **H**.

**Output:** answer to the \((w,H,F')\)-BBD instance.

1 // Given a forest **H** containing more than one tree, we write **L**<sub>H</sub> and **R**<sub>H</sub> for the leftmost and rightmost tree, respectively.

2 // Given a forest **H** containing one tree, we write root(**H**) for the root of **H**.

3 if \(|H|\le\Delta\) then

4 As \(|H|\le\Delta\), retrieve directly the answer to the \((w,H,F')\)-BBD instance, and return it;

5 else if **H** _contains more than one tree and_ \(|L_\mathbf{H}|\ge\Delta/3\) _and_ \(|R_\mathbf{H}|\ge\Delta/3\) **then**

6 Via Algorithm 1, get the answer to the \((w,L_\mathbf{H},F')\)-BBD and \((w,H\backslash L_\mathbf{H},F')\)-BBD instances;

7 Via Lemma 4.6 on **L**<sub>H</sub> and **H**\\**L**<sub>H</sub>, get the answer \((w,H,F')\)-BBD instance, and return it;

8 else

9 \(H_s\leftarrow H\);

10 while _true_ do

11 \(H_\text{next}\leftarrow\varnothing\);

12 if **H**_<sub>s</sub> contains only one tree_ **then**

13 \(H_\text{next}\leftarrow H_s\backslash\text{root}(H_s)\);

14 else

15 if |**L**<sub>**H**_<sub>s</sub>_</sub>|_\<_|**R**<sub>**H**_<sub>s</sub>_</sub>| **then**

16 \(H_\text{next}\leftarrow H_s\backslash L_{H_s}\);

17 else

18 \(H_\text{next}\leftarrow H_s\backslash R_{H_s}\);

19 if |**H**|-|**H**next|_\>_2<sub>3</sub>\(\Delta\) **then**

20 break;

21 \(H_s\leftarrow H_\text{next}\);

22 Via Algorithm 1, get the answer to the \((w,H_s,F')\)-BBD instance;

23 As \(|H\backslash H_s|\le\Delta\), retrieve directly the answer to the \((w,H\backslash H_s,F')\)-BBD, \((w,H_\ell,F')\)-BBD, \((w,H_r,F')\)-BBD instances, where \(H_\ell,H_r\) are defined as in Lemma 4.7.

24 Via Lemma 4.7 on **H** and **H**_<sub>s</sub>_, get the answer of the \((w,H,F')\)-BBD instance, and return it;

1 // Given a forest **H** containing more than one tree, we write **L**<sub>H</sub> and **R**<sub>H</sub> for the leftmost and rightmost tree, respectively.

2 // Given a forest **H** containing one tree, we write root(**H**) for the root of **H**.

3 if \(|H|\le\Delta\), retrieve directly the answer to the \((w,H,F')\)-BBD instance, and return it;

5 else if **H** _contains more than one tree and_ \(|L_\mathbf{H}|\ge\Delta/3\) _and_ \(|R_\mathbf{H}|\ge\Delta/3\) **then**

6 Via Algorithm 1, get the answer to the \((w,L_\mathbf{H},F')\)-BBD and \((w,H\backslash L_\mathbf{H},F')\)-BBD instances;

7 Via Lemma 4.6 on **L**<sub>H</sub> and **H**\\**L**<sub>H</sub>, get the answer \((w,H,F')\)-BBD instance, and return it;

8 else

9 \(H_s\leftarrow H\);

10 while _true_ do

11 \(H_\text{next}\leftarrow\varnothing\);

12 if **H**_<sub>s</sub> contains only one tree_ **then**

13 \(H_\text{next}\leftarrow H_s\backslash\text{root}(H_s)\);

14 else

15 if |**L**<sub>**H**_<sub>s</sub>_</sub>|_\<_|**R**<sub>**H**_<sub>s</sub>_</sub>| **then**

16 \(H_\text{next}\leftarrow H_s\backslash L_{H_s}\);

17 else

18 \(H_\text{next}\leftarrow H_s\backslash R_{H_s}\);

19 if |**H**|-|**H**next|_\>_2<sub>3</sub>\(\Delta\) **then**

20 break;

21 \(H_s\leftarrow H_\text{next}\);

22 As \(|H\backslash H_s|\le\Delta\), retrieve directly the answer to the \((w,H\backslash H_s,F')\)-BBD, \((w,H_\ell,F')\)-BBD, \(((w,H_r,F')\)-BBD instances, where \(H_\ell,H_r\) are defined as in Lemma 4.7.

24 Via Lemma 4.7 on **H** and **H**_<sub>s</sub>_, get the answer of the \((w,H,F')\)-BBD instance, and return it;

