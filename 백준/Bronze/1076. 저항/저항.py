list = [
    "black","brown","red","orange","yellow",
    "green","blue","violet","grey","white"
]


money = ""
for i in range(3):
    color = input()
    index = str(list.index(color))
    if i <2:
        money+=index
    else:
        money = int(money)*10**list.index(color)
        
print(money)