class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        numbers = [str(number) for number in range(1,10)]
        
        def is_valid_row(row, number):
            
            for col in range(9):
                if board[row][col] == number:
                    return False
            return True
        
        def is_valid_column(column, number):
            
            for row in range(9):
                if board[row][column] == number:
                    return False
            return True
        
        def is_valid_box(row, column, number):
            
            start_row = row -  (row % 3)
            start_column = column - (column % 3)
            
            for ro in range(start_row, start_row+3):
                for co in range(start_column, start_column+3):
                    if board[ro][co] == number:
                        return False
            
            return True
        
        def solve(index):
            
            if index == len(cells):
                return True
            
            row, column = cells[index]
            
            for number in numbers:
                if (is_valid_row(row, number) and 
                    is_valid_column(column, number) and
                    is_valid_box(row, column, number)):
                        board[row][column] = number
                        result = solve(index+1)
                        if result:
                            return True
                        else:
                            board[row][column] = "."
        
        cells = list()
        
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    cells.append((row, col))
        
        solve(0)