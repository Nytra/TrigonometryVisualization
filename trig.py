import pygame, random, math
pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 600
WHITE = 255, 255, 255
BLACK = 0, 0, 0
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
TO_RAD = 3.14 / 180

CIRCLE_RADIUS = 200

def demoTrigonometryVisualization():
    x = SCREEN_WIDTH // 2 
    y = SCREEN_HEIGHT // 2
    initialY = y
    initialX = x
    gameOver = False
    while gameOver == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
        screen.fill(BLACK)
        mousePos = [coord for coord in pygame.mouse.get_pos()]

        xLength = (mousePos[0] - initialX) / CIRCLE_RADIUS
        yLength = (initialY - mousePos[1]) / CIRCLE_RADIUS
        xLength = max(-1, min(xLength, 1)) # clamp these values between -1 and 1
        yLength = max(-1 , min(yLength, 1))

        # enter special cases. the trig functions used here are probably wrong or something.
        if xLength == 0 or yLength == 0:
            theta = 0
        elif xLength > 0 and yLength > 0:
            theta = math.atan(yLength / xLength)
        elif xLength < 0 and yLength > 0:
            theta = math.pi + math.atan(yLength / xLength)
        elif xLength < 0 and yLength < 0:
            theta = math.pi + math.atan(yLength / xLength)
        elif xLength > 0 and yLength < 0:
            theta = math.pi * 12/6 + math.atan(yLength / xLength)

        x = round(initialX + CIRCLE_RADIUS * math.cos(theta))
        y = round(initialY + CIRCLE_RADIUS * math.sin(theta) * -1)

        pygame.draw.circle(screen, WHITE, (initialX, initialY), CIRCLE_RADIUS, 1)
        
        pygame.draw.line(screen, GREEN, (initialX, initialY), (x, initialY))
        pygame.draw.line(screen, BLUE, (initialX, initialY), (initialX, y))

        pygame.draw.line(screen, WHITE, (initialX, initialY), (x, y))

        text = font.render("({}, {}) Radians: {}".format(x - initialX, initialY - y, round(theta, 2)), True, WHITE)

        screen.blit(text, (x, y))

        pygame.display.update()

        pygame.time.wait(round(1000 / 60))

# main loop

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.SysFont("monospace", 24)

# init demos here
demoTrigonometryVisualization()

pygame.quit()