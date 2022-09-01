import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

screen_width = 600
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

game_over = False

x1 = 300
y1 = 300

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

game_over = False
game_lose = False
font_style = pygame.font.SysFont("bahnschrift", 25)
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width / 6, screen_height/ 3])

while not game_over:
    while game_lose == True:
        next_step = input("You Lost! Press C-Play Again or Q-Quit", red)
        if next_step == 'q' or 'Q':
            game_over = true

        pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0
        if x1 <= 0 or x1 >= screen_height or y1 <=0 or y1 >= screen_height:
            game_lose = True

    x1 += x1_change
    y1 += y1_change
    screen.fill(white)
    pygame.draw.rect(screen, black, [x1, y1, 10, 10])

    pygame.display.update()

    clock.tick(30)

pygame.quit()
quit()