import sys
import time

class Grid(object):
    def __init__(self, src):
        data = [[b for b in a] for a in src.strip().split('\n')]
            
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
                    raise ValueError("Invalid data is present in data file")
                    
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

def parse_grid_file(file_name):
    return open(file_name, 'r').read()
    
def tick(grid):
    new_data = ''
    for i in range(len(grid.cells)):
        for j in range(len(grid.cells[i])):
            cell = grid.cells[i][j]
            count = grid.count_live_neighbors(i, j)
            if cell:
                if count in [2, 3]:
                    new_data += '1'
                else:
                    new_data += '0'
            else:
                if count == 3:
                    new_data += '1'
                else:
                    new_data += '0'
        if (i + 1) < len(grid.cells):
            new_data += '\n'
        
    return Grid(new_data)
    
    
def Run(src_file, delay):
    try:
        raw_data = parse_grid_file(src_file)
        grid = Grid(raw_data)
    except ValueError:
        print "\nProgram could not run!\nERROR: Invalid data present in grid file.\n"
        sys.exit()
    grid2 = None
    print grid
    raw_input("Press ENTER to begin.")
    while True:
        if grid.is_empty() or (grid2 and (grid2 == grid)):
            break
        
        grid2 = grid
        grid = tick(grid)
        time.sleep(delay)
        
        print grid

if __name__ == '__main__':
    args = sys.argv[1:] # strips out filename
    if not args:
        Run('grid1.txt', .2)
    else:
        src_file = args[0]
        try:
            delay = float(args[1])
        except ValueError:
            print "Invalid time delay given, reverting to default.  Press ENTER to continue..."
            raw_input()
            delay = 0.2
            
        Run(src_file, delay)
