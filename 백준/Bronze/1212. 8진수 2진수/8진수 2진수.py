from sys import stdin

input = stdin.readline

N = int(input(),base = 8)

print(bin(N)[2:])