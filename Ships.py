
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
                    print(f" \u001B[41m\u001B[30m{j}\033[0m", end=" ")
                elif(j == 'L'):
                    print(f" \u001B[42m\u001B[30m{j}\033[0m", end=" ")
                elif(j == 'S'):
                    print(f" \u001B[43m\u001B[30m{j}\033[0m", end=" ")
                elif(j == 'N'):
                    print(f" \u001B[44m\u001B[30m{j}\033[0m", end=" ")
                elif(j == 'P'):
                    print(f" \u001B[45m\u001B[30m{j}\033[0m", end=" ")
                elif(j == 'K'):
                    print(f" \u001B[46m\u001B[30m{j}\033[0m", end=" ")
                elif(j == 'Z'):
                    print(f" \u001B[47m\u001B[30m{j}\033[0m", end=" ")
                elif(j == 'F'):
                    print(f" \u001B[100m\u001B[30m{j}\033[0m", end=" ")
                elif(j == 'T'):
                    print(f" \u001B[105m\u001B[30m{j}\033[0m", end=" ")
                else:
                    print(" " + j, end=" ")

            print("           ", end="")

            print(" "+label[i], end='')
            for j in self.__computerBoard[i]:
                if(j == 'X'):
                    print(f" \u001B[41m\u001B[30m{j}\033[0m", end=" ")
                elif(j == 'L'):
                    print(f" \u001B[42m\u001B[30m{j}\033[0m", end=" ")
                elif(j == 'S'):
                    print(f" \u001B[43m\u001B[30m{j}\033[0m", end=" ")
                elif(j == 'N'):
                    print(f" \u001B[44m\u001B[30m{j}\033[0m", end=" ")
                elif(j == 'P'):
                    print(f" \u001B[45m\u001B[30m{j}\033[0m", end=" ")
                elif(j == 'K'):
                    print(f" \u001B[46m\u001B[30m{j}\033[0m", end=" ")
                elif(j == 'Z'):
                    print(f" \u001B[47m\u001B[30m{j}\033[0m", end=" ")
                elif(j == 'F'):
                    print(f" \u001B[100m\u001B[30m{j}\033[0m", end=" ")
                elif(j == 'T'):
                    print(f" \u001B[105m\u001B[30m{j}\033[0m", end=" ")
                else:
                    # if(j=="O" or j == "*"):
                    #     print(" " + j, end=" ")
                    # else:
                    #     print(" " + "O", end=" ")
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
    ships = {
        "Lotniskowiec": (4, 'L'),
        "Szturmowiec": (3, 'S'),
        "Niszczyciel": (3, 'N'),
        "Fregata": (2, 'F'),
        "Pancernik": (2, 'P'),
        "Kuter": (1, 'K'),
        "Zbiornikowiec": (1, 'Z'),
        "Tralowiec": (1, 'T'),
    }

    __trafienie = False
    __next = {}
    __traf = {
        "L" : [], 
        "S" : [], 
        "N" : [], 
        "F" : [], 
        "P" : [], 
        "T" : [], 
        "Z" : [], 
        "K" : []
    }

    skrot = ["L", "S", "N", "F", "P", "T", "Z", "K"]

    # Wstawianie statków gracza
    def placeShips(self, board):
        for ship in self.ships.keys():
            while(True):
                board.printBoard()
                info = self.ships[ship]
                print(f"\033[93mUstawianie: {ship} {info[0]} masztowy\033[0m")
                x, y, layout = self.getCords()
                if(self.check(x, y, layout, info[0], board.playerBoard)):
                    self.placeShip(x, y, layout, info, board.playerBoard)
                    break
                else:
                    print("Nie można wstawić statku w to miejsce")
                    input("Wcisnij cos")
        board.printBoard()

    # Wstawianie statków komputera
    def computerShips(self, board):
        for ship in self.ships.keys():
            while(True):
                x, y, layout = self.getCompCords()
                info = self.ships[ship]
                if(self.check(x, y, layout, info[0], board.computerBoard)):
                    self.placeShip(x, y, layout, info, board.computerBoard)
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
            for i in range(ship[0]):
                board[x + i][y] = ship[1]
        else:
            for i in range(ship[0]):
                board[x][y + i] = ship[1]

    g = 0
    # Ruch gracza
    def playerMove(self, board):
        while(True):
            x, y = self.shootCords()
            info = self.shoot(x, y, board.computerBoard)
            if(info != "used" and info !="miss"):
                board.printBoard()
                self.g+=1
                print("Trafiono")
                self.isSinkplayer(board.computerBoard)
                if self.isWin(board.computerBoard):
                    return True
                continue
            elif(info == "miss"):
                board.printBoard()
                print("Pudło")
                self.g+=1
                break
            elif(info == "used"):
                board.printBoard()
                print("Już tu trafiałeś")
                continue
        return False

    i = 0

    # Ruch komputera
    def computerMove(self, board):
        while(True):
            x, y = self.shootCompCords()
            info = self.shoot(x, y, board.playerBoard)
            if(info != "used" and info !="miss"):
                board.printBoard()
                print("Trafiono")
                self.i += 1
                # input()
                self.__trafienie = True
                self.what(info, x, y)
                self.isSink(board.playerBoard)
                if self.isWin(board.playerBoard):
                    return True
                continue
            elif(info == "miss"):
                board.printBoard()
                print("Pudło")
                self.i += 1
                break
            elif(info == "used"):
                board.printBoard()
                continue
        return False

    def what(self, info, x, y):
        ile = {"L" : 4, "S" : 3, "N" : 3, "F" : 2, "P" : 2, "T" : 1, "Z" : 1, "K" : 1}
        if(len(self.__traf[info])==0):
            self.__traf[info].append((x, y))
            tmp = []
            for i in range(1, ile[info]):
                if(x-i>=0):
                    tmp.append((x-i, y))
                if(x+i<=9):
                    tmp.append((x+i, y))
                if(y-i>=0):
                    tmp.append((x, y-i))
                if(y+i<=9):
                    tmp.append((x, y+i))
            self.__next[info] = tmp
        # elif(len(self.__traf[info])==1):
        #     tmp = self.__traf[info]
        #     print(self.__next)
        #     lista = self.__next[info]
        #     print("Poprzedni", tmp)
        #     if(tmp[0][0]==x):
        #         for l in lista:
        #             if(l[0]!=x):
        #                 lista.remove(l)
        #     elif(tmp[0][1]==y):
                
        #         for l in lista:
        #             if(l[1]!=y):
        #                 lista.remove(l)
        #     self.__next[info] = lista
        #     print(self.__next)
        #     # input()



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
        if(self.__trafienie):
            if(len(self.__next) == 0):
                self.__trafienie = False
            else:
                cords = self.__next.get(next(iter(self.__next)))[0]
                self.__next.get(next(iter(self.__next))).remove(cords)
                return cords[0], cords[1]

        cords = [None, None]
        cords[0] = rand(0, 9)
        cords[1] = rand(0, 9)
        return cords[0], cords[1]

    # Celowanie w tarczę
    def shoot(self, x, y, board):
        if(board[x][y] == "O"):
            board[x][y] = "*"
            return "miss"
        elif(not(board[x][y] == "O" or board[x][y] == "X" or board[x][y] == "*")):
            tmp = board[x][y]
            board[x][y] = "X"
            return tmp
        elif(board[x][y] == "*" or board[x][y] == "X"):
            return "used"

    # Sprawdzenie czy statek został zatopiony
    def isSink(self, board):
        
        
        for ship in self.skrot:
            zatop = True
            for i in range(10):
                for j in range(10):
                    if board[i][j] == ship:
                        zatop = False
            if(zatop):
                print("Zatopiono", ship)
                self.skrot.remove(ship)
                self.__next.pop(ship)
                # input()
                break

    def isSinkplayer(self, board):
        
        
        for ship in self.skrot:
            zatop = True
            for i in range(10):
                for j in range(10):
                    if board[i][j] == ship:
                        zatop = False
            if(zatop):
                print("Zatopiono", ship)
                # self.skrot.remove(ship)
                # self.__next.pop(ship)
                # input()
                break


    # Sprawdzenie czy gra wygrana
    def isWin(self, board):
        for i in range(10):
            for j in range(10):
                if board[i][j] in ["L", "S", "N", "F", "P", "T", "Z", "K"]:
                    return False
        return True

    # TODO update check?
    # TODO menu
    # TODO instructions


board = Board()
game = GameLogic()
game.placeShips(board)
game.computerShips(board)
board.printBoard()





while(True):
    # if(game.playerMove(board)):
    #     print("Gracz wygrał")
    #     break
    # input("Zakończ turę")
    
    if(game.computerMove(board)):
        print("Komputer wygrał")
        break
    # input("Zakończ turę")

print(game.i)
print(game.g)