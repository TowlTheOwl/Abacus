import pygame
from row import Row

# initialize pygame
pygame.init()
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Abacus")

rows = []
num_rows = 15
for i in range(num_rows):
    interval = (screen_size[0]-200-(5*num_rows))/num_rows
    rows.append(Row(i*(interval+5)+100, interval, 400))


def draw(screen):
    screen.fill((144, 238, 144))

    for row in rows:
        row.draw(screen)
    

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for row in rows:
                row.check_collision(mouse_pos)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        for row in rows:
            row.reset()
    
    draw(screen)
    pygame.display.update()

pygame.quit()