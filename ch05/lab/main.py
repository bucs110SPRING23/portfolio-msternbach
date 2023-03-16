import pygame

def threenp1(n):
    count = 0
    while n > 1.0:
       count += 1
       if n % 2 == 0:
        n = int(n / 2)
       else:
        n = int(3 * n + 1)
    return count


def threenp1range(upper_limit):
    threenplus1_iters_dict = []
    for n in range (2,upper_limit+1):
        threenp1(n)
        threenplus1_iters_dict.append([n,count])
        print(threenplus1_iters_dict)
    return threenplus1_iters_dict

upper_limit = int(input("What is the upper limit: "))
threenp1range(upper_limit)