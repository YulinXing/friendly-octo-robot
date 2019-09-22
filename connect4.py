import turtle
 
screen = turtle.Screen()
screen.delay(0)
 
chip = turtle.Turtle()
chip.shape("circle")
chip.color("green")
chip.penup()
chip.speed(0)
 
connect = []
CHIP_DIST = 30 
ORIGIN_X = -90
ORIGIN_Y = -100
RIGHTMOST_COL = ORIGIN_X + CHIP_DIST * 6
y = chip.ycor()
x = chip.xcor()
for i in range(7):
    connect.append([])
    x = connect[i]
    for j in range(7):
        x.append(0)
        chip.goto(ORIGIN_X + i * CHIP_DIST, ORIGIN_Y + j * CHIP_DIST)
        chip.stamp()
 
chip.color("blue")
chip.goto(ORIGIN_X + 3 * CHIP_DIST, ORIGIN_Y + 7 * CHIP_DIST)
 
running = True
 
 
def r():
    if running:
        x = chip.xcor()
        if x < RIGHTMOST_COL:
            chip.setx(x + CHIP_DIST)
        else:
            chip.setx(ORIGIN_X)
 
 
def l():
    if running:
        x = chip.xcor()
        if x > ORIGIN_X:
            chip.setx(x - CHIP_DIST)
        else:
            chip.setx(RIGHTMOST_COL)
 
 
turn = 1
def d():
    global turn, running
    if running:
        x = int((chip.xcor() - ORIGIN_X) / CHIP_DIST)
        col = connect[x]
        for y in range(len(col)):
            if col[y] == 0:
                chip.sety(ORIGIN_Y + y * CHIP_DIST)
                chip.stamp()
                chip.goto(ORIGIN_X + 3 * CHIP_DIST, ORIGIN_Y + 7 * CHIP_DIST)
                connect[x][y] = turn
                # add code here
                if turn == 1:
                 turn = 2
                 chip.color("red")
                else:
                 turn = 1
                 chip.color ("blue")
                 break
 
 
def check_row(x, y):
    count = 1
    for i in range(1, 4):
        if x + i < 7 and connect[x + i][y] == turn:
            count += 1
        else:
            break
    for i in range(1, 4):
        if x - i > -1 and connect[x - i][y] == turn:
            count += 1
        else:
            break
    if count >= 4:
        return True
    return False
 
 
def check_column(x, y):
    count = 1
    for i in range(1, 4):
        if y + i < 7  and connect[x][y + i] == turn:
            count += 1
        else:
            break
    for i in range(1, 4):
        if y - i > -1 and connect[x][y - i] == turn:
            count += 1
        else:
            break
    if count >= 4:
        return True
    return False
 
 
def has_winner(x, y):
    return check_row(x, y) or check_column(x, y)
 
 
if has_winner(x, y):
    if has_winner(x, y):
        running = False
        print ("Player " + str(turn) + " is the winner!")
    else:
        if turn == 1:
            turn = 2
            chip.color("red")
        else:
            turn = 1
            chip.color("blue")
 
screen.onkey(r, "Right")
screen.onkey(l, "Left")
screen.onkey(d, "Down")
screen.listen()
turtle.done()