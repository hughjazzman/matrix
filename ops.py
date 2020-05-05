from random import randint
import numpy as np
from operator import add

class Matrix:
    def __init__(self, rows=3, columns=3, maxnum=20, grid=None):
        if grid is None:
            self.rows = rows if rows < 6 else 6
            self.columns = columns if columns < 6 else 6
            self.maxnum = maxnum
            self.grid = grid
            self.make_grid()
        else:
            self.rows=length(grid)
            self.columns=length(grid[0]) if self.rows else 0
            self.maxnum=maxnum
            self.grid=grid

    def make_grid(self):
        '''Make a randomized grid'''
        self.grid = [ [ randint(-self.maxnum,self.maxnum) for i in range(self.columns) ] for j in range(self.rows) ]

    def make_identity(self):
        self.grid = [ [ 0 if i != j else 1 for i in range(self.columns) ] for j in range(self.rows) ]

    def print_grid(self):
        print(*self.grid, sep = '\n')

    def is_empty(self):
        return self.grid == []

    def get_rows(self):
        return self.rows

    def get_columns(self):
        return self.columns

    def valid_row(self, row):
        return 0 <= row < self.rows

    def swap_row(self, row1, row2):
        if self.is_empty() or not self.valid_row(row1) or not self.valid_row(row2): return
        self.grid[row1], self.grid[row2] = self.grid[row2], self.grid[row1]

    def scalar_row(self, row, c):
        if self.is_empty() or not self.valid_row(row) or not c: return
        self.grid[row] = list(map(lambda x: c*x, self.grid[row]))

    def scalar_add(self, row_to, row_from, c):
        if self.is_empty() or not self.valid_row(row_to) or not self.valid_row(row_from) or not c: return

        # Get scalar multiple of row_from first
        row = self.grid[row_from].copy()
        row = list(map(lambda x: c*x, row))
        self.grid[row_to] = list(map(add, self.grid[row_to], row))

    def transpose(self):
        if self.is_empty(): return
        self.grid = [[self.grid[j][i] for j in range(self.rows)] for i in range(self.columns)]

    def frac_to_float(self, frac_str):
        try:
            return float(frac_str)
        except ValueError:
            num, denom = frac_str.split('/')
            try:
                leading, num = num.split(' ')
                whole = float(leading)
            except ValueError:
                whole = 0
            frac = float(num) / float(denom)
            return whole - frac if whole < 0 else whole + frac