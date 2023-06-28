a,b = map(int, input().split())

array = [False, False] + [True] * b

primes = []

for i in range(2,b+1):

    if array[i]:

        primes.append(i)

        for j in range(2*i, b+1, i):
            array[j] = False

for i in primes:
    if(i>=a):
        print(i)