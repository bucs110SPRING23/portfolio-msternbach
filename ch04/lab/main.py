import pygame 
import random
import math

pygame.init()
window = pygame.display.set_mode()
font = pygame.font.Font(None, 48)
message = font.render("Pick the white square for player1 and black for player 2", True, "white")

screen_size = pygame.display.get_window_size()
window.fill("pink")
window.blit(message, (360, 150))
pygame.draw.rect(window,"white",[0,0,150,150])
pygame.draw.rect(window,"black",[0,150,150,150])

pygame.display.flip()
pygame.time.wait(2000)


wait = True
bet1 = True
bet2 = True

while wait == True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x5,y5 = pygame.mouse.get_pos()
            if x5 in range (0,151) and y5 in range(0,151):
                bet2 = False
                wait = False
            elif x5 in range (0,151) and y5 in range(150,301):
                bet1 = False
                wait = False

#pygame.draw.ellipse(window,"blue",[0,0,(screen_size[0]),(screen_size[1])],0)
window.fill("pink")
pygame.draw.circle(window,"blue", [screen_size[0]//2,screen_size[1]//2], screen_size[1]//2)
pygame.draw.line(window,"black",(screen_size[0]//2,0),(screen_size[0]//2,screen_size[1]),2)
pygame.draw.line(window,"black",(0,screen_size[1]//2),(screen_size[0],screen_size[1]//2),2)


pygame.display.flip()
pygame.time.wait(2000)

x1 = (screen_size[0]//2)
y1 = (screen_size[1]//2)

points1 = 0
points2 = 0

for i in range(10):
    x2 = random.randrange(0,screen_size[0]+1)
    y2 = random.randrange(0,screen_size[1]+1)
    distance_from_center = math.hypot(x1-x2, y1-y2)
    is_in_circle = distance_from_center <= screen_size[1]//2
    if is_in_circle == True:
        pygame.draw.circle(window,"white",[x2,y2],10)
        points1 = points1 + 1
    elif is_in_circle == False:
        pygame.draw.circle(window,"yellow",[x2,y2],10)
    pygame.display.flip()
    pygame.time.wait(500)
    x3 = random.randrange(0,screen_size[1]+1)
    y3 = random.randrange(0,screen_size[1]+1)
    distance_from_center2 = math.hypot(x1-x3, y1-y3)
    is_in_circle2 = distance_from_center2 <= screen_size[1]//2
    if is_in_circle2 == True:
        pygame.draw.circle(window,"black",[x3,y3],10)
        points2 = points2 + 1
    elif is_in_circle2 == False:
        pygame.draw.circle(window,"green",[x3,y3],10)
    pygame.display.flip()
    pygame.time.wait(500)

points1 = str(points1)
points2 = str(points2)

if points1 > points2:
    font = pygame.font.Font(None, 48)
    text = font.render(f"player 1 wins with a score of {points1}", True, "white")
    window.blit(text, (640, 150))
    if bet1 == True:
        font = pygame.font.Font(None, 48)
        text2 = font.render("your guess was right", True, "white")
        window.blit(text2, (640, 200)) 
    else:
        font = pygame.font.Font(None, 48)
        text2 = font.render("your guess was wrong", True, "white")
        window.blit(text2, (640, 200)) 

elif points1 < points2:
    font = pygame.font.Font(None, 48)
    text = font.render(f"player 2 wins with a score of {points2}", True, "white")
    window.blit(text, (640, 150)) 
    if bet2 == True:
        font = pygame.font.Font(None, 48)
        text2 = font.render("your guess was right", True, "white")
        window.blit(text2, (640, 200)) 
    else:
        font = pygame.font.Font(None, 48)
        text2 = font.render("your guess was wrong", True, "white")
        window.blit(text2, (640, 200)) 
else:
    font = pygame.font.Font(None, 48)
    text = font.render("it's a tie with a score of", True, "white")
    window.blit(text, (640, 150))
    text2 = font.render("you were neither right or wrong", True, "white")
    window.blit(text2, (640, 200)) 

        
pygame.display.flip()
pygame.time.wait(2000)