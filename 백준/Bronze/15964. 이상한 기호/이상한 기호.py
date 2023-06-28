def func(a,b):

    answer = (a+b)*(a-b)
    return answer


a,b = map(int, input().split())


print(func(a,b))
