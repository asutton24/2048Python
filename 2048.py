import random

def movesLeft(b):
    for i in range(4):
        for j in range(4):
            if b[i][j] == 0:
                return True
    for i in range(4):
        for j in range(3):
            if b[i][j] == b[i][j+1]:
                return True
            if b[j][i] == b[j+1][i]:
                return True
    return False
def copy(b):
    t = []
    for i in range(4):
        t.append([0, 0, 0, 0])
    for i in range(4):
        for j in range(4):
            t[i][j] = b[i][j]
    return t
def merge(m, b):
    temp = [b, 0]
    if m == 'w':
        for i in range(4):
            for j in range(3):
                if b[j+1][i] == b[j][i]:
                    b[j][i] *= 2
                    b[j+1][i] = 0
                    temp[1] += b[j][i]
    if m == 's':
        for i in range(3,-1,-1):
            for j in range(3,0,-1):
                if b[j-1][i] == b[j][i]:
                    b[j][i] *= 2
                    b[j-1][i] = 0
                    temp[1] += b[j][i]
    if m == 'a':
        for i in range(4):
            for j in range(3):
                if b[i][j+1] == b[i][j]:
                    b[i][j] *= 2
                    b[i][j+1] = 0
                    temp[1] += b[i][j]
    if m == 'd':
        for i in range(3,-1,-1):
            for j in range(3,0,-1):
                if b[i][j-1] == b[i][j]:
                    b[i][j] *= 2
                    b[i][j-1] = 0
                    temp[1] += b[i][j]
    temp[0] = b
    return temp
def collapseRow(l):
    for j in range(3):
        for i in range(3):
            if l[i] == 0:
                l[i] = l[i+1]
                l[i+1] = 0
    return l

def collapse(m, b):
    if m == 'a':
        for i in range(4):
            temp = collapseRow([b[i][0], b[i][1], b[i][2], b[i][3]])
            b[i][0], b[i][1], b[i][2], b[i][3] = temp[0], temp[1], temp[2], temp[3]
        return b
    if m == 'd':
        for i in range(4):
            temp = collapseRow([b[i][3], b[i][2], b[i][1], b[i][0]])
            b[i][3], b[i][2], b[i][1], b[i][0] = temp[0], temp[1], temp[2], temp[3]
        return b
    if m == 'w':
        for i in range(4):
            temp = collapseRow([b[0][i], b[1][i], b[2][i], b[3][i]])
            b[0][i], b[1][i], b[2][i], b[3][i] = temp[0], temp[1], temp[2], temp[3]
        return b
    if m == 's':
        for i in range(4):
            temp = collapseRow([b[3][i], b[2][i], b[1][i], b[0][i]])
            b[3][i], b[2][i], b[1][i], b[0][i] = temp[0], temp[1], temp[2], temp[3]
        return b
    return b
def randomPiece(b):
    foundZero = False
    while not foundZero:
        x = random.randint(0,15)
        if b[int(x/4)][x%4] == 0:
            foundZero = True
            y = random.randint(0,9)
            if y == 9:
                b[int(x/4)][x%4] = 4
            else:
                b[int(x/4)][x%4] = 2
    return b


def spaces(x):
    if x<10:
        return "   "
    elif x<100:
        return "  "
    elif x<1000:
        return " "
    return ""
def display(b, s, h):
    disp = "Score: "
    disp += str(s) + " High Score: " + str(h) + "\n"
    for i in range(4):
        for j in range(4):
            disp += spaces(b[i][j]) + str(b[i][j]) + " "
        disp += "\n"
    print(disp)

def main():
    print("2048: Use WASD to move the board")
    high = 0
    running = True
    while running:
        board = []
        for i in range(4):
            board.append([0, 0, 0, 0])
        score = 0
        board = randomPiece(board)
        board = randomPiece(board)
        display(board, score, high)
        playing = True
        win = False
        first = True
        playable = True
        while playing:
            if playable:
                copyBoard = copy(board)
                move = input().lower()
                board = collapse(move, board)
                temp1 = merge(move, board)
                board = temp1[0]
                score += temp1[1]
                if score > high:
                    high = score
                board = collapse(move, board)
            zeros = False
            playable = movesLeft(board)
            for i in range(4):
                for j in range(4):
                    if board[i][j] == 0:
                        zeros = True
                    if board[i][j] == 2048 and not win:
                        win = True
            if (copyBoard != board) and zeros:
                board = randomPiece(board)
            if win and first:
                inp = 'a'
                display(board, score, high)
                while inp != 'y' and inp != 'n':
                    inp = input('You Win! Continue? (y/n)\n')
                    if inp == 'n':
                        playing = False
                    elif inp == 'y':
                        first = False
            if not playable:
                playing = False
            display(board, score, high)
        inp = 'a'
        while inp != 'y' and inp != 'n':
            inp = input('Game Over! Play again? (y/n)\n')
            if inp == 'n':
                running = False


main()


