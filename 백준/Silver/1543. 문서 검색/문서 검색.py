from sys import stdin

input = stdin.readline

source_str = input().split('\n')[0]

target_str = input().split('\n')[0]

count = 0
    
copy_source = source_str


while (target_str in copy_source):
    copy_source = copy_source.replace(target_str,'=')

print(copy_source.count('='))