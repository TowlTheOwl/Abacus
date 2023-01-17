import pygame

class SettingButton(pygame.sprite.Spirte):
    def __init__(self, pos):
        super().__init__()

        self.image = pygame.Surface((100, 100))
        self.image.set_colorkey((0, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
    
    def draw(self, screen):
        if self.visible:
            screen.blit(self.image, self.rect)

    def check_collision(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)