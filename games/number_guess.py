"""
🎲 Number Guessing Game - Interactive guessing game with difficulty levels
Demonstrates: random numbers, loops, conditionals, user input, game statistics
"""

import random
import time
from utils.helpers import clear_screen, print_colored, validate_input, animate_text
from colorama import Fore, Style

class NumberGuessingGame:
    def __init__(self):
        self.difficulty_levels = {
            'easy': {'range': (1, 10), 'max_attempts': 5, 'hints': 2},
            'medium': {'range': (1, 50), 'max_attempts': 7, 'hints': 3},
            'hard': {'range': (1, 100), 'max_attempts': 10, 'hints': 4},
            'expert': {'range': (1, 1000), 'max_attempts': 15, 'hints': 5}
        }
        self.stats = {
            'games_played': 0,
            'games_won': 0,
            'total_attempts': 0,
            'best_score': float('inf')
        }
    
    def show_welcome(self):
        """Display welcome message and instructions"""
        clear_screen()
        print_colored("🎲 NUMBER GUESSING GAME 🎲", Fore.CYAN)
        print_colored("=" * 35, Fore.YELLOW)
        print()
        
        animate_text("Welcome to the Number Guessing Game!", 0.03)
        print()
        print_colored("🎯 How to Play:", Fore.GREEN)
        print("• I'll think of a secret number")
        print("• You guess what it is")
        print("• I'll give you hints along the way")
        print("• Try to guess in as few attempts as possible!")
        print()
        print_colored("📊 Difficulty Levels:", Fore.YELLOW)
        for level, info in self.difficulty_levels.items():
            min_num, max_num = info['range']
            attempts = info['max_attempts']
            hints = info['hints']
            print(f"• {level.title()}: Numbers {min_num}-{max_num}, {attempts} attempts, {hints} hints")
        print()
    
    def select_difficulty(self):
        """Let player select difficulty level"""
        print_colored("Choose your difficulty level:", Fore.CYAN)
        options = list(self.difficulty_levels.keys())
        
        for i, level in enumerate(options, 1):
            info = self.difficulty_levels[level]
            min_num, max_num = info['range']
            print(f"{i}. {level.title()} (1-{max_num})")
        
        choice = validate_input(
            f"\nEnter choice (1-{len(options)}): ",
            list(range(1, len(options) + 1)),
            int
        )
        
        return options[choice - 1]
    
    def get_hint(self, secret_number, guess, min_num, max_num, hint_count):
        """Provide a hint to the player"""
        if guess < secret_number:
            if secret_number - guess <= 5:
                return "Very close! Try a bit higher."
            elif secret_number - guess <= 15:
                return "Getting warmer! Go higher."
            else:
                return "Too low! Try a much higher number."
        else:
            if guess - secret_number <= 5:
                return "Very close! Try a bit lower."
            elif guess - secret_number <= 15:
                return "Getting warmer! Go lower."
            else:
                return "Too high! Try a much lower number."
    
    def play_round(self, difficulty):
        """Play a single round of the game"""
        level_info = self.difficulty_levels[difficulty]
        min_num, max_num = level_info['range']
        max_attempts = level_info['max_attempts']
        available_hints = level_info['hints']
        
        secret_number = random.randint(min_num, max_num)
        attempts = 0
        used_hints = 0
        
        clear_screen()
        print_colored(f"🎲 {difficulty.title()} Mode - Number Guessing Game", Fore.CYAN)
        print_colored("=" * 45, Fore.YELLOW)
        print()
        print_colored(f"I'm thinking of a number between {min_num} and {max_num}", Fore.GREEN)
        print_colored(f"You have {max_attempts} attempts and {available_hints} hints", Fore.YELLOW)
        print()
        
        while attempts < max_attempts:
            attempts += 1
            remaining_attempts = max_attempts - attempts + 1
            
            print_colored(f"Attempt {attempts}/{max_attempts}", Fore.BLUE)
            
            # Get player's guess
            guess = validate_input(
                f"Enter your guess ({min_num}-{max_num}): ",
                list(range(min_num, max_num + 1)),
                int
            )
            
            # Check if correct
            if guess == secret_number:
                print_colored("🎉 Congratulations! You guessed it right! 🎉", Fore.GREEN)
                print_colored(f"The secret number was {secret_number}", Fore.CYAN)
                print_colored(f"You used {attempts} attempt(s) and {used_hints} hint(s)", Fore.YELLOW)
                
                # Update statistics
                self.stats['games_played'] += 1
                self.stats['games_won'] += 1
                self.stats['total_attempts'] += attempts
                if attempts < self.stats['best_score']:
                    self.stats['best_score'] = attempts
                
                return True
            
            # Provide hint if available
            if used_hints < available_hints and remaining_attempts > 1:
                use_hint = validate_input(
                    f"Would you like a hint? ({available_hints - used_hints} remaining) (y/n): ",
                    ['y', 'n', 'yes', 'no'],
                    str.lower
                )
                
                if use_hint in ['y', 'yes']:
                    used_hints += 1
                    hint = self.get_hint(secret_number, guess, min_num, max_num, used_hints)
                    print_colored(f"💡 Hint: {hint}", Fore.MAGENTA)
            
            # Show remaining attempts
            if remaining_attempts > 1:
                print_colored(f"You have {remaining_attempts - 1} attempt(s) left", Fore.RED)
            print()
        
        # Game over - didn't guess correctly
        print_colored("😞 Game Over! You ran out of attempts.", Fore.RED)
        print_colored(f"The secret number was {secret_number}", Fore.CYAN)
        
        # Update statistics
        self.stats['games_played'] += 1
        self.stats['total_attempts'] += attempts
        
        return False
    
    def show_statistics(self):
        """Display player statistics"""
        if self.stats['games_played'] == 0:
            print_colored("No games played yet!", Fore.YELLOW)
            return
        
        clear_screen()
        print_colored("📊 YOUR GAME STATISTICS 📊", Fore.CYAN)
        print_colored("=" * 30, Fore.YELLOW)
        print()
        
        win_rate = (self.stats['games_won'] / self.stats['games_played']) * 100
        avg_attempts = self.stats['total_attempts'] / self.stats['games_played']
        
        print_colored(f"Games Played: {self.stats['games_played']}", Fore.GREEN)
        print_colored(f"Games Won: {self.stats['games_won']}", Fore.GREEN)
        print_colored(f"Win Rate: {win_rate:.1f}%", Fore.BLUE)
        print_colored(f"Average Attempts: {avg_attempts:.1f}", Fore.BLUE)
        
        if self.stats['best_score'] != float('inf'):
            print_colored(f"Best Score: {self.stats['best_score']} attempts", Fore.YELLOW)
        
        print()
        print_colored("Press Enter to continue...", Fore.CYAN)
        input()
    
    def play(self):
        """Main game loop"""
        self.show_welcome()
        
        while True:
            # Show menu
            clear_screen()
            print_colored("🎲 NUMBER GUESSING GAME - MAIN MENU 🎲", Fore.CYAN)
            print_colored("=" * 40, Fore.YELLOW)
            print()
            print_colored("1. Play Game", Fore.GREEN)
            print_colored("2. View Statistics", Fore.BLUE)
            print_colored("3. Exit", Fore.RED)
            print()
            
            choice = validate_input(
                "Enter your choice (1-3): ",
                [1, 2, 3],
                int
            )
            
            if choice == 1:
                difficulty = self.select_difficulty()
                self.play_round(difficulty)
                
                # Ask if they want to play again
                play_again = validate_input(
                    "\nPlay another round? (y/n): ",
                    ['y', 'n', 'yes', 'no'],
                    str.lower
                )
                
                if play_again not in ['y', 'yes']:
                    print_colored("Thanks for playing! 👋", Fore.CYAN)
                    break
                    
            elif choice == 2:
                self.show_statistics()
                
            elif choice == 3:
                print_colored("Thanks for playing the Number Guessing Game! 👋", Fore.CYAN)
                break
