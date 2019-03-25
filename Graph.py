from City import *
from queue import PriorityQueue


class Graph():
    def __init__(self):
        self.cities = dict()

    def addCity(self, City: 'City'):
        self.cities[City.id] = City

    def Astar(self, startCity: 'City', resultCity: 'City'):
        priorityqueue = PriorityQueue()
        Citybefore = dict()
        opendict = dict()
        closeddict = dict()

        startCity.currentvalue = City.euclideanDistance2D(startCity, resultCity)
        priorityqueue.put(startCity) #open list
        opendict[startCity] = startCity

        while not priorityqueue.empty():
            currentCity = priorityqueue.get()
            closeddict[currentCity] = currentCity
            try:
                del opendict[currentCity]
            except KeyError:
                pass

            try:
                if closeddict[resultCity]:
                    break
            except KeyError:
                pass

            for neighbourid in currentCity.neighbours:
                neighbour = self.cities[neighbourid]

                try:
                    if closeddict[neighbour]:
                        continue
                except KeyError:
                    pass

                try:
                    if opendict[neighbour]:
                        if neighbour.currentvalue > currentCity.currentvalue + currentCity.neighbours[neighbour] + City.euclideanDistance2D(neighbour, resultCity):
                            neighbour.currentvalue = currentCity.currentvalue + currentCity.neighbours[neighbour] + City.euclideanDistance2D(neighbour, resultCity)
                            Citybefore[neighbour] = currentCity
                except KeyError:
                    #print(currentCity.neighbours[neighbourid])
                    neighbour.currentvalue = currentCity.currentvalue + currentCity.neighbours[neighbourid] + City.euclideanDistance2D(neighbour, resultCity)
                    Citybefore[neighbour] = currentCity
                    priorityqueue.put(neighbour)
                    opendict[neighbour] = neighbour

        while resultCity.id != startCity.id:
            print(resultCity.id, end=", ")
            resultCity = Citybefore[resultCity]
        print(resultCity.id)
