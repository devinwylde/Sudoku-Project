""" COP 3502c -- Project 4: Sudoku
---> GROUP 102 <---
Created by: Harper Fuchs, Blake Wood, Devin Wylde, and Maddy Wirbel
Due Date: December 6th, 2022 """

from board import Board
from random import randint

class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
      # creates an instance of SudokuGenerator
        self.box_width = int(row_length ** 0.5)
        self.board = Board(row_length)
        self.removed_cells = removed_cells

    def get_board(self):
        return self.board

    def valid_in_row(self, row, num):
        # determines if a number is already in a row
      for tile in self.board.boxes[row]:
            if tile.value == num:
                return False
      return True

    def valid_in_col(self, col, num):
      # determines if a number is already in a column
        for row in self.board.boxes:
            if row[col].value == num:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):
      # determines if a number is already in a 3x3 box  
      for i in range(row_start, row_start+3):
            for j in range(col_start, col_start+3):
                if self.board.boxes[i][j].value == num:
                    return False
      return True

    def is_valid(self, row, col, num):
        return self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(row-row%3, col-col%3, num)

    def fill_board(self, position, nums):
        run = True

        while run:
            valid = False
            idx = 0

            while True:
                # break if no numbers to choose or if no conflicts from placing number
                if len(nums) == 0 or valid:
                    break

                # choose an index from list of possible numbers
                idx = randint(0, len(nums) - 1)
                # check for conflicts on number
                valid = self.is_valid(position[0], position[1], nums[idx])
                # place number in grid
                self.board.boxes[position[0]][position[1]].value = nums[idx]
                # delete number from list
                del nums[idx]

            # if no numbers worked, remove number (for backtracking) and return false
            if len(nums) == 0:
                self.board.boxes[position[0]][position[1]].value = -1
                return False

            # if all numbers were placed (at final tile), return true
            if position == [8, 8]:
                return True

            # otherwise (worked and not done), iterate position, run next
            iterated_position = self.board.iterate_by_box(position.copy())
            run = not self.fill_board(iterated_position[0], [1, 2, 3, 4, 5, 6, 7, 8, 9] if (not iterated_position[1]) else nums)
        return True

    def check_solutions(self, position=0):
        # if tile already filled, skip
        if self.board.boxes[position // 9][position % 9].value != -1:
            # unless reached the end, in which case return 1
            if position == 80:
                return 1
            return self.check_solutions(position + 1)

        possible_solutions = 0
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        while True:
            # break when no more numbers to check
            if len(nums) == 0:
                break

            # choose an index from list of possible numbers
            idx = randint(0, len(nums) - 1)
            # check for conflicts on number
            valid = self.is_valid(position // 9, position % 9, nums[idx])
            # place number in grid
            self.board.boxes[position // 9][position % 9].value = nums[idx]
            # delete number from list
            del nums[idx]

            # iterates to check solutions in next
            if valid and position < 80:
                possible_solutions += self.check_solutions(position + 1)
            # however, if reached the end, add 1 to solutions
            elif valid:
                possible_solutions += 1

        # reset tile, return found solutions
        self.board.boxes[position // 9][position % 9].value = -1
        return possible_solutions

    def remove_cells(self):
      # function to remove cells from the completed board in order to setup the game  
      removed = 0
      while removed < self.removed_cells:
          selection = [randint(0, 8), randint(0, 8)]
          if self.board.boxes[selection[0]][selection[1]].value == -1:
              continue
          save_value = self.board.boxes[selection[0]][selection[1]].value
          self.board.boxes[selection[0]][selection[1]].value = -1
          self.board.boxes[selection[0]][selection[1]].is_set = False

          solutions = self.check_solutions()

          if solutions == 1:
              # determines if cells can be edited
              self.board.boxes[selection[0]][selection[1]].can_edit = True
              self.board.boxes[selection[0]][selection[1]].is_perm = False
              removed += 1
          else:
              self.board.boxes[selection[0]][selection[1]].value = save_value
              self.board.boxes[selection[0]][selection[1]].is_set = True


def generate_sudoku(size, removed):
    # function to generate the sudoku board solutions
    generator = SudokuGenerator(size, removed)
    generator.fill_board([0, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9])

    init_board = []
    for row in range(0, size):
        init_board.append([])
        for col in range(0, size):
            init_board[-1].append(generator.board.boxes[row][col].value)
    
    generator.remove_cells()
    return generator.get_board(), init_board
  