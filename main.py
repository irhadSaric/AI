from Graph import *

def euclidean(a, b):
    return sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)


v1 = City(1, 0, 0, {2: -2, 3: 3, 4: 4})
v2 = City(2, 3, 0, {1: -2, 6: -1, 4: 5, 3: 1})
v3 = City(3, 2.5, 3, {1: 3, 2: 1, 8: 1})
v4 = City(4, 3, 2.5, {1: 4, 2: 5, 5: 2, 7: 3})
v5 = City(5, 1.5, 6.5, {4: 2, 7: 0.5})
v6 = City(6, 8, 0, {2: -1, 7: -8})
v7 = City(7, 9, 7.5, {4: 3, 5: 0.5, 8: 1, 6: -8})
v8 = City(8, 9, 0, {7: 1, 1: 8})

graph = Graph()
graph.addCity(v1)
graph.addCity(v2)
graph.addCity(v3)
graph.addCity(v4)
graph.addCity(v5)
graph.addCity(v6)
graph.addCity(v7)
graph.addCity(v8)

for grad in graph.cities:
    for susjed in graph.cities[grad].neighbours:
        graph.cities[grad].neighbours[susjed] = City.euclideanDistance2D(graph.cities[grad], graph.cities[susjed])
        #print(grad, susjed, City.euclideanDistance2D(graph.cities[grad], graph.cities[susjed]))
#print("-------")
for grad in graph.cities:
    print(grad, "8", City.euclideanDistance2D(graph.cities[grad], v8))
#print("***")

graph.Astar(v1, v8)
