import pygame

def run():
    pygame.init()
    icon = pygame.image.load("app/res/images/icon.png")
    pygame.display.set_icon(icon)

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Py-Rex")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        pygame.display.flip()

    pygame.quit()