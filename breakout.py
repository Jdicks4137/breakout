# josh dickey 12/16/16
# this creates a breakout game

import ball
import paddle
import pygame
import sys
import block
from pygame.locals import *


def main():
    pygame.init()
    """Constants that will be used in the program"""
    APPLICATION_WIDTH = 400
    APPLICATION_HEIGHT = 600
    BRICKS_PER_ROW = 10
    BRICK_SEP = 4 #The space between each brick
    BRICK_Y_OFFSET = 70
    BRICK_WIDTH =  (APPLICATION_WIDTH - (BRICKS_PER_ROW -1) * BRICK_SEP) / BRICKS_PER_ROW
    # calculates brick width by taking the width of the screen subtracted from four times one less than the bricks per
    # row and dividing the difference by the bricks per row
    NUM_TURNS = 3
    SCORE = 0
    BLOCKS_REMAINING = 100

    pygame.init()

    main_surface = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT), 0, 32)
    pygame.display.set_caption("breakout")

    #Sets up the colors
    RED = (255, 0, 0)
    ORANGE = (255, 165, 0)
    YELLOW = (255, 255, 0)
    GREEN =(0, 255, 0)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0) # used for ball and paddle
    WHITE = (255, 255, 255)
    colors = [RED, RED, ORANGE, ORANGE, YELLOW, YELLOW, GREEN, GREEN, CYAN, CYAN]

    main_surface.fill(WHITE)

    x_pos = BRICK_SEP
    y_pos = BRICK_Y_OFFSET
    brick_group = pygame.sprite.Group()  # creates a group for the bricks

    for y in range(10):
        for x in range(BRICKS_PER_ROW):
            my_brick = block.Brick(BRICK_WIDTH, colors[y]) # makes brick
            my_brick.rect.x = x_pos # set x position of brick
            my_brick.rect.y = y_pos # set y position of brick
            main_surface.blit(my_brick.block, my_brick.rect)
            brick_group.add(my_brick)
            x_pos = x_pos + BRICK_WIDTH + BRICK_SEP
        y_pos += BRICK_SEP + 8  # determines y position of next row
        x_pos = BRICK_SEP  # resets x position for new row

    line = paddle.Paddle(BLACK)  # creates paddle
    paddle_group = pygame.sprite.Group()
    paddle_group.add(line)

    bouncy = ball.Ball(BLACK, APPLICATION_WIDTH, APPLICATION_HEIGHT)  # creates ball

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        main_surface.fill(WHITE)
        line.move()
        bouncy.move()
        bouncy.collide_paddle(paddle_group)
        bouncy.collide_block(brick_group)
        font_score = pygame.font.SysFont("Ariel", 18)
        label_score = font_score.render("score:" + str(bouncy.score), 1, BLACK)  # adds score to screen
        main_surface.blit(label_score, (0,0))
        if bouncy.rect.bottom >= APPLICATION_HEIGHT:
            bouncy.rect.x = APPLICATION_WIDTH / 2
            bouncy.rect.y = APPLICATION_HEIGHT / 2
            NUM_TURNS -= 1  # this reduces the turns remaining when the ball hits the bottom
            if NUM_TURNS > 0:
                font_1 = pygame.font.SysFont("Ariel", 30)
                label_1 = font_1.render("Fail", 1, BLACK)
                main_surface.blit(label_1, (APPLICATION_WIDTH / 2.25, APPLICATION_HEIGHT / 2.1))
                pygame.display.update()
                pygame.time.wait(2000)
        if NUM_TURNS == 0:  # this adds lines to the end of the program once you have no lives left
            main_surface.fill(WHITE)
            label_score = font_score.render("final score:" + str(bouncy.score), 1, BLACK)  # displays final score at end
            main_surface.blit(label_score, (0, 0))
            font_2 = pygame.font.SysFont("Ariel", 65)
            label_2 = font_2.render("You get nothing!", 1, BLACK)
            main_surface.blit(label_2, (APPLICATION_WIDTH / 11, APPLICATION_HEIGHT / 2.1))
            pygame.display.update()
            pygame.time.wait(2000)
            main_surface.fill(WHITE)
            label_score = font_score.render("final score:" + str(bouncy.score), 1, BLACK)
            main_surface.blit(label_score, (0, 0))
            font_3 = pygame.font.SysFont("Ariel", 75)
            label_3 = font_3.render("You Lose!", 1, BLACK)
            main_surface.blit(label_3, (APPLICATION_WIDTH / 7, APPLICATION_HEIGHT / 2.1))
            pygame.display.update()
            pygame.time.wait(1500)
            main_surface.fill(WHITE)
            label_score = font_score.render("final score:" + str(bouncy.score), 1, BLACK)
            main_surface.blit(label_score, (0, 0))
            font_4 = pygame.font.SysFont("Ariel", 75)
            label_4 = font_4.render("Good Day Sir!", 1, BLACK)
            main_surface.blit(label_4, (APPLICATION_WIDTH / 8, APPLICATION_HEIGHT / 2.1))
            pygame.display.update()
            pygame.time.wait(1750)
            pygame.quit()
            sys.exit()
        main_surface.blit(line.line, line.rect)  # this adds paddle to screen
        main_surface.blit(bouncy.circle, bouncy.rect)  # this adds ball to screen
        for brick in brick_group:
            main_surface.blit(brick.block, brick.rect)  # this adds bricks to screen
        pygame.display.update()

main()  # the main function runs the program
