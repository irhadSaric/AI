import random

import pygame


def add_neighbours(Deque, optimal_move_x, optimal_move_y):
    pass


class Board:
    def __init__(self, matrix):
        self.matrix = matrix
        self.hits = 0
        self.list_of_hits = []
        self.moves = 0

    def display(self, screen):
        BLUE = (0, 0, 255)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)
        YELLOW = (255, 255, 0)

        for i in range(10):
            for j in range(10):
                if self.matrix[i][j].ship_placed and self.matrix[i][j].visited:
                    pygame.draw.rect(screen, YELLOW, self.matrix[i][j].rect)
                elif self.matrix[i][j].visited:
                    pygame.draw.rect(screen, GREEN, self.matrix[i][j].rect)
                elif self.matrix[i][j].ship_placed:
                    pygame.draw.rect(screen, BLUE, self.matrix[i][j].rect)
                else:
                    pygame.draw.rect(screen, RED, self.matrix[i][j].rect, 1)

    def random_place_carrier(self):
        horizontal = random.randint(0, 1)
        if horizontal:
            x = random.randint(0, 9)
            y = random.randint(0, 5)
            for i in range(y, y + 5):
                self.matrix[x][i].ship_placed = True
        else:
            x = random.randint(0, 5)
            y = random.randint(0, 9)
            for i in range(x, x + 5):
                self.matrix[i][y].ship_placed = True

    def _is_valid_placement(self, x, y, ship_length, horizontal):
        if self.matrix[x][y].ship_placed:
            return False
        else:
            if horizontal:
                for i in range(y, y + ship_length):
                    if self.matrix[x][i].ship_placed:
                        return False
                return True
            else:
                for i in range(x, x + ship_length):
                    if self.matrix[i][y].ship_placed:
                        return False
                return True

    def random_place_battleship(self):
        horizontal = random.randint(0, 1)
        if horizontal:
            x = random.randint(0, 9)
            y = random.randint(0, 6)
            if self._is_valid_placement(x, y, 4, True):
                for i in range(y, y + 4):
                    self.matrix[x][i].ship_placed = True
            else:
                x = random.randint(0, 9)
                y = random.randint(0, 6)
                while not self._is_valid_placement(x, y, 4, True):
                    x = random.randint(0, 9)
                    y = random.randint(0, 6)
                for i in range(y, y + 4):
                    self.matrix[x][i].ship_placed = True
        else:
            x = random.randint(0, 6)
            y = random.randint(0, 9)
            if self._is_valid_placement(x, y, 4, False):
                for i in range(x, x + 4):
                    self.matrix[i][y].ship_placed = True
            else:
                x = random.randint(0, 6)
                y = random.randint(0, 9)
                while not self._is_valid_placement(x, y, 4, False):
                    x = random.randint(0, 6)
                    y = random.randint(0, 9)
                for i in range(x, x + 4):
                    self.matrix[i][y].ship_placed = True

    def random_place_submarine(self):
        horizontal = random.randint(0, 1)
        if horizontal:
            x = random.randint(0, 9)
            y = random.randint(0, 7)
            if self._is_valid_placement(x, y, 3, True):
                for i in range(y, y + 3):
                    self.matrix[x][i].ship_placed = True
            else:
                x = random.randint(0, 9)
                y = random.randint(0, 7)
                while not self._is_valid_placement(x, y, 3, True):
                    x = random.randint(0, 9)
                    y = random.randint(0, 7)
                for i in range(y, y + 3):
                    self.matrix[x][i].ship_placed = True
        else:
            x = random.randint(0, 7)
            y = random.randint(0, 9)
            if self._is_valid_placement(x, y, 3, False):
                for i in range(x, x + 3):
                    self.matrix[i][y].ship_placed = True
            else:
                x = random.randint(0, 7)
                y = random.randint(0, 9)
                while not self._is_valid_placement(x, y, 3, False):
                    x = random.randint(0, 7)
                    y = random.randint(0, 9)
                for i in range(x, x + 3):
                    self.matrix[i][y].ship_placed = True

    def random_place_cruiser(self):
        self.random_place_submarine()

    def random_place_destroyer(self):
        horizontal = random.randint(0, 1)
        if horizontal:
            x = random.randint(0, 9)
            y = random.randint(0, 8)
            if self._is_valid_placement(x, y, 2, True):
                for i in range(y, y + 2):
                    self.matrix[x][i].ship_placed = True
            else:
                x = random.randint(0, 9)
                y = random.randint(0, 8)
                while not self._is_valid_placement(x, y, 2, True):
                    x = random.randint(0, 9)
                    y = random.randint(0, 8)
                for i in range(y, y + 2):
                    self.matrix[x][i].ship_placed = True
        else:
            x = random.randint(0, 8)
            y = random.randint(0, 9)
            if self._is_valid_placement(x, y, 2, False):
                for i in range(x, x + 2):
                    self.matrix[i][y].ship_placed = True
            else:
                x = random.randint(0, 8)
                y = random.randint(0, 9)
                while not self._is_valid_placement(x, y, 2, False):
                    x = random.randint(0, 8)
                    y = random.randint(0, 9)
                for i in range(x, x + 2):
                    self.matrix[i][y].ship_placed = True

    def _can_fit_rec(self, x, y, ship_length, horizontal, counter):
        if self.matrix[x][y].visited or x < 0 or x > 9 or y < 0 or y > 9 or counter >= ship_length:
            return 0
        if horizontal:
            if y + ship_length - 1 < 10:
                for i in range(y, y + ship_length):
                    if self.matrix[x][i].visited:
                        return self._can_fit_rec(x, y - 1, ship_length, horizontal, counter + 1)
                return 1 + self._can_fit_rec(x, y - 1, ship_length, horizontal, counter + 1)
            else:
                return self._can_fit_rec(x, y - 1, ship_length, horizontal, counter + 1)
        else:
            if x + ship_length - 1 < 10:
                for i in range(x, x + ship_length):
                    if self.matrix[i][y].visited:
                        return self._can_fit_rec(x - 1, y, ship_length, horizontal, counter + 1)
                return 1 + self._can_fit_rec(x - 1, y, ship_length, horizontal, counter + 1)
            else:
                return self._can_fit_rec(x - 1, y, ship_length, horizontal, counter + 1)

    def _can_fit(self, x, y, ship_length, horizontal):
        return self._can_fit_rec(x, y, ship_length, horizontal, 0)


    def calculate_probabilities(self):
        for i in range(10):
            for j in range(10):
                self.matrix[i][j].value = 0
        for i in range(10):
            for j in range(10):
                self.matrix[i][j].value += self._can_fit(i, j, 5, True)
                self.matrix[i][j].value += self._can_fit(i, j, 5, False)
                self.matrix[i][j].value += self._can_fit(i, j, 4, True)
                self.matrix[i][j].value += self._can_fit(i, j, 4, False)
                self.matrix[i][j].value += self._can_fit(i, j, 3, True)
                self.matrix[i][j].value += self._can_fit(i, j, 3, False)
                self.matrix[i][j].value += self._can_fit(i, j, 3, True)
                self.matrix[i][j].value += self._can_fit(i, j, 3, False)
                self.matrix[i][j].value += self._can_fit(i, j, 2, True)
                self.matrix[i][j].value += self._can_fit(i, j, 2, False)

                #print(self.matrix[i][j].value, end=" ")
            #print()

    def finished(self):
        if self.hits >= 17:
            return True
        return False

    def score(self, x, y):
        if self.matrix[x][y].ship_placed:
            return True
        return False

    def random_play(self, screen):
        while not self.finished():
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            while self.matrix[x][y].visited:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
            if self.score(x, y):
                self.hits += 1
                self.matrix[x][y].visited = True
            else:
                self.matrix[x][y].visited = True
            self.moves += 1
            self._update_screen(screen)
        return self.moves

    def _best_option(self):
        optimal_val = self.matrix[0][0].value
        optimal_x = 0
        optimal_y = 0
        self.calculate_probabilities()
        for i in range(10):
            for j in range(10):
                if self.matrix[i][j].value > optimal_val:
                    optimal_val = self.matrix[i][j].value
                    optimal_x = i
                    optimal_y = j
        if self.matrix[optimal_x][optimal_y].visited:
            return None
        return optimal_x, optimal_y

    def _is_valid_field(self, x, y):
        return 10 > x >= 0 and 10 > y >= 0

    def add_neighbours(self, PQ, optimal_move_x, optimal_move_y):
        # field below the hit field
        if self._is_valid_field(optimal_move_x + 1, optimal_move_y):
            if not self.matrix[optimal_move_x + 1][optimal_move_y].visited:
                self.matrix[optimal_move_x + 1][optimal_move_y].value = 0.25
                PQ.put(self.matrix[optimal_move_x + 1][optimal_move_y])

        # field above the hit field
        if self._is_valid_field(optimal_move_x - 1, optimal_move_y):
            if not self.matrix[optimal_move_x - 1][optimal_move_y].visited:
                self.matrix[optimal_move_x - 1][optimal_move_y].value = 0.25
                PQ.put(self.matrix[optimal_move_x - 1][optimal_move_y])

        # field right to the hit field
        if self._is_valid_field(optimal_move_x, optimal_move_y + 1):
            if not self.matrix[optimal_move_x][optimal_move_y + 1].visited:
                self.matrix[optimal_move_x][optimal_move_y + 1].value = 0.25
                PQ.put(self.matrix[optimal_move_x][optimal_move_y + 1])

        # field left to the hit field
        if self._is_valid_field(optimal_move_x, optimal_move_y - 1):
            if not self.matrix[optimal_move_x][optimal_move_y - 1].visited:
                self.matrix[optimal_move_x][optimal_move_y - 1].value = 0.25
                PQ.put(self.matrix[optimal_move_x][optimal_move_y - 1])

    def add_neighbours_deque(self, PQ, optimal_move_x, optimal_move_y):
        # field below the hit field
        if self._is_valid_field(optimal_move_x + 1, optimal_move_y):
            if not self.matrix[optimal_move_x + 1][optimal_move_y].visited:
                self.matrix[optimal_move_x + 1][optimal_move_y].value = 0.25
                PQ.append(self.matrix[optimal_move_x + 1][optimal_move_y])

        # field above the hit field
        if self._is_valid_field(optimal_move_x - 1, optimal_move_y):
            if not self.matrix[optimal_move_x - 1][optimal_move_y].visited:
                self.matrix[optimal_move_x - 1][optimal_move_y].value = 0.25
                PQ.append(self.matrix[optimal_move_x - 1][optimal_move_y])

        # field right to the hit field
        if self._is_valid_field(optimal_move_x, optimal_move_y + 1):
            if not self.matrix[optimal_move_x][optimal_move_y + 1].visited:
                self.matrix[optimal_move_x][optimal_move_y + 1].value = 0.25
                PQ.append(self.matrix[optimal_move_x][optimal_move_y + 1])

        # field left to the hit field
        if self._is_valid_field(optimal_move_x, optimal_move_y - 1):
            if not self.matrix[optimal_move_x][optimal_move_y - 1].visited:
                self.matrix[optimal_move_x][optimal_move_y - 1].value = 0.25
                PQ.append(self.matrix[optimal_move_x][optimal_move_y - 1])

    def _add_vertical_neighbours_deque(self, deque, optimal_move_x, optimal_move_y):
        if self._is_valid_field(optimal_move_x + 1, optimal_move_y):
            if not self.matrix[optimal_move_x + 1][optimal_move_y].visited:
                self.matrix[optimal_move_x + 1][optimal_move_y].value = 0.25
                deque.appendleft(self.matrix[optimal_move_x + 1][optimal_move_y])

        # field above the hit field
        if self._is_valid_field(optimal_move_x - 1, optimal_move_y):
            if not self.matrix[optimal_move_x - 1][optimal_move_y].visited:
                self.matrix[optimal_move_x - 1][optimal_move_y].value = 0.25
                deque.appendleft(self.matrix[optimal_move_x - 1][optimal_move_y])

    def _add_horizontal_neighbours_deque(self, deque, first_hit):
        # field right to the hit field
        if self._is_valid_field(first_hit.x, first_hit.y + 1):
            if not self.matrix[first_hit.x][first_hit.y + 1].visited:
                self.matrix[first_hit.x][first_hit.y + 1].value = 0.25
                deque.appendleft(self.matrix[first_hit.x][first_hit.y + 1])

        # field left to the hit field
        if self._is_valid_field(first_hit.x, first_hit.y - 1):
            if not self.matrix[first_hit.x][first_hit.y - 1].visited:
                self.matrix[first_hit.x][first_hit.y - 1].value = 0.25
                deque.appendleft(self.matrix[first_hit.x][first_hit.y - 1])

    def play_smart(self, screen):
        while not self.finished():
            from collections import deque

            list_of_moves = []
            deque = deque()

            if self._best_option() is not None:
                optimal_move_x = self._best_option()[0]
                optimal_move_y = self._best_option()[1]
                self.matrix[optimal_move_x][optimal_move_y].visited = True
                self.moves += 1
                self._update_screen(screen)
                list_of_moves.append(self.matrix[optimal_move_x][optimal_move_y])
            else:
                deque.clear()
                for element in self.list_of_hits:
                    self.add_neighbours_deque(deque, element.x, element.y)
                while not self.finished() and len(deque) != 0:
                    next_field = deque.pop()
                    if next_field.ship_placed and not next_field.visited:
                        self.hits += 1
                        self.list_of_hits.append(next_field)
                        next_field.visited = True
                    else:
                        element.visited = True
                    self._update_screen(screen)
                    if self.finished():
                        return self.moves

            while not self.matrix[optimal_move_x][optimal_move_y].ship_placed:
                if self._best_option() is not None:
                    optimal_move_x = self._best_option()[0]
                    optimal_move_y = self._best_option()[1]
                    list_of_moves.append(self.matrix[optimal_move_x][optimal_move_y])
                    self._update_screen(screen)
                    self.matrix[optimal_move_x][optimal_move_y].visited = True
                    self.moves += 1

            self._update_screen(screen)
            self.hits += 1
            self.add_neighbours_deque(deque, optimal_move_x, optimal_move_y)


            while not self.finished() and len(deque) != 0:
                next_field = deque.popleft()
                list_of_moves.append(next_field)
                if next_field.visited:
                    continue
                if next_field.ship_placed and not next_field.visited:
                    self.hits += 1
                    self.add_neighbours_deque(deque, next_field.x, next_field.y)
                self.moves += 1
                next_field.visited = True
                self._update_screen(screen)
        return self.moves

    def _update_screen(self, screen):
        self.display(screen)
        pygame.display.update()
        pygame.time.wait(1)

    def play_smart_v2(self, screen):
        while not self.finished():
            from collections import deque
            list_of_moves = []
            deque = deque()

            if self._best_option() is not None:
                optimal_move_x = self._best_option()[0]
                optimal_move_y = self._best_option()[1]
                self.matrix[optimal_move_x][optimal_move_y].visited = True
                self.moves += 1
                self._update_screen(screen)
                list_of_moves.append(self.matrix[optimal_move_x][optimal_move_y])
            else:
                deque.clear()
                for element in self.list_of_hits:
                    self.add_neighbours_deque(deque, element.x, element.y)
                while not self.finished() and len(deque) != 0:
                    next_field = deque.pop()
                    if next_field.ship_placed and not next_field.visited:
                        self.hits += 1
                        self.list_of_hits.append(next_field)
                        next_field.visited = True
                    else:
                        element.visited = True
                    self._update_screen(screen)
                    if self.finished():
                        return self.moves

            while not self.matrix[optimal_move_x][optimal_move_y].ship_placed:
                if self._best_option() is not None:
                    optimal_move_x = self._best_option()[0]
                    optimal_move_y = self._best_option()[1]
                    #print("uso", optimal_move_x, optimal_move_y)
                    list_of_moves.append(self.matrix[optimal_move_x][optimal_move_y])
                    self._update_screen(screen)
                    self.matrix[optimal_move_x][optimal_move_y].visited = True
                    self.moves += 1
                else:
                    deque.clear()
                    for element in self.list_of_hits:
                        self.add_neighbours_deque(deque, element.x, element.y)
                    while not self.finished() and len(deque) != 0:
                        next_field = deque.pop()
                        if next_field.ship_placed and not next_field.visited:
                            self.hits += 1
                            self.list_of_hits.append(next_field)
                            next_field.visited = True
                        else:
                            element.visited = True
                        self._update_screen(screen)
                        if self.finished():
                            return self.moves
            if self.finished():
                return self.moves
            first_hit = self.matrix[optimal_move_x][optimal_move_y]
            self.list_of_hits.append(first_hit)
            self._update_screen(screen)
            self.hits += 1

            self._add_vertical_neighbours_deque(deque, optimal_move_x, optimal_move_y)

            miss_counter = 0
            tries = 0
            while not self.finished() and miss_counter < 2 and len(deque) != 0:
                self.moves += 1
                next_field = deque.popleft()
                list_of_moves.append(next_field)
                if next_field.visited:
                    continue
                if next_field.ship_placed and not next_field.visited:
                    self.hits += 1
                    self.list_of_hits.append(next_field)
                    next_field.visited = True
                    self._add_vertical_neighbours_deque(deque, next_field.x, next_field.y)
                    self._update_screen(screen)
                else:
                    miss_counter += 1
                    next_field.visited = True
                    self._update_screen(screen)

            if tries <= 2:
                deque.clear()
                self._add_horizontal_neighbours_deque(deque, first_hit)
                miss_counter = 0

                while not self.finished() and miss_counter < 2 and len(deque) != 0:
                    next_field = deque.popleft()
                    self.moves += 1
                    list_of_moves.append(next_field)
                    if next_field.visited:
                        continue
                    if next_field.ship_placed and not next_field.visited:
                        self.hits += 1
                        self.list_of_hits.append(next_field)
                        next_field.visited = True
                        self._add_horizontal_neighbours_deque(deque, next_field)
                        self._update_screen(screen)
                    else:
                        miss_counter += 1
                        next_field.visited = True
                        self._update_screen(screen)
            if self.hits == 16:
                deque.clear()
                for element in self.list_of_hits:
                    self.add_neighbours_deque(deque, element.x, element.y)
                while not self.finished():
                    print(deque)
                    next_field = deque.pop()
                    if next_field.ship_placed and not next_field.visited:
                        self.hits += 1
                        self.list_of_hits.append(next_field)
                        next_field.visited = True
                    else:
                        next_field.visited = True
                    self._update_screen(screen)
        return self.moves

    def _reset(self, screen):
        for i in range(10):
            for j in range(10):
                self.matrix[i][j].visited = False
        self.hits = 0
        self.list_of_hits = []
        self.moves = 0
        self.display_v2(screen)

    def _full_reset(self, screen):
        for i in range(10):
            for j in range(10):
                self.matrix[i][j].visited = False
                self.matrix[i][j].ship_placed = False
        self.hits = 0
        self.list_of_hits = []
        self.moves = 0
        self.display_v2(screen)

    def display_v2(self, screen):
        BLUE = (0, 0, 255)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)
        YELLOW = (255, 255, 0)
        BLACK = (0, 0, 0)

        for i in range(10):
            for j in range(10):
                if self.matrix[i][j].ship_placed and self.matrix[i][j].visited:
                    pygame.draw.rect(screen, YELLOW, self.matrix[i][j].rect)
                elif self.matrix[i][j].visited:
                    pygame.draw.rect(screen, GREEN, self.matrix[i][j].rect)
                elif self.matrix[i][j].ship_placed:
                    pygame.draw.rect(screen, BLUE, self.matrix[i][j].rect)
                else:
                    pygame.draw.rect(screen, BLACK, self.matrix[i][j].rect)
                    pygame.draw.rect(screen, RED, self.matrix[i][j].rect, 1)

    def compare(self, screen):
        counter_a = 0
        counter_b = 0
        counter_c = 0
        average_a = 0
        average_b = 0
        average_c = 0

        for i in range(500):
            current_a = self.play_smart(screen)
            average_a += current_a
            self._reset(screen)
            self._update_screen(screen)

            current_b = self.play_smart_v2(screen)
            average_b += current_b
            self._reset(screen)
            self._update_screen(screen)

            if i < 100:
                current_c = self.random_play(screen)
                average_c += current_c
                self._reset(screen)
                self._update_screen(screen)

            self._full_reset(screen)
            self.random_place_carrier()
            self.random_place_battleship()
            self.random_place_submarine()
            self.random_place_cruiser()
            self.random_place_destroyer()

            if current_a <= current_b:
                counter_a += 1
            else:
                counter_b += 1

        print("A: ", counter_a, ", average: ", average_a / 500)
        print("B: ", counter_b, ", average: ", average_b / 500)
        print("C: ", counter_c, ", average: ", average_c / 100)
        return