**if** ((1 == '-') || (1 == '='))

{

**if** (mask==0) fprintf(stderr,"bad\_leading\_char\_’%c’\backslash n", 1),exit(-2);

**if** (bits(mask)==1) fprintf(stderr,"only\_one\_char\backslash n" ), exit(-2);

_// canonicity check_

**if** ( canon &

((mask & omask) == 0) && (lsb(omask) \> lsb(mask)) ) exit(1);

omask = mask;

**if** (1 == '-') { \*p++ = mask; mask = 0; }

**else**

{

**int** mask2 = 0;

**for** (i=0; i\<order; i++) **if** (mask&Bt(i)) mask2 |= Bt(order-i-1);

**if** ((mask & mask2) && (mask == mask2)) \*p++ = mask | mask2;

**else** { \*p++ = mask; \*p++ = mask2; }

}

mask = 0;

}

**else** if ((’1’ \<= 1) && (1 \<= ’9’)) mask |= Bt(1 - ’1’);

**else** if ((’A’ \<= 1) && (1 \<= ’V’)) mask |= Bt(1 + 9 - ’A’);

**else** fprintf(stderr,"bad\_character\_’%c’\backslash n", 1), exit(-2);

}

\*p = 0;

**if** (mask) fprintf(stderr,"no\_trailing\_’-’\_or\_’=’\backslash n"), exit(-2);

**if** (noncanon) exit(1); // non-canonical if links out of order

