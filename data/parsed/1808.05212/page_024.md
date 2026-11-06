idx = hget(el);

**if** (idx \>= 0) hhit[idx]++;

**else**

{

idx = rem = el % HLEN;

**if** (!rem) rem++;

**while** (hhit[idx]) idx += rem;

hash[idx] = el;

hhit[idx] = 1;

hsiz++;

}

**void** main(**int** argc, **char** ∗argv[])

{

**int** agc = 0; **char** ∗argv[50];

**int** i, ∗p, pat[LINKS], link[LINKS], alive , dead;

**char** 1, ∗pstr , ∗pend, ∗psave;

**int** mask, omask;

**int** usage, inter , sholnk, echo;

**int** canon, noncanon, silent , dflag;

**char** ∗snenv, title[80];

usage = inter = sholnk = echo = silent = dflag = 0;

canon = noncanon = 0;

// set up shadow argc/argv (agc/agv)

agv[agc++] = strdup(argv[0]);

// check for extra args in SN

**if** ((snenv = getenv("SN")) && snenv[0])

{

**char** s[2000];

sprintf(s, "%s", snenv);

**for** (i = 0; i\<strlen(s); i++) **if** (s[i]==’\t’) s[i] = ’\(\cdot\)’;

**for** (i = strlen(s)-1; i\>0; i--) **if** (s[i]==’\(\cdot\)’ ) s[i]=’\0’; **else break**;

pstr = s;

**while** (∗pstr)

{

**while** (∗pstr == ’\(\cdot\)’) pstr++;

pend = pstr;

**while** (∗pend && (∗pend != ’\(\cdot\)’)) pend++; ∗pend = ’\0’;

agv[agc++] = strdup(pstr);

pstr = pend+1;

}

**for** (i = 1; i \< argc; i++) agv[agc++] = strdup(argv[i]);

pstr = 0;

// check args

**for** (i = 1; i \< agc; i++)

{

**if** (agv[i][0] == ’-’) **switch**(agv[i][1])

// present: tally up

// new: record it

// scan 0x or more for hole

