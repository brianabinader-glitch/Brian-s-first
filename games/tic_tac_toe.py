"""
⭕❌ Tic-Tac-Toe Game - Two-player strategy game
Demonstrates: 2D arrays, game logic, user input validation, win conditions
"""

from utils.helpers import clear_screen, print_colored, validate_input, animate_text
from colorama import Fore, Style

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.winner = None
        self.moves = 0
        
    def print_board(self):
        """Print the current game board"""
        clear_screen()
        print_colored("⭕❌ TIC-TAC-TOE GAME ❌⭕", Fore.CYAN)
        print_colored("=" * 30, Fore.YELLOW)
        print()
        
        for i, row in enumerate(self.board):
            print("   ", end="")
            for j, cell in enumerate(row):
                if cell == 'X':
                    print_colored(f" {cell} ", Fore.RED, end="")
                elif cell == 'O':
                    print_colored(f" {cell} ", Fore.BLUE, end="")
                else:
                    print(f" {cell} ", end="")
                
                if j < 2:
                    print_colored("|", Fore.WHITE, end="")
            print()
            
            if i < 2:
                print_colored("   -----------", Fore.WHITE)
        
        print()
        print_colored(f"Current Player: {self.current_player}", 
                     Fore.RED if self.current_player == 'X' else Fore.BLUE)
        print()
    
    def get_move(self):
        """Get valid move from current player"""
        while True:
            try:
                print_colored("Enter your move (row column): ", Fore.YELLOW, end="")
                move = input().strip().split()
                
                if len(move) != 2:
                    print_colored("Please enter two numbers (row and column)", Fore.RED)
                    continue
                
                row, col = int(move[0]) - 1, int(move[1]) - 1
                
                if not (0 <= row <= 2 and 0 <= col <= 2):
                    print_colored("Please enter numbers between 1 and 3", Fore.RED)
                    continue
                
                if self.board[row][col] != ' ':
                    print_colored("That position is already taken!", Fore.RED)
                    continue
                
                return row, col
                
            except ValueError:
                print_colored("Please enter valid numbers", Fore.RED)
            except KeyboardInterrupt:
                print_colored("\nGame interrupted. Goodbye!", Fore.CYAN)
                exit()
    
    def make_move(self, row, col):
        """Make a move on the board"""
        self.board[row][col] = self.current_player
        self.moves += 1
        
        # Check for win
        if self.check_winner():
            self.winner = self.current_player
            self.game_over = True
        elif self.moves == 9:
            self.game_over = True  # Draw
        else:
            # Switch players
            self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def check_winner(self):
        """Check if current player has won"""
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] == self.current_player:
                return True
        
        # Check columns
        for col in range(3):
            if (self.board[0][col] == self.board[1][col] == 
                self.board[2][col] == self.current_player):
                return True
        
        # Check diagonals
        if (self.board[0][0] == self.board[1][1] == 
            self.board[2][2] == self.current_player):
            return True
        
        if (self.board[0][2] == self.board[1][1] == 
            self.board[2][0] == self.current_player):
            return True
        
        return False
    
    def show_winner(self):
        """Display the winner or draw message"""
        self.print_board()
        print_colored("=" * 30, Fore.YELLOW)
        
        if self.winner:
            winner_color = Fore.RED if self.winner == 'X' else Fore.BLUE
            print_colored(f"🎉 Player {self.winner} wins! 🎉", winner_color)
        else:
            print_colored("🤝 It's a draw! 🤝", Fore.YELLOW)
        
        print_colored("=" * 30, Fore.YELLOW)
    
    def reset_game(self):
        """Reset the game for a new round"""
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.winner = None
        self.moves = 0
    
    def show_instructions(self):
        """Show game instructions"""
        clear_screen()
        print_colored("⭕❌ TIC-TAC-TOE INSTRUCTIONS ❌⭕", Fore.CYAN)
        print_colored("=" * 40, Fore.YELLOW)
        print()
        print_colored("🎯 How to Play:", Fore.GREEN)
        print("• Two players take turns")
        print("• Player X goes first")
        print("• Enter row and column numbers (1-3)")
        print("• Get three in a row to win!")
        print()
        print_colored("📋 Example moves:", Fore.YELLOW)
        print("• '1 1' for top-left corner")
        print("• '2 2' for center")
        print("• '3 3' for bottom-right corner")
        print()
        print_colored("Press Enter to start...", Fore.CYAN)
        input()
    
    def play(self):
        """Main game loop"""
        self.show_instructions()
        
        while True:
            self.print_board()
            
            if not self.game_over:
                row, col = self.get_move()
                self.make_move(row, col)
            else:
                self.show_winner()
                
                # Ask for another game
                play_again = validate_input(
                    "\nPlay again? (y/n): ",
                    ['y', 'n', 'yes', 'no'],
                    str.lower
                )
                
                if play_again in ['y', 'yes']:
                    self.reset_game()
                    continue
                else:
                    print_colored("Thanks for playing Tic-Tac-Toe! 👋", Fore.CYAN)
                    break
