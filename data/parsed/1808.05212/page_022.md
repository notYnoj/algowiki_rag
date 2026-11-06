// n-ops are not counting total links properly

// no n-op collision detection in snbin() mode

// snfact() needs (also) to come up with the # of live links.

// broken flag on collision may alwo wish to color links red

// good for 1-32: A-W, use malloc, bit indices

// more extensive iterative mode

// hash array HLEN BIGPRIME

// 101,307,1009,3001,10007,30011,100003,300007,1000003,3000017,

// 10000019,30000001,1000000007,3000000007,1000000007,30000000019

// global structures

ULL hash[HLEN];

int hhit[HLEN];

int hsiz;

// global flags

int xflag = 0;

int wind = 0;

int rflag = 0;

int ascii = 0;

int bw = 0;

// global stats (post run)

ULL gmax; // max swaps

double gavg; // avg swaps

char gpat[MAXL+1]; // match pattern , e.g. "...X...", ";;,...", etc.

double gent[MAXL]; // 0 -\> sorted , ~1 -\> unsorted

ULL gtos; // # of trials conducted (2^n or n! unless monte carlo)

int glo[MAXL];

int ghi[MAXL];

// misc globals

int order = 0;

void snfact(), display();

char ∗getenv();

#define LINKS 600

#define Bt(x) (1ULL\<\<(x))

ULL bits(ULL x) { ULL c = 0; while(x) { c++; x &= x-1; } return c; }

int msb(int x) { while(bits(x) \> 1) x &= x-1; return x; }

int lsb(int x) { return (x & (x-1)) ^ x; }

