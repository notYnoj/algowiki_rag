Ordered by hand
Declared, sorted by the graph
def square(x):
# Each function, named by what it writes;
return x**2
# its parameters already name what it reads.
def offset(x, a):
# Declared in the reverse of their run order.
return a + x
model = flat.declare(
def disc1(b, y2):
flat.function(objective, 'f'),
flat.function(damping, 'c'),
return b 0.2 * y2
flat.function((constraint, 'g'),
def constraint(y1):
return 3.16 - y1
flat.function(offset, 'b'),
flat.function(square, 'a'),
)
def penalty(g):
return jnp.maximum(g, 0.0)**2
def run_cottax(x, y2):
out = flat.run(model, {Inputs: dict(x=x, y2=y2)})
def damping(h, y2):
return h * jnp.exp(-y2)
return out['f'], out['g']
def objective(a, y1, c):
return a + y1 + c
def run_manual(x, y2):
a = square(x)
b = offset(x, a)
y1 = disc1(b, y2)
g = constraint(y1)
h = penalty(g)
c = damping(h, y2)
f = objective(a, y1, c)
return f, g
# Traced from types, not values: a scalar float64 each.
x = y2 = jax.ShapeDtypeStruct((), jnp.float64)
jaxpr_manual = jax.make_jaxpr(run_manual)(x, y2)
jaxpr_cottax = jax.make_jaxpr(run_cottax)(x, y2)
assert str(jaxpr_manual) == str(jaxpr_cottax)
print(jaxpr_cottax)
{ lambda ; a:f64[] b:f64[]. let
c:f64[] = integer_pow[y=2] a
d:f64[] = add c a
e:f64[] = mul 0.2:f64[] b
f:f64[] = sub d e
g:f64[] = sub 3.16:f64[] f
h:f64[] = max g 0.0:f64[]
i:f64[] = integer_pow[y=2] h
j:f64[] = neg b
k:f64[] = exp j
l:f64[] = mul i k
m:f64[] = add c f
n:f64[] = add m 1
in (n, g) }

Figure 21: The same acyclic model ordered by hand (left) and declared in `cottax` and ordered by the graph (right). Both trace to the identical `jaxpr`, printed at the bottom.

