# this is DISGUSTING but dammit, it works
print(sum([i for i in list(map(lambda n: (lambda f, *a: f(f, *a))(lambda rec, n: n if n < 2 else rec(rec, n-1) + rec(rec, n-2), n), range(34))) if i % 2 == 0]))
