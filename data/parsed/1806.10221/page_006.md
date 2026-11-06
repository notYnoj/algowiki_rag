## SUPPLEMENTARY INFORMATION: A NOVEL QUANTUM N-QUEENS SOLVER ALGORITHM AND ITS SIMULATION AND APPLICATION TO SATELLITE COMMUNICATION USING IBM QUANTUM EXPERIENCE

The QASM code of the quantum circuit used in the simulation of our protocol for _N_=4 in IBM Quantum Experience is presented below.

<sup>4</sup> OPENQASM 2.0;<br>
include "qelib1.inc";<br>
<sup>5</sup> qreg qr[25];<br>
creg cr[25];<br>
<sup>6</sup> #Hadamards required for preparation of W-states in each block before the computation starts

<sup>7</sup> h qr[0];<br>
h qr[3];<br>
h qr[4];<br>
h qr[7];<br>
h qr[8];<br>
h qr[11];<br>
h qr[12];<tbc>

