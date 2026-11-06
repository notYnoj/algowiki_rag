**int** sortbit(**int** a) { **return** ((Bt(bits(a)))-1); }

**int** bitpos(**int** x)

{

**return** (

((x&0xFFFF0000) ? 16:0) +

((x&0xFF00FF00) ? 8:0) +

((x&0xF0F0F0F0) ? 4:0) +

((x&0xCCCCCCC) ? 2:0) +

((x&0xAAAAAAAA) ? 1:0) );

}

**void** stir(**int** x, **int** pbuf[])

{

**int** i, l, r, t;

**for** (i = 0; i \< order; i++) pbuf[i] = i;

**for** (i = order; i \> 1; i--)

{

r = i - 1; l = x % i; x /= i;

**if** (1 != r) { t = pbuf[1]; pbuf[1] = pbuf[r]; pbuf[r] = t; }

}

_// hash operations_

**void** hint()

{

**int** idx;

hsiz = 0;

**for** (idx=0; idx\<HLEN; idx++) hhit[idx] = hash[idx] = 0;

}

**int** hget(ULL el)

{

**int** rem, idx;

idx = rem = el % HLEN;

**if** (!rem) rem++;

**do** {

**if** (!hhit[idx]) **return** -1;

**if** (hash[idx] == el) **return** idx;

idx += rem;

} **while** (idx != rem);

**return** -1;

}

**void** hput(ULL el)

{

**int** rem, idx;

**int** t = el;

**if** (hsiz \>= HLEN) printf("hash\_full!"), exit(0);

