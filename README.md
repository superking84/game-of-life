game-of-life
============

Simple Python implementation of Conway's Game of Life

http://en.wikipedia.org/wiki/The_Game_Of_Life

As the title explains, I took upon the challenge of creating a working versino of Conway's Game of Life.  I still
have a lot of work to do, but it's the first thing I thought was actually interesting enough to share on Github.
I may expand the README as I continue work on it, but for now I don't think there's much to say.

A few basic points:
  1. To run: Simply enter 'python gol.py' from the CLI with grid1.txt in the same directory.  This is a demo
     of the game with a preset grid, set to a 1/10 second delay.  Obviously I'll adjust this so that other
     grids can be used as well.
  2. The game (and the program) automatically ends when the board becomes empty.  However, it doesn't end
     when the game reaches stasis (live cells are on the board, but are permanently live due to their arrangement)
     and I am planning on addressing that.
