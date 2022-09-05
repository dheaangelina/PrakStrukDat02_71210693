#iterasi
def fibo_iterative(n):
    n1, n2 = 0,1
    for i in range(n):
        n1, n2 = n2, n1 + n2
    return n1
n = 100
hasil_iter = fibo_iterative(n)

import timeit
print("Iterative")
for i in range(1,101):
    start_iter = timeit.default_timer()
    x = fibo_iterative(i)
    end_iter = timeit.default_timer()
    waktu_iter = end_iter-start_iter
    print("n = {}, {:.10f} detik" .format(i, waktu_iter))

#rekursif
def fibo_recursive(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo_recursive(n-1)+ fibo_recursive(n-2)
n = 100
hasil_rec = fibo_recursive(n)

print("Recursive")
for i in range(1,101):
    start_recur = timeit.default_timer()
    x = fibo_recursive(i)
    end_recur = timeit.default_timer()
    waktu_recur = end_recur-start_recur
    print("n = {}, {:.10f} detik" .format(i, waktu_recur))