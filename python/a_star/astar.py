#!/usr/bin/env python3
# -*- coding: utf_8 -*-

import sys
import heapq

class Cell:
    def __init__(self, x, y, reachable):
        self.reachable = reachable
        self.x = x
        self.y = y
        self.parent = None
        self.g = 0
        self.h = 0

    @property
    def f(self):
        return self.g + self.h
    
    def __lt__(self, other):
        return self.f < other.f

class AStar:
    def __init__(self, width, height):
        self.opened = []
        heapq.heapify(self.opened)
        self.closed = set()
        self.cells = []
        self.grid_width = width
        self.grid_height = height
        
        for x in range(self.grid_width):
            for y in range(self.grid_height):
                self.cells.append(Cell(x, y, True))

        self.place_start(0, 0)
        self.place_goal(self.grid_width - 1, self.grid_height - 1)
    def switch_wall(self, x, y):
        cell = self.get_cell(x, y)
        cell.reachable = not cell.reachable

    def place_start(self, x, y):
        self.start = self.get_cell(x, y)

    def place_goal(self, x, y):
        self.goal = self.get_cell(x, y)
        # compute heuristic
        for cell in self.cells:
            cell.h_value = 10 * (abs(cell.x - self.goal.x) + abs(cell.y - self.goal.y))

    def get_cell(self, x, y):
        return self.cells[x * self.grid_height + y]

    def get_adjacent_cells(self, cell):
        neighbors = []

        if cell.x < self.grid_width-1:
            neighbors.append(self.get_cell(cell.x+1, cell.y))
        if cell.y > 0:
            neighbors.append(self.get_cell(cell.x, cell.y-1))
        if cell.x > 0:
            neighbors.append(self.get_cell(cell.x-1, cell.y))
        if cell.y < self.grid_height-1:
            neighbors.append(self.get_cell(cell.x, cell.y+1))

        return neighbors

    def change_cell(self, adj, cell):
        adj.g = cell.g + 10
        adj.parent = cell

    def process(self):
        heapq.heappush(self.opened, self.start)
        while len(self.opened):
            cell = heapq.heappop(self.opened)
            self.closed.add(cell)
            if cell is self.goal:
                self.display_path()
                break
            adj_cells = self.get_adjacent_cells(cell)
            for adj_cell in adj_cells:
                if adj_cell.reachable and adj_cell not in self.closed:
                    if adj_cell in self.opened:
                        if adj_cell.g > cell.g + 10:
                            self.change_cell(adj_cell, cell)
                    else:
                        self.change_cell(adj_cell, cell)
                        heapq.heappush(self.opened, adj_cell)

    def display_path(self):
        cell = self.goal
        path = []
        while cell.parent is not self.start:
            cell = cell.parent
            path.append((cell.x, cell.y))
        
        start_pos = (self.start.x, self.start.y)
        goal_pos = (self.goal.x, self.goal.y)

        to_print = ""
        for y in range(self.grid_height):
            for x in range(self.grid_width):
                if (x, y) == start_pos:
                    to_print += "S"
                elif (x, y) == goal_pos:
                    to_print += "G"
                elif (x, y) in path:
                    to_print += "x"
                else:
                    to_print += "-"
            to_print += "\n"
        print(to_print)

def main(argv):
    astar = AStar(20, 20)
    astar.process()

if __name__ == "__main__":
    main(sys.argv[1:])
