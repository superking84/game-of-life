import time

class Grid(object):
    def __init__(self, data):
        data = [[b for b in a] for a in data.strip().split(',')]
        self.cells = []
        self.neighbor_coordinates = [(-1,-1),(-1,0),(-1,1),
                                     ( 0,-1),       ( 0,1),
                                     ( 1,-1),( 1,0),( 1,1)]
                                     
        for i in range(len(data)):
            self.cells.append([])
            for j in range(len(data[i])):
                if data[i][j] == '1':
                    self.cells[i].append(1)
                elif data[i][j] == '0':
                    self.cells[i].append(0)
                else:
                    raise ValueError
        
    def __repr__(self):
        return ('\n'.join([str(row) for row in self.cells]) \
                + '\n').replace('1', 'X').replace('0', ' ')
            
    __str__ = __repr__
        
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
            if any([cell for cell in row]):
                return False
        
        return True
        
    def count_live_neighbors(self, row, column):
        count = 0
        
        for i in range(len(self.neighbor_coordinates)):
            newRow = row + self.neighbor_coordinates[i][0]
            newColumn = column + self.neighbor_coordinates[i][1]
            if newRow == len(self.cells):
                newRow = 0
            if newColumn == len(self.cells[i]):
                newColumn = 0
                
            if (self.cells[newRow][newColumn]):
                count += 1
                
        return count
    
def build_grid_from_src(src):
    src = open(src, 'r')
    src = src.readline()
    return Grid(src)
    
def tick(grid):
    new_data = ''
    for i in range(len(grid.cells)):
        for j in range(len(grid.cells[i])):
            cell = grid.cells[i][j]
            count = grid.count_live_neighbors(i, j)
            if cell:
                if count not in [2, 3]:
                    new_data += '0'
                else:
                    new_data += '1'
            else:
                if count == 3:
                    new_data += '1'
                else:
                    new_data += '0'
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
        grid2 = grid
        grid = tick(grid)
        time.sleep(.2)

if __name__ == '__main__':
    Run()