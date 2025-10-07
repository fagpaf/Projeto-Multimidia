import pygame, random, os

class Bird:
    SPRITES = ["yellowbird-midflap.png", "redbird-midflap.png", "bluebird-midflap.png"]

    def __init__(self, x, y):
        sprite = random.choice(self.SPRITES) # Escolhe aleatoriamente a sprite
        self.image = pygame.image.load(os.path.join("assets", "sprites", sprite)).convert_alpha()
        self.x = x
        self.y = y
        self.velocity = 0
        self.gravity = 0.4
        self.jump_strength = -8
        self.jump_sound = pygame.mixer.Sound(os.path.join("assets", "audio", "wing.wav"))

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity

    def jump(self):
        self.velocity = self.jump_strength
        self.jump_sound.play()

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
