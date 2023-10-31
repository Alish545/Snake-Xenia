import pygame
import random
import sys

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
SNAKE_SIZE = 20
SNAKE_SPEED = 10

class Snake:
    def __init__(self):
        self.body = [pygame.Rect(100, 50, SNAKE_SIZE, SNAKE_SIZE)]
        self.direction = "RIGHT"

    def change_direction(self, new_direction):
        if new_direction == "UP" and self.direction != "DOWN":
            self.direction = "UP"
        if new_direction == "DOWN" and self.direction != "UP":
            self.direction = "DOWN"
        if new_direction == "LEFT" and self.direction != "RIGHT":
            self.direction = "LEFT"
        if new_direction == "RIGHT" and self.direction != "LEFT":
            self.direction = "RIGHT"

    def move(self):
        head = self.body[0].copy()
        if self.direction == "RIGHT":
            head.x += SNAKE_SIZE
        if self.direction == "LEFT":
            head.x -= SNAKE_SIZE
        if self.direction == "UP":
            head.y -= SNAKE_SIZE
        if self.direction == "DOWN":
            head.y += SNAKE_SIZE
        self.body.insert(0, head)
        if not self.check_collision_with_food():
            self.body.pop()

    def draw(self, window):
        for segment in self.body:
            pygame.draw.rect(window, BLUE, segment)

    def check_collision_with_food(self):
        return self.body[0].colliderect(game.food.rect)

    def check_collision_with_walls(self):
        return (
            self.body[0].left < 0
            or self.body[0].right > WIDTH
            or self.body[0].top < 0
            or self.body[0].bottom > HEIGHT
        )

    def check_collision_with_self(self):
        return any(self.body[0].colliderect(segment) for segment in self.body[1:])

    def grow(self):
        tail = self.body[-1]
        self.body.append(tail)

class Food:
    def __init__(self):
        self.rect = pygame.Rect(0, 0, SNAKE_SIZE, SNAKE_SIZE)
        self.randomize()

    def draw(self, window):
        pygame.draw.rect(window, BLUE, self.rect)

    def randomize(self):
        self.rect.x = random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
        self.rect.y = random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE

class Button:
    def __init__(self, text, position, action):
        self.text = text
        self.position = position
        self.action = action
        self.font = pygame.font.Font(None, 36)
        text_surface = self.font.render(self.text, True, BLUE)
        self.rect = text_surface.get_rect(center=position)

    def draw(self, window):
        pygame.draw.rect(window, BLUE, self.rect)
        window.blit(self.font.render(self.text, True, WHITE), self.rect)

class SnakeGame:
    def __init__(self):
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.high_score = 0
        self.play_button = Button("Play", (WIDTH // 2, HEIGHT // 2), self.start_game)
        self.play_again_button = Button("Play Again", (WIDTH // 2, HEIGHT // 2 + 50), self.reset_game)
        self.exit_button = Button("Exit", (WIDTH // 2, HEIGHT // 2 + 100), sys.exit)
        self.game_over = False
        self.game_started = False

    def start_game(self):
        self.game_started = True
        self.reset_game()

    def reset_game(self):
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.game_over = False

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and self.game_started:
                    if not self.game_over:
                        if event.key == pygame.K_UP:
                            self.snake.change_direction("UP")
                        elif event.key == pygame.K_DOWN:
                            self.snake.change_direction("DOWN")
                        elif event.key == pygame.K_LEFT:
                            self.snake.change_direction("LEFT")
                        elif event.key == pygame.K_RIGHT:
                            self.snake.change_direction("RIGHT")
                elif event.type == pygame.MOUSEBUTTONDOWN and not self.game_started:
                    if self.play_button.rect.collidepoint(event.pos):
                        self.start_game()
                elif event.type == pygame.MOUSEBUTTONDOWN and self.game_over:
                    if self.play_again_button.rect.collidepoint(event.pos):
                        self.reset_game()
                    elif self.exit_button.rect.collidepoint(event.pos):
                        sys.exit()

            if self.game_started and not self.game_over:
                self.snake.move()
                self.check_collision()

            self.update_display()

            pygame.display.update()
            self.clock.tick(SNAKE_SPEED)

        pygame.quit()

    def check_collision(self):
        if self.snake.body[0].colliderect(self.food.rect):
            self.snake.grow()
            self.food.randomize()
            self.score += 1

            if self.score > self.high_score:
                self.high_score = self.score

        if self.snake.check_collision_with_walls() or self.snake.check_collision_with_self():
            self.game_over = True

    def update_display(self):
        self.window.fill(WHITE)
        if not self.game_started:
            self.play_button.draw(self.window)
        else:
            if self.game_over:
                self.display_game_over()
            else:
                self.snake.draw(self.window)
                self.food.draw(self.window)
                self.display_score()
            if self.game_over:
                self.play_again_button.draw(self.window)
                self.exit_button.draw(self.window)
        self.display_high_score()

    def display_score(self):
        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {self.score}", True, BLUE)
        self.window.blit(text, (10, 10))

    def display_high_score(self):
        font = pygame.font.Font(None, 36)
        text = font.render(f"High Score: {self.high_score}", True, BLUE)
        self.window.blit(text, (WIDTH - 180, 10))

    def display_game_over(self):
        font = pygame.font.Font(None, 72)
        text = font.render("Game Over", True, BLUE)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.window.blit(text, text_rect)

if __name__ == "__main__":
    pygame.init()
    game = SnakeGame()
    game.run()
