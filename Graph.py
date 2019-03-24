from City import *
from queue import PriorityQueue


class Graph():
    def __init__(self):
        self.cities = dict()

    def addCity(self, city: 'City'):
        self.cities[city.id] = city

    def Astar(self, startCity: 'City', resultCity: 'City'):
        priorityQueue = PriorityQueue()
        priorityQueue.put(startCity)
        cityBefore = dict()
        visited = dict()

        for n in self.cities:
            visited[self.cities[n]] = False

        print(visited)

        while not visited[resultCity] and not priorityQueue.empty():
            currentCity = priorityQueue.get()
            print("Visiting: ", currentCity.id)
            if not visited[currentCity]:
                visited[currentCity] = True
                for neighbour in self.cities[currentCity.id].neighbours:
                    if not visited[self.cities[neighbour]]:
                        self.cities[neighbour].currentValue += self.cities[neighbour].neighbours[currentCity.id] + City.euclideanDistance2D(self.cities[neighbour], resultCity)
                        cityBefore[self.cities[neighbour]] = currentCity
                        priorityQueue.put(self.cities[neighbour])

        if visited[resultCity]:
            print("Goal city reached")
            currentCity = resultCity
            while currentCity.id != startCity.id:
                print(cityBefore[currentCity].id)
                currentCity = cityBefore[currentCity]
        else:
            print("Goal city was not reached")