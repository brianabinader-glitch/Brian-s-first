"""
Helper functions for games
"""

import random
import time
from colorama import Fore, Style

def clear_screen():
    """Clear the console screen"""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def print_colored(text, color=Fore.WHITE):
    """Print colored text"""
    print(f"{color}{text}{Style.RESET_ALL}")

def get_random_position(width, height):
    """Get a random position within given bounds"""
    return (random.randint(0, width-1), random.randint(0, height-1))

def format_time(seconds):
    """Format seconds into MM:SS format"""
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f"{minutes:02d}:{seconds:02d}"

def validate_input(prompt, valid_options=None, input_type=str):
    """Validate user input"""
    while True:
        try:
            user_input = input(prompt)
            if input_type != str:
                user_input = input_type(user_input)
            
            if valid_options and user_input not in valid_options:
                print_colored(f"Please enter one of: {', '.join(map(str, valid_options))}", Fore.RED)
                continue
                
            return user_input
        except ValueError:
            print_colored("Invalid input! Please try again.", Fore.RED)
        except KeyboardInterrupt:
            print_colored("\nGoodbye!", Fore.CYAN)
            exit()

def animate_text(text, delay=0.05):
    """Animate text character by character"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
