import pygame
from column import Column
from utils import *

# initialize
pygame.init()
screen_size = (800, 600)
WIDTH, HEIGHT = screen_size
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Abacus")

rows = []
num_rows = 10
for i in range(num_rows):
    interval = (screen_size[0]-200)/num_rows
    rows.append(Column((i*interval + 100, HEIGHT/6), interval-5, HEIGHT*3/5, WIDTH//10))

abacus_rect = pygame.Rect(85, HEIGHT/6-15, WIDTH-175, HEIGHT*3/5+25)

setting_button = SettingButton(WIDTH-100, HEIGHT-100)


# draw screen
def draw(screen):
    screen.fill((230, 238, 230))

    pygame.draw.rect(screen, (0, 0, 0), abacus_rect, 10, 10)

    for row in rows:
        row.draw(screen)
    
    setting_button.draw(screen)


def main(screen):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for row in rows:
                row.check_collision(mouse_pos)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        for row in rows:
            row.reset()
    
    draw(screen)

def run_setting(screen):
    pass

setting = False

# main loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            setting = setting_button.check_collision(mouse_pos)
    
    if not setting:
        main(screen)
    
    else:
        run_setting(screen)
    
    pygame.display.update()

pygame.quit()