A few of the variables are related as follows

\(S_{\mathsf{TS},i}=\mathbf{a}\cdot\mathbf{u}_i=\left(\mathbf{a}^{(pq)}+\mathbf{a}^{(r)}\cdot pq\right)\cdot\mathbf{u}_i\)<br>
\(=\left(\underbrace{\mathbf{a}^{(pq)}\cdot\mathbf{u}_i\mathrm{mod}pq}_{\mathrm{mod}pq\mathrm{bits}}+\underbrace{\mathbf{a}^{(pq)}\cdot\mathbf{u}_i-(\mathbf{a}^{(pq)}.\mathbf{u}_i\mathrm{mod}pq)}_{pq}\cdot pq\right)+\left(\underbrace{\mathbf{a}^{(r)}\cdot\mathbf{u}_i}_{\mathrm{remainingbits}}\right)\cdot pq\)<br>
\(=\left(S_{\mathsf{TS},i}^{(pq)}+S_{\mathsf{C},pq,i}\cdot pq\right)+S_{\mathsf{TS},r,i}\cdot pq\)<br>
\(=S_{\mathsf{TS},pq,i}+S_{\mathsf{TS},r,i}\cdot pq.\)

The above sum in the bracket can be split as follows

\(S_{\mathsf{TS},i}=S_{\mathsf{TS},pq,i}+S_{\mathsf{TS},r,i}\cdot pq,\)<br>
\(=\left(S_{\mathsf{TS},i}^{(pq)}+S_{\mathsf{C},pq,i}\cdot pq\right)+S_{\mathsf{TS},r,i}\cdot pq.\)

Then, we redefine \(\mathcal{C}_{ij}^{(\mathrm{int})}=1\) if and only if all the following events occur simultaneously and is 0 otherwise.

1. **u**_<sub>i</sub>,_**u**_<sub>j</sub> survives the Filtering algorithm_, i.e.<tbc>

\(\mathsf{E}_{\mathsf{LS},\mathbf{a},i}^{(p)}:S_{\mathsf{LS},i}^{(p)}\equiv s_0\mathrm{mod}p,\)<br>
\(\mathsf{E}_{\mathsf{LS},\mathbf{a},j}^{(p)}:S_{\mathsf{LS},j}^{(p)}\equiv s_0\mathrm{mod}p,\)<br>
\(\mathsf{E}_{\mathsf{TS},\mathbf{a},i}^{(pq)}:S_{\mathsf{TS},i}^{(pq)}\equiv\beta\mathrm{mod}pq,\)<br>
\(\mathsf{E}_{\mathsf{TS},\mathbf{a},j}^{(pq)}:S_{\mathsf{TS},j}^{(pq)}\equiv\beta\mathrm{mod}pq.\)

2. **u**_<sub>i</sub>,_**u**_<sub>j</sub> collide over the Carries_, i.e.<tbc>

<tbc>\(\mathsf{E}_{\mathsf{C},pq,\mathbf{a},i,j}:S_{\mathsf{C},pq,i}=S_{\mathsf{C},pq,j}.\)<tbc>

3. **u**_<sub>i</sub>,_**u**_<sub>j</sub> collide over the remaining bits_, i.e.<tbc>

<tbc>\(\mathsf{E}_{\mathsf{TS},r,\mathbf{a},i,j}:S_{\mathsf{TS},r,i}=S_{\mathsf{TS},r,j}.\)

<tbc>where \(\beta\equiv s_0+s_1\mathrm{mod}p\) and \(\beta\equiv s_2\mathrm{mod}q\). The first four events make sure that the vectors **u**_<sub>i</sub>_ and **u**_<sub>j</sub>_ survive the filtering algorithm, and the remaining events constraint **u**_<sub>i</sub>_ and **u**_<sub>j</sub>_ to collide over the carry bits and the remaining bits respectively. Here, the reader should observe that the above constraints are sufficient, but not necessary for the collision over integers.

Now, similar to the modular case, we will compute bounds on the first and second moments of the random variable C<sup>(int)</sup> to prove Lemma 7.0.1.

## 7.1.1 First Moment

**Lemma 7.0.2.** _Let M and n be the same as defined in the above problem **ACI-RESS**. Then the following holds for the Algorithm 4_<tbc>

\(\mathbb{E}_\mathbf{a}\left(\mathcal{C}^{(\mathrm{int})}\right)=\Omega\left(\frac{1}{n}\right).\)

