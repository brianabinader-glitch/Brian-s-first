"""
🐍 Snake Game - Classic arcade game implementation
Demonstrates: pygame, game loops, collision detection, event handling
"""

import pygame
import random
import sys
from utils.colors import GameColors
from utils.helpers import clear_screen, print_colored, format_time

class SnakeGame:
    def __init__(self):
        # Initialize pygame
        pygame.init()
        
        # Game constants
        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 600
        self.GRID_SIZE = 20
        self.GRID_WIDTH = self.WINDOW_WIDTH // self.GRID_SIZE
        self.GRID_HEIGHT = self.WINDOW_HEIGHT // self.GRID_SIZE
        
        # Colors
        self.BLACK = GameColors.BACKGROUND
        self.GREEN = GameColors.SNAKE_HEAD
        self.DARK_GREEN = GameColors.SNAKE_BODY
        self.RED = GameColors.FOOD
        self.WHITE = GameColors.TEXT
        
        # Game state
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption("🐍 Snake Game - Python Games Collection")
        
        # Font for score display
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
        self.reset_game()
    
    def reset_game(self):
        """Reset the game to initial state"""
        # Snake starts in the center, moving right
        center_x = self.GRID_WIDTH // 2
        center_y = self.GRID_HEIGHT // 2
        self.snake = [(center_x, center_y), (center_x - 1, center_y), (center_x - 2, center_y)]
        self.direction = (1, 0)  # Moving right
        self.score = 0
        self.game_over = False
        self.paused = False
        self.start_time = pygame.time.get_ticks()
        self.spawn_food()
    
    def spawn_food(self):
        """Spawn food at a random location"""
        while True:
            x = random.randint(0, self.GRID_WIDTH - 1)
            y = random.randint(0, self.GRID_HEIGHT - 1)
            if (x, y) not in self.snake:
                self.food = (x, y)
                break
    
    def handle_events(self):
        """Handle pygame events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                elif event.key == pygame.K_SPACE:
                    self.paused = not self.paused
                elif event.key == pygame.K_r and self.game_over:
                    self.reset_game()
                elif not self.game_over and not self.paused:
                    # Direction controls
                    if event.key == pygame.K_UP and self.direction != (0, 1):
                        self.direction = (0, -1)
                    elif event.key == pygame.K_DOWN and self.direction != (0, -1):
                        self.direction = (0, 1)
                    elif event.key == pygame.K_LEFT and self.direction != (1, 0):
                        self.direction = (-1, 0)
                    elif event.key == pygame.K_RIGHT and self.direction != (-1, 0):
                        self.direction = (1, 0)
        return True
    
    def update_game(self):
        """Update game logic"""
        if self.game_over or self.paused:
            return
        
        # Move snake
        head_x, head_y = self.snake[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        
        # Check wall collision
        if (new_head[0] < 0 or new_head[0] >= self.GRID_WIDTH or
            new_head[1] < 0 or new_head[1] >= self.GRID_HEIGHT):
            self.game_over = True
            return
        
        # Check self collision
        if new_head in self.snake:
            self.game_over = True
            return
        
        # Add new head
        self.snake.insert(0, new_head)
        
        # Check food collision
        if new_head == self.food:
            self.score += 10
            self.spawn_food()
        else:
            # Remove tail if no food eaten
            self.snake.pop()
    
    def draw_game(self):
        """Draw the game"""
        self.screen.fill(self.BLACK)
        
        # Draw snake
        for i, segment in enumerate(self.snake):
            x = segment[0] * self.GRID_SIZE
            y = segment[1] * self.GRID_SIZE
            color = self.GREEN if i == 0 else self.DARK_GREEN
            pygame.draw.rect(self.screen, color, (x, y, self.GRID_SIZE, self.GRID_SIZE))
            
            # Add border to snake segments
            pygame.draw.rect(self.screen, self.WHITE, (x, y, self.GRID_SIZE, self.GRID_SIZE), 1)
        
        # Draw food
        food_x = self.food[0] * self.GRID_SIZE
        food_y = self.food[1] * self.GRID_SIZE
        pygame.draw.rect(self.screen, self.RED, (food_x, food_y, self.GRID_SIZE, self.GRID_SIZE))
        
        # Draw score
        score_text = self.font.render(f"Score: {self.score}", True, self.WHITE)
        self.screen.blit(score_text, (10, 10))
        
        # Draw time
        elapsed_time = (pygame.time.get_ticks() - self.start_time) / 1000
        time_text = self.small_font.render(f"Time: {format_time(elapsed_time)}", True, self.WHITE)
        self.screen.blit(time_text, (10, 50))
        
        # Draw instructions
        if not self.game_over:
            instructions = [
                "Use arrow keys to move",
                "SPACE: Pause/Resume",
                "ESC: Quit"
            ]
            for i, instruction in enumerate(instructions):
                text = self.small_font.render(instruction, True, self.WHITE)
                self.screen.blit(text, (10, self.WINDOW_HEIGHT - 80 + i * 20))
        
        # Draw pause message
        if self.paused:
            pause_text = self.font.render("PAUSED - Press SPACE to resume", True, self.WHITE)
            text_rect = pause_text.get_rect(center=(self.WINDOW_WIDTH // 2, self.WINDOW_HEIGHT // 2))
            self.screen.blit(pause_text, text_rect)
        
        # Draw game over message
        if self.game_over:
            game_over_text = self.font.render("GAME OVER!", True, self.RED)
            final_score_text = self.font.render(f"Final Score: {self.score}", True, self.WHITE)
            restart_text = self.small_font.render("Press R to restart or ESC to quit", True, self.WHITE)
            
            # Center the text
            game_over_rect = game_over_text.get_rect(center=(self.WINDOW_WIDTH // 2, self.WINDOW_HEIGHT // 2 - 40))
            score_rect = final_score_text.get_rect(center=(self.WINDOW_WIDTH // 2, self.WINDOW_HEIGHT // 2))
            restart_rect = restart_text.get_rect(center=(self.WINDOW_WIDTH // 2, self.WINDOW_HEIGHT // 2 + 40))
            
            self.screen.blit(game_over_text, game_over_rect)
            self.screen.blit(final_score_text, score_rect)
            self.screen.blit(restart_text, restart_rect)
        
        pygame.display.flip()
    
    def run(self):
        """Main game loop"""
        print_colored("🐍 Starting Snake Game...", "green")
        print_colored("Use arrow keys to move, SPACE to pause, ESC to quit", "yellow")
        
        running = True
        while running:
            running = self.handle_events()
            self.update_game()
            self.draw_game()
            self.clock.tick(10)  # 10 FPS for smooth gameplay
        
        pygame.quit()
        print_colored("🐍 Snake Game ended. Thanks for playing!", "cyan")
