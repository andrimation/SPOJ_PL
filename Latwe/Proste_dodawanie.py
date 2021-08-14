counter = int(input())
listOfLists = []

for q in range(counter):
    small_counter = int(input())
    listOfLists.append(list(map(int,input().split())))


for nawias in listOfLists:
    print(sum(nawias))
