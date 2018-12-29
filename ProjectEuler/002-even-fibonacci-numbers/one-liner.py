print(sum(i in list(map((lambda n : n if n < 2 else fib(n-1) + fib(n-2)), range(4000000))) if i % 2 == 0))
