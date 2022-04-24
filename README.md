# reversi
python module for reversi

## revsys module
you can use system module with
`import revsys`

in system module, two classes and a function are available
each can use with

`from revsys import System`

`from revsys import Position`

`from revsys import cui_game`

or you can also write like

`from revsys import System, Position`

### Position(x: int, y: int)
this class is for reversi system.
use as an argument for a method of System objects
you can create an object with

`p = Position(2, 7)`

a first argument is for x, a second one is for y

### System()
this class is for reversi system.
you can control all of the status in reversi with it.
you can use this class with

`s = System()`.

you can use functions below:

`s.put_stone(p: Position)`
for putting stone. you can also use with
`s.put_stone(Position(2, 7))`

`s.can_next() -> bool`
for checking if the game is able to continue

`s.prints()`
for displaying on console

`s.game_status`
get game status as

| code| meaning                                        |
|:---:|:-----------------------------------------------|
|   0 | both players can put a stone somewhere legally |
|   1 | WHITE cannot put a stone but BLACK can         |
|  -1 | BLACK cannot put a stone but WHITE can         |
|  10 | DRAW                                           |
|  11 | BLACK wins                                     |
|   9 | WHITE wins                                     |

### cui_game()
this function is to play reversi on console
you can play only with

`cui_game()`
