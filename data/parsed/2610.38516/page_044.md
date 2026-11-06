<tbc>G. Akl et al.<tbc>

## M Fixed-point reweighting instead of exponentiation

This is the half-quadratic / majorize-minimize reweighting of the \(\ell 0\) project applied inside the WS layer. Implementation: `RWLLayer(mode="reweighted")` in `experiments/pw\_layer.py`; base weights exp(-p<sub>0</sub> c), then `outer`=5 steps of

