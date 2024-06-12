# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 11:01:48 2024

@author: Kitti
"""

import pygame
import random

pygame.init()

#méretezés1
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Harry Potter Game")

#színek
szin1 = (192, 155, 114)
szin2 = (0, 0, 0)

#képek
harry_image = pygame.image.load("harry.png")
snitch_image = pygame.image.load("snitch.png")
dementor_image = pygame.image.load("dementor.png")

#méretezés2
harry_image = pygame.transform.scale(harry_image, (50, 50))
snitch_image = pygame.transform.scale(snitch_image, (30, 30))
dementor_image = pygame.transform.scale(dementor_image, (60, 60))

#alapok
harry_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT - 60]
harry_speed = 6
snitch_pos = [random.randint(0, SCREEN_WIDTH-30), 0]
snitch_speed = 5
dementor_pos = [random.randint(0, SCREEN_WIDTH-60), 0]
dementor_speed = 5
score = 0


#Score
font_path = "HARRYP__.TTF"
font_size = 36
font = pygame.font.Font(font_path, font_size)



running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        harry_pos[0] -= harry_speed
    if keys[pygame.K_RIGHT]:
        harry_pos[0] += harry_speed

    snitch_pos[1] += snitch_speed
    dementor_pos[1] += dementor_speed

    if snitch_pos[1] > SCREEN_HEIGHT:
        snitch_pos = [random.randint(0, SCREEN_WIDTH-30), 0]
    if dementor_pos[1] > SCREEN_HEIGHT:
        dementor_pos = [random.randint(0, SCREEN_WIDTH-60), 0]

    # Check for collisions with the snitch
    if pygame.Rect(harry_pos[0], harry_pos[1], 50, 50).colliderect(pygame.Rect(snitch_pos[0], snitch_pos[1], 30, 30)):
        score += 1
        snitch_pos = [random.randint(0, SCREEN_WIDTH-30), 0]

    if pygame.Rect(harry_pos[0], harry_pos[1], 50, 50).colliderect(pygame.Rect(dementor_pos[0], dementor_pos[1], 60, 60)):
        running = False  # End the game

    screen.fill(szin1)
    screen.blit(harry_image, harry_pos)
    screen.blit(snitch_image, snitch_pos)
    screen.blit(dementor_image, dementor_pos)

    score_text = font.render("Score: " + str(score), True, szin2)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(30)

# Quit Pygame
pygame.quit()
