import pygame


pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

font = pygame.font.SysFont("Kristen ITC", 50)
font2 = pygame.font.SysFont("Kristen ITC", 30)

img = pygame.image.load("kosmos.jpg")
new_size = (800, 600)
new_img = pygame.transform.scale(img, new_size)

hero_img = pygame.image.load("doodle_jump.png")
size_hero = (75, 50)
new_hero_img = pygame.transform.scale(hero_img, size_hero)

x,y = 200, 0
x1,y1 = 140, 80
x2,y2 = 140, 120
x3, y3 = 400, 300

speed = 0.5

zvuk = pygame.mixer.Sound("shagi.mp3")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()



    screen.blit(new_img, (0, 0))

    screen.blit(new_hero_img, (x3, y3))

    text = font.render("Welcome to game!!", True, (0, 0, 100))
    screen.blit(text, (x, y))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y3 = y3 - speed
        zvuk.play()
    if keys[pygame.K_s]:
        y3 = y3 + speed
        zvuk.play()
    if keys[pygame.K_a]:
        x3 = x3 - speed
        zvuk.play()
    if keys[pygame.K_d]:
        x3 = x3 + speed
        zvuk.play()
    if not keys[pygame.K_w] and not keys[pygame.K_s] and not keys[pygame.K_a] and not keys[pygame.K_d]:
        zvuk.stop()







    pygame.display.update()