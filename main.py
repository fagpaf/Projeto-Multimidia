from Game import *

# Inicializa pygame e a música
pygame.init()
pygame.mixer.init()


# Dimenções da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome e Ícone
pygame.display.set_caption("Flappy Bird")
icon = pygame.image.load(os.path.join("assets", "favicon.ico"))
pygame.display.set_icon(icon)

# Definindo a música e o loop dela
music = pygame.mixer.music.load(os.path.join("assets", "audio", "Theme For FlappyBird.wav"))
pygame.mixer.music.play(-1)

# Clock
clock = pygame.time.Clock()
FPS = 60


def main():
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game.bird.jump()

        game.update()
        game.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()