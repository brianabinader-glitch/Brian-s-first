#!/usr/bin/env python3
"""
🎮 Python Games Collection - Main Launcher
Welcome to your first Python game project!
"""

import sys
import os
from colorama import init, Fore, Style

# Initialize colorama for cross-platform colored output
init()

def print_banner():
    """Print a colorful welcome banner"""
    banner = f"""
{Fore.CYAN}╔══════════════════════════════════════════════════════════════╗
║                    🎮 PYTHON GAMES COLLECTION 🎮                    ║
║                                                                      ║
║  Welcome to your first Python game project!                         ║
║  Choose a game to play and explore Python programming concepts.     ║
╚══════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""
    print(banner)

def print_menu():
    """Print the game selection menu"""
    menu = f"""
{Fore.YELLOW}🎯 Available Games:{Style.RESET_ALL}

{Fore.GREEN}1.{Style.RESET_ALL} 🐍 Snake Game          - Classic arcade game with pygame
{Fore.GREEN}2.{Style.RESET_ALL} ⭕ Tic-Tac-Toe         - Two-player strategy game  
{Fore.GREEN}3.{Style.RESET_ALL} 🎲 Number Guessing     - Interactive guessing game
{Fore.GREEN}4.{Style.RESET_ALL} 📊 Game Statistics     - View your game history
{Fore.RED}5.{Style.RESET_ALL} 🚪 Exit                - Quit the program

{Fore.CYAN}Enter your choice (1-5): {Style.RESET_ALL}"""
    return input(menu)

def check_dependencies():
    """Check if required packages are installed"""
    try:
        import pygame
        return True
    except ImportError:
        print(f"{Fore.RED}❌ pygame is not installed!{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Please run: pip install -r requirements.txt{Style.RESET_ALL}")
        return False

def main():
    """Main game launcher function"""
    print_banner()
    
    # Check dependencies
    if not check_dependencies():
        return
    
    while True:
        try:
            choice = print_menu().strip()
            
            if choice == '1':
                print(f"\n{Fore.GREEN}🐍 Starting Snake Game...{Style.RESET_ALL}")
                from games.snake_game import SnakeGame
                game = SnakeGame()
                game.run()
                
            elif choice == '2':
                print(f"\n{Fore.GREEN}⭕ Starting Tic-Tac-Toe...{Style.RESET_ALL}")
                from games.tic_tac_toe import TicTacToe
                game = TicTacToe()
                game.play()
                
            elif choice == '3':
                print(f"\n{Fore.GREEN}🎲 Starting Number Guessing Game...{Style.RESET_ALL}")
                from games.number_guess import NumberGuessingGame
                game = NumberGuessingGame()
                game.play()
                
            elif choice == '4':
                print(f"\n{Fore.GREEN}📊 Game Statistics{Style.RESET_ALL}")
                print("Feature coming soon! 🚧")
                
            elif choice == '5':
                print(f"\n{Fore.CYAN}👋 Thanks for playing! See you next time!{Style.RESET_ALL}")
                break
                
            else:
                print(f"{Fore.RED}❌ Invalid choice! Please enter 1-5.{Style.RESET_ALL}")
                
        except KeyboardInterrupt:
            print(f"\n\n{Fore.CYAN}👋 Goodbye!{Style.RESET_ALL}")
            break
        except Exception as e:
            print(f"{Fore.RED}❌ An error occurred: {e}{Style.RESET_ALL}")
            print("Please try again or check your installation.")

if __name__ == "__main__":
    main()
