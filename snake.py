from cgitb import grey
import pygame
import numpy as np
import random
from sys import exit
from pygame import surface


def update(c, l, t):
    if c == 0:
        pygame.draw.rect(screen, board_colour,
                    pygame.Rect(l, t, 20, 20))
    if c == 1:
        pygame.draw.rect(screen, blob_colour,
                    pygame.Rect(l, t, 20, 20))
    if c == 2 or c == 3:
        pygame.draw.rect(screen, snake_colour,
                    pygame.Rect(l, t, 20, 20))
    pygame.display.flip()         

# Set game to be active
game_active = True

# Create main screen
(width, height) = (400, 400)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Frank\'s Snake Game')

# Create Snake as an empty list
snake = []

# Blob is 1 square
blob = 1

# Set number of squares on board & dimensions
rows = 20
cols = 20
board = np.zeros((rows, cols))

# Create board
board_r = 240
board_g = 190
board_b = 45
left = 0
top = 0
board_colour = (board_r, board_g, board_b)

# Create and randomly place blob
blob_r = 65
blob_g = 200
blob_b = 124
blob_colour = (blob_r, blob_g, blob_b)

rand_row = random.randint(0, 19)
rand_col = random.randint(0, 19)
top = rand_row * 20
left = rand_col * 20
board[rand_row][rand_col] = 1

# Create and randomly place snake
snake_r = 0
snake_g = 173
snake_b = 59
snake_colour = (snake_r, snake_g, snake_b)

rand_row = random.randint(0, 19)
rand_col = random.randint(0, 19)
rand_dir = random.randint(1, 4)
top = rand_row * 20
left = rand_col * 20
board[rand_row][rand_col] = 2
head = [rand_row, rand_col]
snake.append(head)

# Create snake's tail
if rand_dir == 1:
    direction = "DOWN"
    tail = [rand_row - 1, rand_col]
    snake.append(tail)
    board[int((top - 20) / 20)][int(left / 20)] = 3
elif rand_dir == 2: 
    direction = "LEFT"
    tail = [rand_row, rand_col + 1]
    snake.append(tail)    
    board[int(top / 20)][int((left + 20) / 20)] = 3
elif rand_dir == 3:  
    direction = "UP"
    tail = [rand_row + 1, rand_col]
    snake.append(tail)      
    board[int((top + 20) / 20)][int(left / 20)] = 3
else: 
    direction = "RIGHT"
    tail = [rand_row, rand_col - 1]
    snake.append(tail)       
    board[int(top / 20)][int((left - 20) / 20)] = 3

for row in range(rows):
    top = row * 20
    for col in range(cols):
        left = col * 20
        update(board[row][col], left, top)     

# print(snake)
# print(board)

# Game events
while True:
    for event in pygame.event.get():
        # Able to close window
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if direction == "LEFT" or direction == "UP" or direction == "RIGHT":
                        if snake[0][0] > 0:
                            print("Moving up")
                            direction = "UP"
                            dummy = [snake[0][0] - 1, snake[0][1]]
                            board[snake[0][0] - 1, snake[0][1]] = 2
                            snake.insert(0, dummy)
                            board[snake[1][0], snake[1][1]] = 3
                            board[snake[-1][0], snake[-1][1]] = 0
                            snake.pop()  
                        else:
                            print("Cannot move")                      
                elif event.key == pygame.K_DOWN:
                    if direction == "LEFT" or direction == "DOWN" or direction == "RIGHT":
                        if snake[0][0] < 19:
                            print("Moving down")
                            direction = "DOWN"
                            dummy = [snake[0][0] + 1, snake[0][1]]
                            board[snake[0][0] + 1, snake[0][1]] = 2
                            snake.insert(0, dummy)
                            board[snake[1][0], snake[1][1]] = 3
                            board[snake[-1][0], snake[-1][1]] = 0
                            snake.pop()        
                        else:
                            print("Cannot move")                                              
                elif event.key == pygame.K_LEFT:
                    if direction == "LEFT" or direction == "UP" or direction == "DOWN":
                        if snake[0][1] > 0:
                            print("Moving left")
                            direction = "LEFT"
                            dummy = [snake[0][0], snake[0][1] - 1]
                            board[snake[0][0], snake[0][1] - 1] = 2
                            snake.insert(0, dummy)
                            board[snake[1][0], snake[1][1]] = 3
                            board[snake[-1][0], snake[-1][1]] = 0
                            snake.pop()                        
                        else:
                            print("Cannot move")  
                elif event.key == pygame.K_RIGHT:
                    if direction == "DOWN" or direction == "UP" or direction == "RIGHT":
                        if snake[0][1] < 19:
                            print("Moving right")
                            direction = "RIGHT"
                            dummy = [snake[0][0], snake[0][1] + 1]
                            board[snake[0][0], snake[0][1] + 1] = 2
                            snake.insert(0, dummy)
                            board[snake[1][0], snake[1][1]] = 3
                            board[snake[-1][0], snake[-1][1]] = 0
                            snake.pop()                        
                        else:
                            print("Cannot move")  

            for row in range(rows):
                top = row * 20
                for col in range(cols):
                    left = col * 20
                    update(board[row][col], left, top)                      