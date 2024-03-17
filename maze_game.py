board = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 3, 1, 1, 1, 1]
]
inGame = False
u_win = '''
 ________________________
|                        |
|  YOU            WIN!   |
|        O    O          |
|      \________/        |
|________________________|
check my other silly gooses at github.com/ItzCyzmiX!
'''

controls = {
    'up': 'u',
    'down': 'd',
    'left': 'l',
    'right': 'r'
}

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        board[self.y][self.x] = 4
    def update(self):
        board[self.y][self.x] = 4
    def clean(self):
        board[self.y][self.x] = 0
    
    def move(self):
        global inGame
        global controls
        while True:
            m = input('Make a move ->')
            if m == controls['down']:
                self.clean()
                if board[self.y + 1][self.x] == 1:
                    print("Thats a wall!")
                    print(board[self.y + 1][self.x])
                    continue
                elif board[self.y + 1][self.x] == 3:
                    print(u_win)
                    inGame = False
                    break
                else:
                    self.y += 1
                    break
            elif m == controls['up']:
                if board[self.y - 1][self.x] == 1:
                    print("Thats a wall!")
                    print(board[self.y + 1][self.x])
                    continue
                elif board[self.y - 1][self.x] == 3:
                    print(u_win)
                    inGame = False
                    break
                else:
                    self.clean()
                    self.y -= 1
                    break
            elif m == controls['right']:
                if board[self.y][self.x + 1] == 1:
                    print("Thats a wall!")
                    continue
                elif board[self.y][self.x + 1] == 3:
                    print(u_win)
                    inGame = False
                    break
                else:
                    self.clean()
                    self.x += 1
                    break
            elif m == controls['left']:
                if board[self.y][self.x - 1] == 1:
                    print("Thats a wall!")
                    continue
                elif board[self.y][self.x - 1] == 3:
                    print(u_win)
                    inGame = False
                    break 
                else:
                    self.clean()
                    self.x -= 1
                    break
            else:
                print('Invalid input!')
                continue
        self.update()
        

maze_codes = {
    1: ' * ',
    0: '   ',
    4: ' O ',
    3: ' X '
}

def print_maze():
    for i, y in enumerate(board):
        for z, x in enumerate(y):
            print(maze_codes.get(x), end="")
        print()

p = Player(4, 10)

print('''
Controls:
    d -> move down
    u -> move up
    r -> move right
    l -> move left
How to play:
    Move the "O" to "X" to win!

->press enter to begin x to change controls<-
''')
i = input()

if i == 'x':
    
    for c in controls.keys():
        print(f'Set "{c}" to -> ')
        key = ""
        while True:
            key = input()
            if len(key) > 1:
                print('Invalid input!')
            else:
                break
        controls[c] = key
    print(controls)

inGame = True

while inGame:
    print_maze()
    p.move()
    

        

    
