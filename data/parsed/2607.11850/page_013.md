void nfss\_sort(double[] array) {<br>
// find minimum and maximum values in the array<br>
double min, max;<br>
(min, max) = array.getMinAndMax();<br>
// initialize helper array for scatter step<br>
double[] helper\_array = new double[C];<br>
nfss\_core(array, helper\_array, array.start, array.end, min, max, 0);<br>
insertion\_sort(array);<br>
}<br>
void nfss\_core(<br>
double[] array,<br>
double[] helper\_array,<br>
int array\_start,<br>
int array\_end,<br>
double min,<br>
double max,<br>
int pathological\_recursion\_counter<br>
} {<br>
// calculate array basic information<br>
int array\_size = array\_end - array\_start;<br>
double interval = max - min;<br>
double inverse\_interval = 1.0 / interval;<br>
int bucket\_number;<br>
int[] bucket\_offsets;<br>
// Decide on strategy and bucket number based on array size<br>
if (array\_size \> 5000000) {<br>
bucket\_number = 2000;<br>
bucket\_offsets = IPSo\_inspired\_fragment\_scatter(array, helper\_array, array\_start, array\_end, min, max, bucket\_number, inverse\_interval);<br>
} else if (array\_size \> 1000000) {<br>
bucket\_number = 1000;<br>
bucket\_offsets = IPSo\_inspired\_fragment\_scatter(array, helper\_array, array\_start, array\_end, min, max, bucket\_number, inverse\_interval);<br>
} else if (array\_size \> 500000) {<br>
bucket\_number = 200;<br>
bucket\_offsets = IPSo\_inspired\_fragment\_scatter(array, helper\_array, array\_start, array\_end, min, max, bucket\_number, inverse\_interval);<br>
} else if (array\_size \> 10000) {<br>
bucket\_number = 100;<br>
bucket\_offsets = IPSo\_inspired\_fragment\_scatter(array, helper\_array, array\_start, array\_end, min, max, bucket\_number, inverse\_interval);<br>
} else {<br>
bucket\_number = minimum(6500, array\_size);<br>
bucket\_offsets = naive\_scatter(array, helper\_array, array\_start, array\_end, min, max, bucket\_number, inverse\_interval);<br>
}<br>
// calculate interval size and "bad" critical mass<br>
double interval\_size = interval / (bucket\_number - 1);<br>
double critical\_mass = \(\alpha\) \* array\_size;<br>
// decide what to do with each bucket based on bucket size<br>
for (int i = 0; i \< bucket\_number; i++) {<br>
int bucket\_start = array\_start + bucket\_offsets[i];<br>
int bucket\_end = array\_start + bucket\_offsets[i + 1];<br>
int bucket\_size = bucket\_end - bucket\_start;<br>
// insertion sort at the end will handle these buckets<br>
if (bucket\_size \<= small\_threshold) continue;<br>
// pathological buckets that have hardly lost any mass<br>
if (bucket\_size \> critical\_mass) {<br>
// we try a fixed number of times with recursion,<br>
// and if it doesn't work we fall back on some other efficient sort<br>
if (pathological\_recursion\_counter \< 1) {<br>
nfss\_core(array, helper\_array, bucket\_start, bucket\_end,<br>
min + interval\_size \* i,<br>
min + interval\_size \* (i + 1),<br>
pathological\_recursion\_counter + 1);<br>
} else {<br>
fallback\_sort(array, bucket\_start, bucket\_end);<br>
}<br>
} else {<br>
nfss\_core(array, helper\_array, bucket\_start, bucket\_end,<br>
min + interval\_size \* i,<br>
min + interval\_size \* (i + 1),<br>
0);<br>
}<br>
}<br>
}<br>
}<br>
}

**Listing 1: Naive NFS Sort**

