<tbc>correctly on well-scaled data, where native DGEMM rounds only a few percent of the entries correctly, and it is orders of magnitude more accurate under cancellation. The same pipeline provides ZGEMM through an exact 3M scheme with 3_s_ instead of 4_s_ INT8 products. On Xe2 the decisive implementation choices were to keep FP64 out of the memory-bound kernels, to use an exact, division-free CRT with an FP32 quotient, and to adapt the tiling to the behaviour of the vendor INT8 GEMM. Future work includes measurements on Xe3P hardware, transparent interposition into existing electronic-structure codes, batched and small-matrix variants, and the reuse of the residues of _A_ across calls.

##  and data availability

The library is available at `https://github.com/MacraMacra/OS2-Xe` under the MIT license. It is header-only and consists of `ozaki2\_gpu.hpp` and the table of moduli `coprime\_tables.hpp`; the repository also contains the correctness tests, usage examples, and the throughput and accuracy benchmarks.

## Acknowledgements

This work was supported by Latvian Council of Science via Latvian State Research Programme Nr. VPPIZM-CERN-2022/1-0001.

## References

