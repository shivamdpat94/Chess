import pygame

def map(input):
    if input[0] == 'A':
        x = 0
    if input[0] == 'B':
        x = 1
    if input[0] == 'C':
        x = 2
    if input[0] == 'D':
        x = 3
    if input[0] == 'E':
        x = 4
    if input[0] == 'F':
        x = 5
    if input[0] == 'G':
        x = 6
    if input[0] == 'H':
        x = 7
    y = int(input[1]) -1
    return [y,x]

#Pawn Class
class Pawn:
    position = None
    color = None
    piece = 'pawn'
    pic = None
    def __init__(self,Color,Position,Start):
        self.color = Color
        self.position  = Position
        self.start =Start
        if self.color == 'black':
            self.pic = 'BP.png'
        elif self.color == 'white':
            self.pic = 'WP.png'
    def move(self):
        options = []
        if self.color == 'white':
            options.append([self.position[0]+1,self.position[1]])
            if self.position[1] <7:
                options.append([self.position[0]+1,self.position[1]+1])
            if self.position[1] > 0:
                options.append([self.position[0]+1,self.position[1]-1])
            if self.start == True:
                options.append([self.position[0]+2,self.position[1]])

        if self.color == 'black':
            options.append([self.position[0]-1,self.position[1]])
            if self.position[1] <7:
                options.append([self.position[0]-1,self.position[1]+1])
            if self.position[1] > 0:
                options.append([self.position[0]-1,self.position[1]-1])
            if self.start == True:
                options.append([self.position[0]-2,self.position[1]])

        return options

#Rook Class
class Rook:
    position = None
    color = None
    piece = 'rook'
    pic = None
    def __init__(self,Color,Position):
        self.color = Color
        self.position  = Position
        if self.color == 'black':
            self.pic = 'BR.png'
        elif self.color == 'white':
            self.pic = 'WR.png'
    def move(self):
        options = []
        left = self.position[1] -1
        right = self.position[1] +1
        up = self.position[0] +1
        down = self.position[0] -1
        temp = []
        while left >=0:
            temp.append([self.position[0],left])
            left = left -1
        options.append(temp)
        temp = []
        while right <=7:
            temp.append([self.position[0],right])
            right = right +1
        options.append(temp)
        temp = []
        while down >=0:
            temp.append([down, self.position[1]])
            down = down -1
        options.append(temp)
        temp = []
        while up <=7:
            temp.append([up,self.position[1]])
            up = up +1
        options.append(temp)
        return options

#Knight Class
class Knight:
    piece = 'knight'
    position = None
    color = None
    pic = None
    def __init__(self,Color,Position):
        self.color = Color
        self.position  = Position
        if self.color == 'black':
            self.pic = 'BKN.png'
        elif self.color == 'white':
            self.pic = 'WKN.png'
    def move(self):
        xmoves = [-2,-1,1,2]
        options = []
        for xx in xmoves:
            if abs(xx) == 2:
                ymoves = [-1,1]
            else:
                ymoves = [-2,2]
            for yy in ymoves:
                x = self.position[0] + xx
                y = self.position[1] + yy
                if x >= 0 and x <= 7 and y >= 0 and y <= 7:
                    options.append([x,y])
        return options

#Bishop Class
class Bishop:
    piece = 'bishop'
    position = None
    color = None
    pic = None
    def __init__(self,Color,Position):
        self.color = Color
        self.position  = Position
        if self.color == 'black':
            self.pic = 'BB.png'
        elif self.color == 'white':
            self.pic = 'WB.png'
    def move(self):
        options = []
        x = self.position[0] - 1
        y = self.position[1] - 1
        temp = []
        while x >= 0 and y >= 0:
            temp.append([x,y])
            x = x-1
            y = y-1
        options.append(temp)
        x = self.position[0] - 1
        y = self.position[1] + 1
        temp = []
        while x >= 0 and y <= 7:
            temp.append([x,y])
            x = x-1
            y = y+1
        options.append(temp)
        x = self.position[0] + 1
        y = self.position[1] - 1
        temp = []
        while x <= 7 and y >= 0:
            temp.append([x,y])
            x = x+1
            y = y-1
        options.append(temp)
        x = self.position[0] + 1
        y = self.position[1] + 1
        temp = []
        while x <= 7 and y <= 7:
            temp.append([x,y])
            x = x+1
            y = y+1
        options.append(temp)
        return options

#Queen Class
class Queen:
    piece = 'queen'
    position = None
    color = None
    pic = None
    def __init__(self,Color,Position):
        self.color = Color
        self.position  = Position
        if self.color == 'black':
            self.pic = 'BQ.png'
        elif self.color == 'white':
            self.pic = 'WQ.png'
    def move(self):
        options = []
        x = self.position[0] - 1
        y = self.position[1] - 1
        temp = []
        while x >= 0 and y >= 0:
            temp.append([x,y])
            x = x-1
            y = y-1
        options.append(temp)
        x = self.position[0] - 1
        y = self.position[1] + 1
        temp = []
        while x >= 0 and y <= 7:
            temp.append([x,y])
            x = x-1
            y = y+1
        options.append(temp)
        x = self.position[0] + 1
        y = self.position[1] - 1
        temp = []
        while x <= 7 and y >= 0:
            temp.append([x,y])
            x = x+1
            y = y-1
        options.append(temp)
        x = self.position[0] + 1
        y = self.position[1] + 1
        temp = []
        while x <= 7 and y <= 7:
            temp.append([x,y])
            x = x+1
            y = y+1
        options.append(temp)



        left = self.position[1] -1
        right = self.position[1] +1
        up = self.position[0] +1
        down = self.position[0] -1
        temp = []
        while left >=0:
            temp.append([self.position[0],left])
            left = left -1
        options.append(temp)
        temp = []
        while right <=7:
            temp.append([self.position[0],right])
            right = right +1
        options.append(temp)
        temp = []
        while down >=0:
            temp.append([down, self.position[1]])
            down = down -1
        options.append(temp)
        temp = []
        while up <=7:
            temp.append([up,self.position[1]])
            up = up +1
        options.append(temp)
        return options

#King Class
class King:
    piece = 'king'
    position = None
    color = None
    pic = None
    def __init__(self,Color,Position):
        self.color = Color
        self.position  = Position
        if self.color == 'black':
            self.pic = 'BK.png'
        elif self.color == 'white':
            self.pic = 'WK.png'
    def move(self):
        options = []
        xmove = [1,0,-1]
        ymove = [1,0,-1]
        for xx in xmove:
            for yy in ymove:
                if xx!=0 or yy!=0:
                    x = xx + self.position[0]
                    y = yy + self.position[1]
                    if x <=7 and x >=0 and y <=7 and y>=0:
                        options.append([x,y])
        return options

#Gives movable coordinates of selected piece
def get_options(Board,location):
    options = []
    optionss = []
    if Board.board[location[0]][location[1]] != None:
        optionss = Board.board[location[0]][location[1]].move()
    else:
        return False

    #####PAWN#######
    if Board.board[location[0]][location[1]].piece == 'pawn':
        for option in optionss:
            if location[1] != option[1] and Board.board[option[0]][option[1]] != None:
                if Board.board[option[0]][option[1]].color != Board.board[location[0]][location[1]].color:
                    options.append(option)
            elif location[1] == option[1] and Board.board[option[0]][option[1]] == None:
                options.append(option)

    ######KNIGHT######
    if Board.board[location[0]][location[1]].piece == 'knight':
        for option in optionss:
            if Board.board[option[0]][option[1]] == None or Board.board[option[0]][option[1]].color != Board.board[location[0]][location[1]].color:
                options.append(option)

    #####ROOK, BISHOP, QUEEN#######
    elif Board.board[location[0]][location[1]].piece == 'rook' or Board.board[location[0]][
        location[1]].piece == 'bishop' or Board.board[location[0]][location[1]].piece == 'queen':
        for option in optionss:
            for o in option:
                if Board.board[o[0]][o[1]] == None:
                    options.append(o)
                elif Board.board[o[0]][o[1]].color == Board.board[location[0]][location[1]].color:
                    break
                elif Board.board[o[0]][o[1]].color != Board.board[location[0]][location[1]].color:
                    options.append(o)
                    break
    elif Board.board[location[0]][location[1]].piece == 'king':
        for option in optionss:
            if Board.board[option[0]][option[1]] == None or Board.board[option[0]][option[1]].color != Board.board[location[0]][location[1]].color:
                options.append(option)


    return options

#Class of board
class chessboard:
    board = []
    for i in range(0,8):
        board.append([])
        for j in range(0,8):
            board[i].append(None)
    #Gets available movement options for selected piece at 'location', checks if 'target' is in available options, and moves selected piece to 'target' coordinate if so
    def move(self,location, target,turn):
        options = get_options(self,location)
        try:
            if target in options and self.board[location[0]][location[1]].color == turn:
                if self.board[location[0]][location[1]].piece == 'pawn':
                    self.board[target[0]][target[1]] = Pawn(self.board[location[0]][location[1]].color,target,False)
                if self.board[location[0]][location[1]].piece == 'knight':
                    self.board[target[0]][target[1]] = Knight(self.board[location[0]][location[1]].color,target)
                if self.board[location[0]][location[1]].piece == 'rook':
                    self.board[target[0]][target[1]] = Rook(self.board[location[0]][location[1]].color,target)
                if self.board[location[0]][location[1]].piece == 'bishop':
                    self.board[target[0]][target[1]] = Bishop(self.board[location[0]][location[1]].color,target)
                if self.board[location[0]][location[1]].piece == 'queen':
                    self.board[target[0]][target[1]] = Queen(self.board[location[0]][location[1]].color,target)
                if self.board[location[0]][location[1]].piece == 'king':
                    self.board[target[0]][target[1]] = King(self.board[location[0]][location[1]].color,target)
                self.board[location[0]][location[1]] = None
                return True
            else:
                return False
        except:
            return False

#Initiates the board
def setup_board():
    Board = chessboard
    for i in range(0,8):
        for j in range(0,8):
            if i == 1:
                Board.board[i][j] = Pawn('white',[i,j],True)
            if i == 6:
                Board.board[i][j] = Pawn('black',[i,j],True)
            if i == 0:
                if j == 0 or j == 7:
                    Board.board[i][j] = Rook('white',[i,j])
                if j == 1 or j == 6:
                    Board.board[i][j] = Knight('white',[i,j])
                if j == 2 or j == 5:
                    Board.board[i][j] = Bishop('white', [i,j])
                if j == 3:
                    Board.board[i][j] = Queen('white',[i,j])
                if j == 4:
                    Board.board[i][j] = King('white',[i,j])
            if i == 7:
                if j == 0 or j == 7:
                    Board.board[i][j] = Rook('black',[i,j])
                if j == 1 or j == 6:
                    Board.board[i][j] = Knight('black',[i,j])
                if j == 2 or j == 5:
                    Board.board[i][j] = Bishop('black', [i,j])
                if j == 3:
                    Board.board[i][j] = Queen('black',[i,j])
                if j == 4:
                    Board.board[i][j] = King('black',[i,j])
    return Board



#Maps backend tracking to front end chess board window.
def get_input(Board,turn):
    grid = []
    for row in range(8):
        # Add an empty array that will hold each cell
        # in this row
        grid.append([])
        for column in range(8):
            grid[row].append(0)  # Append a cell

    done = False
    finish = None
    start = None
    count = 0
    while not done:
        if count == 1:
            try:
                #Marks option squares green for selected piece
                for option in options:
                    if turn == 'white':
                        grid[7-option[0]][option[1]] = 1
                    elif turn == 'black':
                        grid[option[0]][7-option[1]] = 1

            except:
                pass
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                # Set that location to one
                grid[row][column] = 1
                print("Click ", pos, "Grid coordinates: ", row, column)
                if count ==0:
                    if turn == 'white':
                        start = [7-row,column]
                    elif turn == 'black':
                        start = [row,7-column]
                    count = 1
                    if turn == 'white':
                        options = get_options(Board,[7-row,column])
                    elif turn == 'black':
                        options = get_options(Board,[row,7-column])
                    break
                if count == 1:
                    if turn == 'white':
                        finish = [7-row,column]
                    elif turn == 'black':
                        finish = [row,7-column]
                    done = True

        # Set the screen background
        screen.fill(BLACK)
        # Draw the grid
        for row in range(8):
            for column in range(8):
                if row%2==0 and column%2==0:
                    color = WHITE
                elif row%2==1 and column%2==1:
                    color = WHITE
                else:
                    color = BROWN
                if grid[row][column] == 1:
                    color = GREEN
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])

        # Limit to 60 frames per second
        clock.tick(60)
        for i in range(0,8):
            for j in range(0,8):
                if turn == 'white':
                    xpos = j
                    ypos = 7-i
                elif turn == 'black':
                    xpos = 7-j
                    ypos = i
                # puts peices on board based on Object location in class. Inverts board depending on whose turn it is
                if Board.board[i][j] == None:
                    pass
                elif Board.board[i][j].piece == 'rook' and Board.board[i][j].color == 'white':
                    WR1 =pygame.image.load('WR.png')
                    screen.blit(WR1,(xpos*60, (ypos) * 60))
                elif Board.board[i][j].piece == 'rook' and Board.board[i][j].color == 'black':
                    WR1 =pygame.image.load('BR.png')
                    screen.blit(WR1,(xpos*60, (ypos) * 60))
                elif Board.board[i][j].piece == 'bishop' and Board.board[i][j].color == 'white':
                    WR1 =pygame.image.load('WB.png')
                    screen.blit(WR1,(xpos*60, (ypos) * 60))
                elif Board.board[i][j].piece == 'bishop' and Board.board[i][j].color == 'black':
                    WR1 =pygame.image.load('BB.png')
                    screen.blit(WR1,(xpos*60, (ypos) * 60))
                elif Board.board[i][j].piece == 'knight' and Board.board[i][j].color == 'white':
                    WR1 =pygame.image.load('WKN.png')
                    screen.blit(WR1,(xpos*60, (ypos) * 60))
                elif Board.board[i][j].piece == 'knight' and Board.board[i][j].color == 'black':
                    WR1 =pygame.image.load('BKN.png')
                    screen.blit(WR1,(xpos*60, (ypos) * 60))
                elif Board.board[i][j].piece == 'queen' and Board.board[i][j].color == 'white':
                    WR1 =pygame.image.load('WQ.png')
                    screen.blit(WR1,(xpos*60, (ypos) * 60))
                elif Board.board[i][j].piece == 'queen' and Board.board[i][j].color == 'black':
                    WR1 =pygame.image.load('BQ.png')
                    screen.blit(WR1,(xpos*60, (ypos) * 60))
                elif Board.board[i][j].piece == 'king' and Board.board[i][j].color == 'white':
                    WR1 =pygame.image.load('WK.png')
                    screen.blit(WR1,(xpos*60, (ypos) * 60))
                elif Board.board[i][j].piece == 'king' and Board.board[i][j].color == 'black':
                    WR1 =pygame.image.load('BK.png')
                    screen.blit(WR1,(xpos*60, (ypos) * 60))
                elif Board.board[i][j].piece == 'pawn' and Board.board[i][j].color == 'black':
                    WR1 =pygame.image.load('BP.png')
                    screen.blit(WR1,(xpos*60, (ypos) * 60))
                elif Board.board[i][j].piece == 'pawn' and Board.board[i][j].color == 'white':
                    WR1 =pygame.image.load('WP.png')
                    screen.blit(WR1,(xpos*60, (ypos) * 60))


        pygame.display.flip()
    return start, finish



BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BROWN = (160,82,45)
RED = (255, 0, 0)


WIDTH = 55
HEIGHT = 55
Inc = 55
# This sets the margin between each cell
MARGIN = 5
grid = []
for row in range(8):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(8):
        grid[row].append(0)  # Append a cell

# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)

# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [520, 520]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Lets Play Chess")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()




































Board = setup_board()
start = 1




while(start):


    if start%2 == 1:
        turn = 'white'
        print("White's Move Turn ", start)
    else:
        turn = 'black'
        print("Black's Move Turn", start)
    currpos, topos = get_input(Board,turn)

    # current = input('Current: ')
    # currpos = map(current)
    # to = input('To: ')
    # topos = map(to)
    if Board.move(Board,currpos,topos,turn):
        start = start + 1
    else:
        print('Invalid Arguements..Try Again')


pygame.quit()