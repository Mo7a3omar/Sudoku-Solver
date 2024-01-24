import numpy as np
import tkinter as tk
import random

class SudokuSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.create_gui()

    def create_gui(self):
        self.canvas = tk.Canvas(self.root, width=450, height=450, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        solve_button = tk.Button(self.root, text="Solve", command=self.solve_sudoku)
        solve_button.pack(pady=10)

        clear_button = tk.Button(self.root, text="Clear", command=self.clear_board)
        clear_button.pack(pady=10)

        self.generate_sudoku_puzzle()
        self.draw_board()
        self.draw_numbers()

    def generate_sudoku_puzzle(self):
        self.original_puzzle = np.zeros((9, 9), dtype=int)
        self.sudoku_puzzle = np.zeros((9, 9), dtype=int)
        self.excluded_numbers = [[set() for _ in range(9)] for _ in range(9)]
        self.fill_values()

    def fill_values(self):
        for _ in range(random.randint(17, 25)):
            row, col, num = random.randint(0, 8), random.randint(0, 8), random.randint(1, 9)
            while not self.is_valid_entry(row, col, num):
                row, col, num = random.randint(0, 8), random.randint(0, 8), random.randint(1, 9)
            self.original_puzzle[row, col] = num
            self.sudoku_puzzle[row, col] = num

    def is_valid_entry(self, row, col, num):
        return (
            num not in self.original_puzzle[row, :] and
            num not in self.original_puzzle[:, col] and
            num not in self.original_puzzle[row - row % 3: row - row % 3 + 3, col - col % 3: col - col % 3 + 3]
        )

    def draw_board(self):
        for i in range(10):
            width = 2 if i % 3 == 0 else 1
            self.canvas.create_line(i * 50, 0, i * 50, 450, width=width, fill="black")
            self.canvas.create_line(0, i * 50, 450, i * 50, width=width, fill="black")

    def draw_numbers(self):
        self.canvas.delete("numbers")
        for i in range(9):
            for j in range(9):
                value = self.sudoku_puzzle[i, j]
                x = j * 50 + 25
                y = i * 50 + 25
                color = "black" if value != 0 else "blue"
                self.canvas.create_text(x, y, text="" if value == 0 else str(value),
                                        fill=color, font=("Arial", 14, "bold"), tags="numbers")

    def clear_board(self):
        self.generate_sudoku_puzzle()
        self.draw_numbers()

    def possible(self, row, col, num):
        return (
            num not in self.sudoku_puzzle[row, :] and
            num not in self.sudoku_puzzle[:, col] and
            num not in self.sudoku_puzzle[row - row % 3: row - row % 3 + 3, col - col % 3: col - col % 3 + 3] and
            num not in self.excluded_numbers[row][col]
        )

    def update_domains(self, row, col, num):
        for i in range(9):
            if self.sudoku_puzzle[row, i] == 0:
                self.excluded_numbers[row][i].add(num)
            if self.sudoku_puzzle[i, col] == 0:
                self.excluded_numbers[i][col].add(num)

        box_start_row, box_start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(box_start_row, box_start_row + 3):
            for j in range(box_start_col, box_start_col + 3):
                if self.sudoku_puzzle[i, j] == 0:
                    self.excluded_numbers[i][j].add(num)

    def solve_sudoku(self):
        self.sudoku_puzzle = np.copy(self.original_puzzle)
        self.excluded_numbers = [[set() for _ in range(9)] for _ in range(9)]
        self.draw_numbers()  # Redraw the original puzzle
        self.solution()

    def solution(self):
        empty_cells = [(row, col) for row in range(9) for col in range(9) if self.sudoku_puzzle[row, col] == 0]
        if not empty_cells:
            return True  # Puzzle solved

        row, col = min(empty_cells, key=lambda x: self.count_legal_values(x[0], x[1]))
        for num in range(1, 10):
            if self.possible(row, col, num):
                self.sudoku_puzzle[row, col] = num
                self.update_domains(row, col, num)
                self.draw_numbers()
                self.root.update_idletasks()
                self.root.after(100)  # Add a small delay to make solving visible
                if self.solution():
                    return True

                self.sudoku_puzzle[row, col] = 0
                self.update_domains(row, col, num)
                self.draw_numbers()
                self.root.update_idletasks()
                self.root.after(100)  # Add a small delay to make backtracking visible

        return False

    def count_legal_values(self, row, col):
        count = 0
        for num in range(1, 10):
            if self.possible(row, col, num):
                count += 1
        return count

if __name__ == "__main__":
    root = tk.Tk()
    sudoku_solver_gui = SudokuSolverGUI(root)
    root.mainloop()
