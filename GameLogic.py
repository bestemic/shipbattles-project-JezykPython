class GameLogic:
    ships = [4, 3, 3, 2, 2, 1, 1, 1]

    # TODO end function
    def placeShip(self, board):
        for i in self.ships:
            while(True):
                board.printBoard()
                print("\033[93mSetting ships\033[0m")
                x, y, layout = self.getCords()
                print(self.check(x, y, layout, i, board.playerBoard))
                break
            break

    # TODO exception throwing and messeging
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
                    print(cords[0])
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
                    if board[x][y+1] != "O":
                        return False
        return True

    # TODO update check?
    # TODO putting ships on correct coordinates
    # TODO playing game
    # TODO menu
    # TODO instructions
    # TODO tests
    # TODO documentation
