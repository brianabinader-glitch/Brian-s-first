"""
Color constants for console output
"""

# ANSI color codes
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'  # Reset to default

# Game-specific colors
class GameColors:
    SNAKE_HEAD = (0, 255, 0)      # Green
    SNAKE_BODY = (0, 200, 0)      # Darker green
    FOOD = (255, 0, 0)            # Red
    BACKGROUND = (0, 0, 0)        # Black
    TEXT = (255, 255, 255)        # White
    BORDER = (128, 128, 128)      # Gray
