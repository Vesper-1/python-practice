import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move The Square")

# 背景可选：找不到就用纯色
try:
    background = pygame.image.load("background_image.jpg")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
except:
    background = None

BLUE = (0, 0, 255)
player = pygame.Rect(100, 100, 50, 50)
speed_x, speed_y = 5, 5

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 运动与反弹
    player.x += speed_x
    player.y += speed_y
    if player.left < 0 or player.right > WIDTH:
        speed_x = -speed_x
    if player.top < 0 or player.bottom > HEIGHT:
        speed_y = -speed_y

    # 绘制（都在循环里）
    if background:
        screen.blit(background, (0, 0))
    else:
        screen.fill((30, 30, 30))

    pygame.draw.rect(screen, BLUE, player)
    pygame.display.flip()      # 刷新屏幕
    clock.tick(60)             # 限帧

pygame.quit()
