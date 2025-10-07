from Bird import *

WIDTH, HEIGHT = 800, 600

class Pipe:
    def __init__(self, x):
        # carrega e redimensiona a imagem do cano
        self.image = pygame.image.load(os.path.join("assets", "sprites", "pipe-green.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 500))

        self.top_image = pygame.transform.flip(self.image, False, True)  # cano invertido
        self.bottom_image = self.image

        self.gap = 150
        self.top_height = random.randint(50, HEIGHT - 200)
        self.x = x
        self.speed = 4
        self.passed = False

        iw, ih = self.top_image.get_size()

        # Posições
        self.top_y = self.top_height - self.top_image.get_height()
        self.bottom_y = self.top_height + self.gap

        # Retângulos para colisão
        self.top = pygame.Rect(self.x, self.top_y, iw, self.top_image.get_height())
        self.bottom = pygame.Rect(self.x, self.bottom_y, iw, self.bottom_image.get_height())

    def update(self):
        self.x -= self.speed
        self.top.x = self.x
        self.bottom.x = self.x

    def draw(self, surface):
        surface.blit(self.top_image, (self.top.x, self.top.y))
        surface.blit(self.bottom_image, (self.bottom.x, self.bottom.y))

    def off_screen(self):
        return self.x + self.top_image.get_width() < 0
