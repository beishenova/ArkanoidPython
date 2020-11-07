from random import randrange as rnd
import time
import pygame
import win
import gameover

def game_prekol():
    pygame.init()

    WIDTH = 1200
    HEIGHT = 600
    fps = 60
    paddle_w = 250
    paddle_h = 20
    paddle_speed = 15
    paddle = pygame.Rect(WIDTH // 2 - paddle_w // 2, HEIGHT - paddle_h - 10, paddle_w, paddle_h)
    ball_radius = 20
    ball_speed = 5
    ball_rect = int(ball_radius * 2 ** 0.5)
    ball = pygame.Rect(rnd(ball_rect, WIDTH - ball_rect), HEIGHT // 2, ball_rect, ball_rect)
    dx = 1
    dy = 1
    block_list = [pygame.Rect(10 + 120 * i, 10 + 70 * j, 100, 50) for i in range(10) for j in range(5)]
    color_list = [(rnd(30, 256), rnd(30, 256), rnd(30, 256)) for i in range(10) for j in range(5)]
    color = (255, 255, 255)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()


    def detect_collision(dx, dy, ball, rect):
        if dx > 0:
            delta_x = ball.right - rect.left
        else:
            delta_x = rect.right - ball.left
        if dy > 0:
            delta_y = ball.bottom - rect.top
        else:
            delta_y = rect.bottom - ball.top

        if abs(delta_x - delta_y) < 10:
            dx, dy = -dx, -dy
        elif delta_x > delta_y:
            dy = -dy
        elif delta_y > delta_x:
            dx = -dx
        return dx, dy

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        screen.fill((0, 0, 0))

        [pygame.draw.rect(screen, color_list[color], block) for color, block in enumerate(block_list)]
        pygame.draw.rect(screen, pygame.Color('lightblue'), paddle)
        pygame.draw.circle(screen, pygame.Color('white'), ball.center, ball_radius)
        ball.x += ball_speed * dx
        ball.y += ball_speed * dy

        if ball.centerx < ball_radius or ball.centerx > WIDTH - ball_radius:
            dx = -dx
        if ball.centery < ball_radius:
            dy = -dy
        if ball.colliderect(paddle) and dy > 0:
            dx, dy = detect_collision(dx, dy, ball, paddle)
        hit_index = ball.collidelist(block_list)
        if hit_index != -1:
            hit_rect = block_list.pop(hit_index)
            hit_color = color_list.pop(hit_index)
            dx, dy = detect_collision(dx, dy, ball, hit_rect)
            pygame.draw.rect(screen, hit_color, hit_rect)
            fps += 1.5
        if ball.bottom > HEIGHT:
            gameover.end()
        elif not len(block_list):
            win.start()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.left > 0:
            paddle.left -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
            paddle.right += paddle_speed

        pygame.display.flip()
        clock.tick(fps)


