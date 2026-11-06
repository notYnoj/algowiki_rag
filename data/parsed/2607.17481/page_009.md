<tbc>random projections [3, 7], and truncated Fourier features [1, 11, 27], maintained online per window across all lengths.

## 6 Conclusion

Panache replaces the _L_ fixed-length self-joins of PMP motif discovery with one streaming pass. Every written cell is an exact distance to a valid neighbor, and the benchmark shows full top-20 recovery at the lowest wall time. The limitation is memory. Features, signatures, hash metadata, samples, and profile rows grow linearly with the stream (35.5 GB at 5M samples). Future work will address memory as a binding resource and a GPU implementation.

## References

