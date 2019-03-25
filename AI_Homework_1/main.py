import pygame
from AI_Homework_1.Circle import *
from AI_Homework_1.Point import *
from AI_Homework_1.SweepLine import getIntersections
import time

def computerMove(circle1: 'Circle', circle2: 'Circle', circles: list):
    if circle2.center.x >= circle1.center.x and circle2.center.y >= circle1.center.y:
        tempX = circle2.center.x - circle1.center.x
        newX = circle1.center.x - tempX
        tempY = circle2.center.y - circle1.center.y
        newY = circle1.center.y - tempY
        newCircle = Circle(Point(newX, newY), circle2.radius)
        newCircle.movable = False
        circles.append(newCircle)
    if circle2.center.x <= circle1.center.x and circle2.center.y >= circle1.center.y:
        tempX = circle1.center.x - circle2.center.x
        newX = circle1.center.x + tempX
        tempY = circle2.center.y - circle1.center.y
        newY = circle1.center.y - tempY
        newCircle = Circle(Point(newX, newY), circle2.radius)
        newCircle.movable = False
        circles.append(newCircle)
        #newCircle = Circle(Point(circle2.center.x, -circle2.center.y), circle2.radius)
    if circle2.center.x >= circle1.center.x and circle2.center.y <= circle1.center.y:
        tempX = circle2.center.x - circle1.center.x
        newX = circle1.center.x - tempX
        tempY = circle1.center.y - circle2.center.y
        newY = circle1.center.y + tempY
        newCircle = Circle(Point(newX, newY), circle2.radius)
        newCircle.movable = False
        circles.append(newCircle)
        #newCircle = Circle(Point(-circle2.center.x, circle2.center.y), circle2.radius)
    if circle2.center.x <= circle1.center.x and circle2.center.y <= circle1.center.y:
        tempX = circle1.center.x - circle2.center.x
        newX = circle1.center.x + tempX
        tempY = circle1.center.y - circle2.center.y
        newY = circle1.center.y + tempY
        newCircle = Circle(Point(newX, newY), circle2.radius)
        newCircle.movable = False
        circles.append(newCircle)

        #newCircle = Circle(Point(circle2.center.x, circle2.center.y), circle2.radius)
    return circles

def isOnTable(circle: 'Circle') -> bool:
    c3 = Circle(Point(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), 200)

    return c3.radius > Point.euclidean_distance_2D(c3.center, circle.center) + circle.radius
# === CONSTANS === (UPPER_CASE names)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

BLOCK_SIZE = 50
CIRCLE_RADIUS = int(BLOCK_SIZE / 2)

# === CLASSES === (CamelCase names)

'''
class Button():
'''

# === FUNCTIONS === (lower_case names)

# empty

# === MAIN === (lower_case names)

# --- (global) variables ---

# --- init ---

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_rect = screen.get_rect()

# --- objects ---

'''
button = Button(...)
'''

circles = []
c1 = Circle(Point(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), CIRCLE_RADIUS)
c1.movable = False
print(c1)
c2 = Circle(Point(CIRCLE_RADIUS, CIRCLE_RADIUS), CIRCLE_RADIUS)

circles.append(c1)
circles.append(c2)

rects = []
rects.append(pygame.Rect(SCREEN_WIDTH // 2 - CIRCLE_RADIUS, SCREEN_HEIGHT // 2 - CIRCLE_RADIUS, BLOCK_SIZE, BLOCK_SIZE))
rects.append(pygame.Rect(0, 0, BLOCK_SIZE, BLOCK_SIZE))

selected = None

# --- mainloop ---

clock = pygame.time.Clock()
is_running = True
moves_counter = 1

while is_running:
    # --- events ---

    for event in pygame.event.get():

        # --- global events ---

        if event.type == pygame.QUIT:
            is_running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            selected = None
            if event.button == 1:
                for i, r in enumerate(circles):
                    # Pythagoras a^2 + b^2 = c^2
                    dx = r.center.x - event.pos[0]  # a
                    dy = r.center.y - event.pos[1]  # b
                    distance_square = dx ** 2 + dy ** 2  # c^2

                    if distance_square <= CIRCLE_RADIUS ** 2:  # c^2 <= radius^2
                        selected = i
                        selected_offset_x = r.center.x - event.pos[0]
                        selected_offset_y = r.center.y - event.pos[1]

        elif event.type == pygame.MOUSEBUTTONUP:
            if selected is not None and circles[selected].movable:
                moves_counter += 1
                if len(getIntersections(circles)) > 0 or not isOnTable(circles[selected]):
                    print("Computer wins")
                    is_running = False
                    time.sleep(2)
                if is_running:
                    circles[selected].movable = False
                    circles = computerMove(circles[0], circles[selected], circles)
                    circles.append(Circle(Point(CIRCLE_RADIUS, CIRCLE_RADIUS), CIRCLE_RADIUS))
                if event.button == 1:
                    selected = None

        elif event.type == pygame.MOUSEMOTION:
            if selected is not None and circles[selected].movable:  # selected can be `0` so `is not None` is required
                # move object
                circles[selected].center.x = event.pos[0] + selected_offset_x
                circles[selected].center.y = event.pos[1] + selected_offset_y

        # --- objects events ---

        '''
       button.handle_event(event)
       '''

    # --- updates ---

    # empty

    # --- draws ---

    screen.fill(BLACK)


    pygame.draw.circle(screen, GREEN, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), 200)
    '''
    button.draw(screen)    
    '''

    # draw rect
    for i, r in enumerate(circles):
        if i % 2:
            pygame.draw.circle(screen, RED, (r.center.x, r.center.y), r.radius)
        else:
            pygame.draw.circle(screen, WHITE, (r.center.x, r.center.y), r.radius)

    pygame.draw.line(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))
    pygame.draw.line(screen, WHITE, (0, SCREEN_HEIGHT // 2), (SCREEN_WIDTH, SCREEN_HEIGHT // 2))
    pygame.display.update()

    # --- FPS ---

    clock.tick(25)

# --- the end ---
pygame.quit()