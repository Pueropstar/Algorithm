from sys import stdin

input = stdin.readline

M = int(input())

stack = []


def add(num):
    if(num in stack):
        return
    
    if(type(stack) == type(set())):
        stack.add(num)    
    else:
        stack.append(num)
    
def remove(num):
    if(num not in stack):
        return
    stack.remove(num)

def check(num):
    if(num in stack):
        return 1
    else:
        return 0
    
    
def toggle(num):
    if (num in stack):
        stack.remove(num)
    else:
        if(type(stack) == type(set())):
            stack.add(num)    
        else:
            stack.append(num)
    
def all():
    return set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
def empty():
    return set()
    
for i in range(M):
    command = input().split()
    oper = command[0]
    if (len(command) > 1):
        num = int(command[1])
    if (oper == "add"):
        add(num)
    elif (oper == "remove"):
        remove(num)        
    elif (oper == "check"):
        ans = check(num)
        print(ans)
    elif (oper == "toggle"):
        toggle(num)
    elif (oper == "all"):
        stack = all()
    elif (oper == "empty"):
        stack = empty()
