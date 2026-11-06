<tbc>log<sup>2</sup>(_n_)). Pipelined sorting networks \[10\] have the same cost as our proposal, and offer a fixed latency of around _n/_2 for the full array to be sorted, instead of our elastic latency of \(log(n)\rightarrow n+log(n)\) for the first and last elements respectively.

## VI. CONCLUSION

Sorting algorithms come in all shapes and sizes. In the general case, the limit of \(\mathcal{O}(n\cdot log(n))\) comparisons cannot be lowered, so trade-offs between speed and resource use need to be considered.

Efforts have been made towards fully serial or fully parallel architectures, with a distinct lack of PISO and SIPO approaches in the literature. These are particularly useful when the throughput at the input or output is limited.

A very simple and lightweight implementation of a PISO sorter is presented. It uses O(_n_) resources and is capable of outputting the first sorted element in log(_n_) cycles, streaming the rest in exactly _n_. Its frequency does not drop with size, as the critical paths are constrained within single processing elements, which makes it ideal for scalable applications.

The implementation has been successfully integrated within a BP+OSD decoder in the context of quantum LDPC coding, proving its capabilities in real-world applications such as real- time decoding of error-correcting codes.

## ACKNOWLEDGMENT

This work was supported in part by the project PID2023-147059OB-I00 funded by MCIU/ AEI/ 10.13039/501100011033/ FEDER, UE.

## REFERENCES

**Daniel Bácones** received the bachelor’s degree in both mathematics and computer science and the M.Sc. degree in computer science from the Complutense University of Madrid, Madrid, Spain, in 2016 and 2018, respectively. He was a Research Associate during the time of his M.Sc. with the Department of Computer Architecture and Automatics. His main interests include hyperspectral image compression on field-programmable gate arrays, dealing with fast lossless algorithms that aid with data transmission and more complex lossy algorithms for

long-term storage, a field in which he obtained his Ph.D thesis in 2020.

**Borja Morcillo** received the bachelor and M.Sc. degrees in computer engineering from the Complutense University of Madrid (Madrid, Spain), in 2020 and 2022, respectively. In 2020 he was awarded winner of the Xilinx Open Hardware Design Competition. He is currently a Teaching Assistant (Department of Computer Architecture and Automation, Complutense University of Madrid), while pursuing the Ph.D. degree in hardware design. His main research interests include computer architecture and reconfigurable hardware.

\begin{tabular}{cccccc}
Input & LUT & REG & CARRY8 & Freq & Latency \\
1024x8 & 28132 & 27630 & 1023 & 705MHz & 10+1024 \\
512x8 & 14052 & 13806 & 511 & 705MHz & 9+512 \\
256x8 & 7012 & 6894 & 255 & 705MHz & 8+256 \\
128x8 & 3492 & 3438 & 127 & 705MHz & 7+128 \\
64x8 & 1732 & 1710 & 63 & 705MHz & 6+64 \\
1024x16 & 48592 & 52190 & 1023 & 649MHz & 10+1024 \\
512x16 & 24272 & 26078 & 511 & 649MHz & 9+512 \\
256x16 & 12112 & 13022 & 255 & 649MHz & 8+256 \\
128x16 & 6032 & 6494 & 127 & 649MHz & 7+128 \\
64x16 & 2992 & 3230 & 63 & 649MHz & 6+64 \\
1024x32 & 89002 & 101310 & 2046 & 613MHz & 10+1024 \\
512x32 & 44458 & 50622 & 1022 & 613MHz & 9+512 \\
256x32 & 22186 & 25278 & 510 & 613MHz & 8+256 \\
128x32 & 11050 & 12606 & 254 & 613MHz & 7+128 \\
64x32 & 5482 & 6270 & 126 & 613MHz & 6+64 \\
\end{tabular}





TABLE I

RESULTS FOR DIFFERENT CONFIGURATIONS

