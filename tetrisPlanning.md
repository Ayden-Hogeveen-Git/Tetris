# Tetris Planning

## Game Elements

### Board
  - Tetris board is 10 cells wide and 20 cells tall
  - Each cell could be represented in a 2D array?
    - True if filled, False otherwise?

  - Tetrominoes
    - These are the 7 playing pieces in Tetris
      - The line 
      - The t-piece
      - The 2 z-pieces
      - The 2 l-pieces
      - The square
        - Square needs to be tweaked because it should not respond to rotations, and needs to be offset to look like it has not moved.
        - Rotation Index --> Offset Value
          - 0 : (0, 0)
          - 1 : (0, -1)
          - 2 : (-1, -1)
          - 3 : (-1, 0)
        - When rotating from pos 0 to pos 1:
          - Pos 0 (0, 0) - Pos 1 (0, -1) = End offset (0, 1)
          - Pos 1 (0, -1) - Pos 0 (0, 0) = End offset (0, -1)
      - This offset idea can be applied to all the pieces, especially when they are next to a wall
    - Each of these is made up of cells, will need a matrix of boolean values to represent these pieces in the board array.
    - Each of the pieces have a rotation point
    - Each possible rotation will have an index assigned, and we can add or subtract from that index to rotate the piece around 

### Tile Rotation Tests
  - If one of the tiles will end up off the grid after a rotation
  - If one of the tiles would overlap with an already existing tile
  - LOOKUP: J, L, S, T, Z, tetromino offset data
  - LOOKUP: I tetromino offset data
  - LOOKUP: O tetromino offset data

### UI and etc.
  - We need a next piece window to display the next piece in the bag
  - We need a hold window to hold a piece for later
  - We need a score, time, etc. stuff like that
  
## Collisions
  - Collisions are probably the most important part about our tetris game
    1. Collisions with the walls or floor of the playing area 
       - We need to use each piece's unique state to detect whether it is touching the wall
       - Each piece will have a unique matrix of boolean values
         - False, True, False, False
         - False, True, False, False
         - False, True, False, False
         - False, True, False, False
           - Would be a vertical l piece, in the  
    2. Collisions with other pieces

## To Do List

TODO: Make an icon for the window

TODO: Models of each of the different tetrominoes that can be rotated, dropped and put into a hold window

TODO: UI and Scoring System

TODO: Tetris block generation and falling

TODO: Rigid bodies for each of the pieces

TODO: Line removal