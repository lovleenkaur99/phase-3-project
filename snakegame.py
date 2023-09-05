import pygame as pg
from random import randrange


#to set up the window for the game
WINDOW = 1000;
BLOCK_SIZE = 50;
range = (BLOCK_SIZE // 2, WINDOW - BLOCK_SIZE // 2, BLOCK_SIZE)
random_position = lambda: [randrange(*range), randrange(*range)]
snake = pg.rect.Rect(0, 0, BLOCK_SIZE - 2, BLOCK_SIZE - 2)
snake.center = random_position()
length = 1
segments = [snake.copy()]
snake_dir = (0,0)
time, time_step = 0, 110
food = snake.copy()
food.center = random_position()
screen = pg.display.set_mode([WINDOW] * 2)
clock = pg.time.Clock()
direction = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1 }


while True: 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            
            if event.key == pg.K_w and direction[pg.K_w]:
                snake_dir = (0, -BLOCK_SIZE)
                direction = {pg.K_w: 1, pg.K_s: 0, pg.K_a: 1, pg.K_d: 1 }
            
            if event.key == pg.K_s and direction[pg.K_s]:
                snake_dir = (0, BLOCK_SIZE)
                direction = {pg.K_w: 0, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1 }
            
            if event.key == pg.K_a and direction[pg.K_a]:
                snake_dir = (-BLOCK_SIZE, 0)
                direction = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 0 }
            
            if event.key == pg.K_d and direction[pg.K_d] : 
                snake_dir = (BLOCK_SIZE, 0)
                direction = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 0, pg.K_d: 1 }
        
        screen.fill('black')

        eating = pg.Rect.collidelist(snake, segments[:-1]) != -1

        if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or eating:
            snake.center, food.center = random_position(), random_position()
            length, snake_dir = 1, (0, 0)
            segments = [snake.copy()]

        if snake.center == food.center:
            food.center = random_position()
            length += 1

        [pg.draw.rect(screen, 'red', food)]

        [pg.draw.rect(screen, 'purple', segment) for segment in segments]

        time_now = pg.time.get_ticks()
        if time_now - time > time_step:
            time = time_now
            snake.move_ip(snake_dir)
            segments.append(snake.copy())
            segments = segments[-length:]
        
        pg.display.flip()
        clock.tick(60)






