<tbc>of the erasure gates. The erasure gates deployed after applying the _t_’th layer of \(\wedge(x_1,x_2,z)\) gates are each erasing bits that have the value 1 with probability 2<sup>-2_<sup>t</sup>_</sup>. Thus the expected heat release of each of these gates is H<sub>2</sub>(2<sup>-2_<sup>t</sup>_</sup>). Since there are _n/_2_<sup>t</sup>_ such erasure gates in layer _t_, the expected heat released in this layer is (_n/_2_<sup>t</sup>_)H<sub>2</sub>(2<sup>-2_<sup>t</sup>_</sup>). Thus the total expected heat release is<tbc>

\(\sum_{t=0}^{\mathrm{log}(n)-1}\frac{n}{2^t}\mathrm{H}_2(2^{-2^t}).\)

<tbc>Meanwhile the circuit maps a state with _n_ bits of entropy to only H<sub>2</sub>(2<sup>-_n_</sup>) bits of entropy. By Definition 2.25, the circuit entropy production is therefore:

\(\mathsf{EP}_\mathcal{C}=\mathrm{H}_2(2^{-n})-n+\sum_{t=0}^{\mathrm{log}(n)-1}\frac{n}{2^t}\mathrm{H}_2(2^{-2^t})=\sum_{t=1}^{\mathrm{log}(n)}\frac{n}{2^t}\mathrm{H}_2(2^{-2^t})\ge\frac{n}{2}\mathrm{H}_2(1/4).\)

Which is \(\Omega(n)\).

Next we consider the serial circuit where the _i_’th \(\wedge(x_1,x_2,z)\) gate has the AND of the first _i_ inputs as its first argument, _x_<sub>_i_+1</sub> as its second argument, and 0 as its third argument. The circuit then applies erasure gates on the wires containing inputs _x_<sub>1</sub> and _x_<sub>2</sub>. This circuit is illustrated for _n_=4 in Fig. 1. Again these \(\wedge(x_1,x_2,z)\) gates can be implemented with 0 expected heat release under the promise that _z_=0, so the only source of heat release are the erasure gates. There are a total of _n_ erasure gates in this circuit that erase the individual inputs and _n_-2 erasure gates that erase the partial products \(x_1\wedge x_2\) through \(x_1\wedge\dots\wedge x_{n-1}\). Since the inputs are unbiased bits, the expected heat release of these gates is H<sub>2</sub>(1/2)=1 per gate and _n_ across all gates. For the partial product erasures, the _i_’th such gate erases the value of \(x_1\wedge\dots\wedge x_{i+1}\). Again we know that the _x<sub>i</sub>_ are independently and uniformly distributed bits and therefore the _i_’th partial erasure gate is erasing a bit that has the value 1 with probability 2<sup>-_i_-1</sup>. The expected heat release for this gate is therefore H<sub>2</sub>(2<sup>-_i_-1</sup>). Thus our total expected heat release for the circuit is \(n+\sum_{i=1}^{n-2}\mathrm{H}_2(2^{-i-1})\). Since we have the same overall mapping of inputs to outputs as the binary tree case, our change in entropy is H<sub>2</sub>(2<sup>-_n_</sup>)-_n_. This gives us a circuit entropy production of

\(\mathsf{EP}_\mathcal{C}=(\mathrm{H}_2(2^{-n})-n)+n+\sum_{i=1}^{n-2}\mathrm{H}_2(2^{-i-1})=\sum_{i=2}^n\mathrm{H}_2(2^{-i})\le\sum_{i=2}^n2^{-i}(i+\mathrm{log}(e))\le(3+\mathrm{log}(e))/2\)

which is _O_(1).

Another way one could compute the circuit entropy production of these circuits would be to use Proposition D.1 and sum up the drops of mutual information associated with executing each gate. Since the gates we are considering here are each locally optimal, this would give us the same values of EP<sub>C</sub> that we computed here. Doing so is the primary approach used in prior works (i.e. [YYW26]) to produce lower bounds on the local entropy production of circuits. By using heat functions, we can exactly compute the circuit entropy production by only analyzing the local behavior of the individual gates. This lets us ignore more global properties of the circuit like the drops in mutual information, making our approach better suited to analyzing complex circuits where these mutual information terms are hard to quantify.

## 5.2 Batcher’s odd-even mergesort network

We now give bounds on the circuit entropy production of Batcher’s odd-even mergesort network [Bat68]. We note that the Landauer cost of a sorting network acting on bits chosen uniformly<tbc>

