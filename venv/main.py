import pygame
import sys

# Inicializa o pygame
pygame.init()

# Define as dimensões da janela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Define cores (R, G, B)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Quadrado
x, y = 100, 100
size = 50
square = pygame.Rect(x, y, size, size)

# Controlador de FPS
clock = pygame.time.Clock()
FPS = 60



# Loop principal do jogo
while True:
    # Eventos (ex: fechar a janela)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Pinta o fundo de BLUE
    screen.fill(BLUE)
    pygame.draw.rect(screen, BLACK, square)
    # Atualiza a tela
    pygame.display.flip()

    # Controla FPS
    clock.tick(FPS)
