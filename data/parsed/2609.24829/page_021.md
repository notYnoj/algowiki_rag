We conclude with the following lower bound on parameter-free triangle estimation in the random order data stream model.

**Theorem 5.4** (Data Stream Lower Bound)**.** _Let_ \(\alpha>1\) _and_ \(\beta>0\) _satisfy_ \(\beta<\sqrt{m/2}\) _and_ \(2(\alpha+1)\beta<m/4\)_. Let_ A _be a one-pass, parameter-free algorithm that returns an_ \((\alpha,\beta)\)_-approximation of T with failure probability_ 1_/m_<sup>4</sup> _when the stream is in random order. Then_ A _may require_ \(\Omega(m/\sqrt{\beta})\) _space even when run on an input for any T\<m/_4.

_Proof._ We will use A to establish a communication complexity protocol for \(\mathrm{TOLTRITEST}_{\tau_1,\tau_2}\) when \(\tau_1=2\beta\) and \(\tau_2>2(\alpha+1)\beta\). Specifically, Alice runs A on a random permutation of her edges and then sends the memory state to Bob who instantiates A with the communicated memory state and continues running the algorithm on a random permutation of his edges. Note that the overall random permutation of the stream is random because Alice received each edge independently with probability _p_. We next argue that even though A only returns an \((\alpha,\beta)\) approximation, this is sufficient to determine the value of \(\mathrm{TOLTRITEST}_{\tau_1,\tau_2}\) on the input graph. Hence, by appealing to Theorem 5.1, the algorithm must use \(\Omega(m/\sqrt{\tau_1})\) bits of memory even when there are \(\tau_2\) triangles.

If _T_=0, any \((\alpha,\beta)\) approximation is at most \(\beta\). If \(T_1=\tau_1\), any \((\alpha,\beta)\) approximation is at least \(\tau_1\) and at most \(\tau_1\alpha+\beta\). If \(T_2\ge\tau_2\) then, any \((\alpha,\beta)\) approximation is at least \(\tau_2\). Hence, if

\(\beta<\tau_1\text{and}\alpha\tau_1+\beta<\tau_2\)

then an \((\alpha,\beta)\) approximation is sufficient to distinguish between graphs with 0 triangles, \(\tau_1\) triangles, and at least \(\tau_2\) triangles. This is the case since \(\tau_1=2\beta\) and \(\tau_2>2(\alpha+1)\beta\).

Essentially, this means that any parameter-free algorithm that provides a multiplicative approximation for all values of _T_ is forced to use \(\Theta(m)\) space, even on streams where the actual triangle count is moderately large. More generally, if the algorithm is only required to work when \(T\ge\beta\), then \(\Omega(m/\sqrt{\beta})\) space is still necessary. At a high level, before the algorithm can infer that _T_ is large, it must still be capable of distinguishing between 0 and \(\beta\) triangles, and that already requires \(\Omega(m/\sqrt{\beta})\) space.

## References

