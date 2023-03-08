import pygame

pygame.display.init()

screen = pygame.display.set_mode()

screen.fill("black")

pygame.draw.circle(screen,"red", [600,250], 85)
pygame.draw.circle(screen,"red", [600,400], 115)
pygame.draw.circle(screen,"red", [600,550], 150)

pygame.display.flip()
pygame.time.wait(1000)