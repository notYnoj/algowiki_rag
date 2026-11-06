Indeed, the definition of _g_ satisfies (4). Then the size of each cache line is

\(\sum_{i=1}^{t^\prime+1}g_i\le 2g\)

For easy access to this sequence, we can store the entire sequence in auxiliary memory by leveraging how the terms in the sequence do not surpass _g_ allowing us to store each term \(\left\lfloor lgg\right\rfloor+1=O(lglgm)\) bits. For \(t'+1\le t\le lg^*m\) terms this is \(O(lglgm\cdot lg^*m)\) bits, small enough to fit in _O_(1) words as each word is at least l_gm_ bits. Note that this sequence is only stored once for all cache lines as they have identical internal structures, not individually stored for each cache line which would require _O(r_<sub>#</sub>) words.

We now analyze the cost of insert(_x_) for deterministic cache lines. At every iteration, we move _g_<sub>_i_-1</sub> elements from level _i_-1 to level _i_ using \(\left\lceil lg\left(g_i/g_{i-1}\right)\right\rceil\) comparisons and _g_<sub>_i_-1</sub> swaps which are 3_g_<sub>_i_-1</sub> moves. As elements cannot be moved to different levels in any other way, every element passes through every level once. For the _i_th iteration, we calculate the comparison cost per element spread over _g_<sub>_i_-1</sub> elements _C<sub>G</sub>(i_)

\(C_G(i)=\left\lceil lg\left(g_i/g_{i-1}\right)\right\rceil/g_{i-1}\)

By the recursive relationship of (C.5) and (C.7), we have the bounds for \(i\ge 2\)

\(C_G(i)\le lg2^{g_{i-1}/2^{i-1}}/g_{i-1}\)<br> \(\le 1/2^{i-1}\)

Using base cases (C.3) and (C.4), we find the comparison cost of the first iteration

\(C_G(1)\le\left\lceil lgg_1\right\rceil/g_0\)<br> \(\le\left\lceil lg^{(t)}m\right\rceil\)

Summing over all levels, we obtain the final comparison cost for inserting into a deterministic cache line

\(\sum_{i=1}^{t^\prime+1}C_G(i)=C_G(1)+\sum_{i=2}^{t^\prime+1}C_G(i)=\left\lceil lg^{(t)}m\right\rceil+\sum_{i=2}^{t^\prime+1}1/2^{i-1}<lg^{(t)}m+2\)

For every cache block an element passes through, 3 moves are used to swap the element from its previous cache block to its new position in the cache block of the next level. Over \((t'+1)\) cache blocks, the moves for insertion are \(3(t'+1)\). With \(g'_1=\left\lceil lg^{(t)}m\right\rceil\), and \(g'_i=2^{g_{i-1}^\prime}\), by a straightforward induction on the recurrence in (C.5), one can show that for all \(1\le i\le t'\)

\(g_i>g'_i\) (C.8)

We claim that \(t'\le t-1\). If it is not, we have \(t'\ge t\) as \(t'\) must be an integer, then \(g_{t^\prime}>g'_{t^\prime}\ge g'_t=lgm\) by (C.8), but by definition \(g_{t^\prime}<lgm\) in (C.6), giving us a contradiction. Thus, \(t'\le t-1\). This gives us the final bound for inserting into a deterministic cache line of \(3t'\le 3(t-1+1)=3t\) moves.

\(\blacktriangleright\) **Lemma C.2.** _Inserting into a deterministic cache line requires_ l<sup>(_t_)</sup>_m_+2 _comparisons and_ 3_t moves._

