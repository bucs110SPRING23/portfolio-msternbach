import pygame 
import random
import math

#Part A
pygame.init()
window = pygame.display.set_mode()

screen_size = pygame.display.get_window_size()
print(screen_size)
print(screen_size[0])
print(screen_size[1])

window.fill("pink")

#pygame.draw.ellipse(window,"blue",[0,0,(screen_size[0]),(screen_size[1])],0)
pygame.draw.circle(window,"blue", [screen_size[0]//2,screen_size[1]//2], screen_size[1]//2)
pygame.draw.line(window,"black",(screen_size[0]//2,0),(screen_size[0]//2,screen_size[1]),2)
pygame.draw.line(window,"black",(0,screen_size[1]//2),(screen_size[0],screen_size[1]//2),2)

pygame.display.flip()
pygame.time.wait(2000)

#Part B
x1 = (screen_size[0]//2)
y1 = (screen_size[1]//2)

for i in range(10):
    x2 = random.randrange(0,screen_size[0]+1)
    y2 = random.randrange(0,screen_size[1]+1)
    distance_from_center = math.hypot(x1-x2, y1-y2) #the distance formula
    is_in_circle = distance_from_center <= screen_size[1]//2 #screen width
    if is_in_circle == True:
        pygame.draw.circle(window,"white",[x2,y2],10)
    else:
        pygame.draw.circle(window,"yellow",[x2,y2],10)

pygame.display.flip()
pygame.time.wait(2000)