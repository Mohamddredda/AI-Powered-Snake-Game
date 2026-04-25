import pygame
import random
import sys

pygame.init()

# ma2asat el l3ba
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# alwan
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
dark_green = (3, 125, 80)
brown = (125,56,17)

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

# el sor3a
snake_block = 10
snake_speed = 15 

high_score = 0

# backgrounds
background_image = pygame.image.load(r'pp.jpg')
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

background_image2 = pygame.image.load(r'homepage.jpg') 
background_image2 = pygame.transform.scale(background_image2, (screen_width, screen_height))


def message(msg, color, x, y):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [x, y])


def draw_snake(snake_list, colors):
    """Draw the snake with eyes."""
    for i, part in enumerate(snake_list):
        x, y = part[0], part[1]
        color = colors[i] if i < len(colors) else green 
        pygame.draw.rect(screen, color, [x, y, snake_block, snake_block])

        if i == len(snake_list) - 1: 
            eye_radius = snake_block // 5
            pygame.draw.circle(screen, black,
                               (x + snake_block // 4, y + snake_block // 4),
                               eye_radius)
            pygame.draw.circle(screen, black,
                               (x + 3 * snake_block // 4, y + snake_block // 4), eye_radius)

def minimax(snake_head, food_pos, obstacles, snake_list, depth=3, maximizing=True):
    moves = [(0, -snake_block), (0, snake_block), (-snake_block, 0), (snake_block, 0)]  # up, down, left, right
    best_move = None
    best_score = float('-inf') if maximizing else float('inf')

    def evaluate_move(snake_head, move, food_pos, obstacles, snake_list):
        """Evaluate the score of a given move."""
        new_head = [snake_head[0] + move[0], snake_head[1] + move[1]]

        if new_head[0] < 50 or new_head[0] >= screen_width - 50 or new_head[1] < 50 or new_head[1] >= screen_height - 50:
            return float('-inf') 

        for obstacle in obstacles:
            if (new_head[0] >= obstacle[0] and new_head[0] < obstacle[0] + obstacle[2] and
                new_head[1] >= obstacle[1] and new_head[1] < obstacle[1] + obstacle[3]):
                return float('-inf') 

        # lw 5bt nfso
        if new_head in snake_list[:-1]:
            return float('-inf')

        food_distance = abs(new_head[0] - food_pos[0]) + abs(new_head[1] - food_pos[1])

        return -food_distance 

    for move in moves:
        score = evaluate_move(snake_head, move, food_pos, obstacles, snake_list)
        if maximizing and score > best_score:
            best_score = score
            best_move = move
        elif not maximizing and score < best_score:
            best_score = score
            best_move = move

    return best_move

def ai_move(snake_head, food_pos, obstacles, snake_list):
    return minimax(snake_head, food_pos, obstacles, snake_list)


def create_obstacles(num_obstacles, screen_width, screen_height, snake_block):
    obstacles = []
    for _ in range(num_obstacles):
        x = random.randint(50 // snake_block, (screen_width - 50) // snake_block) * snake_block
        y = random.randint(50 // snake_block, (screen_height - 50) // snake_block) * snake_block
        width = snake_block * 8 
        height = snake_block  
        obstacles.append([x, y, width, height])
    return obstacles



def draw_obstacles(obstacles, color):
    """Draw obstacles on the screen."""
    for obstacle in obstacles:
        pygame.draw.rect(screen, color, [obstacle[0], obstacle[1], obstacle[2], obstacle[3]]) 



def game_loop():
    """Main game loop."""
    global high_score
    game_over = False
    game_close = False

    x1 = screen_width / 2
    y1 = screen_height / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    snake_colors = [green]
    food_x, food_y = None, None

    # EL 7AWAGEZZZZZZ
    obstacles = create_obstacles(8, screen_width, screen_height, snake_block) 
    obstacle_color = brown

    score = 0

    while not game_over:
        while game_close:
            #End screen
            screen.blit(background_image, (0, 0))
            message("Game Over! Click to Continue or Q to Quit", brown, screen_width / 6, screen_height / 3)
            message(f"Your Score: {score}", brown, screen_width / 3, screen_height / 2)
            message(f"High Score: {high_score}", brown, screen_width / 3, screen_height / 1.5)

            if score > high_score:
                high_score = score
                message("New High Score! 🎉", green, screen_width / 4, screen_height / 1.2)

            pygame.display.update()
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        game_loop()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    food_x, food_y = event.pos
                    food_x = food_x // snake_block * snake_block
                    food_y = food_y // snake_block * snake_block

        if food_x is not None and food_y is not None:
            x1_change, y1_change = ai_move([x1, y1], [food_x, food_y], obstacles, snake_list)

        x1 += x1_change
        y1 += y1_change

        # lw 5bt fil frame
        if x1 >= screen_width-50 or x1 < 50 or y1 >= screen_height-50 or y1 < 50:
            game_close = True

        for obstacle in obstacles:
            if (x1 >= obstacle[0] and x1 < obstacle[0] + obstacle[2] and
                y1 >= obstacle[1] and y1 < obstacle[1] + obstacle[3]):
                game_close = True


        screen.blit(background_image, (0, 0))

        draw_obstacles(obstacles, obstacle_color)

        # Draw food
        if food_x is not None and food_y is not None:
            pygame.draw.circle(screen, red, (food_x + snake_block // 2, food_y + snake_block // 2), snake_block // 2)

        # Update snake
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check collision with itself
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake_list, snake_colors)
        message(f"Score: {score}", white, 10, 10)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = None
            food_y = None
            snake_length += 1
            score += 1
            #by2lb fil alwan
            if len(snake_colors) % 2 == 1:
                snake_colors.append(dark_green)
            else:
                snake_colors.append(green)

        clock.tick(snake_speed)

    pygame.quit()
    sys.exit()

def game_start():
    # Home screen
    screen.blit(background_image2, (0, 0))
    message("Welcome to Snake Game!", brown, screen_width / 4, screen_height / 3)
    message("Click to Start", brown, screen_width / 3, screen_height / 2)
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    waiting = False

    screen.blit(background_image, (0, 0))
    message("Click anywhere to put an apple!", brown, screen_width / 4, screen_height / 2)
    pygame.display.update()
    pygame.time.wait(3000)  

    game_loop()

#masili 3ala 7alak
game_start()