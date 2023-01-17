import numpy as np
import pygame

pygame.init()
font = pygame.font.Font(None, 72)

class Bead(pygame.sprite.Sprite):
    def __init__(self, idx, pos, width, height, color):
        super().__init__()
        self.idx = idx

        self.image = pygame.Surface((width, height))
        self.image.set_colorkey((0, 0, 0))
        pygame.draw.ellipse(self.image, color, (0, 0, width, height), 0)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    
    def draw(self, screen):
        if self.visible:
            screen.blit(self.image, self.rect)
    
    def check_collision(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

class Row:
    def __init__(self, pos, width, height):
        self.upper, self.lower = [np.array([1,0]), np.array([0, 1, 1, 1, 1])]
        self.val = 0
        
        self.x = pos
        self.y = 100
        self.width = width
        self.height = height

        self.color = (165, 42, 42)

        # generate beads
        self.beads = []
        num_beads = 7
        for i in range(num_beads):
            bead_height = height//num_beads
            self.beads.append(Bead(i, (self.x, i * bead_height + self.y), self.width, bead_height, self.color))
    
    def reset(self):
        self.upper, self.lower = [np.array([1,0]), np.array([0, 1, 1, 1, 1])]

    def print_row(self):
        data = np.concatenate((self.upper, self.lower))
        print(np.expand_dims(np.asarray(data), axis=1))
    
    def set_val(self):
        self.val = int((np.where(self.upper == 1)[0]) * 5 + (np.where(self.lower == 0)[0]))
    
    def move(self, idx):
        if 0 <= idx <= 6:
            if (idx <= 1) and (idx == int(np.where(self.upper == 1)[0])):
                    self.upper = np.array([0, 0])
                    self.upper[(idx + 1)%2] = 1

            else:
                self.lower = np.array([1, 1, 1, 1, 1])
                self.lower[idx-2] = 0
    
    def change_bead_visibility(self):
        data = np.concatenate((self.upper, self.lower))
        for i in range(len(self.beads)):
            if data[i] == 1:
                self.beads[i].visible = True
            else:
                self.beads[i].visible = False

    def check_collision(self, mouse_pos):
        for bead in self.beads:
            collide = bead.check_collision(mouse_pos)
            if collide:
                self.move(bead.idx)

    def draw(self, screen):
        self.change_bead_visibility()
        for bead in self.beads:
            bead.draw(screen)
        self.set_val()
        text = font.render(str(self.val), True, (0, 0, 0))
        screen.blit(text, (self.x, self.y + self.height + 10))