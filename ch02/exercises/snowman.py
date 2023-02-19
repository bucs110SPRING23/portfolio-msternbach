import pygame

pygame.init()

screen = pygame.display.set_mode()

dimensions = screen.get_size() 
starting_point = (dimensions[0] // 2, dimensions[1] // 2)

radius=200
for _ in range(3)
    pygame.draw.circle(screen,"red", starting_point, radius)
    starting_point[1] = starting_point[1] - radius
    radius = radius//2
    pygame.draw.circle(screen,"red", starting_point, radius)
    

screen.fill("black")
pygame.display.flip()
pygame.time.wait(1000)


#pygame.draw.circle(screen,"red", [500,200], 100)
#pygame.draw.circle(screen,"red", [500,150], 150)



#pygame.draw.rect(screen, "red", dimensions)

#dimensions = [300, 300, 250, 250]
#pygame.draw.rect(screen, "blue", dimensions)