
from random import randint as rand


class Board:

    # private fields

    __playerBoard = [['O'] * 10 for i in range(10)]
    __computerBoard = [['O'] * 10 for i in range(10)]

    # public methods
    def printBoard(self):
        self.clear_screen()
        label = "ABCDEFGHIJ"
        print("      P_L_A_Y_E_R B_O_A_R_D                    C_O_M_P_U_T_E_R B_O_A_R_D")
        print()
        for i in range(10):
            if(i != 0):
                print(" " + str(i + 1), end=' ')
            else:
                print("   " + str(i + 1), end=' ')
        print("          ", end="")
        for i in range(10):
            if(i != 0):
                print(" " + str(i + 1), end=' ')
            else:
                print("   " + str(i + 1), end=' ')
        print()

        for i in range(10):

            print(" "+label[i], end='')
            for j in self.__playerBoard[i]:
                if(j == 'X'):
                    print(f" \u001B[44m\u001B[30m{j}\033[0m", end=" ")
                else:
                    print(" " + j, end=" ")

            print("           ", end="")

            print(" "+label[i], end='')
            for j in self.__computerBoard[i]:
                if(j == 'X'):
                    print(f" \u001B[44m\u001B[30m{j}\033[0m", end=" ")
                else:
                    print(" " + j, end=" ")

            print()

    @property
    def playerBoard(self):
        return self.__playerBoard

    @property
    def computerBoard(self):
        return self.__computerBoard

    @playerBoard.setter
    def playerBoard(self, board):
        self.__playerBoard = board

    @computerBoard.setter
    def computerBoard(self, board):
        self.__computerBoard = board

    def clear_screen(self):
        print('\033[2J\033[0;0H')


class GameLogic:
    ships = [4, 3, 3, 2, 2, 1, 1, 1]

    # Wstawianie statków gracza
    def placeShips(self, board):
        for ship in self.ships:
            while(True):
                board.printBoard()
                print(f"\033[93mSetting ships {ship}\033[0m")
                x, y, layout = self.getCords()
                if(self.check(x, y, layout, ship, board.playerBoard)):
                    self.placeShip(x, y, layout, ship, board.playerBoard)
                    break
                else:
                    print("Nie można wstawić statku w to miejsce")
                    input("Wcisnij cos")
        board.printBoard()

    # Wstawianie statków komputera
    def computerShips(self, board):
        for ship in self.ships:
            while(True):
                x, y, layout = self.getCompCords()
                if(self.check(x, y, layout, ship, board.computerBoard)):
                    self.placeShip(x, y, layout, ship, board.computerBoard)
                    break

    # TODO exception throwing and messeging
    # Pobieranie współrzędnych od gracza
    def getCords(self):
        dict = {
            "a": 0,
            "b": 1,
            "c": 2,
            "d": 3,
            "e": 4,
            "f": 5,
            "g": 6,
            "h": 7,
            "i": 8,
            "j": 9
        }
        while(True):
            cords = input(
                "Podaj współrzędne i układ (horisontal or vertical) oddzielone spacją: ").lower().split(" ")
            try:
                if(len(cords) != 3):
                    raise Exception("Za mało argumenów")
                if(cords[0] not in dict):
                    raise Exception("Niepoprawne dane")
                else:
                    cords[0] = dict.get(cords[0])
                if(not(cords[2] != "v" or cords[2] != "h")):
                    raise Exception("Niepoprawne dane")
                cords[1] = int(cords[1]) - 1
                if(cords[1] < 0 or cords[1] > 9):
                    raise Exception("Niepoprawne dane")

                return cords[0], cords[1], cords[2]
            except ValueError:
                print("Niepoprawne dane")
            except Exception as e:
                print(e)

    # Losowanie koordynatów komputera
    def getCompCords(self):
        cords = [None, None, None]
        cords[0] = rand(0, 9)
        cords[1] = rand(0, 9)
        cords[2] = "v" if rand(0, 1) else "h"

        return cords[0], cords[1], cords[2]

    # Sprawczanie czy dobre współrzędne
    def check(self, x, y, layout, ship, board):
        if(layout == "v"):
            if(x+ship > 10):
                return False
            else:
                for i in range(ship):
                    if board[x + i][y] != "O":
                        return False
        else:
            if(y+ship > 10):
                return False
            else:
                for i in range(ship):
                    if board[x][y+i] != "O":
                        return False
        return True

    # Dodanie statku na planszę
    def placeShip(self, x, y, layout, ship, board):
        if layout == 'v':
            for i in range(ship):
                board[x + i][y] = "X"
        else:
            for i in range(ship):
                board[x][y + i] = "X"

    # Ruch gracza
    def playerMove(self, board):
        while(True):
            x, y = self.shootCords()
            info = self.shoot(x, y, board.computerBoard)
            if(info == "shoot"):
                board.printBoard()
                print("Trafiono")
                self.isSink(board.computerBoard)
                if self.isWin(board.computerBoard):
                    return True
                continue
            elif(info == "miss"):
                board.printBoard()
                print("Pudło")
                break
            elif(info == "used"):
                board.printBoard()
                print("Już tu trafiałeś")
                continue
        return False
    
    # Ruch komputera
    def computerMove(self, board):
        while(True):
            x, y = self.shootCompCords()
            info = self.shoot(x, y, board.playerBoard)

            if(info == "shoot"):
                board.printBoard()
                print("Trafiono")
                self.isSink(board.playerBoard)
                if self.isWin(board.playerBoard):
                    return True
                continue
            elif(info == "miss"):
                board.printBoard()
                print("Pudło")
                break
            elif(info == "used"):
                board.printBoard()
                continue
        return False

    # Wybieranie koordynatów gracza
    def shootCords(self):
        dict = {
            "a": 0,
            "b": 1,
            "c": 2,
            "d": 3,
            "e": 4,
            "f": 5,
            "g": 6,
            "h": 7,
            "i": 8,
            "j": 9
        }
        while (True):
            cords = input(
                "Podaj współrzędne oddzielone spacją: ").lower().split(" ")
            try:
                if(len(cords) != 2):
                    raise Exception("Za mało argumenów")
                if(cords[0] not in dict):
                    raise Exception("Niepoprawne dane")
                else:
                    cords[0] = dict.get(cords[0])
                cords[1] = int(cords[1]) - 1
                if(cords[1] < 0 or cords[1] > 9):
                    raise Exception("Niepoprawne dane")
                return cords[0], cords[1]
            except ValueError:
                print("Niepoprawne dane")
            except Exception as e:
                print(e)

    # Losowanie koordynatów komputera
    def shootCompCords(self):
        cords = [None, None]
        cords[0] = rand(0, 9)
        cords[1] = rand(0, 9)

        return cords[0], cords[1]

    # Celowanie w tarczę
    def shoot(self, x, y, board):
        if(board[x][y]=="O"):
            board[x][y] = "*"
            return "miss"
        elif(board[x][y]=="X"):
            board[x][y] ="#"
            return "shoot"
        elif(board[x][y]=="X" or board[x][y]=="#"):
            return "used"

    # Sprawdzenie czy statek został zatopiony
    def isSink(self, board):
        pass

    #Sprawdzenie czy gra wygrana
    def isWin(self, board):
        for i in range(10):
            for j in range(10):
                if board[i][j] == 'X':
                    return False
        return True



    # TODO update check?
    # TODO playing game
    # TODO menu
    # TODO instructions


board = Board()
game = GameLogic()
game.placeShips(board)
game.computerShips(board)
board.printBoard()
while(True):
    if(game.playerMove(board)):
        print("Gracz wygrał")
        break
    input("Zakończ turę")
    if(game.computerMove(board)):
        print("Komputer wygrał")
        break
    input("Zakończ turę")
