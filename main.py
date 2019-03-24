from Graph import *

v1 = City(1, 0, 0, {2: 2, 3: 3, 4: 4})
v2 = City(2, 3, 0, {1: 2, 6: 1, 4: 5})
v3 = City(3, 2.5, 3, {1: 3})
v4 = City(4, 3, 2.5, {1: 4, 2: 5, 5: 2, 7: 3})
v5 = City(5, 1.5, 6.5, {4: 2, 7: 6})
v6 = City(6, 8, 0, {2: 1, 7: 8})
v7 = City(7, 9, 7.5, {4: 3, 5: 6, 6: 8})

print(2 + City.euclideanDistance2D(v2, v7))
print(3 + City.euclideanDistance2D(v3, v7))
print("__")
graph = Graph()
graph.addCity(v1)
graph.addCity(v2)
graph.addCity(v3)
graph.addCity(v4)
graph.addCity(v5)
graph.addCity(v6)
graph.addCity(v7)

graph.Astar(v1, v7)
