in which the open circle at common link joint indicates non-interference.

## Cost Benefits

The 2-op exchange on three elements yields immediate gains in lowering costs of traditional networks. For example, Paeth [1990] described a median on a 3x3 box, formed by column, row and (single) diagonal sorting, first conceived as a means to reuse column sorts when filtering a large raster image.

\(\text{\texttt{+---+ |1 2 3 | by col s3(1,4,7) s3(2,5,8) s3(3,6,9) |4 5 6 | by row s2(1,2,3) s3(4,5,6) s2(7,8,9) |7 8 9 | diagonal s3(3,5,7) ---+ ---+ s3(a,b,c) (original) is s2(a,b) s2(b,c) s2(a,b) s3(a,b,c) (reworked) is s2(a,c) s2(a,b) s2(b,c)}\)

Column reuse aside, the method leads to efficient median (19 links) and sorting (25) on nine element arrays. In 21 links we find minimum, maximum and median, deletion and inclusion lead both to bare median (19) full sorted (25) forms.

