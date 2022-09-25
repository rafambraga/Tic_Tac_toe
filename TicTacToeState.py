#class that implements a state and the playing logic of the TicTacToe game.
import Square
from TicTacToeAction import TicTacToeAction


class TicTacToeState:
    # Updates the utility value.
    def updateUtility(self):
        print ("Updates the utility value.")
        # TODO The utility value for the TicTacToe game is defined as follows:
        #   - if player has three marks in a row, it is 1
        #   - if the other player has three marks in a row, it is -1
        #   - otherwise it is 0
        #   Note tha "three marks in a row" can actually be a row, a column
        #   or a diagonal.So basically, first find out if there are three
        #   identical values in a row, and if so, check whether the marks belong
        #   to player or not.
        
        if self.field[0]=='X' and self.field[1]=='X' and self.field[2]=='X' or self.field[3]=='X' and self.field[4]=='X' and self.field[5]=='X' or self.field[6]=='X' and self.field[7]=='X' and self.field[8]=='X' or self.field[0]=='X' and self.field[3]=='X' and self.field[6]=='X' or self.field[1]=='X' and self.field[4]=='X' and self.field[7]=='X' or self.field[2]=='X' and self.field[5]=='X' and self.field[8]=='X' or self.field[0]=='X' and self.field[4]=='X' and self.field[8]=='X' or self.field[2]=='X' and self.field[4]=='X' and self.field[6]=='X':
            self.utility=1
            #print("Utility set to 1")
        elif self.field[0]=='O' and self.field[1]=='O' and self.field[2]=='O' or self.field[3]=='O' and self.field[4]=='O' and self.field[5]=='O' or self.field[6]=='O' and self.field[7]=='O' and self.field[8]=='O' or self.field[0]=='O' and self.field[3]=='O' and self.field[6]=='O' or self.field[1]=='O' and self.field[4]=='O' and self.field[7]=='O' or self.field[2]=='O' and self.field[5]=='O' and self.field[8]=='O' or self.field[0]=='O' and self.field[4]=='O' and self.field[8]=='O' or self.field[2]=='O' and self.field[4]=='O' and self.field[6]=='O':
            self.utility=-1
            #print("Utility set to -1")
        else:
            self.utility=0


    # Default constructor.
    def __init__(self):
        self.field = [] # < The field, consisting of nine squares.First three values correspond to first row, and so on.
        for i in range(9):
            self.field.append(Square.EMPTY)
        self.player = Square.X # < The player, either X or O.
        self.playerToMove = Square.X # < The player that is about to move.
        self.utility = 0 # < The utility value of this state.Can be 0, 1 (won) or -1 (lost).

    def getActions(self):
        #  TODO For the TicTacToe game, there is one valid action
        #   for each empty square.The action would then consist
        #   of the position of the empty square and the "color" of
        #   the player to move.
        print("getActions")
        list=[]
        for i in range(len(self.field)):
            if self.field[i] == Square.EMPTY:
                list.append(TicTacToeAction(self.player, i))
        return list

    def getUtility(self):
        return self.utility

    def getResult(self,action):
        #TODO Create a new state and copy all the contents of the current state
        #  to the new one (in particular the field and the player).
        # The player to move must be switched. Then incorporate the action into
        # the field of the new state. Finally, compute the utility of the new state using updateUtility().
        print("getResult")
        state = TicTacToeState()
        state.field = self.field
        move = action.getPlayer()
        position=action.getPosition()
        state.field[position]= move
        state.updateUtility()
        state.utility=state.getUtility()
        if move == Square.X:
            state.playerToMove = Square.O
            state.player = Square.O
        else:
            state.playerToMove = Square.X
            state.player = Square.X
        return state

    def  isTerminal(self):
        #TODO Hint: the utility value has specific values if one of
        # the players has won, which is a terminal state. However,
        # you will also have to check for terminal states in which
        # no player has won, which can not be inferred immediately
        # from the utility value.
        boardFull = False
        for i in range(len(self.field)):
            if self.field[i] == Square.EMPTY:
                boardFull = False
            else:
                boardFull = True
                
        if self.getUtility() !=0:
            return True
        elif boardFull == True:
            return True
        else:
            return False

    def printresult(self):
        s = "" + self.field[0] + "|" + self.field[1] + "|" + self.field[2] + "\n"
        s += "-+-+-\n"
        s += self.field[3] + "|" + self.field[4] + "|" + self.field[5] + "\n"
        s += "-+-+-\n"
        s += self.field[6] + "|" + self.field[7] + "|" + self.field[8] + "\n"
        print(s)
        

    def getPlayer(self):
        return self.player
    
    def restoreState(self,action):
        state = TicTacToeState()
        state.field = self.field
        state.utility = self.utility
        state.player = self.player
        if self.playerToMove == Square.X:
            state.playerToMove = Square.O
        else: 
            state.playerToMove = Square.X
        position=action.getPosition()
        state.field[position]= Square.EMPTY
        state.updateUtility()
    
