from Pipe import *
from Bird import *
import sys


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Game:
    def __init__(self):
        self.background = pygame.image.load(
            os.path.join("assets", "sprites", "flappy-bird-background-800x600.png")
        ).convert()
        self.bird = Bird(170, 200)
        self.pipes = [Pipe(WIDTH + 100)]
        self.score = 0
        self.font = pygame.font.SysFont("Arial", 36)
        self.alive = True
        self.die_sound = pygame.mixer.Sound(os.path.join("assets", "audio", "hit.wav"))
        self.point_sound = pygame.mixer.Sound(os.path.join("assets", "audio", "point.wav"))

    def reset(self):
        self.__init__()

    def show_game_over(self):
        text = self.font.render("GAME OVER", True, (255, 0, 0))
        rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, rect)
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    waiting = False

    def update(self):
        self.bird.update()

        for pipe in self.pipes:
            pipe.update()

        # Spawn de novo pipe
        if self.pipes[-1].x < WIDTH - 250:
            self.pipes.append(Pipe(WIDTH))

        bird_rect = self.bird.get_rect()

        # Pontuação (antes de remover off_screen)
        for pipe in self.pipes:
            if not pipe.passed and bird_rect.left > pipe.top.right:
                pipe.passed = True
                self.jump_sound = pygame.mixer.Sound(os.path.join("assets", "audio", "wing.wav"))
                self.point_sound.play()
                self.score += 1

        # Colisão
        for pipe in self.pipes:
            if bird_rect.colliderect(pipe.top) or bird_rect.colliderect(pipe.bottom):
                self.die_sound.play()
                self.show_game_over()
                self.reset()
                return

        if self.bird.y > (HEIGHT + 100) or self.bird.y < -100:
            self.die_sound.play()
            self.show_game_over()
            self.reset()
            return

        # Remover pipes que saí­ram da tela
        self.pipes = [pipe for pipe in self.pipes if not pipe.off_screen()]

        # depois de atualizar pipes e do bird.update(), antes de remover off_screen
        bird_rect = self.bird.get_rect()

        # Pontuação: quando o lado esquerdo do bird ultrapassa o lado direito do pipe
        for pipe in self.pipes:
            if not pipe.passed and bird_rect.left > pipe.top.right:
                pipe.passed = True
                self.score += 1


    def draw(self, surface):
        surface.blit(self.background, (0, 0))
        self.bird.draw(surface)
        for pipe in self.pipes:
            pipe.draw(surface)

        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        surface.blit(score_text, (10, 10))
