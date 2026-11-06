### Demonstration of BNRS

In order to understand the BNRS sorting, We demonstrate the sorting with a sample input, where _A_=\[24,125,620,124,5\]. The parameters are: _n_=5 and _k_=620. The number of rounds required is \(\lfloor log_5620\rfloor+1=4\).

_Round 1 (divisor n_<sup>0</sup>=1)

- Input Array: `\[24, 125, 620, 124, 5\]`<tbc>

- Digit Extraction (\(\lfloor A[i]/1\rfloor\) (mod 5)):<tbc>

- 24 (mod 5)=4<tbc>

- 125 (mod 5)=0<tbc>

- 620 (mod 5)=0<tbc>

- 124 (mod 5)=4<tbc>

- 5 (mod 5)=0<tbc>

- Digits for Sorting: `\[4, 0, 0, 4, 0\]`<tbc>

- Resultant Array (after applying counting sort): `\[125, 620, 5, 24, 124\]`<tbc>

_Round 2 (divisor n_<sup>1</sup>=5)

- Input Array: `\[125, 620, 5, 24, 124\]`<tbc>

- Digit Extraction (\(\lfloor A[i]/5\rfloor\) (mod 5)):<tbc>

- \(\lfloor 125/5\rfloor\) (mod 5)=25 (mod 5)=0<tbc>

- \(\lfloor 620/5\rfloor\) (mod 5)=124 (mod 5)=4<tbc>

- \(\lfloor 5/5\rfloor\) (mod 5)=1 (mod 5)=1<tbc>

- \(\lfloor 24/5\rfloor\) (mod 5)=4 (mod 5)=4<tbc>

- \(\lfloor 124/5\rfloor\) (mod 5)=24 (mod 5)=4<tbc>

- Digits for Sorting: `\[0, 4, 1, 4, 4\]`<tbc>

- Resultant Array: `\[125, 5, 620, 24, 124\]`<tbc>

_Round 3 (divisor n_<sup>2</sup>=25)

- Input Array: `\[125, 5, 620, 24, 124\]`<tbc>

- Digit Extraction (\(\lfloor A[i]/25\rfloor\) (mod 5)):<tbc>

- \(\lfloor 125/25\rfloor\) (mod 5)=5 (mod 5)=0<tbc>

- \(\lfloor 5/25\rfloor\) (mod 5)=0 (mod 5)=0<tbc>

- \(\lfloor 620/25\rfloor\) (mod 5)=24 (mod 5)=4<tbc>

- \(\lfloor 24/25\rfloor\) (mod 5)=0 (mod 5)=0<tbc>

- \(\lfloor 124/25\rfloor\) (mod 5)=4 (mod 5)=4<tbc>

- Digits for Sorting: `\[0, 0, 4, 0, 4\]`<tbc>

- Resultant Array: `\[125, 5, 24, 620, 124\]`<tbc>

