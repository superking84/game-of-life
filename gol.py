import time
import random

class Cell(object):
    def __init__(self, grid, row, col, live):
        self.live = live
        self.grid = grid
        self.row = row
        self.col = col
        self.neighbors = []
    
    def __repr__(self):
        #return "%s Cell at (%d,%d)" % ("Live" if self.live else "Dead", self.row, self.col)
        return 'X' if self.live else ' '
        
    def __eq__(self, cell2):
        return self.live == cell2.live
        
    def __ne__(self, cell2):
        return self.live != cell2.live
        
    def get_neighbors(self, grid):
        '''
        Identifies all the neighboring cells for a particular
        cell on the provided grid.
        The current code allows the grid to wrap around itself, so the
        left-most cell in a row is the right-hand neighbor of the
        right-most cell in that row, for example.
        If I didn't want to allow that, I could disallow appending
        with negative indexes.
        '''
        neighbor_indexes = [[-1,-1],[-1,0],[-1,1],
                            [0,-1],[0,1],
                            [1,-1],[1,0],[1,1]
                           ]
        cells = grid.cells
        for coord in neighbor_indexes:
            y1, x1 = self.row, self.col
            y2, x2 = coord
            try:
                self.neighbors.append(cells[y1+y2][x1+x2])
            except IndexError:
                pass  
                
    def count_neighbors(self):
        '''
        Returns the number of live neighbors the cell has.
        '''
        err_msg = "This function can only be run on fully-formed Cells."
        assert (self.grid and self.neighbors), err_msg
        count = 0
        
        for neighbor in self.neighbors:
            if neighbor.live:
                count += 1
                
        return count
        

class Grid(object):
    def __init__(self, data):
        data = [[b for b in a] for a in data.strip().split(',')]
        self.cells = []
        
        for i in range(len(data)):
            self.cells.append([])
            for j in range(len(data[i])):
                cell = Cell(self, i, j, False)
                if data[i][j] == 'L':
                    cell.live = True
                self.cells[i].append(cell)
        
        for row in self.cells:
            for cell in row:
                cell.get_neighbors(self)
        
    def __repr__(self):
        return '\n'.join([str(row) for row in self.cells]) + '\n'
            
    __str__ = __repr__
    
    def __getitem__(self, key):
        return self.cells[key]
        
    def __eq__(self, grid2):
        cells = self.cells
        cells2 = grid2.cells
        if len(cells) != len(cells2):
            return False
        for i in range(len(cells)):
            if len(cells[i]) != len(cells2[i]):
                return False
            for j in range(len(cells[i])):
                if cells[i][j] != cells2[i][j]:
                    return False
                    
        return True
        
    def is_empty(self):
        for row in self.cells:
            if any([cell.live for cell in row]):
                return False
        
        return True
    
def build_grid_from_src(src):
    src = open(src, 'r')
    src = src.readline()
    return Grid(src)
    
def tick(grid):
    new_data = ''
    for i in range(len(grid.cells)):
        for j in range(len(grid.cells[i])):
            cell = grid.cells[i][j]
            count = cell.count_neighbors()
            y, x = cell.row, cell.col
            if cell.live:
                if count not in [2, 3]:
                    # cell dies if it does not have 2 or 3 neighbors
                    new_data += 'D'
                else:
                    new_data += 'L'
            else:
                if count == 3:
                    new_data += 'L'
                else:
                    new_data += 'D'
        if (i + 1) < len(grid.cells):
            new_data += ','
        
    return Grid(new_data)
    
    
def Run():
    grid = build_grid_from_src('grid1.txt')
    grid2 = None
    while True:
        print grid
        if grid2 and grid2 == grid:
            break
        if grid.is_empty(): break
        if grid2:
            grid = grid2
        grid2 = tick(grid)
        time.sleep(.1)

if __name__ == '__main__':
    Run()