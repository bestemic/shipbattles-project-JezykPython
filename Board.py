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
                print(" " + j, end=" ")

            print("           ", end="")

            print(" "+label[i], end='')
            for j in self.__computerBoard[i]:
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

    @playerBoard.setter
    def computerBoard(self, board):
        self.__computerBoard = board

    def clear_screen(self):
        print('\033[2J\033[0;0H')
    
