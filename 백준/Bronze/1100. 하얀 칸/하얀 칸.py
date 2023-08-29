
board = [
    ["W","B","W","B","W","B","W","B"],
    ["B","W","B","W","B","W","B","W"],
    ["W","B","W","B","W","B","W","B"],
    ["B","W","B","W","B","W","B","W"],
    ["W","B","W","B","W","B","W","B"],
    ["B","W","B","W","B","W","B","W"],
    ["W","B","W","B","W","B","W","B"],
    ["B","W","B","W","B","W","B","W"],
    
]

arr = []
answer = 0 
for i in range(8):
    arr.append(input().split())



for i in range(8):
    for j in range(8):
        
        if arr[i][0][j] == 'F' and board[i][j] == "W":
            answer+=1

print(answer)