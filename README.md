game-of-life
============

Simple Python implementation of Conway's Game of Life

http://en.wikipedia.org/wiki/The_Game_Of_Life

As the title explains, I took upon the challenge of creating a working version of Conway's Game of Life.  I still
have a lot of work to do, but it's the first thing I thought was actually interesting enough to share on Github.
I may expand the README as I continue work on it, but for now I don't think there's much to say.

So, what is the Game of Life?  Basically, it's a "zero-player" game -- in other words, the game proceeds without
any input needed from an outside source.  The game is based on a grid full of cells which, on any given turn or
"tick" become either "alive" or "dead" based on a small set of simple rules.  For a given tick "n", the rules
are:

1. Any live cell with two or three live neighboring cells remains alive on turn n+1.  A neighboring cell is any
cell directly adjacent to a given cell, whether horizontally, vertically, or diagonally.
2. A live cell with fewer than two or more than three live neighbors will be dead on turn n+1.
3. A dead cell with exactly three live neighbors will be live on turn n+1.

A few basic points:
  1. To run: Simply enter 'python gol.py' from the CLI with grid1.txt in the same directory.  This is a demo
     of the game with a preset grid, set to a 1/10 second delay.
     You can also run the game with a different grid file and time delay if desired, like this: 
        'python gol.py \<filename(no quotes or braces)\> \<timedelay in secs\>'
  2. The game (and the program) automatically ends when the board becomes empty.  However, it doesn't end
     when the game reaches stasis (live cells are on the board, but are permanently live due to their arrangement)
     and I am planning on addressing that.
