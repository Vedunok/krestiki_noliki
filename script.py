import random

class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.scores = {"X": 0, "O": 0, "Ничья": 0}
        self.game_mode = None

    def print_board(self):
        print("\n  0   1   2")
        for i, row in enumerate(self.board):
            print(f"{i} " + " | ".join(row))
            if i < 2:
                print("  ---------")

    def check_winner(self):
        # Проверка строк и столбцов
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return self.board[0][i]

        # Проверка диагоналей
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2]

        return None

    def is_board_full(self):
        return all(cell != " " for row in self.board for cell in row)

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            return True
        return False

    def computer_move(self):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == " "]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.make_move(row, col)

    def reset_game(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def play(self):
        print("Добро пожаловать в Крестики-нолики!")
        print("1. Игрок vs Игрок (PvP)")
        print("2. Игрок vs Компьютер (PvE)")
        self.game_mode = input("Выберите режим (1/2): ")

        while True:
            self.print_board()
            winner = self.check_winner()

            if winner:
                print(f"\nИгрок {winner} победил!")
                self.scores[winner] += 1
                self.print_scores()
                if input("Сыграем еще? (да/нет): ").lower() != "да":
                    break
                self.reset_game()
                continue

            if self.is_board_full():
                print("\nНичья!")
                self.scores["Ничья"] += 1
                self.print_scores()
                if input("Сыграем еще? (да/нет): ").lower() != "да":
                    break
                self.reset_game()
                continue

            if self.current_player == "X" or (self.game_mode == "1" and self.current_player == "O"):
                print(f"\nХод игрока {self.current_player}")
                try:
                    row = int(input("Строка (0-2): "))
                    col = int(input("Столбец (0-2): "))
                    if not (0 <= row <= 2 and 0 <= col <= 2):
                        print("Введите числа от 0 до 2!")
                        continue
                    if not self.make_move(row, col):
                        print("Клетка уже занята!")
                        continue
                except ValueError:
                    print("Введите числа!")
                    continue
            elif self.game_mode == "2" and self.current_player == "O":
                print("\nХод компьютера...")
                self.computer_move()

            self.current_player = "O" if self.current_player == "X" else "X"

    def print_scores(self):
        print("\n--- Счет ---")
        print(f"X: {self.scores['X']} | O: {self.scores['O']} | Ничья: {self.scores['Ничья']}")

if __name__ == "__main__":
    game = TicTacToe()
    game.play()