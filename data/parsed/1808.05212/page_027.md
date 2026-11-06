i = 0;

p = &pat[0];

**if** (!silent&&sholnk)

**while** (\*p++) printf("%d\_%g\\n", i+1, (double)(link[i])/gtos), i++;

// _quit_

exit(0);

}

**void** snfact(**int** pin[], **int** plink[])

{

**int** gfit[64];

**int** \*p;

**int** perm[MAXL];

**int** i, lx, k, t, l, r, q;

ULL ifact, swaps, maxswaps, avgswaps;

**int** tmp, swapped;

**double** entro = 0.0;

// _clear link stats_

i = 0; p = &pin[0]; **while** (\*p++) plink[i++] = 0;

// _run all patterns_

ifact = 1; **for** (i=1; i\<=order; i++) ifact \*= i;

**if** (rflag) ifact = BIGPRIME;

**for** (i=0; i\<order; i++) gfit[i] = 0;

**for** (i=0; i\< MAXL; i++) glo[i] = 100;

**for** (i=0; i\< MAXL; i++) ghi[i] = -1;

maxswaps = avgswaps = 0;

**for** (i=0; i\<ifact; i++)

{

**int** match = 0;

swaps = 0;

p = &pin[0];

lx = 0;

**if** (rflag) stir((**int**)((((**long**)i)\*RANDX)%BIGPRIME), perm);

**else** stir(i, perm);

**while** (t = \*p++)

{

swapped = 0;

l = bitpos(lsb(t));

**while** (t &= t-1)

{

r = 1;

l = bitpos(lsb(t));

**if** (perm[1] \< perm[r])

{

tmp = perm[1]; perm[1] = perm[r]; perm[r] = tmp;

**if** (swapped)

{

fprintf(stderr,"link\_#%d\_(%d,%d)\_collision\\npattern:\_",

