import pygame
Pol = []
KolT = int(input(" Выедите количество точек в полигоне:"))
for i in range(KolT):
    m = input().split()
    n = list(map(int, m))
    Pol.append(n)

pygame.init()
win = pygame.display.set_mode((1000, 1000))

pygame.display.set_caption("My first game")
x = [0, 0, 0, 0]
y = [0, 0, 0, 0]
wight = [50, 50, 50, 50]
height = [50, 50, 50, 50]
speedX = [0, 0, 0, 0]
speedY = [0, 0, 0, 0]
run = True
i = 0
while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()



    if keys[pygame.K_c]:
        i = 0
    if keys[pygame.K_v]:
        i = 1
    if keys[pygame.K_b]:
        i = 2
    if keys[pygame.K_n]:
        i = 3



    if keys[pygame.K_LEFT]:
        x[i] -= 3
    if keys[pygame.K_RIGHT]:
        x[i] += 3
    if keys[pygame.K_UP]:
        y[i] -= 3
    if keys[pygame.K_DOWN]:
        y[i] += 3
    if keys[pygame.K_q]:
        wight[i] += 3
    if keys[pygame.K_e]:
        wight[i] -= 3
    if keys[pygame.K_r]:
        height[i] -= 3
    if keys[pygame.K_t]:
        height[i] += 3

    x += speedX
    y += speedY
    win.fill((0, 0, 0))
    x = list(map(int, x))
    y = list(map(int, y))
    pygame.draw.ellipse(win, (189, 23, 43), (x[0], y[0], wight[0], height[0]))
    pygame.draw.rect(win, (111, 78, 54), (x[1], y[1], wight[1], height[1]))
    pygame.draw.polygon(win, (185, 28, 71), [[height[2]+x[2], 0+y[2]], [0+x[2], 0+y[2]], [(height[2]/2)+x[2], wight[2] + y[2]]])
    pygame.draw.polygon(win, (141, 2, 200), Pol)

    pygame.display.update()

pygame.quit()

