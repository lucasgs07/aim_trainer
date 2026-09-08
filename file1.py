import pygame
import random

W = 1366
H = 768
raio = 15

pygame.init()
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

running = True

def novo_alvo():
     x = random.randint(raio, W - raio)
     y = random.randint(raio, H - raio)
     return x, y

x, y = novo_alvo()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.pos == (x, y) or raio:
            x, y = novo_alvo()

    screen.fill((30, 30, 30))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), raio)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()