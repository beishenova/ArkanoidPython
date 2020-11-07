import pygame
import game


def start():
    pygame.init()

    res = (1200, 600)
    screen = pygame.display.set_mode(res)
    color = (255, 255, 255)
    color_light = (170, 170, 170)
    color_dark = (100, 100, 100)
    width = screen.get_width()
    height = screen.get_height()
    smallfont = pygame.font.SysFont('robot.ttf', 35)
    text = smallfont.render('RESTART', True, color)
    text1 = smallfont.render('QUIT', True, color)
    greetings = smallfont.render('WIN ;)', True, color)

    while True:

        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:
                pygame.quit()

            if ev.type == pygame.MOUSEBUTTONDOWN:
                if quitposx <= mouse[0] and quitposy <= mouse[1]:
                    exit()

                if startposx <= mouse[0] and startposy <= mouse[1]:
                    game.game()

        screen.fill((color_light))

        mouse = pygame.mouse.get_pos()
        startposx = 400
        startposy = 200
        quitposx = 550
        quitposy = 200
        pygame.draw.rect(screen, color_light, [width/2, 50, 140, 40])
        screen.blit(greetings, (450, 80))
        pygame.draw.rect(screen, color_dark, [startposx, startposy, 140, 40])
        screen.blit(text, (startposx + 40, startposy + 5))
        pygame.draw.rect(screen, color_dark, [quitposx, quitposy, 140, 40])
        screen.blit(text1, (quitposx + 50, quitposy + 5))

        pygame.display.update()
