boxHu = boxHd = boxVr = boxVl = "+";

}

**if** (bw)

{

cred = cgrn = cyel = cblu = cpur = ccyn = cltw = cwhi = cbld = cnrm;

}

lnum = 0; p = &pt[0]; **while**(∗p++) lnum++;

lpen = lmin = gtos;

**for** (j = 0; j \< lnum; j++) **if** (lk[j] && (lk[j] \< lmin)) lmin = lk[j];

**for** (j = 0; j \< lnum; j++) **if** (lk[j] && (lk[j] \> lmin) && (lk[j] \< lpen))

lpen = lk[j];

**if** ((lpen∗2) \>= gtos) { lpen = lmin; lmin = 0; }

_// top line_

dsplen = ((lnum\<HALFIHRESH) ? 3:1)∗lnum+10; _// 10 for body line margin junk_

tmargin = Max(dsplen, strlen(anno)) - strlen(anno);

bmargin = Max(dsplen, strlen(anno)) - dsplen;

bwidth = bmargin + dsplen;

printf("%s", cbord);

printf("%s",boxDR);

**for** (j=0; j\<bwidth; j++) printf("%s",boxH); printf("%s\\n",boxDL);

printf("%s",boxV); printf("%s", anno);

**for** (j=0; j \< tmargin; j++) printf("\_");

printf("%s\\n", boxV);

printf("%s",boxVr);

**for** (j=0; j\<bwidth; j++) printf("%s",boxh); printf("%s\\n",boxVl);

printf("%s", cnrm);

**for** (i=0; i\<order; i++)

{

printf("%s%%s\_%C\_>", cbord,boxV,cnrm, (i\>8)?i-9+’A’:i+’1’);

p = &pt[0];

**for** (j=0; j \< lnum; j++)

{

**char** ∗s, t[20];

**int** l, r;

**int** m = ∗p++;

r = bitpos(lsb(m));

l = bitpos(msb(m));

s = boxh;

sprintf(t,"%s%s%s", chorz, s, chorz);

_// feature control_

**if** ((r \<= i) && (i \<= l))

{

s = boxv;

**if** (l == i) s = boxHd;

**if** (r == i) s = boxHu;

