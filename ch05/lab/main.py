import pygame

def threenp1(n):
    count = 0
    while n > 1.0:
       if n % 2 == 0:
        n = int(n / 2)
        count += 1
       else:
        n = int(3 * n + 1)
        count += 1
    return count


def threenp1range(upper_limit):
    threenplus1_iters_dict = []
    for n in range (2,upper_limit+1):
        count = threenp1(n)
        threenplus1_iters_dict.append([n,count])
    return threenplus1_iters_dict

def graph_coordinates(threenplus1_iters_dict):
   window = pygame.display.set_mode()
   pygame.draw.lines(window,"pink",False,threenplus1_iters_dict)
   new_display = pygame.transform.flip(window, False, True)
   width, height = new_display.get_size()
   #new_display = pygame.transform.scale(new_display, (width * 5, height * 5))
   max_so_far = 0
   max_num = 0
   for (i,j) in threenplus1_iters_dict:
      if j > max_so_far:
         max_so_far = j
         max_num = i
   font = pygame.font.Font(None, 55)
   msg = font.render(f"{max_num} had the most iterations with {max_so_far}", True, "white")
   window.blit(msg, (100,100))
   pygame.display.flip()
   pygame.time.wait(2000)
   print(max_num,max_so_far)

def main():
    pygame.init()
    upper_limit = 35 #int(input("What is the upper limit: "))
    ans = threenp1range(upper_limit)
    graph_coordinates(ans)
    pygame.display.flip()
    pygame.time.wait(2000)
    print(ans)

main()