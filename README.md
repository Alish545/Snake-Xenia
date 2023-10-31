# Snake-Xenia

Certainly, I'll explain the code and provide an overview of the Snake game.

# **Code Explanation**:

# 1. Import necessary libraries:

   ```python
   import pygame
   import random
   import sys
   ```

   - `pygame`: Pygame is a Python library for creating 2D games.
   - `random`: Used for generating random numbers.
   - `sys`: Provides access to some variables used or maintained by the interpreter and to functions that interact with the interpreter.

# 2. Define Constants:

   ```python
   WIDTH, HEIGHT = 800, 600
   WHITE = (255, 255, 255)
   BLUE = (0, 0, 255)
   SNAKE_SIZE = 20
   SNAKE_SPEED = 10
   ```

   - `WIDTH` and `HEIGHT` set the dimensions of the game window.
   - `WHITE` and `BLUE` define color constants.
   - `SNAKE_SIZE` sets the size of the snake and food.
   - `SNAKE_SPEED` determines the speed of the snake's movement.

# 3. Define the `Snake` class:

   The `Snake` class represents the player's snake. It has methods for moving the snake, changing its direction, and checking for collisions.

# 4. Define the `Food` class:

   The `Food` class represents the food that the snake needs to eat. It has methods for drawing the food and randomizing its position.

# 5. Define the `Button` class:

   The `Button` class is used to create buttons in the game. It has methods for drawing buttons with text and specifying their actions.

# 6. Define the `SnakeGame` class:

   The `SnakeGame` class manages the game's logic and display. It initializes the game, handles events, and updates the display. It also includes the game loop.

   - `start_game` and `reset_game` methods are used to start and reset the game.
   - `check_collision` checks for collisions between the snake and food or with walls or itself.
   - `update_display` updates the game display.
   - `display_score` and `display_high_score` display the player's score and high score.
   - `display_game_over` displays the "Game Over" message.

# 7. The main game loop is run using `pygame`.

   - The game starts by initializing the Pygame library.
   - An instance of the `SnakeGame` class is created.
   - The game loop handles user input and updates the game state.
   - When the game ends, the program is exited.

# **Game Overview**:

The Snake game is a classic 2D game where the player controls a snake that moves around the screen to eat food while avoiding collisions with the walls and itself. The game features:

- A snake that the player can control using arrow keys.
- Food that appears randomly on the screen for the snake to eat.
- A score that increases each time the snake eats food.
- A high score that is saved and displayed.
- Game over when the snake collides with the walls or itself.

The player's goal is to eat as much food as possible and achieve the highest score without colliding with obstacles. The game provides buttons to start, restart, and exit the game. It offers a simple and fun gameplay experience.
