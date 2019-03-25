from queue import PriorityQueue
from collections import deque
from AI_Homework_1.Circle import *
from AI_Homework_1.Point import *


def getIntersections(circlesList: list) -> bool:
    priorityQueue = PriorityQueue()
    Deque = deque()
    listOfIntersections = set()

    for circle in circlesList:
        priorityQueue.put(EventPoint("s", Point(circle.center.x - circle.radius, circle.center.y), circle))
        priorityQueue.put(EventPoint("e", Point(circle.center.x + circle.radius, circle.center.y), circle))

    while not priorityQueue.empty():
        eventPoint = priorityQueue.get()
        if eventPoint.eventType == "s":
            currentcircle = eventPoint.circleIdentifier
            for circle in Deque:
                if circle.intersects(currentcircle, circle):
                    listOfIntersections.add(circle)
                    listOfIntersections.add(currentcircle)
            Deque.appendleft(currentcircle)
        else:
            if Deque.__len__() != 0:
                Deque.pop()

    return listOfIntersections