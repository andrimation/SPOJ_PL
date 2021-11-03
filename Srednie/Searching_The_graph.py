# Stworzyć algorytm - albo DFS albo BFS który mając określony graf, będzie przechodził po wszystkich elementach
# grafu zaczynając od wskazanego wierzchołka. -> to są chyba grafy skierowane, że jakiś wierzchołek może
# być czyimś sąsiadem, ale ten drugi wierzchołek nie musi być jego ?

# Czyli że np algorytm idzie po wierzchołkach będących sąsiadami jednego wierzchołka "1" -> czyli 1,2,3,4,5,6
# i jeśli np 6 nie ma sąsiadów, to wraca do wierchołka 2 i sprawdza czy ma jakichś nieodwiedzonych sąsiadów.
# Jeśli ma nie odwiedzonych np 2 sąsiadów, to idzie do tego z mniejszą liczbą ( czy na pewno tak ma być ? )
# później wraca znów do 2 i znów sprawdza czy ma sąsiadów nieodwiedzonych. Jeśli nie, to idzie do 3 i sprawdza czy 3 ma nieodwiedzonych
# sąsiadów itd.

# graf ma postać słownika z zagnieżdzoną lista  graph[1] = [2,3,4], graph[2] = [3,6,7] itp

# sys zaimplementuję później

# Znacznik odwiedzenia True/False umieszczam na końcu listy sąsiadów każdego vertexa.


def visitVertexDFS(graph, actualVertex):
    visitList[actualVertex] = True
    print(int(actualVertex), end=" ")
    if graph[actualVertex] == []:
        # print(actualVertex)
        return
    else:
        for neighbour in graph[actualVertex]:
            # print(neighbour,"Sąsiad")
            if visitList[neighbour] == False:
                # steps.append(1)
                visitVertexDFS(graph, neighbour)

# Algorytm BFS działa trochę inaczej - nie odwiedzamy rekurencyjnie wszystkich sąsiadów jakiegoś vertex-a jak leci, ale jak wejdziemy w jakiś vertex
# To wchodzimy we wszystkich jego sąsiadów, ale nie wchodzimy od razu w sąsiadów - tych sąsiadów, czyli najpierw zaznaczamy jako odwiedzonych
# sąsiadów 1 stopnia. Następnie dopiero odwiedzamy sąsiadów kolejnego stopnia

def visitVertexBFS(graph, actualVertex):
    queue = []  # Samo .pop(0)  zabiera pierwszy element z listy, a append dodaje element na końcu listy -> czyli mamy kolejkę
    visitList[actualVertex] = True
    queue.append(actualVertex)
    while queue:
        actualVertex = queue.pop(0)
        visitList[actualVertex] = True
        print(actualVertex,end=" ")
        for element in graph[actualVertex]:
            if visitList[element] == False:
                queue.append(element)
                visitList[element] = True

# Main

testCounter = int(input())
graphCounter = 1
for test in range(testCounter):
    graphVertices = int(input())
    graph = {}
    print("graph ",graphCounter)
    for inputLine in range(graphVertices):
        vertex = input().split()
        graph[vertex[0]] = [x for x in vertex[2:]]

    question = list(input().split())
    while question != ['0', '0']:
        visitList = {key: False for key in graph.keys()}
        if question[1] == '1':
            visitVertexBFS(graph, question[0])
        else:
            visitVertexDFS(graph, question[0])
        print()
        question = list(input().split())
    graphCounter += 1





