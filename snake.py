from cgitb import grey
import pygame
import numpy as np
import random
from sys import exit
from pygame import surface

(width, height) = (400, 400)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Frank\'s Snake Game')

snake = 2
blob = 1
rows = 20
cols = 20
board = np.zeros((rows, cols))

board_r = 240
board_g = 190
board_b = 45
left = 0
top = 0
board_colour = (board_r, board_g, board_b)
for row in range(rows):
    top = row * 20
    for col in range(cols):
        left = col * 20
        pygame.draw.rect(screen, board_colour,
                        pygame.Rect(left, top, 20, 20))
        pygame.display.flip()      

blob_r = 65
blob_g = 200
blob_b = 124
blob_colour = (blob_r, blob_g, blob_b)

rand_row = random.randint(0, 19)
rand_col = random.randint(0, 19)
top = rand_row * 20
left = rand_col * 20
pygame.draw.rect(screen, blob_colour,
                pygame.Rect(left, top, 20, 20))
pygame.display.flip()    

snake_r = 0
snake_g = 173
snake_b = 59
snake_colour = (snake_r, snake_g, snake_b)

rand_row = random.randint(0, 19)
rand_col = random.randint(0, 19)
rand_dir = random.randint(1, 4)
top = rand_row * 20
left = rand_col * 20

pygame.draw.rect(screen, snake_colour,
                pygame.Rect(left, top, 20, 20))
pygame.display.flip()    

if rand_dir == 1:
    pygame.draw.rect(screen, snake_colour,
                    pygame.Rect(left, top - 20, 20, 20))
    pygame.display.flip()
elif rand_dir == 2:
    pygame.draw.rect(screen, snake_colour,
                    pygame.Rect(left + 20, top, 20, 20))
    pygame.display.flip()   
elif rand_dir == 3:
    pygame.draw.rect(screen, snake_colour,
                    pygame.Rect(left, top + 20, 20, 20))
    pygame.display.flip()   
else:
    pygame.draw.rect(screen, snake_colour,
                     pygame.Rect(left - 20, top, 20, 20))
    pygame.display.flip()      

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()