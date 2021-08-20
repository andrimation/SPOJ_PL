list = [
    [".",".",".","."],
    [".",".",".","."],
    [".",".",".","."],
    [".",".",".","."],
]

for element in range(len(list)//2):
    list[element+1][0]= 1

print(list)