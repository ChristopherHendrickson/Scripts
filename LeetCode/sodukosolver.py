#Bruteforce Soduko solver

class Solution:
    
    def updateDicts(self,rows,columns,squares):
        #create/update dictionarys containing values in each row, column, and square 

        for i in range(9):
            columns[str(i)] = [self.board[x][i] for x in range(9)]
            rows[str(i)] = self.board[i]
        
        newSquares = {
            '0':[],'1':[],'2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[],
        }

        for i in range(9):
            for ii in range(9):
                key=str(3*(i//3)+ii//3)
                newSquares[key].append(self.board[i][ii])
        for (key,value) in newSquares.items():
            squares[key]=value
    
    
    #The solver iterates over a range of 0-80, being each node of the puzzle
    #This function converts the node number to a row and col number of that node in the board object
    def getRowCol(self,node):
        return (node//9,node%9)

    #Check if the value we are trying already occurs on the same row, col or square. Return true if it does not
    def validValueAtNode(self,value,row,col,rowsDict,columnsDict,squaresDict):
        if value > 9:
            return False
        rowKey = str(row)
        colKey = str(col)
        squareKey = str(3*(row//3)+col//3)
        value=str(value)
        return not (value in (rowsDict[rowKey]) or value in (columnsDict[colKey]) or value in (squaresDict[squareKey]))
        


    def solveSudoku(self, board):
        #Save indices of numbers that should not be altered
        self.board=board
        default = []
        for i in range(9):
            for ii in range(9):
                if self.board[i][ii] != '.':
                    default.append(str(i)+','+str(ii))
        #initialize dictionarys to store values in each row, column and square to make comparisons
        rowsDict = {
            '0':[],'1':[],'2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[],
        }
        columnsDict = {
            '0':[],'1':[],'2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[],
        }
        squaresDict = {'0':[],'1':[],'2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[],
        }

        
        self.updateDicts(rowsDict,columnsDict,squaresDict)


        nodeTrying = 0
        while True:
            row,col = self.getRowCol(nodeTrying)

            #move passed nodes that should not be altered
            while str(row)+','+str(col) in default:
                nodeTrying+=1 
                row,col = self.getRowCol(nodeTrying)
            
            if nodeTrying == 81: #if we make it passed the last node in the puzzle, we have solved it
                break
            
            #Find the starting value to try in the node. eg if we previously tried 4 and it failed later in the puzzle, continue here from 5
            if self.board[row][col] == '.':
                rangeStart = 1
            else:
                rangeStart=int(self.board[row][col])+1
            
            #iterate over the possible alues in the noe and check if valid
            for value in range(rangeStart,10):
                isValid=False
                if self.validValueAtNode(value,row,col,rowsDict,columnsDict,squaresDict):
                    isValid = True
                    nodeTrying+=1
                    self.board[row][col]=str(value)
                    self.updateDicts(rowsDict,columnsDict,squaresDict)
                    break
            
            #if we get to 9 and it still wasnt valid, an earlier number was incorrect
            if value >= 9 and not isValid: 
                isValid = True
                self.board[row][col]='.'
                self.updateDicts(rowsDict,columnsDict,squaresDict)
                nodeTrying-=1 
                row,col = self.getRowCol(nodeTrying)

                #Move backwards until we are not at an unchangeable number, and until we are at a node that was not 9.
                #If the node was 9 and we know this variation does not work, then the error is in an earlier node, so we must also reset this value
                while str(row)+','+str(col) in default or self.board[row][col]=='9':
                    if str(row)+','+str(col) not in default:
                        self.board[row][col]='.'
                        self.updateDicts(rowsDict,columnsDict,squaresDict)
                    nodeTrying-=1 
                    row,col = self.getRowCol(nodeTrying)

                
                
            



board = [["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]]

answer = [["5","3","4","6","7","8","9","1","2"],
        ["6","7","2","1","9","5","3","4","8"],
        ["1","9","8","3","4","2","5","6","7"],
        ["8","5","9","7","6","1","4","2","3"],
        ["4","2","6","8","5","3","7","9","1"],
        ["7","1","3","9","2","4","8","5","6"],
        ["9","6","1","5","3","7","2","8","4"],
        ["2","8","7","4","1","9","6","3","5"],
        ["3","4","5","2","8","6","1","7","9"]]

Solution().solveSudoku(board)
print(board)
print(board==answer)